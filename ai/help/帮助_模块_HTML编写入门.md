# 帮助:模块/HTML编写入门

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3A%E6%A8%A1%E5%9D%97/HTML%E7%BC%96%E5%86%99%E5%85%A5%E9%97%A8
revid：39277 · 抓取时间：2026-11-09T14:27:10+08:00

---

{{LuaNav}}
本节将会讲解，如何使用Lua来生成HTML

大多数情况下，我们使用模板（template）还是为了重复完成一段HTML代码的生成，所以仅仅是像[[帮助:模块/替换模板入门|上节]]里那样在一句话里挖坑填的话，是远远没法达到可应用的层面的。所以本节就来讲下，'''如何使用Lua来渲染HTML代码'''。

==基本说明==
在lua中，生成HTML的核心是将符合HTML语言标准的内容（标签，CSS样式）以字符串（string）的形式从模块中return给MediaWiki，然后进一步在MW的parser中渲染成网页内容，一般来说我们需要一个string类型的变量来存放HTML内容，名称因人而异，以下我们以“res”为例进行演示：
<pre>
local res = ''   -- 初始化一个空的字符串
  res  =  res .. <some other string>    -- 使用“..”拼接其他的字符串内容直到我们满意
return res    --返回全部内容
</pre>
*返回的最终内容必须是<code>string</code>类型，如果是table会在页面上生成一个“#table”标记，并不会打印具体内容，如果需要查看具体内容，可以选择使用<code>mw.dumpObject()</code>函数或者将内容循环后<code>tostring()</code>
*由于lua模块的执行时机在MediaWiki的解析器（parser）之前，这意味着我们可以
**在lua中生成MediaWiki支持的Mark up语言，譬如<nowiki>{{</nowiki>、<nowiki>[[link]]</nowiki>、<nowiki>[[file:</nowiki>等等，见例[1]
**也可以直接书写符合HTML语言规范的内容，见例[2]
'''例[1]'''
<pre>
local res = ''
if path ~= nil then
  res = '[[file:'..image..'|'..size..'px'..'|link='..link..']]'
end
return res
</pre>

'''例[2]'''
<pre>
local res = ''
for _i, v in ipairs(table) do 
  if _i == 1 then  
    res = res .. '<div class="data-group">'  
  end   
    res = res .. '<span>' .. v .. '</span>'   
  if _i == table.maxn(table) then 
    res = res ..'</div>' 
  end
end
return res
</pre>

==拼字符串==
拼字符串的具体思路我们已经在上面有了介绍，核心是通过“<code>..</code>”连接符来链接多个string（或string类型的变量自身）
*注意，<code>..</code>连接符两段的变量类型必须都是string，否则lua会返回异常
*<code>..</code>会忽略换行行为，因此为了代码便于阅读，我们可以将不同内容进行换行，方便维护，见例[3]
'''例[3]'''
<pre>
local res = ''
  res = res .. data.name ..
             data.icon ..
             data.description ..
             data.quantity
return res
</pre>

==mw.html库==
在小段的HTML内容构建中，字符串拼接方式更为方便，但当我们需要构建大段HTML内容时，上述拼接方法的缺点就会暴露出来
# 不便阅读和维护
#不方便插入变量

在这时，我们推荐使用MediaWiki继承的mw.html库来构建内容，下面是一段通用的调用示例：
<pre>
local html = mw.html.create()
local your_html_res = ''

return tostring(your_html_res) 
</pre>

当然，这段代码中没有渲染任何HTML标签，只是调用了<code>mw.html.create()</code>，这是这一方法的核心，至于实际存放字段的名字<code>your_html_res</code>，您可以自行定义，下面是一段保护常用元素的代码片段。
<pre>
local html = mw.html.create()
local res_html = html
  :tag('div'):addClass('tt-socket-item'):cssText('display:inline-block;'):attr('data-name',data.hash)
    :tag('div'):addClass('tt-socket-text'):wikitext(data.name):done()
    :tag('div'):addClass('tt-socket-icon tt-tier'..data.inventory.tierType):wikitext(_getImage(data.icon,40,'')):done()
    :tag('div'):addClass('tt-socket-name')
      :tag('div'):addClass('tt-socket-type'):wikitext(data.itemTypeDisplayName):done()
    :done()
  :done()
return  tostring(res_html)
</pre>
===mw.html:tag===
:<code>html:tag( tagName, args )</code>
核心，在上述例子中，通过重复使用<code>:tag()</code>构建了完整的div结构，同样，tag()可以构建诸如span、table、tr、td、th等各种合法的HTML标签，以及MediaWiki中支持的解析器标签。
<pre>
local html = mw.html.create()
local res_html = html
  :tag('div'):done()
return  tostring(res_html)
</pre>
===mw.html:addClass===
:<code>html:addClass( class string )</code>
核心，可以连接在<code>:tag()</code>之后为其添加指定的类
<pre>
local html = mw.html.create()
local res_html = html
  :tag('div'):addClass('tt-socket-item'):done()
return  tostring(res_html)
</pre>
===mw.html:cssText===
:<code>html:cssText( css string )</code>
核心，可以连接在<code>:tag()</code>之后为其添加指定的CSS文字
<pre>
local html = mw.html.create()
local res_html = html
  :tag('div'):addClass('tt-socket-item'):cssText('display:inline-block;'):done()
return  tostring(res_html)
</pre>
===mw.html:attr===
:<code>html:attr( name, value )</code>
:<code>html:attr( table )</code>
核心，可以连接在<code>:tag()</code>之后为其添加指定的属性，尤其是为指定的标签添加自定义属性时（比如配合js制作筛选器）。
<pre>
local html = mw.html.create()
local res_html = html
  :tag('div')
    :addClass('tt-socket-item')
    :cssText('display:inline-block;')
    :attr('data-name',data.hash)
  :done()
return  tostring(res_html)
</pre>
===mw.html:wikitext===
:<code>html:wikitext( ... )</code>
核心，用来装载任何自定义的string类型内容，当其中的对象有nil值时，会在第一个nil处stop。
<pre>
local html = mw.html.create()
local res_html = html
    :tag('div'):addClass('tt-socket-text'):wikitext(data.name):done()
return  tostring(res_html)
</pre>
===mw.html:done===
<code>:done()</code>用于返回当前节点的上级节点（若当前节点为顶级节点，则返回当前节点）

可以使用<code>:done()</code>来在同一语句中创建多个同级节点
<pre>
h:tag('div')
    :tag('span'):addClass('item1'):done()
    :tag('span'):addClass('item2')
</pre>
返回
<pre>
<div>
    <span class="item1"></span>
    <span class="item2"></span>
</div>
</pre>

若没有<code>:done()</code>，item2将成为item1的子节点
<pre>
<div>
    <span class="item1">
        <span class="item2"></span>
    </span>
</div>
</pre>

===其他===
完整的内容参考：[https://www.mediawiki.org/wiki/Extension:Scribunto/Lua_reference_manual#HTML library MediaWiki/HTML library（英文文档）]
