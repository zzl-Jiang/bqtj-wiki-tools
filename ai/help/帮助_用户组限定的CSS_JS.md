# 帮助:用户组限定的CSS/JS

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3A%E7%94%A8%E6%88%B7%E7%BB%84%E9%99%90%E5%AE%9A%E7%9A%84CSS/JS
revid：42148 · 抓取时间：2026-11-09T14:27:11+08:00

---

{{编辑手册nav}}
除了Common.CSS以外，mw还支持特定用户组单独加载的样式表：
* <code><nowiki>[[MediaWiki:Group-</nowiki>'''''example'''''<nowiki>.css]]</nowiki></code>
* <code><nowiki>[[MediaWiki:Group-</nowiki>'''''example'''''<nowiki>.js]]</nowiki></code>

例如，管理员专用的css列表：[[MediaWiki:Group-sysop.css]]，在此页面书写的样式将对sysop用户组单独生效。

==应用==
可以用来隐藏一些管理员专用的功能和按钮，例如数据维护的链接等等，一来可以防止内容被破坏，二来可以使一般用户看到的内容更加简洁。例如我们可以在目标内容的div上加一个class：
<code><nowiki><div class="admin-panel">想要对普通用户隐藏的内容</div></nowiki></code>

*在Common.css中加入：
<code>.admin-panel
{display:none}</code>
*在Group-sysop.css中加入：
<code>.admin-panel
{display:initial!important;}</code>
{{Data Help
|页面名=帮助:用户组限定的CSS/JS
|描述文字=限定用户组的CSS/JS编辑
|解说=
|symbol=
|主分类=帮助
|子分类=进阶
|tags=编程,JS,CSS
|sortkey=61
|关键=no
|catsortkey=3
|guide=no
|难度=进阶
|角色=设计者
|灰机功能=no
}}
