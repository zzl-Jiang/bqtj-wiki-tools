# 帮助:Semantic MediaWiki/list格式

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3ASemantic%20MediaWiki/list%E6%A0%BC%E5%BC%8F
revid：33366 · 抓取时间：2026-11-09T14:27:10+08:00

---

List（清单）允许将SMW查询的结果按照清单的方式呈现出来。

*当ask函数后没有查询结果时，默认会用list格式输出。

==格式参数==
{| class="wikitable"
|-
! 参数 !! 类型 !! 默认值 !! 解释
|-
| sep || 文本 || ， || 数值的分隔符
|-
| template || 文本 || 空 || 封装模板
|-
| introtemplate || 文本 || 空 || 前置模板
|-
| outrotemplate || 文本 || 空 || 后置模板
|-
| userparam || 文本 || 空 || 自定义参数
|-
| named args || yes/no || no || 是否传递命名参（no则传递序号参）
|-
| imort-annotation || yes/no || no || 
|}
*{{note}}template、introtemplate、outrotemplate、userparam、named args参数同template格式，具体查阅[[help:Semantic Mediawiki/template格式|template格式]]

==例子==
<pre>
<nowiki>{{#ask:
[[has fiction::+]]
|format=list
}}</nowiki>
</pre>
'''结果'''：

{{#ask:
[[has fiction::+]]
|format=list
}}

===分隔符===
通过一些特定的分隔符，我们可把ask结果进行进一步处理，例如将分隔符换成<nowiki>&nbsp;{{!}}&nbsp;</nowiki>后，就可以作为navbox打印了。通过特定的分隔符还可以结合数组函数#array，这里不再赘述。
<pre>
<nowiki>{{#ask:
[[has fiction::+]]
|format=list
|sep=&nbsp;{{!}}&nbsp;
}}
</pre>
'''结果'''：

{{#ask:
[[has fiction::+]]
|format=list
|sep=&nbsp;{{!}}&nbsp;
}}
{{NavboxSMW}}
