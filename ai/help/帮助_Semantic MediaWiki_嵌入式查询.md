# 帮助:Semantic MediaWiki/嵌入式查询

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3ASemantic%20MediaWiki/%E5%B5%8C%E5%85%A5%E5%BC%8F%E6%9F%A5%E8%AF%A2
revid：33386 · 抓取时间：2026-11-09T14:27:10+08:00

---

嵌入式查询是Semantic Mediawiki的核心功能之一，详细介绍如下
==解析器函数#ask==
语法：
<code><nowiki>{{#ask: <查询条件> |<?展示属性> | … }}</nowiki></code>

SMW的ask函数主要由三部分构成
*查询条件：即如何选择页面（参见：[[help:Semantic Mediawiki/选择页面|选择页面]]）
*要展示的属性：（参见：[[help:Semantic Mediawiki/结果呈现|结果呈现]]）
*参数：附加参数，详见下文
例子：
<pre><nowiki>
{{#ask:
 [[Category:人类]]
 [[Has fiction::联盟]] 
 |?HP
 |?MP
}}</nowiki></pre>
{{#ask:
 [[Category:人类]]
 [[Has fiction::联盟]] 
 |?hp
 |?mp
}}
===解析器函数#show===
语法：
<code><nowiki>{{#show: 页面 |?属性 }}</nowiki></code>
{{main|help:解析器函数#show}}
这种写法实际上等价于
<code><nowiki>{{#ask: 页面 |?属性 |mainlabel=-|headers=hide}}</nowiki></code>

==ask函数的参数==
上文引入了ask的两个参数“mainlabel”和“headers”。下面会介绍完整的ask参数
{| class="wikitable sortable"
! 参数
! 可填写的值
! 解释
|-
| <kbd>format</kbd>
| format类型
| 选择结果展示出来的格式 (参见[[Help:Semantic Mediawiki/结果的format|结果的format]])
|-
| <kbd>limit</kbd>
| 必须是非负数
| 打印出的最大结果数量 (在table下是行数)，默认值是50,最大值为100,超过100需要修改站点配置方案(需要联系站长或者职员)
|-
| <kbd>offset</kbd>
| 数值
| 起始位置，表示从第几个开始。例如<code><nowiki>limit=10|offset=4</nowiki></code>表示获取查询结果的第4个到第13个项目。
|-
| <kbd>sort</kbd>
| 查询属性的名字
| 制定一个查询属性，所有结果会按照这个属性值来排序 (参见[[Help:Semantic Mediawiki/选择页面|选择页面]])
|-
| <kbd>order</kbd>
| 升序<kbd>ascending</kbd>/<kbd>asc</kbd><br>降序<kbd>descending</kbd>/<kbd>desc</kbd>/<kbd>reverse</kbd><br>乱序<kbd>random</kbd>/<kbd>rand</kbd><br />
| 如何排序，默认方式是<kbd>ascending</kbd>（升序） (参见[[Help:Semantic Mediawiki/选择页面|选择页面]])<br>可以填写多个，用“,”分开（当排序关键字多于一个时,依次对多个sort生效）
|-
| <kbd>align</kbd>
| <kbd>right</kbd>, <kbd>center</kbd>, <kbd>left</kbd>
|只对format为<kbd>table</kbd> and <kbd>broadtable</kbd>时生效，决定文字的水平排列方式 (参见[[Help:Semantic Mediawiki/结果的format|结果的format]])
|-
| <kbd>headers</kbd>
| <kbd>show</kbd>, <kbd>plain</kbd>, <kbd>hide</kbd>
| 控制第一行的样式<kbd>show</kbd>是默认值。hide隐藏，plain是不带链接的纯文本
|- 
| <kbd>mainlabel</kbd>
| 纯文本
| 文本会被显示在第一行的第一个单元格内，如果是“-”则会隐藏第一列标题
|-
| <kbd>index</kbd>
| 数字
| 控制record类型中哪一个数值被展示，仅对property的类型（type）为record时生效。（参见[[Help:Semantic Mediawiki/Record类型|Record]]）
|-
| <kbd>link</kbd>
| <kbd>none</kbd>, <kbd>subject</kbd>, <kbd>all</kbd>
| 控制结果中的值是否带链接， <kbd>all</kbd> 为全部带链接，<kbd>subject</kbd>只有第一列带链接，<kbd>none</kbd>则是全部不带链接。
{{Note}} 链接亦可以通过对查询属性进行单独控制来取消，详情参见“[[help:Semantic Mediawiki/结果呈现|结果呈现]]部分”
|-
| <kbd>default</kbd>
| 纯文本
|当query返回结果为空值时所显示的文字
|-
| <kbd>intro</kbd>
| 纯文本
| 展示结果之前的文字描述
|-
| <kbd>outro</kbd>
| 纯文本
| 展示结果之后的文字内容
|-
| <kbd>searchlabel</kbd>
| 纯文本
| 当超过默认limit限制后，点击查看更多的链接文字
|}

==参数的一些应用==
我们可以强行不打印结果然后留下一个链接
<code><nowiki>{{#ask:[[category:战士]]|limit=0|searchlabel=点我查看更多}}</nowiki></code>
*结果：{{#ask:[[category:战士]]|limit=0|searchlabel=点我查看更多}}

也可以隐藏掉链接
<code><nowiki>{{#ask:[[category:战士]]|limit=3|searchlabel=}}</nowiki></code>
*结果：{{#ask:[[category:战士]]|limit=3|searchlabel=}}

===default===
<code><nowiki>{{#ask:[[category:盗贼]]|default=暂无}}</nowiki></code>
*结果：{{#ask:[[category:盗贼]]|default=暂无}}

==为结果排序==
<code><nowiki>{{#ask:[[hp::+]]|?hp|sort=hp}}</nowiki></code>
*结果：{{#ask:[[hp::+]]|?hp|sort=hp}}
===多关键字排序===
<code><nowiki>{{#ask:[[hp::+]]|?hp|?mp|sort=hp,mp|order=ascending,descending}}</nowiki></code>
*结果：{{#ask:[[hp::+]]|?hp|?mp|sort=hp,mp|order=ascending,descending}}
{{Note}}注意，此处“hp”和“mp”的属性类型均为“number”才能实现数字由大到小的排序，如果是page或者text，只会按照字符排序，详情参见[[help:Semantic Mediawiki/属性类型|属性的类型]]

==修改首行文字==
<code><nowiki>{{#ask:[[hp::+]]|?hp=生命值|?mp=法力值|mainlabel=英雄页面|sort=hp,mp|order=ascending,descending}}</nowiki></code>
*结果：{{#ask:[[hp::+]]|?hp=生命值|?mp=法力值|mainlabel=英雄页面|sort=hp,mp|order=ascending,descending}}

===一些技巧===
<code><nowiki>{{#ask:[[category:战士]]|?hp=生命值|?mp=法力值|?=战士|mainlabel=-}}</nowiki></code>
*结果：{{#ask:[[category:战士]]|?hp=生命值|?mp=法力值|?=战士|mainlabel=-}}
{{NavboxSMW}}
