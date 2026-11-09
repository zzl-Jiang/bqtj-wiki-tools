# 帮助:模块/Hello world

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3A%E6%A8%A1%E5%9D%97/Hello%20world
revid：42082 · 抓取时间：2026-11-09T14:27:10+08:00

---

{{LuaNav}}
学习程序语言，通常会从完成一个Hello world开始。

所以接下来我们就先讲下，如何在Mediawiki中，完成Hello world。

==模块==
在Mediawiki中，Lua代码必须保存在特定的[[h:help:命名空间#模块命名空间|命名空间]]下才能生效，该命名空间名字为<code>Module:</code>，也可以使用中文的<code>模块:</code>

例如我们可以创建一个文章，标题叫<code>Module:Foo</code>，该文章就会以Lua代码的形式，创建一个可供调用（invoke）的模块。

实际操作一下，创建一个<code>Module:Foo</code>（该例子中的模块名称就是冒号后面的“Foo”），内容为：
<pre>
local p = {}

function p.hello( frame )
    return "Hello, world!"
end

return p
</pre>

===注意===
*开头的<code>local p = {}</code>和结尾的<code>return p</code>不能省略

==调用模块==
模块创建好后，可以使用<code>#invoke</code>（或使用中文的<code>#调用</code>）这个解析器函数，来调用模块。

格式是<code><nowiki>{{#invoke:模块名称|函数名称|参数1|参数2...|参数N}}</nowiki></code>

{{新手帮助
|按照这个调用格式，如果我们想要调用之前创建好的那个模块，各个项目的取值方法：
*<code>模块名称</code>为<code>Foo</code>（这个Foo取自刚才我们的页面名<code>Module:Foo</code>中，半角冒号后面的<code>Foo</code>）
*<code>函数名称</code>为<code>hello</code>（这个hello，是我们刚刚代码中<code>function p.hello( frame )</code>中的<code>hello</code>）
*因为没有参数，所以不需要传入参数
所以最终调用的指令为<code><nowiki>{{#invoke:Foo|hello}}</nowiki></code>
}}

我们调用<code><nowiki>{{#invoke:Foo|hello}}</nowiki></code>，结果就会是：
<pre>
Hello, world!
</pre>

===什么时候在invoke的时候传递模板参数===
在上面的例子里，在模板里通过<code><nowiki>{{#invoke:模块名称|函数名称|参数1|参数2...|参数N}}</nowiki></code>调用lua模块时，传递了若干参数，这些参数都是模板里的参数，需要按照wikitext的语法书写，可能是<code><nowiki>{{{1|}}}</nowiki></code>、<code><nowiki>{{{2|}}}</nowiki></code>也可能是<code><nowiki>{{{paramn|{{{1|}}}}}}</nowiki></code>

这是一般常见的，用枚举的方法传递参数，但对于模板到底有哪些参数，特别是命名参都不太了解的情况下，很难一一列举，或者你觉得这样写很繁琐，也可以不用手写传递参数，而是可以在module里通过frame拿到全部的参数（<code>require('Module:Arguments').getArgs</code>）：
:[[帮助:模块/获取模板参数]]
