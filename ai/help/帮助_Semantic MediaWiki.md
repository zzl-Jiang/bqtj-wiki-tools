# 帮助:Semantic MediaWiki

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3ASemantic%20MediaWiki
revid：39566 · 抓取时间：2026-11-09T14:27:10+08:00

---

{{编辑手册nav}}{{infobox
|bodystyle=clear:right
|title=Semantic Mediawiki
|image=[[File:SemanticMediaWiki_Logo.png|300px]]
|label1=官方站点
|data1=[https://www.semantic-mediawiki.org semantic-mediawiki.org] 
|label2=Mediawiki官网页面
|data2=[https://www.mediawiki.org/wiki/Extension:Semantic_MediaWiki Semantic Mediawiki]
}}
'''Semantic Mediawiki'''又称“SMW”、<del>“双马尾”</del>，是MediaWiki的一个大型扩展插件集（expansion），它主要用来为基于Mediawiki搭建的站点提供数据存储和查询（data query）解决方案。
Semantic Mediawiki是一款开源插件，最早由德国人[https://www.semantic-mediawiki.org/wiki/User:Markus_Kr%C3%B6tzsch Markus Krötzsch]和[https://www.semantic-mediawiki.org/wiki/User:Denny_Vrandecic Denny Vrandecic]创建。是全球范围内应用最为广泛的Mediawiki数据查询扩展。（类似的解决方案还有Cargo和Wiki Data）

==SMW的定位==
*SMW是一款功能性明确的MW“扩展”，实际上它比一般意义上的扩展（Expension）要庞大且复杂的多，安装、配置、使用都远比一般插件扩展复杂，更丰富的功能意味着更高的使用门槛和性能消耗。
*SMW的功能是为维基页面set data然后提供类数据库的query方式。如前文所述，SMW不是唯一的数据查询解决方案，它的两个主要类比概念是Cargo和Wikidata

==SMW的应用==
*影视、文学、动漫等对图谱有着较高需求的站点，譬如章节目录、Episode分集信息的构建、存储、调用等等
*一些数据结构呈二维扁平结构的游戏类数据。

== 替代方案 ==
===Lua查询MongoDB===
对于数据本身呈多维树状结构的（比如JSON），推荐使用MongoDB进行存储查询，
:详情参考：'''[[帮助:MongoDB支持]]'''

===使用SMongo作为替代方案===
在灰机，您可以选择使用'''[[帮助:SMongo|SMongo]]'''作为SMW扩展<code><nowiki>{{#ask:}}</nowiki></code>函数的替代品，同SMW相比他具有以下优势：
*'''小巧灵活'''：只需要搬运一个模板和模块既可以使用，语法完全继承了SMW的ask函数，对于熟悉SMW的人来说，可以快速上手。
*'''性能飙升'''：由于使用lua查询MongoDB，性能有着质的飞跃，响应速度是SMW的数十倍甚至百倍（视查询条件的复杂程度而定）。
*'''限制较少'''：以query条件为例，由于性能问题，SMW限制了同时并列条件的最大数量（4个），在SMongo里，可以一口气写上40个条件也没问题。由于使用tabx存储、更新数据，也省去了#set之苦。
*'''便于修改'''：核心是用Lua模块编写，有能力的开发者可以自行修改和扩展，带来更多的特性。

==安全使用SMW==
请勿滥用SMW，以免对数据库造成过大压力
*关于请求限制：参加[[博客:让灰机变得更稳定_2]]，灰机对单次Ask的上限等核心参数进行了更高的约束，以避免滥用，但并不会影响正常使用。一次查询结果超过100的，可以分次查询，使用offset参数。
*关于query的优化，一次show和一次ask对于服务器来说都是1次query，因此我们推荐多用ask，尽可能的少用show函数。ask取到多个参数然后使用format=template封装处理可以大大压缩请求压力。

==灰机的SMW==
目前灰机全面支持SMW，但是SMW并没有作为默认开启的组件，需要站长、管理员在站点[[帮助:站点等级|管理面板]]手动开启SMW选项后才能生效。
一经开启后，SMW和以下组件会被启用：
*Semantic Mediawiki
*Semantic Forms
*Semantic Result Formats
*Arrays
*Data命名空间{{main|help:命名空间}}

===已知的不兼容问题===
<s>由于灰机使用了MySQL5.6，导致部分SMW查询语法在灰机上会产生runtime exception的致命错误。该问题已经确认为SMW的bug（只兼容到MySQL5.5），包括可能不限于部分ask函数中的查询条件（例如条件组合和逻辑与的缩写方式等）。SMW官方确认会在下一个版本中予以修复(尚无时间表)</s>

==SMW特殊页面==
*特殊:询问(Special:Ask)
*特殊:按属性搜索(Special:Search by property)
*特殊:浏览(Special:Browse)
**特殊:浏览/<页面名称>(Special:Browse/<页面名称>)，查看指定页面的属性
*特殊:概念(Special:Concepts)
*特殊:属性(Special:Properties)

==SMW基础概念==
[[File:smw property.jpg|thumb|“亚巴顿”页面上的属性（左栏）及其具体数值（右栏）]]
===property与value===
通过赋值，每个页面都可能拥有若干属性（property），以右图为例，亚巴顿的属性“Agility”的数值就是“17”
*取值：通过#show函数，我们可以取到任意一个页面的任意一个值（只要存在）
**<code><nowiki>{{#show:<页面名称>|?<属性名称>|link=}}</nowiki></code>
例如<code><nowiki>{{#show:亚巴顿|?agility|link=none}}</nowiki></code>即可得到“17”
::{{main|help:Semantic Mediawiki/嵌入式查询}}

===使用ASK函数查询（query）===
[[file:ask example.jpg|right|300px|thumb|查询结果]]
*show函数只能展示一个数值，如果我们是想查询多个数值，就必须用到#ask函数
::{{main|help:Semantic Mediawiki/嵌入式查询}}
**<code><nowiki>{{#ask:<条件>|?<属性名称1>|?<属性名称2>|?<属性名称3>……|其他参数}}</nowiki></code>
ask函数默认返回一个表格，例如<code><nowiki>{{#ask:[[category:防具物品]]|?name en|?Item cost}}</nowiki></code>得到结果如左图。

需要注意的是，这里只是简单的介绍一下ask能做什么，对于SMW而言，#ask是最核心，最复杂的函数，这里不再展开赘述，如何灵活掌握和应用ask函数需要大量的实践和摸索。

===如何查看页面上的已有数值（property）===
通过特殊页面：“特殊:浏览(Special:Browse)”来实现
*写法一：www.yoursite.huiji.wiki/wiki/特殊:浏览/页面名称
*写法二：ww.yoursite.huiji.wiki/wiki/Special:Browse/页面名称

===#set函数===
我们在上面讲了如何取值，下面着重介绍如何赋值。解析器函数#set允许用户在页面中设定一个或若干数据（property及其value）
::{{main|帮助:解析器函数#set}}

===#subobject函数与子对象===
[[File:subobject.jpg|thumb|subobject(子对象)与页面的关系]]
上述的#set函数是通过在页面上直接建立属性，这里“页面（PAGE）”就是对象。除此之外，SMW还允许每个页面上外挂若干个“子对象”，然后子对象也可以像页面一样拥有自己的属性和数值，结构见右图。

====添加子对象====
::{{main|帮助:解析器函数#subobject}}

====查询子对象====
::{{main|help:Semantic Mediawiki/子对象查询}}

==在Lua中查询SMW==
*[https://github.com/SemanticMediaWiki/SemanticScribunto/blob/master/docs/README.md 官方文档]
在lua中查询ask的效率要高很多很多，而且对结果的操作更加随心所欲，因为返回的结果是一个合法的luaTable，可以利用lua函数做各种处理。

===mw.smw.ask===
<pre>
local _qry = {}
local etty = {
  'Activition',
}
for __ , _v in pairs(etty) do
  table.insert( _qry, '?'.._v )
end

_qry.mainlabel = '-'
_qry.limit = 1
table.insert(_qry, '[[Has skill id::'..xxxx..']]')
local result = mw.smw.ask( _qry )
--------------------------------------
if result then
  result = result[1]
  ocal _qry = {}
  local etty = {
    'Activition',
  }
  for __ , _v in pairs(etty) do
    table.insert( _qry, '?'.._v )
  end
  _qry.mainlabel = '-'
  _qry.limit = 1
  table.insert(_qry, '[[Has skill id::'..v['id']..']]')
  local result = mw.smw.ask( _qry )
  --------------------------------------
  if result then
    result = result[1]
      __activition = result['Activition'] or 'default value'
  end
end
        
</pre>

{{NavboxSMW}}
{{Data Help
|页面名=帮助:Semantic MediaWiki
|描述文字=Semantic MediaWiki
|解说=
|symbol=
|主分类=帮助
|子分类=复杂
|tags=机制,扩展,模板,编程,语义化,SMW
|sortkey=50800
|关键=no
|catsortkey=4
|guide=no
|难度=复杂
|角色=开发者
|灰机功能=no
}}
