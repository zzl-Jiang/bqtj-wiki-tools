# 帮助:AWB机器人

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3AAWB%E6%9C%BA%E5%99%A8%E4%BA%BA
revid：39556 · 抓取时间：2026-11-09T14:27:09+08:00

---

{{编辑手册nav}}
<callout>注意，AWB现在启动时需要科学上网，启动项加载完成后就可以断开了</callout>
'''[[wikipedia:wikipedia:AutoWikiBrowser|AutoWikiBrowser]]'''是一个适用于所有编辑者，特别是站长、数据管理员的自动批处理bot软件。
*软件[http://sourceforge.net/projects/autowikibrowser/ 下载]下载
*详细的说明和使用文档可以在[[wikipedia:Wikipedia:AutoWikiBrowser/User manual|这里]]查看。

==何时使用AWB==
我们'''推荐'''在以下场景使用AWB、
*大规模的维护页面，比如清洁页面（删除冗余的杂碎内容，对齐模板参数，修改分类，批量删除分类，添加消歧义和重定向）
*批量替换链接，或者模板，常见于译名出现变更时，用以搜索和替换。
*获取引用了特定模板的页面列表

===不建议使用AWB的场景===
以下情况我们建议使用[[帮助:灰机Wiki数据更新器]]
*上传、更新模板内的参数
*批量传图，批量创建data页面
*批量删除页面

以下情况我们建议使用自定义的[[帮助:Python|python脚本]]
*您会写python
**有过于具体的修改、替换方案，尤其是带着本地数据对照修改页面时

==准备==
在使用AutoWikiBrowser之前，首先需要建立一个[[帮助:机器人#机器人账号|机器人账号]]。同时需要在您的站点建立这一页面“Project:AutoWikiBrowser/CheckPage”

*例如在[[lotr:首页|魔戒中文维基]]，即为页面[[lotr:魔戒中文维基:AutoWikiBrowser/CheckPage|http://lotr.huiji.wiki/wiki/魔戒中文维基:AutoWikiBrowser/CheckPage]]
*需要搬运的内容为[[AWB与机器人/CheckPage]]。请将此页面全部源代码复制到需要使用AWB的维基下的同名词条，并替换“用户名”为需要使用的机器人用户名。

*在AutoWikiBrowser中，进行如下设置：

[[文件:AWB1.png|left|thumb|600px|点击右下角站点名进行设置（默认为en.wikipedia）]]
[[文件:AWB2.PNG|left|thumb|420x420px|选择custom]]
[[文件:awb new 1.jpg|left|thumb|420x420px|输入要编辑的站点名，例如lotr.huiji.wiki(灰机现在已经是https协议，记得将默认的http修改为https)]]

[[文件:AWB4.PNG|left|thumb|600px|点击此处配置账号]]
[[文件:awb new 1.jpg|left|thumb|420x420px|使用您的机器人账户登录]]
{{clear}}

==使用说明==
*AWB的使用方法大致分为两步：
**第一步——make list （准备页面列表），AWB提供了丰富的预选项，可以通过分类、特定用户贡献、最近更改、引用模板等方式来进行组合，并通过filter做进一步是筛除，注意，make list不限制操作次数，每次选取的列表会被叠加，你可以选择去重或者重新排序，也可以将列表手动导出到txt文本。
**第二步，执行操作，下方有各种执行标签，集成了常用的维护、清洁、修改功能，根据你的需求进行勾选，最后执行
**当登录账号在网站上的用户权限包含<code>机器人</code>时，才会出现bots标签，勾选auto save可以启动自动保存功能，否则只能手动的，逐条保存修改命令。
[[File:awb new 4.jpg|400px|left|thumb|只有bot账户才能开启auto save]]
{{clear}}
*默认开启REDIRECT FOLLOW功能，即会跟着重定向跳转条目，如果您想操作重定向页面，可以在顶部的功能菜单里去掉这个选项。
[[File:awb new3.jpg|400px|left|thumb|在此处开启/关闭跟随重定向功能]]

{{clear}}
==批量替换==
[[File:awb new 7.jpg|400px|thumb|left]]
AWB提供的高级替换功能，支持对替换进行条件判断，可以自行组合并开启正则表达式匹配。
{{Data Help
|页面名=帮助:AWB机器人
|描述文字=AutoWikiBrowser
|解说=
|symbol=
|主分类=帮助
|子分类=进阶
|tags=机器人,编程,管理,数据更新,编辑,维基化
|sortkey=50200
|关键=no
|catsortkey=3
|guide=no
|难度=进阶
|角色=开发者
|灰机功能=no
}}
