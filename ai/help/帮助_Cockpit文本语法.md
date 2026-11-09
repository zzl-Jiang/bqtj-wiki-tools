# 帮助:Cockpit文本语法

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3ACockpit%E6%96%87%E6%9C%AC%E8%AF%AD%E6%B3%95
revid：41606 · 抓取时间：2026-11-09T14:27:09+08:00

---

cockpit文本语法是灰机驾驶室中使用的一种文本标签格式，目前在如下功能中生效：
*用户留言/对话；
*页面评论。

随着驾驶室版本的升级，cockpit语法可能会扩充一些新功能，届时将在本帮助文档中更新使用方法。

==排版==
*回车会在提交时处理为<code><nowiki><br /></nowiki></code>，实际显示的时候<code><nowiki><br /></nowiki></code>会被处理为<code><nowiki><p></nowiki></code>。
*在二次编辑（例如编辑评论）时，此前输入的回车会显示为<code><nowiki><br /></nowiki></code>。
*不支持本文未列出的其他标签。这些标签均会被处理为文本。

==站内链接==
与跨wiki链接的写法一致，但只支持灰机wiki的站点。

与跨wiki链接的区别：
*wiki前缀不可省略，因为cockpit语法不依赖mediawiki上下文————不论是当前站点的链接还是跨站链接均需要写前缀。
*指向灰机主站的前缀需要使用www，而不是h。
*该语法不会判断页面是否存在（不存在灰链）。
<pre>
// 指向灰机文档中心的链接
[[www:communityCenter]]
// 可以换个显示名称
[[www:communityCenter|文档中心]]
// 支持namespace
[[warcraft:模板:fa]]
[[warcraft:模板:fa|Font Awesome]]
// 但是这种写法是错的（因为必须加prefix）：
[[communityCenter]]
[[模板:fa]]
</pre>
==指向用户的链接==
以<code>User:,user:,用户:</code>开头的双方括号会被处理为用户链接，不支持修改显示名称。
<pre>
// 指向狗头人，首字母不区分大小写
[[user:serGawen]]
// 不支持这样写：
[[user:serGawen|狗头人]]
</pre>

==指令==
方括号内以冒号开头的字符串会被视为指令。目前支持：
===emoji===
<pre>
[[:emoji:mouse]]
// 输出🐭
</pre>
emoji指令的主要功能是兼容此前留言中的emoji。实际使用时，你可以直接通过输入法或者复制粘贴使用emoji。
