# 帮助:Huiji缓存

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3AHuiji%E7%BC%93%E5%AD%98
revid：41621 · 抓取时间：2026-11-09T14:27:09+08:00

---

{{编辑手册nav}}
灰机有多层缓存机制来优化用户的访问速度。{{See also|帮助:提升访问速度}}
{| class="wikitable" style=""
!style="background: #2a4b8d;color: #fff;"|
!style="background: #2a4b8d;color: #fff;"|
!style="background: #2a4b8d;color: #fff;" |缓存类型
!style="background: #2a4b8d;color: #fff;" |来自
!style="background: #2a4b8d;color: #fff;" |缓存内容
!style="background:#2a4b8d;color: #fff;" |缓存时间
!style="background: #2a4b8d;color: #fff;" |影响
!style="background: #2a4b8d;color: #fff;" |主动刷新方法
|- style="background: #a3a3a3;color: #eee;"
| colspan="2" |本地缓存
|浏览器缓存
|浏览者电脑
|图片，脚本等资源
|depends
|所有人
|因浏览器而异
|-style="background: #428bca;color: #eee;"
| rowspan="4" |服务器缓存
| rowspan="2" |文件级缓存
|style="background: rgba(51, 51, 51, 0.21);"|CDN缓存
|style="background: rgba(51, 51, 51, 0.21);"|灰机服务器
|style="background: rgba(51, 51, 51, 0.21);"|图片、字体、CSS和Javascript
|style="background: rgba(51, 51, 51, 0.21);"|立刻（图片）
1h（CSS/JS）
|style="background: rgba(51, 51, 51, 0.21);"|所有人
|style="background: rgba(51, 51, 51, 0.21);"|调试按钮(仅管理员、行政员可见)
?debug=1
|-
|style="background: rgba(91, 192, 222, 0.27);"|静态缓存
|style="background: rgba(91, 192, 222, 0.27);"|灰机服务器
|style="background: rgba(91, 192, 222, 0.27);"|绝大多数页面的Html
|style="background: rgba(91, 192, 222, 0.27);"|24h
|style="background: rgba(91, 192, 222, 0.27);"|匿名用户
|style="background: rgba(91, 192, 222, 0.27);"|ctrl+R
|-
|style="background: rgba(185, 148, 95, 0.36);" rowspan="2" |内存级缓存
|style="background: rgba(185, 148, 95, 0.36);"|ParserCache
|style="background: rgba(185, 148, 95, 0.36);"|MediaWiki
|style="background: rgba(185, 148, 95, 0.36);"  rowspan="2" |模板、统计数据、动态列表、页面是否存在等需要耗时查询的内容
|style="background: rgba(185, 148, 95, 0.36);"|1天
|style="background: rgba(185, 148, 95, 0.36);"|所有人
|style="background: rgba(185, 148, 95, 0.36);"|清除缓存按钮(仅管理员、行政员可见)
?action=purge
|-
|style="background: rgba(240, 173, 78, 0.57);"|非ParserCache
|style="background: rgba(240, 173, 78, 0.57);"|MediaWiki
|style="background: rgba(240, 173, 78, 0.57);"|depends
|style="background: rgba(240, 173, 78, 0.57);"|所有人
|style="background: rgba(240, 173, 78, 0.57);"|无
|}

==本地缓存==
储存在您浏览器中的缓存，'''与网站无关'''。

'''缓存内容'''：图片，脚本等资源。

'''缓存时间'''：由文件头和浏览器决定。

'''主动刷新方法'''：
* Firefox/Safari：按住“Shift”的同时单击“刷新”，或按“<code>Ctrl-F5</code>”或“<code>Ctrl-R</code>”（Mac为“<code>⌘-R</code>”）
* Edge/Google Chrome：按“<code>Ctrl-Shift-R</code>”（Mac为“<code>⌘-Shift-R</code>”）
* Internet Explorer<sup>✝</sup>：按住“Ctrl”的同时单击“刷新”，或按“<code>Ctrl-F5</code>”
* Opera<sup>✝</sup>：在“工具→首选项”中清除缓存

==静态缓存==
将数据库查找、逻辑处理后生成的最终Html和域名对应起来，下次访问相同域名时直接输出最终结果。

'''缓存内容'''：绝大多数页面的Html。

'''常见情况'''：修改页面后，未登录用户并没有看到最新内容。

'''缓存时间'''：24小时。

'''例外'''：为了方便大家浏览最新内容，'''登录用户'''会绕过本层缓存，直接看到最新信息。

'''主动刷新方法'''：登录，或匿名状态下强制刷新页面。

<code>TIPS：当编辑者编辑完页面后，如果期望匿名访问者马上看到最新的更改，可以退出登录或者使用浏览器的“匿名模式”访问当前页面并强制刷新（按“Ctrl-Shift-R”,Mac为“⌘-Shift-R”），即可保证匿名访问的缓存页面同步到最新状态。</code>

==CDN缓存==
{{see also|帮助:FAQ/为什么刚传的新图没有显示？}}
全称是“Content Delivery Network"。缓存小文件到物理距离与访问者最近的服务器，以提升加载速度。

'''缓存内容'''：图片、字体、CSS和Javascript。

'''缓存时间'''：图片：更新后立即刷新，CSS/JS: 1小时。

'''调试方法'''：在页面后加<code>?debug=1</code>然后刷新、或者点击“'''<i class="fa fa-plug"></i>调试'''”按钮（仅管理员可见）。

==Memcached缓存==
{{see also|帮助:FAQ/为什么修改了模板/CSS没有立刻生效？}}
读取数据库、解析维基文本的速度慢于读取内存，所以我们将一些常用的内容放在了内存中。

'''缓存内容'''：模板、统计数据、动态列表、页面是否存在等需要耗时查询的内容。

'''常见情况'''：常见于修改了模板内容后并没有显示更新。（因为修改了模板，不等于修改引用了模板的页面，所有引用了该模板的页面不会自动更新，需要等待一定的时间由MediaWiki刷新，当页面发生编辑时，会自动刷新Memcached缓存。）

'''缓存时间'''：由程序依照需求分配。

'''主动刷新方法'''：
* 清除ParserCache（即正文中的缓存），在页面后加<code>?action=purge</code>然后刷新（全部MediaWiki网站通用）、或者点击“'''<i class="fa fa-eraser"></i>清除缓存'''”按钮（在灰机仅管理员可见）。
* 非ParserCache（正文以外的缓存），需要耐心等待缓存失效。
{{Data Help
|页面名=帮助:Huiji缓存
|描述文字=缓存机制
|解说=
|symbol=<i class="fa fa-eraser" aria-hidden="true"></i>
|主分类=帮助
|子分类=简单
|tags=机制,编辑,管理
|sortkey=6
|关键=no
|catsortkey=1
|guide=no
|难度=简单
|角色=通用
|灰机功能=no
}}
