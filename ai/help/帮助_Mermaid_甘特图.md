# 帮助:Mermaid/甘特图

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3AMermaid/%E7%94%98%E7%89%B9%E5%9B%BE
revid：42399 · 抓取时间：2026-11-09T14:27:09+08:00

---

<!-- 帮助:Mermaid/时序图 -->
{{子页面列表|目标页面=帮助:Mermaid|隐藏前缀=1}}
{{编辑手册nav}}{{HuijiOnly}}

时序图用来说明谁按顺序对谁做了什么，适合请求流程、交互步骤、协议握手这类内容。

==基本结构==
第一行固定是<code>sequenceDiagram</code>，然后是参与者，最后是一步一步的连线：

<pre lang="mermaid" data-caption="最小的一张时序图" data-thumb-style="float:right;width:280px">
sequenceDiagram
    autonumber
    participant 读者
    participant 站点助手
    读者-&gt;&gt;站点助手: 提问
    站点助手--&gt;&gt;读者: 回答
</pre>

*参与者可以不写，出现过的名字会自动加入。但先写一遍更好，可以按住想要的顺序排列。
*需要短名字时写<code>participant U as 读者</code>，之后都用<code>U</code>。
*开头加一行<code>autonumber</code>会自动编号。

==连线==
*<code>-&gt;&gt;</code>：实线加箭头，最常用
*<code>--&gt;&gt;</code>：虚线加箭头，用于回答或返回
*<code>-&gt;</code> / <code>--&gt;</code>：同上，但只有线、没有箭头
*<code>-x</code> / <code>--x</code>：终点是叉，表示失败或取消
*<code>-)</code> / <code>--)</code>：终点是开口箭头，表示异步消息

==注记与激活==
*<code>Note right of 某参与者: 文字</code>：在该参与者右边放一段旁注。<code>left of</code>、<code>over A,B</code>同理。
*<code>activate A</code> / <code>deactivate A</code>：给 A 画一根激活条，表示这段时间它在干活。
**省事写法是在连线上加<code>+</code>或<code>-</code>：<code>A-&gt;&gt;+B: 开始</code>、<code>B--&gt;&gt;-A: 结束</code>。

==分组==

<pre lang="mermaid" data-caption="alt 分支" data-thumb-style="float:right;width:280px">
sequenceDiagram
    读者-&gt;&gt;知识库: 查“道具 层”
    alt 查到了
        知识库--&gt;&gt;读者: 3 条切片
    else 没查到
        知识库--&gt;&gt;读者: 空
    end
</pre>

*<code>loop 每 10 分钟</code> … <code>end</code>：循环
*<code>alt 查到了</code> … <code>else 没查到</code> … <code>end</code>：分支
*<code>opt 可选步骤</code> … <code>end</code>：可选
*<code>par 并行</code> … <code>and</code> … <code>end</code>：并行
*<code>rect rgb(240, 240, 240)</code> … <code>end</code>：给一段加底色。颜色会受站点配色影响，谨慎使用。
*<code>critical</code> / <code>break</code>：关键段与中断段

==完整示例==
<pre lang="mermaid" data-caption="站点助手回答一个问题">
sequenceDiagram
    autonumber
    participant U as 读者
    participant A as 站点助手
    participant K as 知识库
    U-&gt;&gt;A: 这个道具在第几层？
    activate A
    A-&gt;&gt;K: 检索 道具 层
    alt 查到了
        K--&gt;&gt;A: 3 条切片
        A--&gt;&gt;U: 第 3 层，第 2 个房间
    else 没查到
        K--&gt;&gt;A: 0 条
        A--&gt;&gt;U: 知识库里没有
    end
    deactivate A
    Note over A,K: 回答必须带来源
</pre>

==注意==
*消息文字里的分号（<code>;</code>）有时会被当成语句分隔，遇到奇怪的截断就换成全角分号。
*参与者名字带空格、括号时可以加引号：<code>participant U as "读者（未登录）"</code>。
*链接（<code><nowiki>[[页面]]</nowiki></code>）在时序图里同样可以使用，写法见[[帮助:Mermaid#给节点加链接|给节点加链接]]。
