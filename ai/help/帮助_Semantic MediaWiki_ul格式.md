# 帮助:Semantic MediaWiki/ul格式

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3ASemantic%20MediaWiki/ul%E6%A0%BC%E5%BC%8F
revid：33374 · 抓取时间：2026-11-09T14:27:10+08:00

---

Ul（无序列表）允许将SMW查询的结果按照无序列表的方式呈现出来

==格式参数==
{| class="wikitable"
|-
! 参数 !! 类型 !! 默认值 !! 解释
|-
| sep || 文本 || ， || 数值的分隔符
|-
| columns || 整数 || 3 || 将结果以分栏的形式呈现
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
|format=ul
}}</nowiki>
</pre>
'''结果'''：

{{#ask:
[[has fiction::+]]
|format=ul
}}
{{NavboxSMW}}
