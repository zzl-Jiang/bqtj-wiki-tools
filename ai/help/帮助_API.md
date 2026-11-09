# 帮助:API

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3AAPI
revid：39547 · 抓取时间：2026-11-09T14:27:09+08:00

---

{{编辑手册nav}}
本页面为灰机的开放API官方文档。

==综述==
灰机基于MediaWiki {{CURRENTVERSION}}，支持MediaWiki内核所包含标准API，此部分文档可以在https://mediawiki.org找到，在此不再赘述。灰机内部所使用的网络API种类繁多，其中很多还处于不断变化调整的时期，灰机无法保证其稳定性。原则上，只有在此页列出的API才适用于生产环境。如果您的应用需要使用其他的数据，可联系我们。

==MW的官方API==

:灰机API endpoint为<code>/api.php</code>。
:也可以遵照MediaWiki默认的<code>/w/api.php</code>
例如:
<pre>
https://asoiaf.huijiwiki.com/w/api.php
https://asoiaf.huijiwiki.com/api.php
</pre>
endpoint的书写请严格对照[https://www.mediawiki.org/wiki/API:Main_page MediaWiki的官方文档]。

如您需要返回json数据，可加上format=json，如需要xml，可以加上format=xml，具体不在一一赘述。

===在python中调用===
灰机的API path是默认的，不需要进行修改，对于一些其他的MediaWiki网站，其路径可能是修改过的，需要指定path，以mwclient为例，做比较如下：
<pre>
 site = Site(prefix + '.' + 'huijiwiki.com')  # 自定义路径前置的
 site = Site('wiki.somewiki.com/' + prefix, path='/')  # 自定义路径后置的
 site = Site(prefix + '.' + 'fandom.com', path='/')  # 修改了api路径的（比如Fandom）
</pre>

==restful API==
MediaWiki最新版本中除了传统的PHP API外，新增了restful API，主要用于Html和Wikitext的转换。详情请参阅：https://qmtxd.huijiwiki.com/api/rest_v1/

==页面相关==
===统计数据===
page action count
*<pre>https://huijidata.com/stats/pages/{sitePrefix-pageId}/types/{type};fromDate={YYYY-MM-DD};toDate={YYYY-MM-DD};</pre>
*示例: https://huijidata.com/stats/pages/dnfcn-934/types/edit;fromDate=2017-01-01;toDate=2018-01-01



top pages
*<pre>https://huijidata.com/stats/pages/{type};sitePrefix={sitePrefix};fromDate={fromDate};toDate={toDate};top={top}</pre>
*示例: https://huijidata.com/stats/pages/edit;sitePrefix=dnfcn;fromDate=2017-01-01;toDate=2018-01-01;top=2

参数说明:

*sitePrefix-pageId:站点的前缀和页面ID （必须）

*type: edit, poll, comment, rate, view, upload其中之一 （必须) 

*fromDate:YYYY-MM-DD （可选，不指定默认起始）

*toDate:YYYY-MM-DD（可选，不指定默认当前）

*top:前多少个 (可选，不指定默认10)

==站点相关==
===获得当前站点的属性===
* 示例：/api.php?action=query&meta=siteinfo&siprop=general
与MediaWiki内核中的同名方法参数一致，但是返回的数据中多了group、prefix、avatar、property、sysop、bureaucrat几条属性。

===获得当前站点的统计===
* 示例：/api.php?action=query&meta=siteinfo&siprop=statistics
与MediaWiki内核中的同名方法参数一致，但是返回的数据中多了followers、rating、score、donate、donategoalmet几条属性

===统计数据===
site action count
*<pre>https://huijidata.com/stats/sites/{sitePrefix}/types/{type};fromDate={fromDate};toDate={toDate}</pre>
*示例: https://huijidata.com/stats/sites/lotr/types/edit;fromDate=2017-01-01;toDate=2018-01-01

