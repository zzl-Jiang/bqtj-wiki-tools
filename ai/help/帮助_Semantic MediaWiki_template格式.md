# 帮助:Semantic MediaWiki/template格式

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3ASemantic%20MediaWiki/template%E6%A0%BC%E5%BC%8F
revid：33372 · 抓取时间：2026-11-09T14:27:10+08:00

---

SMW允许通过format=template来封装请求查询结果，具体语法如下
<pre>
<nowiki>{{#ask:[[category:xxx]]|?Has name
format=template
|template=yourtemplate
|...
}}</nowiki>
</pre>
==template格式的参数==
通过模板封装ask结果，template格式的参数如下
{| class="wikitable"
!可选参数
!数值类型
!默认值
!解释
|-
|sep
|文本
|,
|取值分隔符
|-
|template
|文本
|空值
|指定的封装模板名称
|-
|named  args
|yes/no
|no
|给模板传递的参数是命名参（yes）还是序号参（no），请参见[[help:模板参数|模板参数]]
|-
|userparam
|文本
|空值
|向模板传入一个用户自订的参数<nowiki>{{{userparam}}}</nowiki>
|-
|intro
|文本
|空值
|前置文本（可以使用HTML）
|-
|introtemplate
|文本
|空值
|前置模板
|-
|outro
|文本
|空值
|后置文本（可以使用HTML）
|-
|outrotemplate
|文本
|空值
|后置模板
|-
|import-annotation
|yes/no
|no
|
|}

==template格式的优点==
使用template格式封装参数具有以下优点
*灵活的改变查询结果的顺序，否则只能按照默认的顺序打印结果
*能够根据返回结果做更多处理，例如拼出ID、链接、图片等等
*根据返回结果自定义是否添加链接
*模板中可以嵌套css和html代码，以及其他由[[help:解析器函数|解析器函数]]和[[help:解析器扩展标签|解析器扩展标签]]提供的逻辑运算功能。

==如何在封装模板中处理查询结果==
以这一查询为例<code><nowiki>{{#ask:[[has fiction::联盟]]|?hp|?mp|link=none}}</nowiki></code>
通过默认查询得到的结果是：
{{#ask:[[has fiction::联盟]]|?hp|?mp|link=none}}

如果我们指定一个模板[[template:example/templateformat]]来封装查询结果，那么直观的来说，上述表格的每一行结果都会被传递给模板，并且分别作为模板的三个序号参，以第一行为例：
*Test页面/吉安娜=<nowiki>{{{1|}}}</nowiki>
*55=<nowiki>{{{2|}}}</nowiki>
*140=<nowiki>{{{3|}}}</nowiki>

我们在模板中书写如下代码
<pre>
<nowiki>**{{#replace:{{{1}}}|Test页面/|}}的法力为<span style="color:blue">{{{3|}}}</span>，体力为<span style="color:green">{{{2|}}}</span></nowiki>
</pre>

那么
<pre>
<nowiki>{{#ask:[[has fiction::联盟]]
|?hp
|?mp
|link=none
|format=template
|template=example/templateformat
}}</nowiki>
</pre>
的结果如下
{{#ask:[[has fiction::联盟]]
|?hp#m
|?mp
|link=none
|format=template
|template=example/templateformat
}}

===named args===
如果你不想在模板里处理一堆序号参，而是想用命名参（当请求结果超过20个以上时会非常重要，序号参往往会导致混乱）
可以这样书写
<pre>
<nowiki>{{#ask:[[has fiction::联盟]]
|?hp
|?mp
|link=none
|named args=yes
|format=template
|template=example/templateformat
}}</nowiki></pre>
这样做后你需要在模板中将参数改写为<code><nowiki>{{{?Hp}}},{{{?Mp}}}</nowiki></code>
*{{note}}问号必须添加
*{{note}}首字母必须大写
*{{note}}_会被转义成空格

===userparam===
如果你想引入查询之外的一个常量或变量（可缺省参数）参与模板逻辑运算，可以使用userparam来实现。在模板之中使用<code><nowiki>{{{userparam}}}</nowiki></code>来调取这个参数。如果查询是放在一个模板之中，也可以使用这种方法
<code>|userparam=<nowiki>{{{某个模板参数|默认值}}}</nowiki></code>来灵活处理，如果模板给一个参数，则把此参数传递如模板，如果缺省，则用一个默认值。
*案例：[[rimworld:template:Meleeweapondata]]

==introtemplate和outrotemplate==
类似ask默认格式的intro和outro参数，这两部分模板只会加载一次，封套在整个查询结果的起始两端，也就意味着我们可以用各种html标签将结果套起来，例如<nowiki><table><div><gallery></nowiki>等等。

举一个将结果处理然后封套成表格的例子
*intro模板
<pre>
<table class="wikitable sortable"><tr><th>英雄</th><th>生命值</th><th>法力值</th></tr>
</pre>
*封装模板
<pre>
<tr><td>{{{1|}}}</td><td>{{{2|}}}</td><td>{{{3|}}}</td></tr>
</pre>
*outro模板
<pre>
</table>
</pre>
*{{note}}这里的table写法可以换成wikitext
*{{note}}这里只是简单介绍一下方法，因此例子很简单，事实上这样的结果无需用模板，直接format=table即可，但是当我们需要将结果进行复杂预处理然后再以表格呈现时，format=table就无能为力了，这时候我们就需要使用上述手段，下面是一些实操案例：
**[[rimworld:template:Meleeweapondata]]
**[[rimworld:地貌#植物物种]]
==嵌套限制==
模板之中可以再次使用ask来查询，这里的嵌套查询亦可以再次使用fomat=template。但是这样循环嵌套有一个限制，具体通过<code>$maxRecursionDepth</code>参数来配置，默认为2,即查询A中可以通过模板B来嵌套查询C，查询C可以使用模板D，但是模板D中的查询就不能继续使用format=template

==复杂案例==
*[[dota:Template:Ability box]]
{{NavboxSMW}}
