# 帮助:Mermaid/流程图

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3AMermaid/%E6%B5%81%E7%A8%8B%E5%9B%BE
revid：42402 · 抓取时间：2026-11-09T14:27:09+08:00

---

<!-- 帮助:Mermaid/流程图 -->
{{子页面列表|目标页面=帮助:Mermaid|隐藏前缀=1}}
{{编辑手册nav}}{{HuijiOnly}}

流程图是 mermaid 最常用的一种，把谁连着谁、先做什么后做什么画成一张图。流程、层级、依赖关系、简单的决策树都用它。

==图表头==
第一行写<code>flowchart 方向</code>，旧写法<code>graph 方向</code>也支持。方向决定整张图往哪边长：

<pre lang="mermaid" data-caption="LR：从左往右" data-thumb-style="float:right;width:280px;clear:both">
flowchart LR
    A[填写] --&gt; B[提交] --&gt; C[审核] --&gt; D[发布]
</pre>

<pre lang="mermaid" data-caption="TD：从上往下" data-thumb-style="float:right;width:200px;height:300px;clear:both">
flowchart TD
    A[填写] --&gt; B[提交] --&gt; C[审核] --&gt; D[发布]
</pre>

*<code>LR</code>：从左往右，横版，适合步骤少的流程
*<code>RL</code>：从右往左
*<code>TD</code>（或<code>TB</code>）：从上往下，默认
*<code>BT</code>：从下往上

==节点==
<code>A</code>是节点的 id，后面那对括号的形状决定它长什么样：

<pre lang="mermaid" data-caption="节点形状一览" data-thumb-style="float:right;width:240px;height:240px;clear:both">
flowchart TD
    A[矩形] --- B(圆角) --- C([胶囊]) --- D[[子程序]] --- E[(圆柱)] --- F((圆)) --- G(((同心圆))) --- H{菱形} --- I{{六边形}} --- J[/平行四边形/] --- K[/梯形\] --- L>旗子]
</pre>

*<code>A[文字]</code>：矩形，最常用
*<code>A(文字)</code>：圆角
*<code>A([文字])</code>：胶囊（开始 / 结束）
*<code><nowiki>A[[文字]]</nowiki></code>：子程序
*<code>A[(文字)]</code>：圆柱（数据库）
*<code>A((文字))</code>：圆
*<code>A(((文字)))</code>：同心圆
*<code>A{文字}</code>：菱形（判断）
*<code><nowiki>A{{文字}}</nowiki></code>：六边形
*<code>A[/文字/]</code>：平行四边形（输入 / 输出）
*<code>A[/文字\]</code>：梯形
*<code>A&gt;文字]</code>：旗子（注释形状）

*只写 id 不写括号（<code>A --&gt; B</code>）的时候，块里显示的就是 id 本身。
*同一个 id 只算一个块。写两次<code>A[甲]</code>、<code>A[乙]</code>，后写的文字会盖掉前面的，这也是后面才连到的节点仍能正常写的原因。

