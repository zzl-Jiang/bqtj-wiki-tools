# 帮助:狗头人APP(v2)

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3A%E7%8B%97%E5%A4%B4%E4%BA%BAAPP%28v2%29
revid：42044 · 抓取时间：2026-11-09T14:27:11+08:00

---

{{编辑手册nav}}
[[File:splash-xhdpi.png|240px|right|非常高清的狗头人]]
狗头人APP在2024年3月更新至2.x。由于改动较大，本文将作为一篇完整的帮助文档阐述如何使用和配置。
*[[帮助:狗头人APP]]仍对1.x版本有效，但1.x版本将逐渐淘汰。
==亮点概述==
*极简流程，不再需要强制注册APP（但也取消了评论和收藏功能）。
*改善浏览体验，虽然仍然是webview但是会更加流畅。

==下载和更新==
APPv2与旧版狗头人APP包名一致，可直接升级。
===安卓===
[https://dl.huijiwiki.com/huijiapp/app-release-latest.apk <span class="btn btn-primary">{{fa|android}} 灰机本地下载</span>]

===IOS===
即将上线

==热更新==
应用版本高于2.1.0的安装包内置了热更新功能。当应用本体稳定后，我们会对应用本体提供热更新包。可以通过如下方式获取：
*点击应用首页右上方的齿轮按钮；
*点击“资源更新”右侧的查看按钮（如无该选项则表示该版本的应用暂不提供热更新包）；
*选择一个稳定版本进行更新。应用会在更新后自动重启。

===关于“接受所有编译器版本”===
如果勾选了“接受所有编译器版本”，则可以选择所有应用版本可用的最新热更新包，但可能会出现bug。

==APP的实现==
新版APP使用uni-app技术开发，同时支持IOS和Android平台。

==弃用的旧版本功能==
*旧版本的用户系统将被弃用，已注册的用户信息、已生成的评论信息等也将在一段时间后销毁。
*如未来有需要，我们将在灰机的用户系统基础上创建与灰机Wiki相通的新版用户系统。

==前端优化指引==

===表格===
过宽的表格（table）会强行撑大页面。如果表格具有<code>wikitable</code>类，维基皮肤会自动为其增加一个带有横向滚动条的外壳。
===图片===
不要使用过大的图片（不论是分辨率还是文件大小）。在引用图片时使用适当的自适应样式可以在容器（包括页面）变窄时使图片自动变窄。参考[[帮助:图片教程#宽度适配]]
===布局===
善用[[帮助:BOOTSTRAP|bootstrap]]的响应式布局。此外，我们建议有足够能力的站点使用grid或flex对现有布局进行改进。
===页面渲染===
不要使用过高开销的模板、函数，不要进行过于复杂的嵌套（尤其是SMW）。
===页面渲染（前端）===
不要过于依赖Javascript。

==站点的收录==
[[File:appv2-home.png|240px|right|APPV2首页]]
狗头人APPv2.x不再强制禁止访问未收录站点，而是采用了“站点推荐列表”的方式进行站点的筛选。

处于推荐列表中的站点会显示在APP首页中，未收录的站点可通过APP顶部的“直接访问”文本框进行访问。

如希望自己的站点出现在APP首页，请首先按如下方式进行检查：
*站点主题符合“游戏”或“文化”；
*完成度达标；
**有效条目数>200
**核心概念基本完成，不存在结构性内容缺陷，灰链处于可控范围
*基本没有适配问题；
**可使用手机浏览器访问站点以确认适配问题

===申请方式===
由机长或管理员向维基管理组（a.k.a.三狗一猫）进行申请。
*可以通过任意官方灰机QQ群申请。
*可以通过邮箱（support@huiji.wiki）申请。

申请时请自报站点信息。

==开发与适配==

===样式补丁===
Wiki页面在APP2.0中打开时，body会增加一个class<code>huijiapp</code>。对app侧进行的适配可以使用这个选择器进行操作。
<pre>
.infobox {/*在所有终端生效*/
font-size:14px;}
.huijiapp .infobox {/*仅在app端生效*/
font-size:16px;
}
</pre>
旧版本的<code>mediawiki:app.css</code>将在新版本中弃用。

为了便于调试，你可以在浏览器UA中增加字符串<code>HuijiApp/2.0</code>来模拟APP侧的页面显示效果。

请注意，以下配置应当严格按照json格式（下例中包含了注释，但json格式不允许注释）。

===快捷入口===
[[File:appv2-siteintro.png|240px|right|快捷入口]]

在站点中建立<code>MediaWiki:AppWikiConfig.json</code>可以用于配置APP端的“索引”页，建立<code>MediaWiki:AppToolConfig.json</code>可用于配置APP端的“工具”页。未建立这些页面的站点仍可通过APP正常访问，但不会出现相应的快捷入口。

====索引页配置格式====

<pre>
// MediaWiki:AppWikiConfig.json
{
    // 顶栏背景，app2.x弃用
    "bannerImage": "https://huiji-public.huijistatic.com/ff14/uploads/9/9f/Logo_6_0.png/800px-Logo_6_0.png",
    "pageGroups": [
        { // 分组名称
            "label": "掉落查询",
            "pages": [
                {
                    // 图标，可以不配或留空字符串
                    "icon": "https://huiji-public.huijistatic.com/ff14/uploads/3/3a/000058.png",
                    // 显示名称。如果不配置会使用title
                    "label": "坐骑",
                    // 页面标题（即链接）
                    "title": "坐骑获取方式"
                }
            ]
        }
    ]
}
</pre>
====工具页的配置方式====
<pre>
// MediaWiki:AppToolConfig.json
{
    "pageGroups": [
        {
            // label：已弃用，因为不知道是干什么的
            "label": "1",
            "pages": [
                {
                    // 显示名称
                    "label": "物品检索器",
                    // 实际页面标题（链接）
                    "title": "ItemSearch"
                }
            ]
        }
    ]
}</pre>

==法务信息==
*[[Project:App隐私政策|App隐私政策]]
