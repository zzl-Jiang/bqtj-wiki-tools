# 帮助:狗头人APP

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3A%E7%8B%97%E5%A4%B4%E4%BA%BAAPP
revid：39605 · 抓取时间：2026-11-09T14:27:11+08:00

---

{{编辑手册nav}}
==狗头人APP==
“'''狗头人APP'''”是由灰机wiki和灰机GAME打造的wiki阅读APP，作为灰机wiki在移动平台阅读体验的延申。
:请注意，狗头人APP像灰机WIKI一样，是一个平台框架，其中的内容'''不完全取决于'''灰机和狗头人团队。
:<span class="text-danger">注意：APP账号与网站不通用（[[帮助:狗头人APP#社交化功能|why？]]）</span>
:<span class="text-danger">注意：使用体验与站点自行优化有关（[[帮助:狗头人APP#APP的优化指引|如何优化APP体验？]]）</span>
:<span class="text-danger">注意：WIKI站点样式、配色由社区自行设计和修改</span>
==APP下载==

狗头人APP目前还属于测试阶段，各大应用市场申请审核中。

请访问[[灰机wiki:AppDownload]]获取下载地址。<!--
{{AppDownload}}-->
{{clear}}

==APP预览==
<gallery heights = 220>
File:APP截图1.jpg
File:APP截图2.jpg
File:APP截图3.jpg
File:APP截图4.jpg
File:APP截图5.jpg
File:APP截图6.jpg
</gallery>

==APP的实现==
[[File:flutter-lockup-c13da9c9303e26b8d5fc208d2a1fa20c1ef47eb021ecadf27046dea04c0cebf6.png|right|200px]]
狗头人APP使用<code>[https://flutter.dev/ flutter]</code>开发，将同时支持IOS与Android平台。

==开发者声明==
APP由“WIKI阅读+资讯+社交化讨论”模块组成，现阶段，用户突出的需求为WIKI阅读，因此我们会优先部署相关功能，其他功能会在日后逐步添加。
:由于APP无法100%的实现网页的wiki编辑体验，所以我们完全放弃了编辑功能
===资讯===
“'''资讯'''”模块由APP原生界面开发，内容来自灰机GAME，以游戏和流行文化为主。

===社交化功能===
:<span class = "text-danger">'''本APP采用全新的手机实名用户体系'''，与现有的网站用户数据不共通。</span>
:<span class = "text-danger">根据国家的法律法规要求，狗头人APP使用手机作为用户身份验证标识，注册信息将会被记录，违法行为可能被追责。</span>

为了符合国家对于'''APP的实名制注册'''要求，狗头人APP采用手机作为身份标识进行注册，注册完成后，用户可以自行指定新的密码。
*所有灰机wiki的用户都需要重新注册新的APP账号，可以与灰机wiki已有的账号相同，也可以不同，不做硬性关联
**剥离APP与wiki编辑者账户可以避免概念上和各种意义上的混淆和困惑。
**我们一如既往的鼓励wiki编辑者在PC端进行贡献，我们也会持续的关注和改善PC端的编辑、使用体验。但手机端及APP端的使用习惯、场景都与wiki的编辑流程和模式相背离，因此我们不希望您把狗头人APP视为“灰机wiki”在移动端的延伸，因为充其量它是且只能是“灰机wiki阅读体验在移动端的延伸”。

===WIKI阅读===
由于wiki是'''UGC'''模式，页面中嵌套了大量由编辑者自己撰写的模板、JS脚本、Lua代码等开发者团队无法准确预估的内容和样式，'''因此无法对页面内容进行APP原生层面的开发'''，目前所有的'''wiki条目页面部分'''只能采用webview嵌套的方式呈现。

:各个站点的前端样式由站点自行设计、修改，APP开发团队不适合也没有权限去进行修改，因此狗头人APP的阅读体验、加载速度将很大程度上取决于子站点自身：

（'''站长、管理员、开发者请注意'''）：
*<span class = "text-danger">原始页面的书写是否规范？对窄屏支持和适配的程度越高，APP阅读体验越好</span>；
*<span class = "text-danger">原始页面的性能是否合理？冗余代码、嵌套模板越少，APP加载速度越快</span>；

尽管如此，灰机APP开发团队依然会努力对APP的使用和体验进行优化，包括且不限于对各个站点前端样式、代码书写的指导，也希望广大使用者能够多一些理解和耐心。

===CSS补丁===
*APP全局加载：[[h:MediaWiki:app.css]]
**各站点自行加载：<site>:MediaWiki:app.css

:在灰机主站的<code>[[MediaWiki:App.css]]</code>会对所有子站点生效，因此这里做过的优化部分，各个站点就无需再做了
:各个站点可以单独在本站的<code>MediaWiki:App.css</code>页面单独书写仅在APP加载的样式表，该站点的机长、管理员都有权限进行修改

====备选方案====
你也可以在自己站点的<code>Mediawiki:common.css</code>中添加app中的css补丁。
*相对于在<code>app.css</code>中写样式而言，在<code>common.css</code>中写样式生效更快，且更容易管理。但你需要在所有仅在app端生效的选择器前增加<code>.huijiapp</code>。例如：
<pre>.infobox {/*在所有终端生效*/
font-size:14px;}
.huijiapp .infobox {/*仅在app端生效*/
font-size:16px;
}</pre>
访问[[灰机APP更新日志/20200507]]以获得与该方案相关的资料。

===APP的优化指引===
灰机会对已经收录的站点会进行针对性的优化，但整体的体验依然非常依赖站点团队对历史内容、后续生产内容所进行的持续优化，下面是一些需要注意的要点：
#【前端适配】：尽量减少或不用table对页面布局，已有的table使用“wikitable”类（灰机的js脚本会对这个类的table套一个适配的外壳），以方便灰机进行针对性优化；
#【前端适配】：不要使用尺寸过大的图片，或者在窄屏上不友好的布局方式；
#【前端适配】：模板、页面内元素不要使用定宽，特别是大于240px的定宽，可以使用bootstrap预设的响应式类或者使用相对宽度（width:100%）；
#【加载优化】：页面不要使用过高的开销或冗余的嵌套模板，请尽量将页面的裸加载时长控制在3s以内，以1s以内为佳。大量模板嵌套、SMW查询会拖慢页面的首次加载速度；
#【加载优化】：页面不要使用冗余、非必要的JavaScript脚本；
#【交互优化】：<span class = "text-danger">由于现阶段Flutter的固有缺陷，调用默认浏览器组件的行为将无法进行操作，比如网页表单，需要开发者注意</span>此问题会随着Flutter框架的更新而得到解决。

==APP的站点收录==
目前分为“GAME”和“Culture”两个大类，分别收录，首批收录为灰机'''邀请'''制，后续收录方式为”'''申请-审批'''“制：

===申请条件===
*主题符合“<code>GAME</code>”或者“<code>Culture</code>”范围以内的灰机托管站点
*托管站点'''达到一定的完成度'''：
**站点有效条目数<code>>200</code>
**核心概念基本完成，不存在结构性内容缺陷

以下情况'''不会'''被APP收录
*站点存在大量低质量页面、空页面或者未经翻译英文页面的
*站点不属于上述范畴的
*<code>站点样式优化较差，在移动端体验极差的，或是大量使用过时的前端技术进行布局的</code>（比如table）

===申请方式===
符合上述条件的站点，必须由机长或者管理员向[[user:SerGawen]]发起申请，才能被APP录入
*联系方式可以通过QQ群、邮箱（support@huiji.wiki/ga@huiji.wiki）
**<s>如果您没有上述方式，就不要凑热闹了</s>

===申请通过后的自行配置工作===
在APP收录通过后，还有一些简单的后续工作需要机长（或管理员）自行配置，流程参加[[#配置APP|下一章节]]。


==配置APP==
为了配合'''狗头人APP'''的更新，目前采用站点自配置APP主页的方式，即通过内容审核的站点需要自行配置若干json页面，以决定哪些内容展示在该站点在'''APP中的首页上'''。
[[File:APP截图3.jpg|300px|配置完成实例（实际截图）|right]]
'''实际参考图参见右侧'''
*APP首页导航：<nowiki>https://</nowiki><code>prefix</code>.<nowiki>huijiwiki.com/wiki/MediaWiki:AppWikiConfig.json</nowiki>
**例子：https://tarsylia.huijiwiki.com/wiki/MediaWiki:AppWikiConfig.json
{| class="wikitable"
|-
! key !! 说明 !! 建议
|-
| bannerImage || 显示在app首页的顶部banner图 || 建议尺寸：800 × 150<br>png或jpg，不宜过大，
|-
| pageGroups[item]<br>&nbsp;<code>label</code> || 分组的展示标题 || 例如“人物”、“地点”、“推荐词条”
|-
| pageGroups[item]<br>&nbsp;pages[item]<br>&nbsp;&nbsp;<code>icon</code>  || 条目的配套小图标，可以单独配置，也可以所有都用相同的抽象icon || 64×64，最好是jpg
|-
| pageGroups[item]<br>&nbsp;pages[item]<br>&nbsp;&nbsp;<code>label</code>  || 条目链接的显示文字，可以和链接一样 || 
|-
| pageGroups[item]<br>&nbsp;pages[item]<br>&nbsp;&nbsp;<code>title</code>  || 指向的条目名称 || 
|}
*APP工具导航：<nowiki>https://</nowiki><code>prefix</code>.<nowiki>huijiwiki.com/wiki/MediaWiki:AppToolConfig.json</nowiki>
**例子：https://warframe.huijiwiki.com/wiki/MediaWiki:AppToolConfig.json
{| class="wikitable"
|-
! key !! 说明 !! 建议
|-
| pageGroups[item]<br>&nbsp;<code>label</code> || 分组的展示标题，'''不显示''' || 
|-
| pageGroups[item]<br>&nbsp;pages[item]<br>&nbsp;&nbsp;<code>label</code>  || 条目链接的显示文字，可以和链接一样 || 
|-
| pageGroups[item]<br>&nbsp;pages[item]<br>&nbsp;&nbsp;<code>title</code>  || 指向的条目名称 || 
|}



==关于狗头人APP==

===狗头人APP的目的===
'''狗头人APP是一个以追求商业盈利为目的的APP'''：狗头人APP不是一个为了“改善移动端体验”或者“造福wiki编辑者”而开发的APP，因为<code>在移动端根本无法编辑wiki，移动端的浏览行为对wiki模式的贡献近乎于零</code>。
为了开发、维护狗头人APP<s>，狗头人需要支付额外的蜡烛</s>，因此追求商业目的是非常自然的，所以狗头人在这里把实情坦诚相告，以避免不必要的误会发生。除此之外，狗头人APP还可以：
*将wiki的用户流自然分开，贡献者留在PC端，消费者（AKA“白嫖者”）导向移动端，从而实现用户逻辑和体验的分离。
*有效防止别有用心者利用移动端UA爬取灰机的内容。
==更新日志==
{{#ask: [[patch type::app]]
 |?Patch date=更新日期
 |?Patch brief=更新摘要
 |format=broadtable
 |link=subject
 |headers=plain
 |searchlabel=...更多结果
 |class=wikitable 
}}
{{Data Help
|页面名=帮助:狗头人APP
|描述文字=狗头人APP的介绍与配置
|解说=
|symbol=<i class="fa fa-address-book-o" aria-hidden="true"></i>
|主分类=帮助
|子分类=简单
|tags=手册,编辑
|sortkey=45
|关键=yes
|catsortkey=4
|guide=yes
|难度=复杂
|角色=通用
|灰机功能=no
}}
