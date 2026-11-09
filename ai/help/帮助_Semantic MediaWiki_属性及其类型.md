# 帮助:Semantic MediaWiki/属性及其类型

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3ASemantic%20MediaWiki/%E5%B1%9E%E6%80%A7%E5%8F%8A%E5%85%B6%E7%B1%BB%E5%9E%8B
revid：33382 · 抓取时间：2026-11-09T14:27:10+08:00

---

'''属性'''（property）是SMW中最基本的数据单元，属性可以有不同的类型（data type）
==属性的定义==
===标准语法===
定义方式如下，会留下文字链接。
*<code><nowiki>[[属性名称::属性值]]</nowiki></code>
这是SMW的原生定义属性方法，本意是在文章之中将链接定义为“语义属性”，例如：
<pre>
[[is nation::中华人民共和国]]的首都是[[is capital::北京]]。
萨尔（[[Has name en::Thrall]]）曾经是[[Has fiction::部落]]的[[Has title::大酋长]]。
</pre>

===静默语法===
亦可以通过解析器函数<code>#set</code>来静默定义:
<code><nowiki>{{#set:属性名称=属性值}}</nowiki></code>
{{main|help:解析器函数#set}}
这种定义方法可以同时定义n条属性，且不会在页面留下任何内容。

==属性的类型==
SMW的属性可以有很多类型，默认配置文件下的属性如果不加任何声明，其属性是“page”，灰机wiki的默认SMW熟悉类型是“<code>text</code>”
*亦可以通过在属性页面（参见[[help:Semantic Mediawiki/命名空间|property命名空间]]）书写代码改变其类型：
*<code><nowiki>[[Has type::类型名称]]</nowiki></code>
**{{note}}在通过默认或是set函数命名属性时，“<code>Has type</code>”字段是不能占用的，因为这是SMW的系统保留属性，如果错误声明将会返回一条错误信息。
可填写的类型见下表：
{| class="wikitable"
!页面
!数据类型
!解释
!由……扩展提供
|-
|
|<kbd>Annotation URI</kbd>
|标注URI类型 与URL类似，极为少用
|Semantic MediaWiki
|-
|
|<kbd>Boolean</kbd>
|布尔值，数值为 (true/false)（中文下等同于是/否）
|Semantic MediaWiki
|-
|
|<kbd>Code</kbd>
|未经格式化的文本(类似Text)
|Semantic MediaWiki
|-
|
|<kbd>Date</kbd>
|时间点
|Semantic MediaWiki
|-
|
|<kbd>Email</kbd>
|电邮地址
|Semantic MediaWiki
|-
|
|<kbd>Geographic coordinate</kbd>
|地理位置坐标
|Semantic Maps
|-
|
|<kbd>Monolingual text</kbd>
|含有语言代码的文本
|Semantic MediaWiki
|-
|
|<kbd>Number</kbd>
|数字
|Semantic MediaWiki
|-
|
|<kbd>Page</kbd>
|<默认属性>维基页面，默认带有链接
|Semantic MediaWiki
|-
|
|<kbd>Quantity</kbd>
|自定义单位（度量衡） 包括数值和计数单位
|Semantic MediaWiki
|-
|
|<kbd>Record</kbd>
|记录类型，带有固定的序号
|Semantic MediaWiki
|-
|
|<kbd>Telephone number</kbd>
|基于<nowiki>RFC 3966</nowiki>标准的国际通用电话号码格式
|Semantic MediaWiki
|-
|
|<kbd>Temperature</kbd>
|温度 (类似 Quantity)
|Semantic MediaWiki
|-
|
|<kbd>Text</kbd>
|文本
|Semantic MediaWiki
|-
|
|<kbd>URL</kbd>
|URI、URN和URL
|Semantic MediaWiki
|}
===各种属性类型的实例 ===
<div style="max-width: 1500px; overflow: scroll;">
{| class='wikitable sortable'
!Datatype
!属性例子
!数值例子
!查询结果
!无连接查询（#-）结果
|-
|[[Special:Types/Annotation_URI|Annotation URI]]
|[[Property:Has annotation uri]]
|[[Has annotation_uri::http://www.semantic-mediawiki.org]]
|{{#show: {{FULLPAGENAME}} | ?Has annotation uri }}
|{{#show: {{FULLPAGENAME}} | ?Has annotation uri#- }}
|-
|[[Special:Types/Boolean|Boolean]]
|[[Property:Has boolean]]
|[[Has boolean::true]]
|{{#show: {{FULLPAGENAME}} | ?Has boolean }}
|{{#show: {{FULLPAGENAME}} | ?Has boolean#- }}
|-
|[[Special:Types/Code|Code]]
|[[Property:Has code]]
|[[Has code::Code
这是一个栗子
{{FULLPAGENAME}}
FULLPAGENAME]] 
|{{#show: {{FULLPAGENAME}} | ?Has code }}
|{{#show: {{FULLPAGENAME}} | ?Has code#- }}
|-
|[[Special:Types/Date|Date]]
|[[Property:Has date]]
|[[Has date::2015-05-22T17:32]]
|{{#show: {{FULLPAGENAME}} | ?Has date }}
|{{#show: {{FULLPAGENAME}} | ?Has date#- }}
|-
|[[Special:Types/EMail|EMail]]
|[[Property:Has email address]]
|[[Has email address::president@whitehouse.gov]]
|{{#show: {{FULLPAGENAME}} | ?Has email address }}
|{{#show: {{FULLPAGENAME}} | ?Has email address#- }}
|-
|[[Special:Types/Geographic coordinates|Geographic coordinate]]
|[[Property:Has coordinates]]
|[[Has coordinates::32°42′54″ N, 117°9′45″ W]]
|{{#show: {{FULLPAGENAME}} | ?Has coordinates }}
|{{#show: {{FULLPAGENAME}} | ?Has coordinates#- }}
|-
|[[Special:Types/Number|Number]]
|[[Property:Has number]]
|[[Has number::47000.11]]
|{{#show: {{FULLPAGENAME}} | ?Has number }}
|{{#show: {{FULLPAGENAME}} | ?Has number#- }}
|-
|[[Special:Types/Page|Page]]
|[[Property:Has example]]
|[[Has example::Semantic MediaWiki]]
|{{#show: {{FULLPAGENAME}} | ?Has example }}
|{{#show: {{FULLPAGENAME}} | ?Has example#- }}
|-
|[[Special:Types/Quantity|Quantity]]
|[[Property:Area]]
|[[Area::1052km²]]
|{{#show: {{FULLPAGENAME}} | ?Area }}
|{{#show: {{FULLPAGENAME}} | ?Area#- }}
|-
|[[Special:Types/Record|Record]]
|[[Property:Soccer result]]
|[[Soccer result::2016-09-01;中国;韩国;2;3]]
|{{#show: {{FULLPAGENAME}} | ?Soccer result }}
|{{#show: {{FULLPAGENAME}} | ?Soccer result#- }}
|-
|[[Special:Types/Telephone number|Telephone number]]
|[[Property:Telephone number]]
|[[Telephone number::+1-800-225-5288]]
|{{#show: {{FULLPAGENAME}} | ?Telephone number }}
| {{#show: {{FULLPAGENAME}} | ?Telephone number#- }}
|-
|[[Special:Types/Temperature|Temperature]]
|[[Property:Has temperatureExample]]
|[[Has temperatureExample::23°C]]
|{{#show: {{FULLPAGENAME}} | ?Has temperatureExample }}
|{{#show: {{FULLPAGENAME}} | ?Has temperatureExample#- }}
|-
|[[Special:Types/Text|Text]]
|[[Property:SomeProperty]]
|[[SomeProperty::Did you create the page for Tokyo 東京 ? Yes ✓]]
|{{#show: {{FULLPAGENAME}} | ?SomeProperty }}
|{{#show: {{FULLPAGENAME}} | ?SomeProperty#- }}
|-
|[[Special:Types/URL|URL]]
|[[Property:Has_URL]]
|[[Has_URL::http://www.whitehouse.gov]]
|{{#show: {{FULLPAGENAME}} | ?Has_URL }}
|{{#show: {{FULLPAGENAME}} | ?Has_URL#- }}
|}</div>

==Boolean类型==
{{main|help:Semantic Mediawiki/Boolean类型}}
==Code类型==
类似type，有着特殊的样式，用来装在技术性内容，很少用。
==Date类型==
{{main|help:Semantic Mediawiki/Date类型}}

==Monolingual text==
{{main|help:Semantic Mediawiki/Monolingual text类型}}

==Number类型==
Number类型取代了1.0时代的float和integer两种类型
*number类型可以正确的按照数学大小来排序，否则只能像text一样按照字符排序（40>500）
*number类型的数字可以有分位符，例如:<code><nowiki>{{#show:{{FULLPAGENAME}}|?Has number}}</nowiki></code>
结果：{{#show:{{FULLPAGENAME}}|?Has number}}

如果不希望以这种形式出现，可以书写为
*<code><nowiki>{{#show:{{FULLPAGENAME}}|?Has number#}}</nowiki></code>
结果：{{#show:{{FULLPAGENAME}}|?Has number#}}
==Page类型==
Page是SMW的默认属性类型，他具有如下特点
*自带链接
*全部255位字符都可以被查询
*当重定向发生后，page类型的属性也会被自动重定向
==Quantity==
{{main|help:Semantic Mediawiki/Quantity类型}}
==Record==
{{main|help:Semantic Mediawiki/Record类型}}
==Text==
<code>'''Text是灰机开启SMW后默认的属性类型，覆盖了SMW的原始配置（Page型），请多加留意'''</code>

Text是SMW中除了PAGE之外最常用的属性类型，它具有如下特点
*长度可以超过255字符（但超过72字符时只有前40字符会被搜索，其他情况下最多搜索72个字符）
*可以使用标记语言（br、链接等等）
*不会自动重定向
*不支持[[help:Semantic Mediawiki/负属性|负属性]]反查
除此之外，通过设定允许值，可以限定text属性的内容范围，参见：[[help:Semantic Mediawiki/允许值|允许值]]

==Temperature==
Temperature是SMW中预设好转换关系的quantity属性，支持的单位如下：
*K：开，热力学温度（默认值）
*℃：摄氏
*°F：华氏
*°R：兰式温标

{{navboxSMW}}
