# 帮助:Semantic MediaWiki/category格式

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3ASemantic%20MediaWiki/category%E6%A0%BC%E5%BC%8F
revid：33360 · 抓取时间：2026-11-09T14:27:10+08:00

---

category格式允许将SMW查询到的结果以MW默认的分类页面样式呈现出来

==格式参数==
{| class="wikitable"
|-
! 参数 !! 类型 !! 默认值 !! 解释
|-
| colums || 整数 || 3 || 将结果以分栏的形式呈现
|-
| delim || 文本 || 空 || 分隔符
|-
| template || 文本 || 空 || 封装模板
|-
| userparam || 文本 || 空 || 自定义参数
|-
| named args || yes/no || no || 是否传递命名参（no则传递序号参）
|-
| imort-annotation || yes/no || no || 
|}
*{{note}}template、userparam、named args参数同template格式，具体查阅[[help:Semantic Mediawiki/template格式|template格式]]
==例子==
<pre>
<nowiki>{{#ask:
[[has fiction::+]]
|format=category
}}</nowiki>
</pre>
'''结果'''：

{{#ask:
[[has fiction::+]]
|format=category
}}
{{NavboxSMW}}
