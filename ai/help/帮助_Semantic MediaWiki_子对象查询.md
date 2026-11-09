# 帮助:Semantic MediaWiki/子对象查询

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3ASemantic%20MediaWiki/%E5%AD%90%E5%AF%B9%E8%B1%A1%E6%9F%A5%E8%AF%A2
revid：35322 · 抓取时间：2026-11-09T14:27:10+08:00

---

本文介绍的是SMW中的子对象（subobject）概念而非#subobject函数，如果需要查询函数的使用，{{main|帮助:解析器函数#subobject}}
==查询当前页面上的所有子对象==
<code><nowiki>{{#ask: [[-Has subobject::{{FULLPAGENAME}}]] }}</nowiki></code>
例子:<br />
先在页面上定义两个子对象<!--
-->{{#subobject:Thrall
|Has race=orc
|Has class=shaman
}}<!---->{{#subobject:Jaina
|Has race=human
|Has class=mage
}}<!--
--><pre>
{{#subobject:Thrall
|Has race=orc
|Has class=shaman
}}

{{#subobject:Jaina
|Has race=human
|Has class=mage
}}
</pre>
'''查询'''：
<pre>
{{#ask: [[-Has subobject::{{FULLPAGENAME}}]] 
|?Has race
|?Has class
}}
</pre>
'''结果如下'''
{{#ask: [[-Has subobject::{{FULLPAGENAME}}]] 
|?Has race
|?Has class
}}

*注意"-" 此处使用的查询条件里用到了负属性概念，{{main|help:Semantic Mediawiki/负属性}}

==查询特定的属性==
===show'''本页'''面特定子对象的某个值===
<code><nowiki>{{#show:#Thrall|?Has race}}</nowiki></code>
结果：{{#show:#Thrall|?Has race}}
===show其他页面特定子对象的某个值===
<code><nowiki>{{#show:Test页面#Mafurion|?Has class}}</nowiki></code>
结果：{{#show:Test页面#Mafurion|?Has class}}
===ask本页面特定子对象===
<code><nowiki>{{#ask:[[#Thrall]]|?Has race|?Has class}}</nowiki></code>
结果：{{#ask:[[#Thrall]]|?Has race|?Has class}}
===ask其他页面特定子对象===
<code><nowiki>{{#ask:[[Test页面#Mafurion]]|?Has race|?Has class}}</nowiki></code>
结果：{{#ask:[[Test页面#Mafurion]]|?Has race|?Has class}}

==查询子对象父对象的某个属性==
===方法一===
例子STEP1:<br />
<pre>
{{#ask: [[Has race::night elf]]
|format=template 
|template=SMWexampletemplate/1
|link=none
}}
</pre>
例子STEP2，在<code>SMWexampletemplate/1</code> 里
<pre>
{{#ask: [[Has subobject::{{{1}}}]]
|?Has author
|?Has game
}}
</pre>
结果：
{{#ask: [[Has race::night elf]]
|format=template 
|template=SMWexampletemplate/1
|link=none
}}

===方法二===
{{main|help:解析器函数#arraymap}}
<code><nowiki>{{#arraymap:{{#ask: [[Has race::night elf]]|link=none}}|,|@@@@|{{#ask:[[Has subobject::@@@@]]|?Has author|?Has game}}}}</nowiki></code>

结果：
{{#arraymap:{{#ask: [[Has race::night elf]]|link=none}}|,|@@@@|{{#ask:[[Has subobject::@@@@]]|?Has author|?Has game}}}}
{{NavboxSMW}}
