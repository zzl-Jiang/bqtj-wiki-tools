# 帮助:MongoDB支持

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3AMongoDB%E6%94%AF%E6%8C%81
revid：42455 · 抓取时间：2026-11-09T14:27:09+08:00

---

{{编辑手册nav}}{{版本要求|2.2.0}}
'''MongoDB'''是一款著名的nosql数据库。灰机通过引入MongoDB的支持，实现了结构化数据的存储和查找，使得具有编程能力的站长可以更加细腻便捷地构筑维基。
MongoDB的数据非常适合与[[帮助:Mustache模板|Mustache模板]]搭配使用。
==功能概述==
*目的与使用Semantic MediaWiki类似，用以在维基上存储数据并在文章页面有针对性的查询和聚合。
*这是一项灰机wiki单独开发的功能，仅在本维基平台上提供技术支持，其他使用MediaWiki的托管平台不保证此类功能一定存在并能够按照本文档所述的方法进行操作。

== 对比 ==
{| class="wikitable"
|-
! 数据解决方案 !! 藉由Extension !! 数据库形式 !! 存储方式 !! 查询
|-
| SMW || Semantic MediaWiki || MySQL / SPARQL || Wikitext(解析器函数)  || [[帮助:解析器函数|解析器函数]]、[[帮助:模块|lua模块（module）]]
|-
| 灰机Mongo || HuijiMidware || MongoDB || data页面  || 默认仅支持[[帮助:模块|lua模块（module）]] <br>SMongo 支持使用[[帮助:模板|模板（template）]]化的SMW语法查询
|}

== 存储数据 ==
在Data（3500）[[help:命名空间|命名空间]]下，通过为标题添加后缀，内容类型将会从纯文本变为指定类型。

