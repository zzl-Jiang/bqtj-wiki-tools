# 帮助:灰机Wiki数据更新器/更新日志

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3A%E7%81%B0%E6%9C%BAWiki%E6%95%B0%E6%8D%AE%E6%9B%B4%E6%96%B0%E5%99%A8/%E6%9B%B4%E6%96%B0%E6%97%A5%E5%BF%97
revid：42660 · 抓取时间：2026-11-09T14:27:11+08:00

---

<noinclude>本页记录了[[帮助:灰机Wiki数据更新器|灰机Wiki数据更新器]]的最新更新日志。

过往更新日志请参考下面的链接：
*[[/2018-2026年|2018-2026年(经典版本)]]
*[[/2017年|2017年]]

==更新日志==
</noinclude><includeonly>[[/更新日志|查看完整更新日志]]</includeonly>
<strong>2026年11月7日 v3.1.5</strong>
<ul>
<li>综合：</li>
<ol><li>将“同步资料到工作区”功能移动到任务面板位置，现在这个功能不再需要额外校验权限（自动确认+认证用户即可使用）</li><li>调整了其他权限设置，并保持提示文字的一致性，现在，行政员权限可以正确的继承管理员权限，并获得等同于开发者权限的校验（MCP+CLI功能）</li>
</ol></ul><strong>2026年11月7日 v3.1.2c</strong>
<ul>
<li>综合：</li>
<ol><li>单独版本可以通过界面功能升级到MCP版本</li><li>清除了文件上错误添加的`Zone.Identifier` 标记</li>
</ol></ul><strong>2026年11月7日 v3.1.2b</strong>
<ul>
<li>综合：</li>
<ol><li>修复了3.1.2版本打包错误的问题（MCP版本被错误打包成了无MCP版本且无法正常启动webview导致界面是浏览器版本）</li><li>在版本号处增加了正确的标注可以看到是否为mcp版本，现在 -mcp版/单独版通过自动更新能正确的更新内容</li>
</ol></ul><strong>2026年11月7日 v3.1.2</strong>
<ul>
<li>综合：</li>
<ol><li>增加了自动检测更新的功能</li><li>优化了配色方案</li>
</ol></ul><strong>2026年11月6日 v3.1.1</strong>
<ul>
<li>Bug fix：</li>
<ol><li>修复一个CLI的bug导致可能的命令无法正常结束阻塞后续操作</li>
</ol>
</ul><strong>2026年11月6日 v3.1.0</strong>
<ul>
<li>综合：</li>
<ol><li>使用FastAPI + React + pywebview重构</li><li>新版增加MCP集成，CLI工具和AI Harness支持</li>
</ol>
</ul>
