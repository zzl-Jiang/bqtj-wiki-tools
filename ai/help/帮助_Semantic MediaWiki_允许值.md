# 帮助:Semantic MediaWiki/允许值

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3ASemantic%20MediaWiki/%E5%85%81%E8%AE%B8%E5%80%BC
revid：33376 · 抓取时间：2026-11-09T14:27:10+08:00

---

'''允许值'''（Allows value）是SMW的一种特殊属性，它能够限定一个属性（property）所被允许的值（value）
==例子==
我们可以为<code>[[help:Semantic Mediawiki/属性类型|property]]:职业</code>做一个允许值限定：
:<code><nowiki>[[Allows value::战士]]</nowiki></code>
:<code><nowiki>[[Allows value::法师]]</nowiki></code>
:<code><nowiki>[[Allows value::术士]]</nowiki></code>
:<code><nowiki>[[Allows value::德鲁伊]]</nowiki></code>
:<code><nowiki>[[Allows value::牧师]]</nowiki></code>
:<code><nowiki>[[Allows value::圣骑士]]</nowiki></code>
:<code><nowiki>[[Allows value::猎人]]</nowiki></code>
:<code><nowiki>[[Allows value::潜行者]]</nowiki></code>
:<code><nowiki>[[Allows value::萨满]]</nowiki></code>
:<code><nowiki>[[Allows value::武僧]]</nowiki></code>
:<code><nowiki>[[Allows value::死亡骑士]]</nowiki></code>
:<code><nowiki>[[Allows value::恶魔猎手]]</nowiki></code>

==排序==
对于类型为[[help:Semantic Mediawiki/属性类型#text|text]]的属性，可以制定一个排位顺序，语法如下：
:<code><nowiki>[[Allows value::a - 战士]]</nowiki></code>
:<code><nowiki>[[Allows value::b - 法师]]</nowiki></code>
:<code><nowiki>[[Allows value::c - 术士]]</nowiki></code>
:<code><nowiki>[[Allows value::d - 德鲁伊]]</nowiki></code>
:<code><nowiki>[[Allows value::e - 牧师]]</nowiki></code>

*通过排序，就可以使用“大于”和“小于”来筛选属性范围：
{{main|help:Semantic Mediawiki/选择页面}}

:<code><nowiki>[[property name::<c-术士]]</nowiki></code>

{{navboxSMW}}