例如，以.json结尾的条目，会自动将内容类型变为Json数据。以.tab结尾的条目，将自动转换为表格型。tabx是对tab进行的扩展，突破了表格只能存储二维数据的限制。具体方法请参阅[https://www.npmjs.com/package/excel-as-json 这里]。

{| class="wikitable"
!命名
!普通Data页面
!Data:xxx<code>.json</code>
!Data:xxx<code>.tab</code>
!Data:XXX<code>.tabx</code>
|-
|定制化编辑器
|✘
|✔️
|✔️
|✔️
|-
|Schema检查
|✘
|✔️
|✔️
|✔️
|-
|映射至MongoDB
|✘
|✔️
|✔️
|✔️
|-
|<nowiki>页面直接使用{{}}嵌套</nowiki>
|✘
|✘
|✔️
|✔️
|-
|排序
|✘
|✘
|✔️
|✔️
|-
|自定义复杂结构
|✘
|✔️
|✘
|✔️
|}
===文件大小===
过大的文件会增加线上渲染和预览的压力，导致超时，无法手动编辑和查看，因此建议：
*tab/tabx不要超过2mb
*json不要超过500kb
过大的文件请自己检查并批处理，丢弃不必要的冗余信息

===使用tab和tabx请注意===
*tab/tabx的数据结构：注意，必须严格遵循第一行是表头，每一行为一条数据的结构，反之（每一列为一条数据）则无法正常查询。
*tab和tabx格式提供Excel的上传和导出功能，但是请注意Excel中的数据类型和tab/tabx可能并不相符，并且Excel中没有要求每一列的数据格式统一，而tab和tabx是严格要求每一列数据的类型是一致的（<code>string/boolean/number</code>）。tab/tabx将检测第二行的数据，以自动建立字段类型的schema，将True/False转换为boolean，数字转换为number型。
**如果Excel中的第二行数据有空白，将会影响类型的判断。对于这种情况，建议在Excel表的第二行录入一组假数据，便于tab/tabx进行类型判断。
<!--*对数据使用协议有需求的站点可以通过编辑tab/tabx的原始json手动更改license（默认值为CC0-1.0）。mediawiki关于表格数据协议的文档可在[https://www.mediawiki.org/wiki/Help:Tabular_Data 此处]查阅。-->

:另行参阅：[[帮助:模块/MongoDB函数]]、[[帮助:灰机Wiki数据更新器]]


===使用灰机JSON编辑器添加JSON数据页面===
:'''[[帮助:灰机Json编辑器]]'''

== 删改数据 ==
[[File:Screenshot 2017-12-26 15.25.03.png|300px|thumb|center|tab页面还支持直接上传Excel或CSV]]
通过具有MongoDB支持的Data页面录入数据后，维基将自动管理该数据的生命周期，用户只需像修改维基一样对数据进行编辑，后台MongoDB的内容也会自动同步更新。

== 查询数据 ==
通过具有MongoDB支持的Data页面录入数据后，即可通过灰机提供的API进行查询和聚合。


====数据形态====

MongoDB中的数据都是以Json形式存在的。

{| class="wikitable"
|-
!命名 !! 结构&关系
|-
|Data:xxx.json||与JSON的读取规则完全一致，每一个.json页面是一个document，数据id是页面名字，例如"Data:xxxxx.json"
|-
|Data:xxx.tab||第一行表头作为key，以下每一行都是一个document，数据id是页面名字+行数，后面的每一个单元格为值的对象。
|-
|Data:XXX.tabx||与tab类似，但是支持多层级结构，[https://www.npmjs.com/package/excel-as-json 在tab的基础上，扩充了表头的语义]
|}

==== Lua查询 ====
{{expand|主要条目：'''[[帮助:模块|模块]]'''}}
灰机提供了以下四个函数供用户在lua模块中操作MongoDB：
*<code>'''mw.huiji.db.find'''( filter, options )</code> [[帮助:模块/使用MongoDB函数读取JSON#mw.huiji.db.find()|查看更多]]
*<code>'''mw.huiji.db.aggregate'''( pipeline, options )</code> [[帮助:模块/使用MongoDB函数读取JSON#mw.huiji.db.aggregate()|查看更多]]
*<code>'''mw.huiji.db.findOne'''( filter, options )</code>
*<code>'''mw.huiji.db.count'''( filter, options )</code> 

另行参考官方文档，（英文）：[https://docs.mongodb.com/php-library/current/tutorial/crud/#find-many-documents Find]、[https://docs.mongodb.com/php-library/current/tutorial/crud/#find-one-document FindOne]、[https://docs.mongodb.com/php-library/current/tutorial/crud/#complex-queries-with-aggregation Count]、[https://docs.mongodb.com/php-library/current/tutorial/crud/#complex-queries-with-aggregation Aggregate]


====使用SMongo查询====
{{expand|主要条目：'''[[帮助:SMongo|SMongo]]'''}}
利用灰机提供的零件，使用封装成普通模板的SMongo来进行数据查询，语法风格与SMW的<code><nowiki>{{#ask:}}</nowiki></code>函数完全一致


==== Javascript查询 ====
Javascript查询可通过WebAPI进行，目前API还处于实验阶段，请参照www.huijiwiki.com/api/rest_v1/的文档进行使用。（各维基须将www替换为自己维基的站点前缀，如warcraft）

== MongoDB数据管理==
在新版本灰机wiki的驾驶室中，可以通过“MongoDB”标签查询和管理本站点下的数据内容。

[[File:20230720110508.png|400px]]



;[[templatemanager:Manifest:GlobalSearch|灰机workshop提供的页面查询框架]]

== 范例 ==
[[h:ff14:首页|最终幻想XIV维基]]是使用本文所列的MongoDB方法搭建的。
* Data页面示例：[[ff14:Data:Item/12937.json]]。
* 数据库示例：[https://ff14.huijiwiki.com/api/rest_v1/namespace/data?filter={%22_id%22:%22Data:Item/12937.json%22}]。
* Lua查询示例： [[ff14:模块:Item/RecipeList]]
{{Data Help
|页面名=帮助:MongoDB支持
|描述文字=查询MongoDB数据
|解说=
|symbol=
|主分类=帮助
|子分类=复杂
|tags=编程,管理,数据更新
|sortkey=52300
|关键=yes
|catsortkey=4
|guide=no
|难度=复杂
|角色=开发者
|灰机功能=yes
}}
