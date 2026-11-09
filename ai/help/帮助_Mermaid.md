# 帮助:Mermaid

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3AMermaid
revid：42400 · 抓取时间：2026-11-09T14:27:09+08:00

---

<!-- 帮助:Mermaid（www:帮助:Mermaid） -->
{{子页面列表|目标页面=帮助:Mermaid|隐藏前缀=1}}
{{编辑手册nav}}{{HuijiOnly}}

本页说明如何在维基页面里写 mermaid 图。可以写在哪里、画出来是什么样，由皮肤提供的零件决定；写法本身和写 wikitext 一样简单。

底层使用 [https://mermaid.js.org/ mermaid] 12.2.0，本页的语法说明均按该版本编写。

==阅读本文档==
本文档（包括子页面）中除了触发mermaid加载的pre标签说明之外，其他说明均不额外在wikitext侧提供mermaid示例。

你可以点开mermaid图后，通过右边栏查看这张图的语法和配置。

如果你还是不太熟悉，你可以让huijiAgent（包括siteAgent和workspaceAgent）帮你写。他会生成mermaid图，点开图片后可以在右边栏看到实现代码。

==安装==
本功能由零件 CockpitMermaid 提供，需要站点管理员安装。安装后刷新页面，页面上已有的<code>&lt;pre lang="mermaid"&gt;</code>会自动变成图。

*一键安装、手动安装、更新、开关：见[[templatemanager:manifest:cockpitMermaid|零件中心]]
*站点配色与主题（<code>window.mermaidConfig</code>）：在同一个零件的说明里配置
*未安装零件的站点，看到的仍是一段源代码

==单张图的自定义设置==
以下属性直接写在<code>&lt;pre lang="mermaid"&gt;</code>标签上，MediaWiki 会保留它们：

*<code>data-caption="登录流程"</code>：图下方的一行说明文字，同时作为大图的标题。不写则不显示。
*<code>data-width="640"</code>：缩略框宽度。纯数字按 px 计算，也可以写<code>100%</code>、<code>40em</code>。默认 100%，不会超出正文栏宽。
*<code>data-height="360"</code>：缩略框高度。默认不设置，按图自身的比例撑开，可以完整看到全图。设置后为固定高度，图会等比缩放到能放下的尺寸。
*<code>data-theme="dark"</code>：只给这一张图换主题。
*<code>data-look="classic"</code>：只给这一张图换外观。
*<code>data-curve="step"</code>：只给这一张图换连线形状。
*<code>data-thumb-style="float:right;width:240px;height:240px"</code>：其中的 CSS 会原样拼到缩略框行内 style 的末尾，因此可以覆盖宽高、让图浮到文字旁边。
**这等于把排版交给作者。<code>float</code> 之后正文会绕着图流，窄屏上正文可能只剩一窄条。
**写了<code>height:</code>之后不再按图的比例撑开，否则图会按固有比例撑出盒子、被裁掉一部分。

示例：

<pre>
&lt;pre lang="mermaid" data-caption="登录流程" data-width="640" data-curve="step"&gt;
graph TD
    A[打开页面] --&gt; B{已登录？}
&lt;/pre&gt;
</pre>

*可选值写错不会导致图画不出来。控制台会报一条信息，该值被忽略。例如把<code>handDrawn</code>写进<code>data-curve</code>，会提示那是<code>data-look</code>的值。
*优先级：标签属性 > 站点全局配置 > 默认值。因此整站配了深色，某一张图仍可以单独使用浅色。

==给节点加链接==
图里的文字可以直接写 wiki 链接，写法和 wikitext 一致：

*内链：<code><nowiki>[[页面名]]</nowiki></code>，或<code><nowiki>[[页面名|显示文字]]</nowiki></code>
*外链：<code><nowiki>[https://example.com]</nowiki></code>，或<code><nowiki>[https://example.com 显示文字]</nowiki></code>
*两种都可以省略显示文字，此时内链显示页面名，外链显示 URL 本身。

带链接的标签必须用双引号包起来。mermaid 自己用方括号表示形状（<code>A[文本]</code>是矩形，<code><nowiki>A[[文本]]</nowiki></code>是子程序），不加引号时标签会在第一个<code>]</code>处被切断。引号是 mermaid 的语法要求，标签内有特殊字符就需要引起来，渲染时不会显示。

<pre lang="mermaid" data-caption="节点里的链接" data-thumb-style="float:right;width:280px">
graph LR
    A["本页：[[帮助:Mermaid|Mermaid 帮助]]"]
    A --&gt; B["外链：[https://mermaid.js.org/ 官网]"]
</pre>

*引号外面的<code><nowiki>[[…]]</nowiki></code>不会被当作链接，那是 mermaid 的形状语法，<code><nowiki>A[[x]]</nowiki></code>仍是子程序形状。
*链接对整个节点生效。点击节点的任意位置，或者点击连线上的标签，都会跳转，而不是只有那段文字可点。
**原因是图里的文字是 SVG 文本，把一行拆成普通文字和链接分别处理会让后面的部分错位（实测），因此零件选择把整个节点作为链接。节点会带下划线，鼠标移上去是手型，右键可以在新标签页打开。
*一个标签只识别第一个链接。
*内链指向当前站点，外链按原地址跳转。文字颜色跟随图的主题。
*可以写链接的位置就是可以写字的位置：节点标签、连线标签、子图标题。

==和知识库、站点助手的关系==
不需要为了 AI 单独写一份描述。知识库采集的是页面的原始 HTML，<code>&lt;pre lang="mermaid"&gt;</code>里的定义还是源码，不是浏览器里画完的图。因此那段定义会原样进入切片（标记为<code>mermaid</code>代码块），站点助手可以读到节点、连线、文字和注释。

*图本身不会被看到。它是浏览器执行 JS 才画出来的，知识库拿到的只有源码。
*因此关键结论最好在正文里也写一遍，不要只放在图里：助手能读出谁连着谁，读不出为什么。
*定义里的注释（<code>%% 说明</code>）也会进入切片，需要给助手补充上下文时可以写在那里。

==Mermaid语法==
各图种的细节在对应子页中，完整语法见官方文档（在页面最下面）。

===图表头===
每个图的第一行决定画什么图和方向，这一行写错后面全不对。

<pre lang="mermaid" data-caption="LR：从左往右" data-thumb-style="float:right;width:240px;clear:both">
flowchart LR
    A[打开页面] --&gt; B{有缓存？}
    B -- 有 --&gt; C[直接显示]
    B -- 没有 --&gt; D[去服务器取]
</pre>

<pre lang="mermaid" data-caption="TD：从上往下" data-thumb-style="float:right;width:240px;clear:both">
flowchart TD
    A[打开页面] --&gt; B{有缓存？}
    B -- 有 --&gt; C[直接显示]
    B -- 没有 --&gt; D[去服务器取]
</pre>

*流程图用<code>flowchart 方向</code>，旧写法<code>graph 方向</code>也支持。节点形状、箭头、子图、样式等细节见[[帮助:Mermaid/流程图|流程图]]。
*方向：<code>LR</code>左右，<code>RL</code>右左，<code>TD</code>（或<code>TB</code>）上下，<code>BT</code>下上。不写方向默认为<code>TD</code>。
*换图种只需换掉第一行，后面的语法也随之改变：
**<code>flowchart</code>：流程图，大多数场合使用这个，见[[帮助:Mermaid/流程图|流程图]]
**<code>sequenceDiagram</code>：时序图，见[[帮助:Mermaid/时序图|时序图]]
**<code>gantt</code>：甘特图，见[[帮助:Mermaid/甘特图|甘特图]]
**<code>flowchart</code>加子图：泳道图，见[[帮助:Mermaid/泳道图|泳道图]]
**<code>stateDiagram-v2</code>：状态图
**<code>classDiagram</code>：类图
**<code>erDiagram</code>：实体关系图
**<code>pie title 标题</code>：饼图
**<code>timeline</code>：时间线
**<code>mindmap</code>：思维导图，见[[帮助:Mermaid/思维导图|思维导图]]
*图种之间的语法不通用。把流程图的写法放进<code>sequenceDiagram</code>只会报错，拿不准时先写流程图。

===通用的几条===
以下几条与图种无关，流程图、时序图里都一样：

<pre lang="mermaid" data-caption="换行和特殊字符" data-thumb-style="float:right;width:260px">
flowchart LR
    A["第一行&lt;br&gt;第二行"] --&gt; B["带 [方括号] 的文字"]
    B --&gt; C["很长的说明文字会自动折行，不需要自己断"]
</pre>

*换行：<code>&lt;br&gt;</code>、<code>&lt;br/&gt;</code>、<code>&lt;br /&gt;</code>三种都支持，大小写不影响。
*只有换行可用。<code>&lt;b&gt;</code>、<code>&lt;span&gt;</code>这类标签不起作用，要么当普通文字显示，要么被直接去掉。图里的文字是 SVG 文本，不是 HTML。
*注释：以<code>%%</code>开头的一行不会画出来。知识库会把它当正文读入，可以给助手留一点上下文。
*标签里需要出现方括号、引号、竖线时，整段用双引号包起来：<code>A["带 [方括号] 的文字"]</code>。
*链接：见上文[[#给节点加链接|给节点加链接]]，需要包在引号里，且对整个节点生效。
*节点形状、箭头、子图、给单个块上样式：见[[帮助:Mermaid/流程图|流程图]]。

===不适合：家族树===
mermaid 的流程图是分层布局，节点按 rank 一层层排列，连线只会往下或往旁边走。而族谱的核心是夫妻并排、同辈共用一条竖线往下分，这类同级之间的连线它表达不了。硬画的结果是一团交叉箭头，比列表更难读。

血缘、族谱这类内容直接用嵌套列表或表格效果好得多。

===不能用的：图里自带的配置块===
mermaid 允许在定义最前面写一段配置（<code>---</code>包起来的<code>config:</code>，或者<code>%%{init: …}%%</code>）。本零件会把这两段整段删掉再渲染，控制台会提示一句。

原因是它能让某一张图绕过站点统一配置，最典型的是打开<code>htmlLabels</code>或换掉整张图的配色，而链接、缩略图尺寸、配色这些功能都建立在统一配置之上。需要按图调整样式时，使用上文的自定义设置和[[帮助:Mermaid/流程图|流程图]]里的<code>style</code>、<code>classDef</code>。

==示例==
===带说明和自定义设置的图===
<pre lang="mermaid" data-caption="登录流程" >
graph TD
    A[打开页面] --&gt; B{已登录？}
    B -- 是 --&gt; C[加载内容]
    B -- 否 --&gt; D[跳转登录]
</pre>

===带链接的图===
<pre lang="mermaid">
graph LR
    A["图洛斯·拉索米尔（[[老图洛斯·拉索米尔|Senior]]）"]
    A --&gt; B["本模块由[https://mermaid.js.org/ mermaid]提供"]
</pre>

==沙盒==
想随手试语法，可以用驾驶室里的这个工具：[https://club.huijiwiki.com/wiki/%E7%89%B9%E6%AE%8A:%E9%A9%BE%E9%A9%B6%E5%AE%A4#/tools/mermaid Mermaid 沙盒]。

*左边写代码，Ctrl+S 或者点运行按钮，右边直接出图，能拖动、滚轮缩放。
*它用 mermaid 的默认配置（白底），不读站点配置，所以看到的配色跟本页的图不一样，语法效果是一致的。
*解析失败时错误直接显示在右边，包含出错的行号。
*它画的是 mermaid 原始效果，不会生成正文里那种缩略图。

没有驾驶室权限的话，在任意页面存一个<code>&lt;pre lang="mermaid"&gt;</code>也能看效果。

==官方文档==
*[https://mermaid.js.org/intro/ 介绍与图种列表]
*[https://mermaid.js.org/syntax/flowchart.html 流程图]
*[https://mermaid.js.org/syntax/sequenceDiagram.html 时序图]
*[https://mermaid.js.org/syntax/stateDiagram.html 状态图]
*[https://mermaid.js.org/syntax/gantt.html 甘特图]
*[https://mermaid.js.org/config/theming.html 主题与配置]


{{Data Help
|页面名=帮助:知识库
|描述文字=知识库
|解说=使用
|symbol=<i class="fa fa-list-pie-chart" aria-hidden="true"></i>
|主分类=帮助
|子分类=进阶
|tags=编辑,文章,编程,管理,
|sortkey=99
|关键=no
|catsortkey=3
|guide=no
|难度=进阶
|角色=管理者
|灰机功能=yes
}}
