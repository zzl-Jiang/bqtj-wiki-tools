# 帮助:Semantic MediaWiki/Quantity类型

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3ASemantic%20MediaWiki/Quantity%E7%B1%BB%E5%9E%8B
revid：33356 · 抓取时间：2026-11-09T14:27:10+08:00

---

'''Quantity类型'''是一种用来记录度量衡单位的属性
==语法==
*<code><nowiki>[[has type::quantity]]</nowiki></code>
==度量转换==
如果我们想定义1瓦特和千瓦、马力之间的关系，可以这样声明：
:<code><nowiki>[[Corresponds to::1 W]]</nowiki></code>
:<code><nowiki>[[Corresponds to::0.001 kW]]</nowiki></code>
:<code><nowiki>[[Corresponds to::0.0013410220 hp]]</nowiki></code>
进阶：
:<code><nowiki>[[Corresponds to::1 W, Watt, Watts,瓦,瓦特]]</nowiki></code>
:<code><nowiki>[[Corresponds to::0.0013410220 hp,bhp,horsepower,马力]]</nowiki></code>
==显示单位==
*<code><nowiki>[[display units::km,ft,miles]]</nowiki></code>
{{navboxSMW}}
