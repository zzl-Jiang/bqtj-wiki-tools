# 帮助:Semantic MediaWiki/Boolean类型

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3ASemantic%20MediaWiki/Boolean%E7%B1%BB%E5%9E%8B
revid：33350 · 抓取时间：2026-11-09T14:27:10+08:00

---

'''Boolean类型'''的属性只有两种可能的数值，可以是<code>true</code>/<code>false</code>，也可以是是1/0或者yes/no。
*在中文环境下会自动切换成“是”与“否”。
*如果想使用要给可选数值多于2的布尔类型，可以通过“允许值”功能对一个text类型的属性做操作，使其可以在多个值之间出现，例如“可能——也许——很可能——肯定”
{{main|help:Semantic Mediawiki/允许值}}
==在嵌入式查询中展示boolean类型==
使用自定义文字替代布尔值的默认true/false值：
<pre><nowiki>
{{#ask:{{FULLPAGENAME}}
|?Has boolean#成功,失败
}}
</nowiki></pre>
结果：
{{#ask:[[{{FULLPAGENAME}}]]|?Has boolean#成功,失败}}

===类boolean查询===
如果我们想知道“人类”中的角色是不是法师，一般来说需要查询：
<pre><nowiki>
{{#ask:[[category:人类]]
|?is mage#是法师,不是法师
}}
</nowiki></pre>
问题来了，如果我们都没有<code>is mage</code>这个属性，也没有将其设为boolean该怎么办，我们碰巧知道页面上有一个对应职业的分类，那么可以在即使没有boolean值的情况下模拟一个boolean值（因为“<code>?category:法师</code>”这个分类要么'''有'''，要么'''没有'''，不可能有薛定谔的坍缩状态，因此它的存在本身就是一个'''布尔值'''。）
<pre><nowiki>
{{#ask:[[category:人类]]
|?category:法师#是法师,不是法师
}}</nowiki></pre>：
结果：
{{#ask:[[category:人类]]|?category:法师#是法师,不是法师}}

我们再进一步美化一下查询结果：
<pre><nowiki>
{{#ask:[[category:人类]]
|?category:法师#<i class="fa fa-check" aria-hidden="true" style="color:green"></i>,<i class="fa fa-times" aria-hidden="true" style="color:red></i>
}}</nowiki></pre>
结果：
{{#ask:[[category:人类]]|?category:法师#<i class="fa fa-check" aria-hidden="true" style="color:green"></i>,<i class="fa fa-times" aria-hidden="true" style="color:red></i>}}
{{#set:Has boolean=true}}
{{navboxSMW}}
