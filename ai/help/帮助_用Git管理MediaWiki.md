# 帮助:用Git管理MediaWiki

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3A%E7%94%A8Git%E7%AE%A1%E7%90%86MediaWiki
revid：39609 · 抓取时间：2026-11-09T14:27:11+08:00

---

{{编辑手册nav}}
<callout class="warning" style="overflow:hidden;">
<h4>这篇文档假定您已熟知Git。</h4>
想要了解更多关于Git的知识，您可以搜索Git教程。
</callout>
对于开发者而言，往往需要在多个不同页面上编写代码，时间一长就难免头晕脑胀。常见的做法是在线下编写代码，再将代码复制到Wiki上。但是你可知道，用Git就能直接管理MediaWiki的页面？

首先，你需要为你的Git打一个补丁。参阅：[https://github.com/Git-Mediawiki/Git-Mediawiki/wiki/User-manual Git-MediaWiki文档]。

之后，你就可以使用
<pre>
git clone mediawiki::http://yourwiki.huijiwiki.com
</pre>
来获得维基源码。

Git-MediaWiki在获取整个维基时速度非常慢，建议采用shallow clone，并且只clone部分页面（可以采用分类或者直接输页面名）而不是所有页面。
<pre>
git clone -c remote.origin.pages='Module:Infobox' -c  remote.origin.shallow=true mediawiki::http://templatemanager.huijiwiki.com
</pre>

结果：
[[文件:Git-mw.png|frameless|300px]]

进行修改后，你可以使用
<pre>
git commit -a -m "commit message"
</pre>
<pre>
git config remote.origin.mwLogin 'UserName'
git config remote.origin.mwPassword 'PassWord'
git push 
</pre>
来提交代码。
{{Data Help
|页面名=帮助:用Git管理MediaWiki
|描述文字=使用Git管理MediaWiki
|解说=
|symbol=<i class="fa fa-github" aria-hidden="true"></i>
|主分类=帮助
|子分类=复杂
|tags=编程,管理,数据更新
|sortkey=52000
|关键=no
|catsortkey=4
|guide=no
|难度=复杂
|角色=开发者
|灰机功能=no
}}
