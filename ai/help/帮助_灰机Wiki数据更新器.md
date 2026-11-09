# 帮助:灰机Wiki数据更新器

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3A%E7%81%B0%E6%9C%BAWiki%E6%95%B0%E6%8D%AE%E6%9B%B4%E6%96%B0%E5%99%A8
revid：42668 · 抓取时间：2026-11-09T14:27:11+08:00

---

{{编辑手册nav}}{{HuijiOnly}}
'''灰机Wiki数据更新器'''(HuijiUpdater)最早是由[[User:Yuee|Yuee]]开发的机器人小程序，用于处理一些常见的数据更新需求。是“[[帮助:推土机架构|推土机]]”架构的重要工具。V3版本在Yuee经典版本的源代码基础上，由DeepSeek在[[User:SerGawen|SerGawen]]的指挥下耗资￥20元巨款历时10个小时开发而成。

==下载==

通过下方地址下载程序（2026年11月9日更新）：

*<span class="label bg-primary">V3完整版</span>：[https://dl.huijiwiki.com/huiji-updater-V3/releases/3.1.5/HuijiUpdater-3.1.5-win64.zip v3.1.5]（zip约70MB）
**<span class="label bg-success">V3 独立版</span>：[https://dl.huijiwiki.com/huiji-updater-V3/releases/3.1.5/HuijiUpdater-3.1.5-win64-no-mcp.zip v3.1.5]（不含MCP，体积减半）
**<span class="label bg-success">MCP包</span>：[https://dl.huijiwiki.com/huiji-updater-V3/releases/3.1.5/huiji-updater-mcp-3.1.5-win64.zip mcp独立包]

*<span class="label bg-danger">经典版</span>：[https://dl.huijiwiki.com/huijiwiki_bot_gui_v0.3.46.zip v0.3.46]（2023年1月19日更新）

下载后解压到任意位置，执行根目录下的'''HuijiUpdater.exe'''即可启动程序
{{HuijiCollapsed
|title=点击查看完整更新日志
|ID=111|text-style=font-size:80%;background:#fff;border:1px solid #333;|title-style=padding:4px;font-size:80%;
|text=
{{:help:灰机Wiki数据更新器/更新日志}}
}}

{{:帮助:灰机Wiki数据更新器/v3}}


====manifest校验====
{{Mbox
|type=content|border=danger
|text=仅限V3版本支持
}}
类似wikitext校验，通过manifest进行文件一致性校验，提供类似的功能。

==基本使用方法==
===登录与权限===
使用灰机Wiki的账号和密码即可进行登录。

为了保证Wiki内容不被随意破坏，因此后续进行操作时，登录的账号必须同时拥有所操作Wiki的'''[[帮助:用户权限|机器人]]'''和'''[[帮助:用户权限|管理员]]'''权限（请注意：根据相关权限设置，这意味着该站点至少存在1位进行过高级实名认证的机长权限用户，否则无法进行管理员权限的发放）。建议开一个新账号进行机器人操作。

勾选'''保持登录状态'''可以在下次启动程序时，跳过登录界面。

*参考：'''[[帮助:用户权限|设置用户权限]]'''

===任务管理===
*'''新建'''一个任务
*为任务设定'''Wiki Key'''，每个Wiki的Key就是 '''xxx.huiji.wiki''' 中的 '''xxx''' 部分
*设置任务名称和描述。这两项仅供用户识别任务用，不会影响任务执行
*选择一个'''指令'''，并配置指令相关的参数。关于指令说明请参考后面详细描述部分
*设置'''线程数'''和'''编辑摘要'''
*'''运行'''任务


==经典功能==

{| class="wikitable"
!width=180px|指令名称||功能目标||简述
|-
|上传Excel文件（模板）||用来批量创建指定预设模板的页面（key-value模式）||读取指定Excel文件，并将其中的数据更新到Wiki中，会与[[#wikitext|wikitext]]进行对比。Excel格式要求请参考后面详述部分
|-
|上传Excel文件（简易）||用来批量创建制定内容的页面（freetext模式）||读取指定Excel文件的第一个工作表（Sheet），以第一列（A列）为页面名，以第二列（B列）为页面内容，将内容批量更新到Wiki中，会与[[#wikitext|wikitext]]进行对比
|-
|上传Excel文件（JSON）||批量将JSON更新到Wiki||读取指定Excel文件的工作表（Sheet）将二维数据更新为JSON数据
|-
|批量删除 / 恢复||批量增删页面||读取一个Excel，以其中第一个工作表的第一列（A列）为页面标题列表，批量删除或恢复删除这些页面
|-
|批量操作页面||对指定规则的页面列表进行批量操作||根据命名空间（需要填写命名空间ID）、分类、SMW查询条件或通过Excel文件提供的标题列表，对符合条件的页面进行批量操作。操作内容包括：批量刷新缓存、保存条目列表、解析模板数据到Excel文件、保存源代码到文本。
|}
===wikitext校验===
{{Mbox
|type=content|border=danger
|text=自V3版本起，本功能已经被manifest校验取代
}}
进行编辑的功能，都需要指定一个wikitext目录，程序会将生成的页面内容，在成功编辑到Wiki后，在本地以文本形式（txt）保存一个备份，在下次进行更新时，会将新生成的页面内容与本地备份进行对比，如果一样就不进行上传，以减少服务器压力和任务执行时间。

如果需要忽视该功能的话，可以于任务设置中关闭对比（不推荐），或是在wikitext中找到对应文件删除。



===上传Excel数据到维基模板===
{{Mbox
|type=content|border=danger
|text=该部分功能可能已经不符合主流AI工作架构，不是V3版本的核心功能，但出于兼容目的但仍然可以使用
}}

===数据格式===
'''模板模式'''需要在Excel中，以如下方式罗列数据

[[File:updater demo.png|400px|link=]]

灰机Updater更新上述表格时会创建'''页面名甲'''，'''页面名乙'''，'''页面名丙'''…等页面。

其中'''页面名甲'''的源代码内容为
<pre><nowiki>{{模板名
|表头1=数据B2
|表头2=数据C2
|表头3=数据D2
…
}}</nowiki></pre>
*Excel表上第一行第二格开始后的所有表头实际上就是网页模板中的参数名[[File:updater demo2.png|x18px|link=]]
*Excel表上第二行起所有第二列以后的内容就是网页模板中对应参数的赋值[[File:updater demo3.png|x18px|link=]]
**页面名乙、页面名丙…等页面的内容可类推。

'''另外，可以在表头或是页面名最前面加“!”（半角惊叹号），有该符号的数据列或是行，不会被上传到Wiki中。'''

====参数说明====
;选择数据Excel文件
*上传全部工作表：该选项为默认值，会上传工作薄中所有工作表。<code>'''但是会跳过所有以“Sheet”开头的工作表（Excel默认工作表名称）'''</code>
*上传第一个工作表：不论第一个工作表是什么名字，都上传第一个工作表

;模板名称
可以设置3种形式来指定模板名称，
*使用<code>'''单元格A1'''</code>：'''默认'''选项，使用A1的值作为模板名称，例如：“Template Name”
*使用<code>'''表单页的名字'''</code>：使用当前表单（sheet）的名字作为模板名称。
*指定模板名称：在客户端中手动输入一个模板名，将以此模板逐个创建页面（不用填写命名空间“template/模板”）

;额外设置
*不保留空值模式：默认情况不勾选该项目。勾选时，生成Wiki文本时，会跳过值为空的数据项。
<table>
<tr><td colspan=2>例如上面例子中，如果数据C3是空值</td></tr>
<tr><td style="text-align:center;padding: 10px 10px 0 10px;">'''不勾选'''该项目生成的文本</td><td style="text-align:center;padding: 10px 10px 0 10px;">'''勾选'''该项目生成的文本</td></tr>
<tr><td style="vertical-align: top;padding: 10px;"><pre><nowiki>{{Template Name
|表头1=数据B3
|表头2=
|表头3=数据D3
…
}}<!--Template [模板名] end--></nowiki></pre></td>
<td style="vertical-align: top;padding: 10px;"><pre><nowiki>{{Template Name
|表头1=数据B3
|表头3=数据D3
…
}}<!--Template [模板名] end--></nowiki></pre></td>
</tr></table>
*只替换模板内容模式：默认情况不勾选该项目。勾选时，程序会先从Wiki中获取该页面的内容，并将新生成的内容，替换页面内容中同名模板（如果页面中有多个该名称模板，将只替换第一个），然后编辑到Wiki。使用该选项可以保存页面中模板之外的编辑内容。

===下载维基模板数据到Excel===
{{Mbox
|type=content|border=danger
|text=该部分功能可能已经不符合主流AI工作架构，不是V3版本的核心功能，但出于兼容目的但仍然可以使用
}}

在基本中选择“批量操作页面”，在第二个标签内选择“解析模板数据到excel文件”
====选择页面====
使用updater通用的选择控件，支持以下4种方式来生产页面list
#命名空间：例如“0”代表主空间，“3500”代表data空间，灰机的命名空间编号规则可以在：'''[[help:命名空间|命名空间]]'''查阅
#分类：例如“data”，会选择所有“分类:data”下的页面
#SMW语法：输入合法的SMW查询条件，例如<nowiki>“[[name::+]]”</nowiki>
#文件列表：提交一个excel工作表
====解析方式====
*默认会解析页面中的所有[[help:模板|模板]]以及其中的所有参数
*输入指定的模板（多个用“|”分隔）可以解析制定模板内的所有参数
<gallery heights="300">
File:下载数据1.png|基本
File:下载数据2.png|选择页面
File:下载数据3.png|选择要解析的模板
File:下载数据4.png|执行
File:下载数据5.png|执行结果
</gallery>
====总结====
上传/下载功能结合使用能够允许编辑者像操作Github的代码库一样随时随地的pull/push维基上的数据。
*允许我们批量建立、更新特定的页面内容。
*也可以在线下批量处理、修改维基上的格式化数据。下载的excel文件可以进一步的转化成csv、json等格式提供给更高级的脚本语言（例如python）来做进一步的自动化处理。待修改完毕后再以excel文件的形式回灌到维基页面中即可

===批量刷新页面===
{{Mbox
|type=content|border=danger
|text=该部分功能可能已经不符合主流AI工作架构，不是V3版本的核心功能，但出于兼容目的但仍然可以使用
}}
在<code>读取数据</code>模式中，通过选择<code>刷新</code>操作，可以批量执行页面刷新，目前支持两种方式
*通过<code>API</code>申请刷新页面（推荐）：藉由MediaWiki的API来提交刷新页面的job queue，在站点Job没有积压的情况下可以快速秒刷大量页面的[[help:huiji缓存|Memory Cache缓存]]。
*通过空编辑来刷新页面：藉由对指定页面进行无意义的空编辑来刷新页面，由于需要进行物理操作，因此时间会较慢，仅在特殊情况下使用。

以上两种方法在选择Excel表格作为页面列表时，仅对第一张表进行操作。

==操作系统UI缩放导致的界面问题解决方案==
{{Mbox
|type=content|border=danger
|text=仅限经典版本
}}

由于个人制作，水平有限，本程序在Windows8/10开启系统UI缩放的情况下，会出现界面控件大小受到影响的问题（常见于使用4k分辨率桌面的用户），无法正常使用，临时解决方法如下：
#启用兼容性模式打开
#任选推荐配置，然后选择“否，使用其他配置再试一次”
#勾选“程序已打开，但未正确显示”
#勾选“当选择较大的字体设置时程序无法正确显示”
下一步、保存、测试，即可照常使用
<gallery mode="packed" heights="200px">
File:updater issue 1.png
File:updater issue 2.png
File:updater issue 3.png
</gallery>
{{Data Help
|页面名=帮助:灰机Wiki数据更新器
|描述文字=灰机数据更新器
|解说=
|symbol=
|主分类=帮助
|子分类=进阶
|tags=机器人,编程,管理,数据更新,编辑,维基化,Excel,
|sortkey=50400
|关键=no
|catsortkey=3
|guide=no
|难度=进阶
|角色=开发者
|灰机功能=yes
}}
