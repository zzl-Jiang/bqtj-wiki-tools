# 帮助:Mustache模板/dot写法

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3AMustache%E6%A8%A1%E6%9D%BF/dot%E5%86%99%E6%B3%95
revid：14976 · 抓取时间：2026-11-09T14:27:09+08:00

---

<callout class="danger">本节所列的写法已经被灰机弃用。</callout>
Mustache可以用于处理数组等复杂的数据结构。
对于Html:Test2：
<pre>
{{#repo}}
  <b>{{name}}</b>
{{/repo}}
</pre>
===调用===
使用<nowiki>{{#html:Test2|repo..name=Jon|repo..name=Dany|repo..name=Tyrion}}</nowiki>可以得到：
===结果===
{{#html:Test2|repo..name=Jon|repo..name=Dany|repo..name=Tyrion}}

===解释===
为了更好的利用Mustache，#html解析器会依照下列格式构建一个参数树状结构。
{| class="wikitable"
!参数格式
!PHP示意
!JSON示意
|-
|a
|array( a => true )
|{a:true}
|-
|a.b
|array( a => array( b => true ) )
|<nowiki>{a:{b:true}}</nowiki>
|-
|a.b.c
|array( a => array( b => array( c => true ) ) )
|<nowiki>{a:{b:{c:true}}}</nowiki>
|-
|a = bob
|array( a => bob )
|{a: "bob"}
|-
|a.b=cat
|array( a => array( b => cat ）
|<nowiki>{a: {b:"cat"}}</nowiki>
|-
|a.b=cat
a.d = frog
|array( a => array( b => cat, d => frog ) )
|<nowiki>{a: {b: "cat", d:"frog"}}</nowiki>
|-
|a.b=cat
a.b=dog
|array( a => array( b => array ( cat, dog ) ) )
|<nowiki>{a:{b:["cat, "dog"]}}</nowiki>
|-
|a..b=cat
|array( a => array ( array( b => cat ) )
|{a:[{b:"cat"}]}
|-
|a..b=cat
a..b=dog
|array( a => array( array ( b => cat ), array( b => cat) ) )
|{a:[{b:"cat"}, {b:"dog"}]}
|}
<callout class="warning"><h4>可视化编辑</h4><p>目前，可视化编辑器在保存时会去掉重复的参数，这导致#html无法处理a..b=cat
a..b=dog之类的情况。解决方法是将#html封装到一个模板中，不要直接在允许可视化编辑的内容页面使用。</p></callout>
;对于更多详情，请参阅：https://mustache.github.io/mustache.5.html
