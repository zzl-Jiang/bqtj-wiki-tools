# 帮助:Semantic MediaWiki/负属性

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3ASemantic%20MediaWiki/%E8%B4%9F%E5%B1%9E%E6%80%A7
revid：33392 · 抓取时间：2026-11-09T14:27:10+08:00

---

'''负属性'''（inverse properties）是SMW在嵌入式查询中的一种特殊方式，查询的'''方向'''会反转“inverse”。
==语法==
<code>-</code>
例子：<code><nowiki>[[-Has fiction::联盟]]</nowiki></code>

===实例===
*<code><nowiki>{{#ask:[[-Has fiction::Test页面/吉安娜]]}}</nowiki></code>
结果：{{#ask:[[-Has fiction::Test页面/吉安娜]]}}
===其他写法的比较===
*<code><nowiki>{{#ask:[[Test页面/吉安娜]]|?Has fiction|mainlabel=-|headers=hide}}</nowiki></code>:{{#ask:[[Test页面/吉安娜]]|?Has fiction|mainlabel=-|headers=hide}}
*<code><nowiki>{{#show:Test页面/吉安娜|?Has fiction}}</nowiki></code>:{{#show:Test页面/吉安娜|?Has fiction}}

==subobject的应用==
这一属性主要应用在子对象的查询上
{{main|help:Semantic Mediawiki/子对象查询}}

{{navboxSMW}}
