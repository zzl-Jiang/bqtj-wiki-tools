# 帮助:Bot

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3ABot
revid：39551 · 抓取时间：2026-11-09T14:27:09+08:00

---

{{编辑手册nav}}
'''Bot'''，即通常MediaWiki用户口中所说的“机器人”，但他并不是“robot”或者“android”的意思。
:概括的说，bot一般指的是在MediaWiki或其他维基软件中，通过调用[[帮助:API|系统接口]]（API）来实现的action（例如edit、delete、info、purge等等）的自动化。
*bot通常来说伴随着大批量、大规模的重复性操作。与人为的构思条目、编辑内容有着较大的区别，为了避免对正常编辑者编辑行为的误导、混淆，我们通常会在软件层将bot操作进行特殊标记，不会在默认的贡献列表、修改记录中出现；
**在灰机，bot行为不会被统计为编辑数量，因此也不会进入用户编辑次数排行榜的统计之中，在最近更改中，通过点选“显示机器人”可以查看bot操作。
*同时为了避免混淆个人贡献，我们一般不鼓励使用默认的用户身份进行bot操作，而是鼓励创建专门的bot账号，并授予bot权限，专门处理bot行为。

==bot的操作==
===使用已有的bot框架===
*[[帮助:AWB机器人|AutoWikiBrowser]]，简称“AWB”，是一个适用于所有编辑者，特别是站长、数据管理员的自动批处理bot软件。
*[[帮助:灰机Wiki数据更新器|灰机Wiki数据更新器]]，简称“Updater”，是一个针对灰机构建的，python编写的GUI功能bot软件，与AWB功能互补。

===在编程语言中使用bot===
在Python、JS（线下）、MediaWiki JS（线上）或者其他编程语言，比如C#中，用户可以自行调用MediaWiki的API来进行脚本操作，通过对编辑行为的<code>edit</code>中添加<code>bot=True</code>的字段，来进行bot操作。
*Python中使用requests库进行直接通信，endpoint的书写请严格对照[https://www.mediawiki.org/wiki/API:Main_page MediaWiki的官方文档]。
*Python中使用[[帮助:Python#方法二：直接交互|mwclient库]]来进行操作，mwclient是已经封装过的官方API脚本，底层使用requests实现，可以简化代码的书写。

==关于pywikibot==
出于以下原因，我们不推荐使用pywikibot
#没有GUI
#需要编程基础
#功能与AWB、Updater重叠
#配置环境繁琐

==AWB、Updater与python脚本的比较==
===建议使用AWB的场景===
我们'''推荐'''在以下场景使用AWB、
*大规模的维护页面，比如清洁页面（删除冗余的杂碎内容，对齐模板参数，修改分类，批量删除分类，添加消歧义和重定向）
*批量替换链接，或者模板，常见于译名出现变更时，用以搜索和替换。
*获取引用了特定模板的页面列表

===建议使用Updater的场景===
以下情况我们建议使用[[帮助:灰机Wiki数据更新器]]
*上传、更新模板内的参数
*批量传图，批量创建data页面
*批量删除页面

===建议使用本地脚本的场景===
以下情况我们建议使用自定义的[[帮助:Python|python脚本]]
*您会写python
**有过于具体的修改、替换方案，尤其是带着本地数据对照修改页面时
{{Data Help
|页面名=帮助:Bot
|描述文字=Bot机器人
|解说=
|symbol=
|主分类=帮助
|子分类=进阶
|tags=机器人,编程,管理,数据更新
|sortkey=50300
|关键=no
|catsortkey=2
|guide=no
|难度=进阶
|角色=开发者
|灰机功能=yes
}}
