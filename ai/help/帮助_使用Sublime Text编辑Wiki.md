# 帮助:使用Sublime Text编辑Wiki

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3A%E4%BD%BF%E7%94%A8Sublime%20Text%E7%BC%96%E8%BE%91Wiki
revid：33690 · 抓取时间：2026-11-09T14:27:10+08:00

---

[http://www.sublimetext.com/ Sublime Text]是一个著名的文本编辑器。使用它的插件[https://github.com/tosher/Mediawiker Mediawiker]可以直接编辑MediaWiki。这样一来好处多多。比如可以使用更灵活的正则替换，搭配其他工具使用更是威力无边~

[[File:sublime 配置1.png|600px]]
==安装==

#首先通过需要安装[http://www.sublimetext.com/ Sublime Text]
#在Sublime Text界面中，使用快捷键 <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> 打开命令窗口，输入“install package”进行搜索，使用指令“Package Control: Install Package”
#稍作等待后（等待期间最下方状态栏会显示Loading repositories），会出现可安装的插件列表，在其中输入“Mediawiker”，进行安装即可
#安装结束后，可能需要重新启动Sublime Text。如果在Sublime中按 <kbd>Alt</kbd> + <kbd>F1</kbd> 可以弹出一个菜单，第一个选项是“Open page”，则表示安装成功
#第2、3步中，如果遇到了错误，请科学上网后重试

==配置==

点击主菜单“Preferences”→“Package Settings”→“Mediawiker”→“Setting - Default”，可以打开默认的配置文件。

该配置文件是json格式的，可以通过编辑该文件，添加新的站点设置。建议先将“Mediawiker.sublime-settings -- Mediawiker”的内容复制到“Mediawikier.sublime-settings -- User”中后再在“Mediawikier.sublime-settings -- User”中进行修改。

一个站点的配置如下（没有注释的使用默认值即可）：

 "English wikipedia": {   // 站点显示名称
       "authorization_type": "login",  // 使用login模式
       "host": "en.wikipedia.org",  // 在灰机中是“xxx.huijiwiki.com”
       "path": "/",  // 在灰机wiki中，使用“/”
       "pagepath": "/wiki/",
       "username": "",  // 灰机wiki的账号
       "password": "", // 灰机wiki的密码
       "domain": "",
       "https": true,
       "is_ssl_cert_verify": true,
       "proxy_host": "",
       "use_http_auth": false,
       "http_auth_login": "",
       "http_auth_password": "",
       "oauth_access_secret": "",
       "oauth_access_token": "",
       "oauth_consumer_secret": "",
       "oauth_consumer_token": "",
       "cookies_browser": "chrome",
       "preview_custom_head": [], 
       "retry_timeout": 30,
       "is_wikia": false,
       "show_red_links": false
 },
[[File:sublime 配置.png|600px]]
保存后即可生效。

在新版Mediawiker中建议先将“Mediawiker.sublime-settings -- Mediawiker”的内容复制到“Mediawikier.sublime-settings -- User”中后再在“Mediawikier.sublime-settings -- User”中进行修改，修改内容同上。

[[File:sublime 配置2.png|600px]]


==使用==

按 <kbd>Alt</kbd> + <kbd>F1</kbd> 激活主菜单，选择“Select Wiki”，通过新的菜单选中你配置好的自己的Wiki，然后就可以在主菜单中正常使用各种功能了。

==更多==
*本插件附带Wiki代码语法着色，除了可以自动着色Wiki上的文章内容外，还会自动着色本地后缀为“.mediawiki”、“.wiki”和“.wikipedia”的文件（可以通过配置增加）
*本插件会占用 <kbd>Alt</kbd> + <kbd>F3</kbd> 快捷键，如果需要使用该快捷键功能，可以在键位配置中去掉
*更多功能说明请参考[https://github.com/tosher/Mediawiker https://github.com/tosher/Mediawiker]
