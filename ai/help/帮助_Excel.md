# 帮助:Excel

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3AExcel
revid：39550 · 抓取时间：2026-11-09T14:27:09+08:00

---

{{编辑手册nav}}
Excel是线下整理数据的重要工具。

==应用==
===文学主题===
对于文学类主题维基，Excel的作用主要是整理和生成译名表。整理好的内容可以导入到MediaWiki:Huiji-translation-pairs中作为自动翻译的补充，详情可以参考：
:'''[[帮助:自动翻译]]'''

===游戏主题===
对于制作游戏类主题维基，Excel的作用更为显著，可以帮助我们在线下快捷整理数据，借由'''[[帮助:灰机Wiki数据更新器|灰机数据更新器]]'''快速的被部署到线上。

灰机直接支持上传到Data命名空间下的Excel文件包括xls，xlsx以及csv（comma seperated values，逗号间隔数值）文件。

==dump已有页面的信息==
#打开“灰机数据更新器”，设置好项目路径（wiki key）
#选择“基本-批量操作页面”
#通过“命名空间”或者“分类”等方式选择页面
#在“解析”中勾选解析模板数据到Excel文件
#指定保存的目录和文件名
#点击或使用alt+R“运行”
<gallery>
File:dump模板1.png
File:dump模板2.png
File:dump模板3.png
File:dump模板4.png
</gallery>

==导入为tab/tabx格式的数据文件==
通过将整理好的Excle文件上传到指定的页面位置，可以使其直接进入MongoDB数据库，作为数据源在wiki中被查询。

===页面的构建===
#在data:命名空间下，创建页面名字以<code>.tab</code>或者<code>.tabx</code>结尾即可。
#编辑页面，支持直接将Excel文件包括xls，xlsx以及csv（comma seperated values，逗号间隔数值）上传。
##为保证正确识别每列的数据类型（string、boolean、number等），第二行不能为空，实在没有数据可以做一行假数据来告诉程序这一列是什么数据类型，例如True/False会被正确识别为boolean布尔值，带引号的字符串则会被识别为string字符串类型。
##文件的第一列，即表头中不能出现英文、下划线以外的内容
##单元格中不能出现制表符，比如硬换行（excel中的shift+enter）。
#保存后即可存储为MongoDB数据。

===数据的查询===
灰机支持的MongoDB查询方式包括：
*使用Lua模块内封装的<code>mw.huiji.db.*</code>函数进行查询：'''[[帮助:MongoDB支持#Lua查询]]'''
*使用基于SMongo的模板进行SMW风格的查询：'''[[帮助:SMongo]]'''，请注意schema的读取。

==使用Excel批量创建页面==

需要在Excel中，以如下方式罗列数据

[[File:updater demo.png|400px|link=]]

灰机数据更新器更新上述表格时会创建'''页面名甲'''，'''页面名乙'''，'''页面名丙'''…等页面。

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

'''参数说明'''
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
{{Data Help
|页面名=帮助:Excel
|描述文字=Excel的使用
|解说=
|symbol=
|主分类=帮助
|子分类=进阶
|tags=编程,Excel,数据更新
|sortkey=50500
|关键=no
|catsortkey=3
|guide=yes
|难度=进阶
|角色=开发者
|灰机功能=no
}}
