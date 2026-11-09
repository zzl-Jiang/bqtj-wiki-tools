# 帮助:Wiki标记语言

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3AWiki%E6%A0%87%E8%AE%B0%E8%AF%AD%E8%A8%80
revid：39562 · 抓取时间：2026-11-09T14:27:10+08:00

---

{{编辑手册nav}}
'''Wiki标记语言'''（'''[[wikipedia:Wiki markup language|Wiki markup language]]'''），亦称'''Wiki Markup'''、'''Wikitext'''、'''wiki代码'''，是一种轻量级标记（Markup）语言，被用于撰写Wiki网页，例如维基百科，最初是一个简单化的，非正统的，中间性的HTML。它的最终目的是被wiki软件转换成HTML，并且重新回到浏览器中。该语言最初创建于1995年，在最初的wiki站点WikiWikiWeb用于格式化页面。


==构成==
[[File:wikitext介绍.jpg|600px]]
*'''样式控制'''：类似现在流行的Markdown语言，主要是HTML语言的简化写法。
*'''逻辑运算'''：通过[[help:解析器函数|解析器函数]]扩展提供，现在已经被吸收成为MediaWiki的默认组件，并可以通过其他扩展增加新的函数，适用于逻辑结构简单、嵌套较少的场景，能够便捷的为编辑者提供一些格式化、判断上的便利。对于较为复杂的逻辑运算，我们推荐使用[[帮助:模块|Lua]]模块来实现。
*'''数据存储与查询'''：非默认功能，通过[[帮助:Semantic_Mediawiki|Semantic MediaWiki]]扩展提供，藉由新定义的解析器函数来实现数据的存、查。由于性能问题，更适合文字类的图谱化信息，对于大批量、频繁更新的结构化数据，wikitext已经很难胜任，在灰机，我们推荐使用[[帮助:MongoDB支持|JSON和MongoDB]]来实现。

==概述==
===初衷===
wikitext在最初的使命是一种简化书写的HTML语言
*例如，我们通过“<code><nowiki>[[链接]]</nowiki></code>”即可书写一个站点的内链，而不用手打一串
<code><nowiki><a href="http://www.huiji.wiki/wiki/链接" class="extiw" title="链接"><i class="fa fa-paperclip"></i> 页面分类</a></nowiki></code>

大部分情况下，在MediaWiki的源代码编辑器中，wikitext可以与HTML语言混用，除非是一些有注入风险的html标签和属性，譬如<code><a></code>和CSS属性中的<code>url</code>，他们会被wikitext处理掉，无法生效。
*这些可以通过JavaScript来异步添加，当然，这需要额外的[[帮助:开发者101|开发者权限]]。
*除了使用JS之外，灰机还提供了[[帮助:Mustache模板|Mustache模板]]，在Mustache中，可以自由的书写全部的HTML语言（以及JavaScript），同样需要开发者权限。

===引入逻辑===
随着维基的发展，wikitext引入了一个重要的概念——“[[help:解析器函数|解析器函数]]”，从而其内容和功能也从单纯的样式控制扩展到了“样式控制”+“逻辑运算”。

这一变革带来了许多深远的影响，MediaWiki也因此以其独树一帜的逻辑运算功能成为维基软件中最全能的一个。但也带来了一些缺陷，并在日后逐渐浮出水面：
*MediaWiki的解析器函数使用的语法是<code><nowiki>{{#}}</nowiki></code>+参数（arguments）而非真正逻辑语言常用的起止符配对机制。这使得一段逻辑有多长都要全部放在双括号中，结果就是wikitext书写的逻辑嵌套非常难读、难以维护并且给可视化编辑器造成了巨大的兼容障碍（需要parser/escape很多极端的情况），作为参数分隔的管道符“<code>|</code>”还常常与书写表格的pipe语法互相冲突导致样式解析失常。
*解析器函数需要被MediaWiki的Parser进行处理，样式控制的部分被还原成HTML，逻辑部分需要被处理成PHP函数，在特别复杂的wikitext嵌套情况下会导致网页加载速度变慢。极端情况下（例如高频度的?action=purge或其他触及批量刷新缓存的操作），还有可能卡死数据库（突出表现在Semantic MediaWiki的#ask和#show函数上）。

===替代方案===
*'''逻辑运算'''：随着[[帮助:模块|Lua]]被引入MediaWiki，这种真正的程序语言可以完全取代解析器函数，以绕过效率较低的parser机制，从而大大减少页面加载、渲染所需的时间。
*'''数据查询'''：灰机引入了全新的[[帮助:MongoDB支持|JSON+MongoDB]]架构，通过Lua函数来实现数据查询，可以有效减轻对关系型数据库的依赖和压力，同时提高开发的灵活性和查询效率。类似的架构还有在gemepedia上被广泛应用的Cargo（基于关系型数据库的表格存储、查询语法）。

==灰机wiki支持的标记语法==
灰机采用MediaWiki搭建，MediaWiki支持大多数常见的HTML标签。
:主条目：'''[[帮助:编辑页面]]'''
关于逻辑运算部分请参考
:主条目：'''[[帮助:解析器函数]]'''
关于数据存储和查询可以使用SMW
:主条目：'''[[帮助:Semantic_Mediawiki|Semantic MediaWiki]]'''
{{Data Help
|页面名=帮助:Wiki标记语言
|描述文字=Wiki标记语言(Mark up)
|解说=
|symbol=<i class="fa fa-wikipedia-w" aria-hidden="true"></i>
|主分类=帮助
|子分类=入门
|tags=编辑,维基化
|sortkey=31
|关键=yes
|catsortkey=2
|guide=no
|难度=入门
|角色=编辑者
|灰机功能=no
}}
