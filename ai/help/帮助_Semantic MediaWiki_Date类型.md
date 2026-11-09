# 帮助:Semantic MediaWiki/Date类型

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3ASemantic%20MediaWiki/Date%E7%B1%BB%E5%9E%8B
revid：33352 · 抓取时间：2026-11-09T14:27:10+08:00

---

'''Date类型'''是记录时间日期的专属类型
*支持多语言
*支持时区offset
*支持改变格式
以本页面记录的date为例，默认<code><nowiki>{{#show:{{FULLPAGENAME}}|?Has date}}</nowiki></code>显示为：{{#show:{{FULLPAGENAME}}|?Has date}}

==MEDIAWIKI==
通过添加#MEDIAWIKI使得日期格式用mediawiki的样式输出：
*<code><nowiki>{{#show:{{FULLPAGENAME}}|?Has date#MEDIAWIKI}}</nowiki></code>
结果：
{{#show:{{FULLPAGENAME}}|?Has date#MEDIAWIKI}}

==LOCL==
例子：<code><nowiki>{{#show:{{FULLPAGENAME}}|?Has date#LOCL}}</nowiki></code>
结果：{{#show:{{FULLPAGENAME}}|?Has date#LOCL}}

==ISO==
例子：<code><nowiki>{{#show:{{FULLPAGENAME}}|?Has date#ISO}}</nowiki></code>
结果：{{#show:{{FULLPAGENAME}}|?Has date#ISO}}

==F（Free模式）==
例子：
<pre><nowiki>
{{#ask:{{FULLPAGENAME}}
|?Has date#GR-F[Y/m/d H:i:s]=通用格式
|?Has date#-F[Y/m/d H:i:s]=样式2
|?Has date#-F[D M j G:i:s T Y]=样式3
|?Has date#-F[l jS \of F Y h:i:s A]=样式4
}}</nowiki></pre>
结果：
{{#ask:[[{{FULLPAGENAME}}]]
|?Has date#GR-F[Y/m/d H:i:s]=通用格式
|?Has date#-F[Y/m/d H:i:s]=样式2
|?Has date#-F[D M j G:i:s T Y]=样式3
|?Has date#-F[l jS \of F Y h:i:s A]=样式4
}}

==SORTKEY==
返回Julian day的记法
例子：<code><nowiki>{{#show:{{FULLPAGENAME}}|?Has date#SORTKEY}}</nowiki></code>
结果：{{#show:{{FULLPAGENAME}}|?Has date#SORTKEY}}

===JD(儒略日记法)===
::参见：'''[[wikipedia:Julian day|Julian day]]'''
*<code><nowiki>{{#show:{{FULLPAGENAME}}|?Has date#JD}}</nowiki></code>
结果：
{{#show:{{FULLPAGENAME}}|?Has date#JD}}

==纪元==
在[[Test页面/日期]]页面上<code><nowiki>[[Has date::3BC]]</nowiki></code>
*<code><nowiki>{{#show:Test页面/日期|?Has date}}</nowiki></code>得到结果：{{#show:Test页面/日期|?Has date}}
{{#show:{{FULLPAGENAME}}|?Has date#}}+2:00
==时区偏移（offset）==
===+/-时间量===
*<code>Feb 28 2004 23:00+2:00</code>=<code>29 February 2004 01:00:00</code>
*<code>Feb 28 1900 23:00+2:00</code>=<code>1 March 1900 01:00:00</code>
===时区===
::参考：[[wikipedia:List_of_time_zones_by_country|List_of_time_zones_by_country]]
*<code>ADT</code>, <code>AST</code>, <code>CET</code>, <code>CST</code>, <code>CXT</code>, <code>EST</code>, <code>HAC</code>, <code>HAT</code>, <code>HNR</code>, <code>MEZ</code>, <code>MST</code>, <code>NFT</code>等等
{{#set:Has date=2015-05-22T17:32}}
{{navboxSMW}}
