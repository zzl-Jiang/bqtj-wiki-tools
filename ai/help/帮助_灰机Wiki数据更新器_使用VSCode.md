# 帮助:灰机Wiki数据更新器/使用VSCode

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3A%E7%81%B0%E6%9C%BAWiki%E6%95%B0%E6%8D%AE%E6%9B%B4%E6%96%B0%E5%99%A8/%E4%BD%BF%E7%94%A8VSCode
revid：42523 · 抓取时间：2026-11-09T14:27:11+08:00

---


在之前，我们介绍过使用sublimes来编辑wiki，参考：'''[[帮助:使用Sublime Text编辑Wiki]]'''。类似的，我们也可以使用<s>世界上最好用的</s>本地IDE工具Visual Studio Code（简称 VS Code）来编写wiki，特别是[[help:模块|lua]]模块代码。
[[File:VSCode维护代码3.jpg|400px|thumb|配合Chrome进行前端调试]]
== 辅助工具 ==
尽管我们可以通过VS Code的extension来操作MediaWiki的api来和灰机wiki通信（见“内置接口”章节），但我们还是推荐下载[[帮助:灰机Wiki数据更新器|灰机updater]]来进行内容同步。

== 这么干的好处 ==
#<s>感觉自己是一个真正的编程小能手</s>
#VS Code的代码着色和本地辅助更为丰富，极大提高写代码的效率
#充分利用本地性能，减少浏览器（特别是Chrome）对电脑性能的压力
#还可以方便的维护Gadget命名空间下的css、js甚至是主空间的文章页面
#方便传图、传文件，刷新页面 一锅端，填坑速度+500%



== 步骤 ==
[[File:VSCode维护代码1.jpg|400px|right|thumb|图1]]
[[File:VSCode维护代码2.jpg|400px|right|thumb|图2]]
#在本地创建一个文件夹，用来存放代码
#创建一个空文本文件，并命名为“<code>module_2_test.wiki</code>”，保存。（注意：由于windows不允许文件名中出现“:”\"等字符，因此我们需要使用下面的字符串进行转义）
#配置好灰机updater，在“<code>任务设置-基本</code>”中选择“<code>以文本更新</code>”模式（'''右图1'''）
#在“<code>文本</code>”标签中选择之前的文件目录，勾上“<code>转换文件名</code>”（'''右图2'''）
#打开VS Code，导入之前的文件夹，配置好lua语法高亮与.wiki的匹配关系后即可使用本地IDE来维护wiki上的代码。
#在修改完代码后，点击灰机updater的“运行”按钮，即可完成代码的上传。
{| class="wikitable" style="text-align:center"
!符号
|\||/||:||*||"
|-
!转义
|_0_||_1_||_2_||_3_||_4_
|}

== Fetch内容 ==
*目前灰机updater仅支持使用文件列表来fetch内容。

== 使用扩展插件编辑 ==

与Sublimes类似，VS Code的extension库中也有用户上传的相关工具，能够实现VS Code与MediaWiki的直接通信。但我们'''更推荐你使用灰机自己的updater'''<!-- ewiv已经没有了，开发者也停止更新了
#打开VS Code，在<code>View——Extension</code>中搜索“MediaWiki”
#找到<code>ewiv</code>这个插件，安装，完成配置即可（由“夕舞八弦”发布）
[[File:VSCode维护代码4.jpg|400px|left]]-->

#前往[https://marketplace.visualstudio.com/items?itemName=RoweWilsonFrederiskHolme.wikitext Wikitext插件安装页面]点击Install，或者打开VS Code，在菜单栏【View】-【Extension】中搜索<code>rowewilsonfrederiskholme.wikitext</code>，然后安装它。
#在VS Code中按Ctrl+逗号，在顶部搜索框输入<code>@ext:rowewilsonfrederiskholme.wikitext</code>，按照以下配置来输入：
:: Api Path: <code>/api.php</code>
:: Article Path: <code>/wiki/</code>
:: Auto Login: 建议选择<code>Always</code>
:: Enable JavaScript: 打勾
:: Get CSS: 打勾
:: Host: 你的灰机站点主机名，例如彩虹六号围攻Wiki是<code>r6s.huijiwiki.com</code>
:: Password: 你的密码
:: Redirects: 根据需求选择是否要自动重定向，打勾后，在获取有重定向的页面时会直接得到重定向后的页面结果。
:: Transfer Protocol: 选择<code>https://</code>
:: User Name: 你的用户名
完成后关闭本设置页面。配置完成！
=== 基本命令 ===
* 按F1后会打开一个输入框，输入命令：
** <code>Login with your account</code>：登陆到站点，在设置项「Auto Login」中选择 Always ，则会在上传页面时自动登录。
** <code>Logout, if you are already logged in</code>：登出。
** <code>Pull page to edit</code>：获取一个页面，选择后要输入页面名称，然后按回车就会开始获取。
** <code>Post your edit to the website</code>：上传编辑，选择后要输入页面名称，然后要输入编辑摘要，随后上传编辑。
* 按Ctrl+Shift+V可以预览编辑。虽然效果并不像网站上一样，但是也能看出是否有语法错误。
=== 快速编辑 ===
Wikitext插件可以使用<code>@</code>来激活一些快速的 Wikitext 格式，例如<code>@table</code>可以快速生成一个表格。

当然你也可以使用 VS Code 自带的代码片段功能，自定义常用的大型模板片段来快速输入。

关于代码片段功能详情请参考：[https://code.visualstudio.com/docs/editor/userdefinedsnippets Snippets in Visual Studio Code]

=== 快速切换到 VS Code 编辑 ===
利用 URL Scheme，可以快速的从浏览器把当前页面调到 VS Code 中打开，以下是格式：

<code>vscode://rowewilsonfrederiskholme.wikitext/PullPage?RemoteBot=true&TransferProtocol=https%3A&SiteHost=%2F%2F$key$.huijiwiki.com&APIPath=%2Fw%2Fapi.php&Title=$fullpagename$</code>

在该URL中：
* <code>vscode://</code>为唤起 VS Code 应用程序所使用的Scheme，它必须位于URL的开头，你可以把它换成其他基于VS Code打造的IDE，例如Google的<code>antigravity-ide://</code>
* <code>$key$</code>为你所在站点的 Wiki key，例如彩虹六号围攻站（r6s.huijiwiki.com）为<code>r6s</code>。
* <code>$fullpagename$</code>为指定页面的完整名称，也就是如果有空间名应该加上空间名，比如说<code>首页</code>或者<code>模板:Sandbox</code>。
