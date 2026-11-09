# 帮助:Semantic MediaWiki/结果的format

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3ASemantic%20MediaWiki/%E7%BB%93%E6%9E%9C%E7%9A%84format
revid：33390 · 抓取时间：2026-11-09T14:27:10+08:00

---

本文主要介绍SMW的#ask函数可选参数“format”中支持的数据类型，例如table、template等等，SMW会将查询结果按照对应的格式展现出来。

==由Semantic Mediawiki提供的默认格式==
相关格式的细节和参数设置请点开链接查看。
{| class="wikitable sortable"
!格式
!描述
!添加于
!分类
!作者
|-
|rdf
|将结果输出为RDF
|1.5.5
|export
|Markus Krötzsch
|-
|feed
|将结果输出为RSS和订阅feed
|1.8.0
|export
feed
xml
|MWJames
|-
|dsv
|将结果输出为UNIX式样的分隔符分隔型取值（Delimiter Separated Value，DSV）
|1.6.0
|export
plaintext
|Jeroen De Dauw
|-
|[[#jason|json]]
|将结果输出为JASON格式
|1.4.2
|export
plaintext
|MWJames
Jeroen De Dauw
Fabian Howahl
|-
|csv
|将结果输出为Windows风格的逗号分隔型取值格式
|1.2.1
|export
plaintext
|Nathan Yergler
Markus Krötzsch
|-
|[[#debug|debug]]
|用于分析查询应答过程之中的问题的调试信息
|0.7
|misc
|Markus Krötzsch
|-
|[[#count|count]]
|返回结果的个数（匹配页面数量的计数），而不是结果本身
|0.7
|misc
|Markus Krötzsch
|-
|[[help:Semantic Mediawiki/embedded格式|embedded]]
|嵌入所选定的文章
|0.7
|misc
|Markus Krötzsch
|-
|[[help:Semantic Mediawiki/template格式|template]]
|利用所指定的模板对结果进行处理并展示
|0.7
|misc
|Markus Krötzsch
|-
|[[help:Semantic Mediawiki/ol格式|ol]]
|将结果输出为有序列表
|0.7
|misc
|Markus Krötzsch
|-
|[[help:Semantic Mediawiki/table格式|table]]
|将结果输出为表格
|0.4
|misc
|Markus Krötzsch
|-
|[[help:Semantic Mediawiki/ul格式|ul]]
|将结果输出为无序列表
|0.7
|misc
|Markus Krötzsch
|-
|[[help:Semantic Mediawiki/category格式|category]]
|采用首字母为小节标题，并采用MediaWiki类别页面样式的分栏式列表
|1.4.3
|misc
|David Loomer
Yaron Koren
|-
|[[help:Semantic Mediawiki/list格式|list]]
|将结果输出为以逗号（默认分隔符）分隔的清单（不换行）
|0.7
|misc
|Markus Krötzsch
|-
|[[#broadtable|broadtable]]
|将结果输出为宽表格
|0.4
|misc
|Markus Krötzsch
|}

==Semantic Mediawiki扩展所提供的格式==
{| class="wikitable sortable"
!格式
!描述
!提供方
!新增于
!类别
!作者
|-
|tagcloud
|在标签云（tag cloud）之中显示所查询到的数据
|Semantic Result Formats（语义结果格式）
|1.5.3
|misc
|Jeroen De Dauw
|-
|bibtex
|生成供采用BibTeX格式文件下载数据的链接
|Semantic Result Formats（语义结果格式）
|1.4.3
|export
|Steren Giannini
Frank Dengler
|-
|product
|用于显示所查询到的全部数值型数据的乘积
|Semantic Result Formats（语义结果格式）
|1.6.0
|math
|Jeroen De Dauw
|-
|outline
|根据属性取值，采取层级结构式大纲（hierarchical outline）的方式罗列页面
|Semantic Result Formats（语义结果格式）
|1.4.3
|misc
|Yaron Koren
|-
|map
|在交互式地图上显示所查询到的地理数据
|Semantic Maps（语义地图）
|0.1
|geo
|Jeroen De Dauw
|-
|googlepie
|利用Google Charts API（谷歌条图应用编程接口）生成饼图
|Semantic Result Formats（语义结果格式）
|1.4.0
|charts
|Denny Vrandecic
|-
|googlemaps
|在谷歌地图（Google Maps）上显示所查询到的地理数据
|Semantic Maps（语义地图）
|0.1
|geo
|Jeroen De Dauw
|-
|googlebar
|利用Google Charts API（谷歌条图应用编程接口）生成条图
|Semantic Result Formats（语义结果格式）
|1.4.0
|charts
|Denny Vrandecic
|-
|hash
|逗号分隔型列表，且带有括在英文圆括号当中的额外输出以及额外的格式编排选项
|Semantic Result Formats（语义结果格式）
|1.6.1
|misc
|Danwe
|-
|gallery
|用于将查询结果显示为动态画廊，并且其输出与使用MediaWiki内置画廊标签时相同。
|Semantic Result Formats（语义结果格式）
|1.5.0
|misc
|Rowan Rodrik van der Molen
Jeroen De Dauw
|-
|icalendar
|采用iCalendar格式导出数据
|Semantic Result Formats（语义结果格式）
|1.4.2
|export
|Markus Krötzsch
Denny Vrandecic
Jeroen De Dauw
|-
|jqplotpie
|利用 jqPlot Javascript 库生成饼图
|Semantic Result Formats（语义结果格式）
|1.5.1
|charts
|Sanyam Goyal
Yaron Koren
MWJames
|-
|average
|用于显示所查询到的全部数值型数据的均值
|Semantic Result Formats（语义结果格式）
|1.4.2
|math
|Yaron Koren
|-
|kml
|采用KML格式来导出地理数据
|Semantic Maps（语义地图）
|1
|geo
export
|Jeroen De Dauw
|-
|oltree
|将查询结果显示为树状结构（嵌套式HTML有序列表）
|Semantic Result Formats（语义结果格式）
|1.7.1
|misc
|F.trott
|-
|openlayers
|在OpenLayers地图上显示地理数据
|Semantic Maps（语义地图）
|0.1
|geo
|Jeroen De Dauw
|-
|calendar
|在日历上显示关联有日期时间的页面
|Semantic Result Formats（语义结果格式）
|1.4.0
|time
|Yaron Koren
|-
|timeline
|采用交互式事件轴（interactive eventlines）来显示查询结果
|Semantic Result Formats（语义结果格式）
|1.4.0
|misc
|Markus Krötzsch
Jeroen De Dauw
|-
|timeline
|采用交互式时间轴（interactive timelines）来显示查询结果
|Semantic Result Formats（语义结果格式）
|1.4.0
|misc
|Markus Krötzsch
Jeroen De Dauw
|-
|tree
|将查询结果显示为树状结构（嵌套式HTML项目符号列表）
|Semantic Result Formats（语义结果格式）
|1.7.1
|misc
|F.trott
|-
|array
|逗号分隔型列表，且带有括在英文圆括号当中的额外输出以及额外的格式编排选项
|Semantic Result Formats（语义结果格式）
|1.6.1
|misc
|Danwe
|-
|yahoomaps
|在雅虎地图（Yahoo! Maps）上显示所查询到的地理数据
|Semantic Maps（语义地图）
|0.1
|geo
|Jeroen De Dauw
|-
|median
|用于显示所查询到的全部数值型数据的中位数
|Semantic Result Formats（语义结果格式）
|1.6.0
|math
|Jeroen De Dauw
|-
|sum
|用于显示所查询到的全部数值型数据的总计（或者说总和）
|Semantic Result Formats（语义结果格式）
|1.4.2
|math
|Nathan Yergler
|-
|max
|用于显示所查询到的全部数值型数据的最大值
|Semantic Result Formats（语义结果格式）
|1.4.2
|math
|Yaron Koren
|-
|min
|用于显示所查询到的全部数值型数据的最小值
|Semantic Result Formats（语义结果格式）
|1.4.2
|math
|Yaron Koren
|-
|vcard
|采用vCard格式导出数据
|Semantic Result Formats（语义结果格式）
|1.4.2
|export
|Markus Krötzsch
Denny Vrandecic
Frank Dengler
|}
==broadtable==
broadtable和table没有本质区别，只是width=100%
==JSON==
专属参数
prettprint：类型（yes/no)，默认值为空，开启后会优化排版格式
===例子===
<pre>
<nowiki>{{#ask:[[has fiction::+]]
|?hp|?mp
|format=JSON
|prettyprint=yes}}
</nowiki>
</pre>

结果：（请自行使用notepad++等工具打开查看）
{{#ask:[[has fiction::+]]
|?hp|?mp
|format=JSON
|prettyprint=yes}}

==debug==
SMW提供的debug工具，帮助判断是在哪一步出了何种错误
===例子===
<code><nowiki>{{#ask:[[has fiction::+]]
|?hp|?mp
|format=debug
}}</nowiki></code>

debug结果：

{{#ask:[[has fiction::+]]
|?hp|?mp
|format=debug
}}
{{NavboxSMW}}
