# 帮助:Semantic MediaWiki/Record类型

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3ASemantic%20MediaWiki/Record%E7%B1%BB%E5%9E%8B
revid：33358 · 抓取时间：2026-11-09T14:27:10+08:00

---

'''记录'''（Record）类型，是SMW中的一种属性类型，通过多种其他类型的属性以“Has field”的方式组合成为一条记录。
==赋值语法==
*成为Record类型：<code><nowiki>[[Has type::Record]]</nowiki></code>
*声明记录格式：<code><nowiki>[[Has fields::属性A; 属性B; 属性C]]</nowiki></code>
**属性A、属性B、属性C的type都需要单独在各自的属性页面定义。
例子：[[Property:Soccer_result]]
*为Soccer result赋值：<code><nowiki>{{#Set:Soccer result=2016-09-01;中国;韩国;2;3}}</nowiki></code>

===赋值需要注意的地方===
*部分数值可以缺省，使用?或者空着，例如<code><nowiki>{{#Set:Soccer result=2016-09-01;?;;2;3}}</nowiki></code>
*最后的数值可以直接省略，record会自动装入前面的数值，例如：<code><nowiki>{{#Set:Soccer result=2016-09-01;中国;韩国;}}</nowiki></code>
*赋值用到“<code>;</code>”的地方需要使用<code>\</code>进行mask，例如：<code><nowiki>{{#Set:Soccer result=2016-09-01;队伍A\;队伍B联队;队伍C;0;0}}</nowiki></code>

===记录赋值实例===
记录赋值的好处就是可以将页面中分散的属性集合起来成为一组新的数据，例如在正文中收集内容：
:<code><nowiki>[[Soccer guest team::中国]]队在[[Soccer date::2034年6月1日]]举行的[[Soccer home team::刚果]]世界杯中[[Soccer guestscore::10]]:[[Soccer homescore::0]]击败了东道主夺冠。</nowiki></code>
然后写一段代码来收集上述数据（完全可以封装成一个模板）
<pre>
<nowiki>{{#set:
Soccer result={{#show:{{FULLPAGENAME}}|?Soccer date}};
{{#show:{{FULLPAGENAME}}|?Soccer guest team}};
{{#show:{{FULLPAGENAME}}|?Soccer home team}};
{{#show:{{FULLPAGENAME}}|?Soccer guestscore}};
{{#show:{{FULLPAGENAME}}|?Soccer homescore}}
}}</nowiki>
</pre>
结果：[[Soccer guest team::中国]]队在[[Soccer date::2034年6月1日]]举行的[[Soccer home team::刚果]]世界杯中[[Soccer guestscore::10]]:[[Soccer homescore::0]]击败了东道主夺冠。
{{#set:
Soccer result={{#show:{{FULLPAGENAME}}|?Soccer date}};{{#show:{{FULLPAGENAME}}|?Soccer guest team}};{{#show:{{FULLPAGENAME}}|?Soccer home team}};{{#show:{{FULLPAGENAME}}|?Soccer guestscore}};{{#show:{{FULLPAGENAME}}|?Soccer homescore}}
}}

==查询==
上面我们成功记录了一条record，下面介绍如何query
===打印record===
<pre>
<nowiki>{{#ask: [[{{FULLPAGENAME}}]] |?Soccer result
}}</nowiki>
</pre>
结果：{{#ask: [[{{FULLPAGENAME}}]] |?Soccer result}}
===打印record细节===
<pre><nowiki>
{{#ask:
 [[{{FULLPAGENAME}}]]
 |?Soccer result
 |?Soccer result#MEDIAWIKI=日期 |+index=1
 |?Soccer result=客队 |+index=2
 |?Soccer result=主队 |+index=3
 |?Soccer result=客队得分 |+index=4
 |?Soccer result=主队得分 |+index=5
}}</nowiki>
</pre>
结果：
{{#ask:
 [[{{FULLPAGENAME}}]]
 |?Soccer result
 |?Soccer result#MEDIAWIKI=日期 |+index=1
 |?Soccer result=客队 |+index=2
 |?Soccer result=主队 |+index=3
 |?Soccer result=客队得分 |+index=4
 |?Soccer result=主队得分 |+index=5
}}
===查询===
record的每个field都可以单独设定条件，例如，我们要查询的条件如下：
#球赛日期再2000年之后
#中国队是客场
#中国队的对手不是日本队
#双方任意比分
ask书写如下：

:<code><nowiki>{{#ask:[[Soccer result::>2000/01/01;中国;!日本;?;?]]</nowiki></code>
:<code><nowiki>|?Soccer result}}</nowiki></code>

结果：
{{#ask:[[Soccer result::>2000/01/01;中国;!日本;?;?]]
|?Soccer result}}

关于查询语法，参考：[[help:Semantic Mediawiki/选择页面|选择页面]]

==替代方案==
===subobject===
某种意义上来说，Record的功能完全被函数#subobject取代，可以酌情选择究竟是用record还是#subobject
{{main|help:解析器函数#subobject}}
===array===
:需要扩展Arrays
{{main|help:解析器函数#Array}}
{{navboxSMW}}
