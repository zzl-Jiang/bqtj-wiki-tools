# 帮助:Mermaid/泳道图

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3AMermaid/%E6%B3%B3%E9%81%93%E5%9B%BE
revid：42397 · 抓取时间：2026-11-09T14:27:09+08:00

---

<!-- 帮助:Mermaid/泳道图 -->
{{子页面列表|目标页面=帮助:Mermaid|隐藏前缀=1}}
{{编辑手册nav}}{{HuijiOnly}}

泳道图用来看哪一步归谁负责：一张流程图，按部门、系统或角色切成几条竖着的道。

mermaid 没有原生泳道图，做法是拿<code>subgraph</code>当泳道，每个子图就是一条道。

==思路==

<pre lang="mermaid" data-caption="两条道" data-thumb-style="float:right;width:300px">
flowchart LR
    subgraph 编辑
        direction TB
        A[写草稿] --&gt; B[保存]
    end
    subgraph 审核
        direction TB
        C[复查] --&gt; D[发布]
    end
    B --&gt; C
</pre>

*外层写成<code>flowchart LR</code>，从左往右，子图就会并排成竖着的几条道。
*每个子图里写<code>direction TB</code>，让这条道里的流程从上往下走。
*跨道的连线写在子图外面。写在里面会被当成同一道内部的线。

==示例==
<pre lang="mermaid" data-caption="一次更新的三条泳道">
flowchart LR
    subgraph 前端["前端"]
        direction TB
        A[页面] --&gt; B[组件]
    end
    subgraph 后端["后端"]
        direction TB
        C[接口] --&gt; D[(数据库)]
    end
    subgraph 运维["运维"]
        direction TB
        E[日志] --&gt; F[告警]
    end
    B --&gt; C
    C --&gt; E
</pre>

==写法细节==
*子图标题带空格、括号时用引号包起来：<code>subgraph 前端["前端（Web）"]</code>。
*想让某条道更宽或者更靠前，直接在子图里多写几步。布局是自动的，没有泳道宽度这类参数。

==跟节点、箭头的关系==
道里面用的还是流程图的语法，节点形状、箭头、样式全部照旧，见[[帮助:Mermaid#Mermaid语法|帮助页的语法一节]]。