top sites
*<pre>https://huijidata.com/stats/sites/{type};fromDate={fromDate};toDate={toDate};top={top}</pre>
*示例: https://huijidata.com/stats/sites/rate;fromDate=2017-01-01;toDate=2018-01-01;top=2

参数说明:

*sitePrefix:站点的前缀 例如魔戒-lotr 星露谷-xinglugu（必须）

*type: edit, poll, comment, rate, view, upload其中之一 （必须) 

*fromDate:YYYY-MM-DD （可选，不指定默认起始）

*toDate:YYYY-MM-DD（可选，不指定默认当前）

*top:前多少个 (可选，不指定默认10)

==用户相关==
===获得当前登录用户的属性===
{{版本要求|2.0.10|and after}}
* 示例：https://lotr.huiji.wiki/api.php?action=query&titles=%E9%A6%96%E9%A1%B5&prop=huijiinfo&inprop=besteditors
通过inprop参数传入需要获取的用户属性，每条属性用<code>|</code>分割。

inprop的可选值为：
<pre>
          'protection',
          'talkid',
          'watched', # private
          'watchers', # private
          'visitingwatchers', # private
          'notificationtimestamp', # private
          'subjectid',
          'url',
          'readable', # private
          'preload',
          'displaytitle',
          'viewership',
          'editorship',
          'besteditors'
</pre>

===获得任意用户的属性===
* 示例：https://www.huiji.wiki/api.php?action=query&list=huijiusers&ususers=SerGawen|yiyi|%E5%8C%97%E8%90%BD%E5%B8%88%E9%97%A8&usprop=avatar|gender|context
通过ususers参数传入目标用户的用户名，每个用户名用<code>|</code>分割。
通过usprop参数传入需要获取的用户属性，每条属性用<code>|</code>分割。
<pre>
'blockinfo',
'groups',
'implicitgroups',
'rights',
'editcount',
'registration',
'emailable',
'gender',
'centralids',
'designation',
'avatar',
'gender',
'status',
'province',
'city',
'birthday',
'followingcount',
'followercount',
'stats',
'level',
'followingsites',
'context',
</pre>

===统计数据===
user action count
*<pre>https://huijidata.com/stats/users/{userId}/types/{type};fromDate={fromDate};toDate={toDate};sitePrefix={sitePrefix};category={category}</pre>
*示例: https://huijidata.com/stats/users/1/types/edit;fromDate=2017-01-01;toDate=2018-01-01;sitePrefix=hearthstone;category=龙

top users
*<pre>https://huijidata.com/stats/users/{type};fromDate={fromDate};toDate={toDate};sitePrefix={sitePrefix};top={top}</pre>
*示例: https://huijidata.com/stats/users/rate;sitePrefix=hearthstone;fromDate=2017-01-01;toDate=2018-01-01;top=2

参数说明:

*userId: 用户ID (必须)

*type: edit, poll, comment, rate,upload 其中之一 （必须) 

*fromDate:YYYY-MM-DD （可选，不指定默认起始）

*toDate:YYYY-MM-DD（可选，不指定默认当前）

*sitePrefix:站点的前缀 例如魔戒-lotr 星露谷-xinglugu（可选，不指定默认灰机全站点）

*category:页面的分类 （可选，不指定默认无）  

*top:前多少个 (可选，不指定默认10)

==获得符合特定条件的用户集合==
===被关注===
示例： /api.php?action=query&list=allhuijiusers&followedby=Reasno
===关注某个用户===
示例:  /api.php?action=query&list=allhuijiusers&following=Reasno
===关注某个站点===
示例:  /api.php?action=query&list=allhuijiusers&followingsite=asoiaf

[[Category:开发者]]
{{Data Help
|页面名=帮助:API
|描述文字=灰机API
|解说=
|symbol=
|主分类=帮助
|子分类=复杂
|tags=开发,编程,管理,
|sortkey=51900
|关键=no
|catsortkey=4
|guide=no
|难度=复杂
|角色=开发者
|灰机功能=yes
}}
