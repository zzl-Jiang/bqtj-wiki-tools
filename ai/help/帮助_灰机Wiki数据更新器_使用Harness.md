# 帮助:灰机Wiki数据更新器\使用Harness

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3A%E7%81%B0%E6%9C%BAWiki%E6%95%B0%E6%8D%AE%E6%9B%B4%E6%96%B0%E5%99%A8%5C%E4%BD%BF%E7%94%A8Harness
revid：42636 · 抓取时间：2026-11-09T14:27:11+08:00

---

{{编辑手册nav}}{{quote|现在是AI辅助编辑WIKI的时代|}}

历史的巨轮滚滚向前，从前推荐的[[帮助:灰机Wiki数据更新器/使用VSCode|使用VS Code]]编辑wiki的方法现在已经过时了，本文主要着重探讨如何使用流行的Harness来编辑wiki。
[[File:use harness.jpg|400px|center|link=]]
==前言==
你需要什么？
*一个可以正常工作的Harness，它不特指“DeepSeek Harness”，也可以是VS Code这样的IDE（包括跟它类似的Trae或者Code Buddy\Work Buddy），或者是Pi，OMP，或者各种各样的CLI（qwen、kimi、claude）。你的大模型来源也可以不拘一格，无论是免费积分，还是中转站又或者是自己的付费API，总之，只要有足够的token，剩下的区别主要是你荷包的承受能力，以及对Coding流程的熟悉程度。
*[[帮助:灰机Wiki数据更新器|huijiWiki Updater V3]]：一句话介绍Updater V3——“关于灰机wiki的AI知识库+线上线下同步工具+请求探针”，让你的本地Harness耳聪目明。

===我该怎么选？===
**简单的一句话问题，使用HujiAgent提问；
**需要简单的批量操作，使用灰机工作区；
**工作量比较大的重复性劳动，使用[[帮助:灰机Wiki数据更新器|huijiWiki Updater V3]]，因为他不需要消耗宝贵的token；
**宏大的更新项目，涉及到管线复用，使用AI Harness架构+[[帮助:灰机Wiki数据更新器|huijiWiki Updater V3]]；

===我应该避免什么？===
*向DeepSeek网页版，豆包APP许愿开发wiki功能
**Why? 任何在线AI都不可能了解灰机wiki的实际情况，只能通过训练时的基本知识（原生MediaWiki）和临时抱佛脚搜到的网络信息（大概率会被灰机服务器拦截屏蔽），得出的结论不具备准确性，大概率导致水土不服或者无法正常使用，变成屎山代码。

==工作流程示例==
*在你的本地硬盘创建一个目录（工作区），将VS Code\Trae\Code Buddy的工作区设定为这个目录。
*打开你下载的huijiWiki Updater V3，使用你的bot账号登录（确认这是一个可以正常编辑的账号，同时具有你想要维护站点的管理员和机器人权限）
[[File:harness1.jpg|400px|center|link=]]
*新建一个任务，输入你要维护站点的key，为了避免日后维护时挠头，你可以写上任务描述，例如“批量更新数据”、“维护物品道具信息”。
[[File:harness2.jpg|400px|center|link=]]
*打开刚创建的任务，将工作区目录设置为你刚才创建的本地文件夹，选择“页面同步”，将所有[[帮助:命名空间|命名空间]]选中，点击“获取页面”，如果一切顺利的话，你将在几分钟~数个小时内获得一套完整的本地页面环境。（具体时间取决于拉取的页面数量）
**为什么要尽可能多到拉取页面到本地？因为页面越多，特别是模板、模块、JavaScript\CSS（他们通常以Gadget空间页面出现），就越能全面的呈现wiki的真实情况，对于AI来说，在海量代码中分析逻辑是人类不具备的强项，这是最大化利用AI能力的方式。同网页或者app提问的AI相比，本地Harness的AI所获得的参考资料更为全面，因此更能掌控全局。
[[File:harness3.jpg|400px|center|link=]]
*打开huijiWiki Updater V3的“AI增强”，点击“同步资料”、“一键植”入，接下来你的AI将开启“超级赛亚人状态”并大幅降低token消耗量。
[[File:harness4.jpg|400px|center|link=]]
*拿起“仙女棒”，对你的AI大模型说清楚需求，然后坐等许愿成真。
*一切尘埃落定后，你可以手动点击 刷新+以文本更新将页面提交到线上，也可以让你的AI通过updater提供的CLI命令自动提交更新。
*当需要查看预览时，你可以让你的AI直接请求到真实的渲染页面，并进行反馈修正，避免原生的本地或机房fetch请求被cloudflare拦截。
**对于大部分AI开发场景来说，如何纠偏是决定能否快速将功能实现的关键，如果没有稳定的反馈链路，AI将很难通过简单的修订达到预期设计，页面预览功能保证AI能够真实的得到工作结果的反馈。特别是对于那些Harness中自带多模态能力的AI来说，这是事半功倍的关键。

==典型工作场景==
*将xxx游戏进行解包，数据转换成灰机wiki支持的格式，部署到线上，然后用Gsearch+huiji-Tooltip快速实现一套异步加载的检索器；
*帮我分析这部文学著作，按照章节、人物、地点、事件等多个维度解析，然后结合灰机wiki推荐的模板功能，为我搭建wiki；
*这个wiki年久失修，有很多旧的实现代码，我不知道该怎么优化他们并更新到一个理想的完成度；
*我需要在几千个页面中找到一些前后矛盾的翻译和术语，按照一个给定的术语表勘正他们；

==推荐链接==
现在各大软件处于推荐期，如果你从来没用过集成的工具，通过下面的链接点击注册可以获得积分（用来免费使用大模型），链接都是狗头人的，请自行取用，如果你有自己的推荐链接，也可以联系狗头人发布在这里供他人使用！
*发现过期了可以群里反馈：[http://qm.qq.com/cgi-bin/qm/qr?_wv=1027&k=4qonX-_C29PNQvT-cvAMrL_GRnjyyWzq&authKey=REP3ZPSZmpvKN2dOizOCSnzEMolicScGSHUHiRDiW1anFzuqRxVSsfJIQXCXlP7Y&noverify=0&group_code=1053537685 点此加群向狗头人反馈]
;WorkBuddy:
*[https://www.workbuddy.cn/events/invite?inviteCode=cddi613mrl4 2,000 WorkBuddy积分]
;Trae:
*[https://www.trae.cn/events/code-fission/AP4DSK23NFFY?utm_source=copy_link&utm_medium=code_fission 3,000 Trae积分]
;Qoder:
*[https://qoder.com/activities?referral_code=CL73NUM7V4SCcAZhvxQrgEXB5VJBZR2z 500 Qoder积分]

{{Data Help
|页面名=帮助:灰机Wiki数据更新器\使用Harness
|描述文字=使用Harness
|解说=
|symbol=<i class="fa fa-file-text" aria-hidden="true"></i>
|主分类=帮助
|子分类=复杂
|tags=编程,管理,数据更新,Lua
|sortkey=52100
|关键=no
|catsortkey=4
|guide=no
|难度=复杂
|角色=开发者
|灰机功能=no
}}
