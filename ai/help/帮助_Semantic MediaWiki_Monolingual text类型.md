# 帮助:Semantic MediaWiki/Monolingual text类型

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3ASemantic%20MediaWiki/Monolingual%20text%E7%B1%BB%E5%9E%8B
revid：33354 · 抓取时间：2026-11-09T14:27:10+08:00

---

'''SMW'''通过Monolingual text类型是属性来定义多语言之间的对应关系。
==语法==
<code>内容@语言代码</code>
<pre>
{{#subobject:
 |Has text with language=Nation@en
}}{{#subobject:
 |Translation=Country
 |Has text with language=国家@zh-hans
}}{{#subobject:
 |Translation=Country
 |Has text with language=Nación@es
}}
{{#subobject:
 |Translation=Country
 |Has text with language=國家@zh-hant
}}
</pre>
{{#subobject:
 |Has text with language=Nation@en
}}{{#subobject:
 |Translation=Country
 |Has text with language=国家@zh-hans
}}{{#subobject:
 |Translation=Country
 |Has text with language=Nación@es
}}{{#subobject:
 |Translation=Country
 |Has text with language=國家@zh-hant
}}

== 例子 ==
<pre>
{{#ask:
 [[Has text with language::+]]
 |?Has text with language
}}
</pre>
{{#ask:
 [[Has text with language::+]]
 |?Has text with language
}}

<pre>
{{#ask:
 [[-Has text with language::{{FULLPAGENAME}}]]
 |?Language code
 |?Text
}}
</pre>
{{#ask:
 [[-Has text with language::{{FULLPAGENAME}}]]
 |?Language code
 |?Text
}}

<pre>
{{#ask:
 [[Language code::en]]
 |?Text
 |?-Has text with language
}}
</pre>
{{#ask:
 [[Language code::en]]
 |?Text
 |?-Has text with language
}}

<pre>
{{#ask:
 [[Has text with language::?@~zh*]]
 |?Has text with language=Text |+index=1
 |?Has text with language=Code |+index=2
}}
</pre>
{{#ask:
 [[Has text with language::?@~zh*]]
 |?Has text with language=Text |+index=1
 |?Has text with language=Code |+index=2
}}
{{navboxSMW}}
