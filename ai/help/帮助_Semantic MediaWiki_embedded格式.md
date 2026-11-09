# 帮助:Semantic MediaWiki/embedded格式

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3ASemantic%20MediaWiki/embedded%E6%A0%BC%E5%BC%8F
revid：33362 · 抓取时间：2026-11-09T14:27:10+08:00

---

Embedded（嵌入）格式允许使用SMW将其他页面嵌入当前页面，这一参数会执行mediawiki的includeonly和noinclude标签。

==参数==
===通用参数===
{| class="wikitable sortable"
! 参数
! 可填写的值
! 解释
|-
| <kbd>limit</kbd>
| 必须是非负数
| 打印出的最大结果数量 (在table下是行数)，默认值是500
|-
| <kbd>offset</kbd>
| 数值
| 展示结果的起点，例如查询出10个结果，offest=2时从第二个开始打印，第一个会被跳过
|-
| <kbd>sort</kbd>
| 查询属性的名字
| 制定一个查询属性，所有结果会按照这个属性值来排序 (参见[[Help:Semantic Mediawiki/选择页面|选择页面]])
|-
| <kbd>order</kbd>
| 升序<kbd>ascending</kbd>/<kbd>asc</kbd><br>降序<kbd>descending</kbd>/<kbd>desc</kbd>/<kbd>reverse</kbd><br>乱序<kbd>random</kbd>/<kbd>rand</kbd><br />
| 如何排序，默认方式是<kbd>ascending</kbd>（升序） (参见[[Help:Semantic Mediawiki/选择页面|选择页面]])<br>可以填写多个，用“,”分开（当排序关键字多于一个时,依次对多个sort生效）
|-
| <kbd>align</kbd>
| <kbd>right</kbd>, <kbd>center</kbd>, <kbd>left</kbd>
|只对format为<kbd>table</kbd> and <kbd>broadtable</kbd>时生效，决定文字的水平排列方式 (参见[[Help:Semantic Mediawiki/结果的format|结果的format]])
|-
| <kbd>headers</kbd>
| <kbd>show</kbd>, <kbd>plain</kbd>, <kbd>hide</kbd>
| 控制第一行的样式<kbd>show</kbd>是默认值。hide隐藏，plain是不带链接的纯文本
|- 
| <kbd>mainlabel</kbd>
| 纯文本
| 文本会被显示在第一行的第一个单元格内，如果是“-”则会隐藏第一列标题
|-
| <kbd>index</kbd>
| 数字
| 控制record类型中哪一个数值被展示，仅对property的类型（type）为record时生效。（参见[[Help:Semantic Mediawiki/Record类型|Record]]）
|-
| <kbd>link</kbd>
| <kbd>none</kbd>, <kbd>subject</kbd>, <kbd>all</kbd>
| 控制结果中的值是否带链接， <kbd>all</kbd> 为全部带链接，<kbd>subject</kbd>只有第一列带链接，<kbd>none</kbd>则是全部不带链接。
{{Note}} 链接亦可以通过对查询属性进行单独控制来取消，详情参见“[[help:Semantic Mediawiki/结果呈现|结果呈现]]部分”
|-
| <kbd>default</kbd>
| 纯文本
|当query返回结果为空值时所显示的文字
|-
| <kbd>intro</kbd>
| 纯文本
| 展示结果之前的文字描述
|-
| <kbd>outro</kbd>
| 纯文本
| 展示结果之后的文字内容
|-
| <kbd>searchlabel</kbd>
| 纯文本
| 当超过默认limit限制后，点击查看更多的链接文字
|}
===专有参数===
{| class="wikitable"
|-
! 参数 !! 类型 !! 默认值 !! 解释
|-
| embedformat || 文本 || h1 || 标题的html样式
|-
| embedonly || yes/no || no || 不显示标题
|}

==例子==
<code><nowiki>{{#ask:[[news date::+]]
|format=embedded
|embedformat=h3}}</nowiki></code>

'''结果如下'''：
{{#ask:[[news date::+]]
|format=embedded
|embedformat=h4}}

==注意事项==
embed会将页面的分类一并嵌入，为了避免造成误加分类，可以在原页面的分类项前后套上noinclude标签
*同样的，为了精简篇幅，也可以将想要被嵌入的页面用includeonly圈起来。
*SMW的语义部分不会被嵌入，无需额外处理
{{NavboxSMW}}
