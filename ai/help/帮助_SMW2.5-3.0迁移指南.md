# 帮助:SMW2.5-3.0迁移指南

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3ASMW2.5-3.0%E8%BF%81%E7%A7%BB%E6%8C%87%E5%8D%97
revid：41631 · 抓取时间：2026-11-09T14:27:10+08:00

---

灰机Wiki将于近日将Semantic MediaWiki扩展程序更新到3.0.x，届时现有的SMW查询功能可能会出现不兼容的情况。本文档将说明2.5.x-3.0.x之间的改动和兼容方式。
*迁移概述原文：[https://github.com/SemanticMediaWiki/SemanticMediaWiki/blob/master/docs/technical/migration-guide-3.0.md]

==长求总==
如果你嫌废话太多，可以按如下步骤操作（记住这些操作只有smw版本升级后才有效）：
#检查你的站点是否使用了Semantic Mediawiki。可以尝试访问<code>special:ask</code>快速验证。如果没有开启，可以忽略本文档。
#*你可以访问<code>property:Has_query</code>页查看哪些页面使用了查询语句（包括通过模板嵌套的）。但该功能不会显示哪些语句需要修复。
#所有在<code>#ask</code>中使用的模板，包括由<code>template</code>，<code>introtemplate</code>和<code>outrotemplate</code>参数指定的模板，请将模板中的参数占位符<code><nowiki>{{{?参数名}}}</nowiki></code>更换为<code><nowiki>{{{参数名}}}</nowiki></code>，即移除问号。
#如果你在上述模板中使用了<code><nowiki>{{{userparam}}}</nowiki></code>等由查询语句传入的参数，请根据本文档'''[[#基础参数的标准化]]'''一节的说明替换为新写法。
#*再来个长求总：即如果传入的参数不是从数据里来的（而是从查询语句里来的），那就加个井号
#如果你的查询语句使用了列表格式（<code>format=list</code>），可考虑将他们替换为<code>format=plainlist</code>。
#如果使用了有序或无序列表格式（<code>format=ul</code>或<code>format=ol</code>），请检查实际输出结果是否对布局产生了影响。

==概述==
*format为<code>列表</code>,<code>无序列表</code>或<code>有序列表</code>时，输出结果将由相应的html标签包裹。
**例如输出列表时，结果将会是一个<code><nowiki><span class="smw-format list-format"></nowiki></code>包裹，每个子元素为一个<code><nowiki><span class="smw-row"></nowiki></code>。
**相应地，如果format为无序列表，包裹元素将变为<code><nowiki><ul class="smw-format ul-format"></nowiki></code>，结果也会放在<code><nowiki><li class="smw-row"></nowiki></code>中。
*新增一个<code>纯列表（plainlist）</code>格式，输出结果将全部放在一个p元素中，并以逗号分隔。
*<code>模板(format=template)</code>格式现在是<code>plainlist</code>格式的别名。由于plainlist现在是默认格式（但灰机的默认值是broadtable），<strike>因此可以在没有指定format=template的时候直接指定template参数</strike>（在灰机需要指定format=template或format=plainlist）。
*向模板传递参数时，基本参数均以<code>#</code>开头，部分参数名称也发生了变化。参考[[#基础参数的标准化]]。
*输出结果的分隔符现在包含值分隔符<code>sep</code>，属性分隔符<code>propsep</code>和结果行分隔符<code>valuesep</code>三个参数。
*列表末尾分隔符参数已移除，即不会在列表末尾两个元素之间输出<code>,and</code>。
*smw使用的模板参数定义中不需要再添加问号前缀（即模板中的参数原先写作<code><nowiki>{{{?参数名}}}</nowiki></code>，现在可以写作<code><nowiki>{{{参数名}}}</nowiki></code>。
*移除了<code>template arguments</code>参数。现在只要勾选了named args(<code>named args=1</code>)就会自动将所有请求的属性传递给模板。
*移除了<code>columns</code>参数。

==改动细节==
===输出格式（format参数）===
{| class="wikitable"
!原格式!!新格式!!说明
|-
| - || list || 输出单行列表，并由一个html元素包裹。
|-
| list || plainlist || 输出无包裹的列表（并且可以使用template参数）。<code><nowiki>{{#show}}</nowiki></code>函数默认使用该格式输出。
|-
| ol || ol || 有序列表，增加外层包裹
|-
| ul || ul || 无序列表，增加外层包裹
|-
| template || template || 弃用，现在是plainlist的别名。
|}
===<code>#ask</code>和<code>#show</code>的参数===
{| class="wikitable"
!原参数名!!新参数名!!说明
|-
|sep||sep||现在可以对有序和无需列表使用了
|-
| - || propsep ||新增参数。用于分割输出结果的多组key-value。
|-
|valuesep || valuesep || 同一个参数的多个值在输出时可以被trim。该参数可以设置折叠后的展开符号。
|-
|template arguments || - || 不再使用。
|-
|columns || - || 不再使用。
|}
===基础参数的标准化===
适用于<code>template</code>，<code>introtemplate</code>和<code>outrotemplate</code>指定的模板。

所有基本参数均以<code>#</code>开头，以与搜索结果传入的参数区分。
{| class="wikitable"
!原参数名 !! 新参数名 !! 说明
|-
|userparam || #userparam || 由<code>#ask</code>的<code>userparam</code>参数定义，传递给搜索结果的模板。
|-
| -  || #rowcount || 输出搜索结果的总数。
|-
| - || #rownumber || 输出当前条目的序号。如果在搜索结果中翻页，页码也会影响该输出。在<code>introtemplate</code>和<code>outrotemplate</code>同样有效（how？）
|-
| # || # || 弃用。请使用<code>#rownumber</code>
|-
| smw-resultquerycondition || #querycondition	|| 
|- 
| smw-resultquerylimit || #querylimit ||
|- 
| smw-resultqueryoffset || #resultoffset ||
|}

==列出所有包含查询语句的页面==
所有包含<code>#ask</code>和<code>#show</code>语句的页面都将额外增加一个smw属性“has_query”（目前版本就有），因此可以访问相应维基的<code>property:Has_query</code>页查看哪些页面执行了查询，从而对SMW版本迁移的结果做出验证。
*模板中includeonly部分的查询语句不视为查询，但如果该模板被引用，则引用该模板的页面会有该属性。
*Has_query也是一个SMW属性，这表示你可以通过<code>special:ask</code>进一步筛选结果。

==列表样式改动示例==
列表样式的HTML标签包裹、及新增的分隔符属性示例。

假定有一个查询的无模板输出结果（<code>plainlist</code>，不设置模板）如下：
<pre>INTROTEMPLATE
F-0401/Asoka (Version: 3.8 PROPSEP Developer: Shae Erley VALUESEP Keeley Considine PROPSEP Company:  Edgewire) SEPARATOR
F-0401/Stim (Version: 1.8 PROPSEP Developer: Kerrill Blabie VALUESEP Gelya Barnewall PROPSEP Company:  Bluejam PROPSEP Website: http://paginegialle.it/diam/id/ornare.aspx)
OUTROTEMPLATE
... further results </pre>

则在使用list输出时将变为如下结果：
<pre><p>
    INTROTEMPLATE
    <span class="smw-format list-format">
        <span class="smw-row">
            <span class="smw-field">
                <span class="smw-value">
                    <a href="/wiki/F-0401/Asoka" title="F-0401/Asoka">F-0401/Asoka</a>
                </span>
            </span>
            (
            <span class="smw-field">
                <span class="smw-field-label">
                    <a href="/wiki/Property:Version" title="Property:Version">Version</a>
                </span>
                :
                <span class="smw-value">3.8</span>
            </span>
            PROPSEP
            <span class="smw-field">
                <span class="smw-field-label">
                    <a href="/wiki/Property:Developer" title="Property:Developer">Developer</a>
                </span>:
                <span class="smw-value">Shae Erley</span>
                VALUESEP
                <span class="smw-value">Keeley Considine</span>
            </span>
            PROPSEP
            <span class="smw-field">
                <span class="smw-field-label">
                    <a href="/wiki/Property:Company" title="Property:Company">Company</a>
                </span>
                :
                <span class="smw-value">
                    <a href="/mw/index.php?title=Edgewire&amp;action=edit&amp;redlink=1" class="new"
                        title="Edgewire (page does not exist)">Edgewire</a>
                </span>
            </span>
            )
        </span>
        SEPARATOR
        <span class="smw-row">
            <span class="smw-field">
                <span class="smw-value">
                    <a href="/wiki/F-0401/Stim" title="F-0401/Stim">F-0401/Stim</a>
                </span>
            </span>
            (
            <span class="smw-field">
                <span class="smw-field-label">
                    <a href="/wiki/Property:Version" title="Property:Version">Version</a>
                </span>
                :
                <span class="smw-value">1.8</span>
            </span>
            PROPSEP
            <span class="smw-field">
                <span class="smw-field-label">
                    <a href="/wiki/Property:Developer" title="Property:Developer">Developer</a>
                </span>:
                <span class="smw-value">Kerrill Blabie</span>
                VALUESEP
                <span class="smw-value">Gelya Barnewall</span>
            </span>
            PROPSEP
            <span class="smw-field">
                <span class="smw-field-label">
                    <a href="/wiki/Property:Company" title="Property:Company">Company</a>
                </span>
                :
                <span class="smw-value">
                    <a href="/mw/index.php?title=Bluejam&amp;action=edit&amp;redlink=1" class="new"
                        title="Bluejam (page does not exist)">Bluejam</a>
                </span>
            </span>
            PROPSEP
            <span class="smw-field">
                <span class="smw-field-label">
                    <a href="/wiki/Property:Website" title="Property:Website">Website</a>
                </span>
                :
                <span class="smw-value">
                    <a rel="nofollow" class="external text"
                        href="http://paginegialle.it/diam/id/ornare.aspx">http://paginegialle.it/diam/id/ornare.aspx</a>
                </span>
            </span>)
        </span>
    </span>
    OUTROTEMPLATE
    <span class="smw-list-furtherresults">
        <a href="..." title="...">... further results</a>
    </span>
</p></pre>

其中默认输出的括号、冒号等符号可在相应的Message页（即Mediawiki:页）设置。
{| class="wikitable"
!Message页面名||默认值||说明
|-
|smw-format-list-separator|| ,||即上文的<code>SEPARATOR</code>
|-
|smw-format-list-property-separator|| ,||即上文的<code>PROPSEP</code>
|-
|smw-format-list-value-separator|| ,||即上文的<code>VALUESEP</code>
|-
|smw-format-list-field-label-separator|| :||出现在属性的key-value之间
|-
|smw-format-list-other-fields-open|| (||出现在条目名（页面名）之后，属性列表之前
|-
|smw-format-list-other-fields-close|| )||出现在属性列表之后
|}
