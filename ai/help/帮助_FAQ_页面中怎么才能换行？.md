# 帮助:FAQ/页面中怎么才能换行？

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3AFAQ/%E9%A1%B5%E9%9D%A2%E4%B8%AD%E6%80%8E%E4%B9%88%E6%89%8D%E8%83%BD%E6%8D%A2%E8%A1%8C%EF%BC%9F
revid：39745 · 抓取时间：2026-11-09T14:27:09+08:00

---

==源代码编辑器==
在'''[[help:编辑页面|源代码编辑器]]'''中相当于直接书写Html代码，而Html代码是不存在<code>“回车=换行”</code>这种规则的，实现换行只有两种方法：
#书写一段新的段落，即“<code><nowiki><p></p></nowiki></code>”
#使用强制换行符：<code><nowiki><br/></nowiki></code>

因此在编辑过程中，源代码编辑器中的标记语言需要通过MediaWiki的Parser被解析成为对应的Html代码：为了实现换行可以对应的输入：
#方法一：段末敲击两下回车，即“空一行”，这种代码会被MediaWiki的Parser解析为一个新的段落（<code><nowiki><p></p></nowiki></code>）。
#方法二：段末添加<nowiki> <br> </nowiki> 或者 <nowiki> <br/> </nowiki>，这种代码会被MediaWiki的Parser解析为强制换行符：<code><nowiki><br/></nowiki></code>。

==br和换行的比较以及选择==
*方法一的换行方法是html语言中的“真换行”，方法二是“假换行”
*真换行是p标签，能够被皮肤中的段落样式所应用，反之br会导致行间距与正文不同，造成视觉上的文字拥挤，不利于维基化和样式设计。

==可视化编辑器==
所见即所得，回车=换行

==模板中的换行==
在源代码编辑器中，目前版本的MediaWiki会把<code><nowiki>{{}}</nowiki></code>中的单换行解析成一个新的<code><nowiki><p></p></nowiki></code>，故而会出现”换行“
*这个情况在版本较老的MediaWiki，比如1.19（wikia/fandom）中不会被解析成<code><nowiki><p></p></nowiki></code>

因此从wikia/fandom搬运代码时，可能会出现上述问题，解决方法很简单，删掉模板中无意义的换行即可，如果为了方便阅读，可以使用注释换行，例如
<pre>
{{template
|param =1
|html = <div>{{{1|}}}<!--
--></div>
}}</pre>

[[Category:FAQ]]