===节点里的文字===
*换行：<code>&lt;br&gt;</code>、<code>&lt;br/&gt;</code>、<code>&lt;br /&gt;</code>三种都支持，大小写不影响。
*只有换行可用。<code>&lt;b&gt;</code>、<code>&lt;span&gt;</code>这类标签不起作用，要么当普通文字显示，要么被直接去掉。图里的文字是 SVG 文本，不是 HTML。
*标签里需要出现方括号、引号、竖线时，整段用双引号包起来：<code>A["带 [方括号] 的文字"]</code>。
*链接（<code><nowiki>[[页面|文字]]</nowiki></code> / <code><nowiki>[https://… 文字]</nowiki></code>）要求同上，必须写在带引号的标签中，见[[帮助:Mermaid#给节点加链接|给节点加链接]]。

==箭头==
<pre lang="mermaid" data-caption="连线样式一览" data-thumb-style="float:right;width:240px;height:240px">
flowchart TD
    A --&gt; B
    B --- C
    C -.-&gt; D
    D ==&gt; E
    E &lt;--&gt; F
    F --o G
    G --x H
    H -- 是 --&gt; I
</pre>

*<code>A --&gt; B</code>：实线加箭头
*<code>A --- B</code>：实线，不带箭头
*<code>A -.-&gt; B</code>：虚线加箭头，表示弱相关或可选
*<code>A ==&gt; B</code>：粗线加箭头，表示主要路径
*<code>A &lt;--&gt; B</code>：双向箭头
*<code>A --o B</code> / <code>A --x B</code>：圆头 / 叉头
*线拉长（跨列）：<code>A ---&gt; B</code>、<code>A ----&gt; B</code>

线上写字有两种写法，效果一样：

*<code>A -- 是 --&gt; B</code>：文字写在两条杠之间。箭头是<code>--&gt;</code>，文字夹在少一个<code>-</code>的位置。
*<code>A --&gt;|是| B</code>：文字用竖线包起来。
*文字里需要带方括号、竖线时整体加引号：<code><nowiki>A -- "见 [[规则]]" --> B</nowiki></code>

==子图（subgraph）==

<pre lang="mermaid" data-caption="两个子图" data-thumb-style="float:right;width:300px">
flowchart LR
    subgraph 前端
        A[页面] --&gt; B[组件]
    end
    subgraph 后端
        C[接口] --&gt; D[(数据库)]
    end
    B --&gt; C
</pre>

*<code>subgraph 标题</code> … <code>end</code>把若干节点框在一起，节点定义照常写在里面。
*需要被别处引用时给它一个 id：<code>subgraph one["标题"]</code>。标题里有方括号或空格就加引号。
*子图内部可以单独指定方向，在里面写一行<code>direction LR</code>。
*跨子图的连线写在子图外面。
*泳道图就是靠这个画的，见[[帮助:Mermaid/泳道图|泳道图]]。

==给单个块上样式==

<pre lang="mermaid" data-caption="style / classDef / linkStyle 各一处" data-thumb-style="float:right;width:280px">
flowchart LR
    A[普通] --&gt; B[强调] --&gt; C[普通]
    style B stroke-width:3px,font-weight:bold
    classDef hot stroke-width:2px
    class A,C hot
    linkStyle 0 stroke-width:2px
</pre>

三种写法，都单独占一行，写在节点和连线下面：

*<code>style 节点id 属性:值,属性:值</code>：只改一个块。这里的 id 是括号**前面**那个词，<code>B[乙]</code> 的 id 是 <code>B</code>，不是「乙」。
*<code>classDef 类名 属性:值,属性:值</code>：定义一组样式。挂到块上有两种写法，<code>class 节点id,节点id 类名</code>，或者在连线上直接写<code>A:::类名</code>。
*<code>linkStyle 序号 属性:值,属性:值</code>：改连线。序号按连线在定义里出现的顺序从 0 数，<code>linkStyle 0 stroke-width:3px</code> 是第一根线，<code>linkStyle 0,1 …</code> 可以一次写好几个，<code>linkStyle default stroke-width:3px</code> 是全部连线。

几个容易踩的点：

*属性之间用半角逗号，最后一项后面不用加。
*<code>linkStyle</code> 的序号写超了会让**整张图都画不出来**（实测：只有三条线时写 <code>linkStyle 3</code> 直接抛异常，页面上一片空白）。先数清楚有几根线。
*<code>classDef</code> 写在用它的那几行前面或后面都行；<code>class</code> 里的 id 必须真的在定义里出现过。
*值里本身带逗号会有歧义。<code>stroke-dasharray:3,2</code> 能通过解析，但逗号后面那截会被当成独立声明丢掉；改用空格写法<code>stroke-dasharray: 4 4</code>。

*这些属性可以写，但不要用来配色。<code>fill:</code>、<code>stroke:</code>、<code>color:</code>会盖掉站点统一的配色，深色站上很容易糊成一片；改<code>stroke-width</code>、<code>stroke-dasharray</code>、<code>font-weight</code>、<code>font-size</code>这类粗细、虚线、字重是安全的。
*线型（直角或曲线）是整张图的配置，单张图可以用块属性<code>data-curve</code>修改，见[[帮助:Mermaid#单张图的自定义设置|单张图的自定义设置]]。

==一条完整的例子==
<pre lang="mermaid" data-caption="站点助手怎么回答一个问题">
flowchart TD
    A[读者打开页面] --&gt; B{登录了吗？}
    B -- 否 --&gt; C[跳去登录]
    C --&gt; B
    B -- 是 --&gt; D[读取知识库]
    subgraph 缓存层
        D --&gt; E[(切片缓存)]
        D --&gt; F[站点图谱]
    end
    E --&gt; G[拼装回答]
    F --&gt; G
    G --&gt; H{有来源吗？}
    H -- 有 --&gt; I[回答 + 引用]
    H -- 没有 --&gt; J[说不知道]
    style J stroke-width:3px
</pre>

==注意==
*不要用它画族谱或血缘图。流程图的布局是分层的，同级之间那种夫妻并排、兄弟共用一条竖线的连线画不出来，硬画就是一团箭头。详见[[帮助:Mermaid#不适合：家族树|主页面那节]]。
*定义里可以写注释，一行以<code>%%</code>开头，不会画出来。知识库会把它当正文读进去。
*语句之间也可以用<code>;</code>隔开，但换行更清楚。
*需要给某个块加链接时，见[[帮助:Mermaid#给节点加链接|给节点加链接]]，链接是整块生效的。
