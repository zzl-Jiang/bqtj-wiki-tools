# 帮助:Semantic MediaWiki/概念

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3ASemantic%20MediaWiki/%E6%A6%82%E5%BF%B5
revid：33388 · 抓取时间：2026-11-09T14:27:10+08:00

---

概念（Concept）是SMW用来存储查询的页面，可以被理解为“动态分类”。藉由描述该概念的条件，会组成一个跨分类的概念集合，并提供给嵌入式查询功能作为搜索范围。
==定义概念==
概念的定义必须在命名空间为“concept”的页面下进行，例如我们在<code>Concept:Samantic Web envents 2008</code>页面下书写下列代码，就定义了一个名为“Samantic Web envents 2008”的概念
例如：
::<code><nowiki>{{#concept:</nowiki></code>
:: <code><nowiki>[[Category:Event]]</nowiki></code>
:: <code><nowiki>[[Start date::> Jan 1 2008]]</nowiki></code>
:: <code><nowiki>[[Start date::< Dec 31 2008]]</nowiki></code> 
::<code><nowiki>}}</nowiki></code>

==概念嵌套==
概念的定义中可以嵌套其他的定义，例如
::<code><nowiki>{{#concept:</nowiki></code>
:: <code><nowiki>[[Concept::Events in 2007]]</nowiki></code>
:: <code><nowiki>[[Start date::> Jan 1 2008]]</nowiki></code>
:: <code><nowiki>[[Start date::< Dec 31 2008]]</nowiki></code> 
::<code><nowiki>}}</nowiki></code>

{{navboxSMW}}
