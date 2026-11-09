# 帮助:Mermaid/思维导图

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3AMermaid/%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE
revid：42395 · 抓取时间：2026-11-09T14:27:09+08:00

---

<!-- 帮助:Mermaid/思维导图 -->
{{子页面列表|目标页面=帮助:Mermaid|隐藏前缀=1}}
{{编辑手册nav}}{{HuijiOnly}}

思维导图（也叫脑图）用来把一个主题一层层摊开，适合目录、知识结构、方案拆解。它在 mermaid 里的关键字是<code>mindmap</code>。

它的写法和其他图种差别最大：没有节点 id，没有箭头，层级全靠缩进。

==基本结构==
第一行是<code>mindmap</code>，之后每行一个节点，缩进一层就是下一级：

<pre lang="mermaid" data-caption="最小的一张思维导图" data-thumb-style="float:right;width:280px">
mindmap
  root((站点))
    内容
      模板
      模块
    样式
</pre>

*根节点只有一个。多写一个同级根会直接报错（<code>There can be only one root</code>）。
*缩进用空格，两格或四格都行，但全篇要一致；混着写会得到意料之外的层级。
*一行的内容就是这个节点的文字，没有 id 可以引用，也没有连线可以写。
*节点里要手动换行就写<code>&lt;br&gt;</code>。

==节点形状==
默认是方框。在文字两边加括号可以换形状：

*<code>甲[文字]</code>：方形
*<code>甲(文字)</code>：圆角矩形
*<code>甲((文字))</code>：圆
*<code>甲)文字(</code>：云朵
*<code>甲))文字((</code>：爆炸形
*<code>甲{{文字}}</code>：六边形

<pre lang="mermaid" data-caption="六种形状" data-thumb-style="float:right;width:300px">
mindmap
  root((形状))
    方[方形]
    圆角(圆角)
    圆((圆))
    云)云(
    爆炸))爆炸((
    六边{{六边形}}
</pre>

*形状只是好看，不带含义。跟流程图不一样，这里没有「菱形表示判断」这种约定。
*括号要紧贴文字。写成<code>甲 [文字]</code>（中间有空格）时，括号会被当成节点文字的一部分。

==颜色==
*同一级的节点会自动分色，十一组一循环，超过就从头再来。
*配色和其他图种一样由站点统一决定，见[[templatemanager:manifest:cockpitMermaid|零件中心]]。

==适合画什么==
*目录、知识结构、需求分层、方案对比。
*不适合表达谁连谁（那是流程图），也不适合表达顺序和时间（时序图、甘特图）。

==注意==
*思维导图的左右布局是自动的，没有方向参数，<code>data-*</code> 里也没有方向这一项。
*<code>::icon(...)</code> 能通过解析，但画不出图标，不要写。mermaid 现在的图标由 iconify 提供（只认<code>前缀:名字</code>这样的写法），而它内置只注册了两套图种自用的小图标，没有 Font Awesome。写了之后唯一的实际效果是给节点文字后面多出一块底色。
*站点那套<code>fa fa-cog</code>图标是给 HTML 用的（<code>&lt;i class="fa fa-cog"&gt;</code>），mermaid 画的是 SVG，图标由它自己生成，两边不通用。
*节点一多，缩略图里的字会小到看不清。层级超过四层、或者一层有七八个节点以上时，考虑拆成两张，或者在正文里改用嵌套列表。
