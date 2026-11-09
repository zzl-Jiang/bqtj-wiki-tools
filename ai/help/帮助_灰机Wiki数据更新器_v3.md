# 帮助:灰机Wiki数据更新器/v3

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3A%E7%81%B0%E6%9C%BAWiki%E6%95%B0%E6%8D%AE%E6%9B%B4%E6%96%B0%E5%99%A8/v3
revid：42672 · 抓取时间：2026-11-09T14:27:11+08:00

---

==HuijiWiki Updater V3==
[[File:updatrerV3.jpg|400px|center|link=]]
HuijiWiki Updater V3 是对原 PyQt5 版灰机 Wiki 更新器的重写：

*简单来说，如果你是一名熟练的vibe coder，他'''不会'''取代你的任何已有的工作流和harness工具，相反，他会无缝并入你的灰机wiki项目；而如果你是一位不熟悉编程的“面向豆包选手”，他提供了完整的GUI可视化界面，以及轮椅级别的植入，快速增强Trae、WorkBuddy等常见的免费token工具，助你快速起飞。
:[[帮助:灰机Wiki数据更新器\使用Harness]]
*优化了部分功能的入口，使之更符合AI时代的使用习惯
**独立的页面同步、图片同步功能，聚焦于'''工作区与线上页面的同步关系'''，提供类似github desktop的同步机制，确保你关心的wiki内容和本地工作区实现“无缝对接”
**完整的manifest文件校验，新增的远程删除页面功能，允许将本地不存在的页面在线上删除（注意风险，需要管理员以上权限）
*完整继承原Qt版本的所有功能，100%移植，确保历史功能延续（仍然提供经典版本下载）
*AI增强面板 <span class="label bg-danger">NEW</span>——
**一键植入灰机AI文档和帮助文档，常用工具集和针对各种Harness的技能包，让大模型立刻了解灰机wiki的开发流程和特点。
**通过启用通信中继，以本地http请求+MCP的方式，为本地工作区的全部Harness架构提供直接访问灰机线上页面，请求API的功能（注意，需要[[帮助:开发者101|开发者]]权限，该功能尚在测试阶段，未来可能会产生权限收紧，恕不另行通知）简言之，能够让大模型看得到、摸得着灰机wiki的页面，大幅提高开发的准确度，减少不必要的token浪费。
**完整功能的CLI命令支持，允许你的AI Harness实现全链路的自动化构建，接入可复用工作流

==V3版本功能==
{{Mbox
|type=content|border=danger
|text=
基础权限:<code>认证用户</code>和<code>自动确认用户</code><br>页面同步\文件同步\Excel操作\Wiki维护\AI增强需要<code>bot</code>和<code>管理员+</code>权限<br>MCP和CLI额外需要<code>开发者</code>或者<code>机长</code>权限
}}
{| class="wikitable"
!width=180px|功能大类||功能目标||简述
|-
|页面同步||同步你的本地工作区与线上页面||原updater“以文本更新”+“批量操作页面”的一部分，增加Manifest校验和完整的增改删同步操作，实现工作区与线上Wiki页面的闭环，同时优化了选择页面控件，允许多命名空间同步拉取
请注意：'''由于Windows文件名不支持一些符号，需要转义这些符号，转义规则请见下面的表：
{| class="wikitable" style="text-align:center"
!符号
|\||/||:||*||"
|-
!转义
|_0_||_1_||_2_||_3_||_4_
|}
例如 “<code>module_2_getData</code>” 等于 “<code>module:getData</code>”
|-
|文件同步||同步你的本地工作区与线上的多媒体文件||原updater“更新图片”+“批量操作页面”的一部分，增加了拉图到本地的操作
|-
|Excel操作||经典功能集成||参见经典版本功能的上传Excel文件（模板）+上传Excel文件（简易）+上传Excel文件（JSON）
|-
|WIKI维护||批量维护页面||经典版本功能的“批量删除 / 恢复”、“读取重定向”、“批量移动”、“批量刷新页面”
|-
|AI增强  <span class="label bg-danger">NEW</span>||AI工具集||Harness文档植入、页面预览、接入信息、CLI命令
|-
|“5 by 5”  <span class="label bg-danger">COMING</span>||线上线下桥接||联通灰机Agent/Workspace与本地Harness，实现双向协作
|}


===资料同步===
AI知识包同步会在工作区生成：
<pre>
ai/
  README.md                 索引
  wiki-workflow.md          工作区映射、任务参数、安全规则
  cli.md                    全部 CLI 命令
  preview.md                预览接口说明
  mcp.md                    MCP 挂载配置
  huiji/facts-26199.md      灰机事实清单（主站 p/26199）
  help/                     灰机主站 Help 文档（按 revid 增量）
  templatemanager/          TemplateManager 组件清单
  external/huiji-wiki-bot.md 第三方技能引荐
  cache/                    预览缓存
  .meta.json                revid 增量记录
</pre>

*事实清单与主站帮助文档。
**帮助文档按 <code>revid</code>增量更新，未变化的页面直接跳过。
*TemplateManager 资料来自 <code>templatemanager.huijiwiki.com</code>当前包含：
**<code>Manifest:GlobalSearch</code>（gsearch 检索器）
**<code>Manifest:MathJax3</code>（mathJax3）
**<code>Manifest:鼠标提示框</code>（HuijiTooltip）
[[File:updaterV3 ai.jpg|400px|center|link=]]

===Harness 文档植入===

支持勾选并一键写入以下入口文件：
<pre>
| 工具                 | 文件                                      |
| ------------------ | --------------------------------------- |
| AGENTS.md（通用）      | `AGENTS.md`                             |
| Claude Code        | `CLAUDE.md`                             |
| Cursor             | `.cursor/rules/huiji-updater.mdc`       |
| GitHub Copilot     | `.github/copilot-instructions.md`       |
| CodeBuddy          | `CODEBUDDY.md`                          |
| Trae               | `.trae/rules/huiji-updater.md`          |
| Claude Agent Skill | `.claude/skills/huiji-updater/SKILL.md` |
| DSH Agent Skill    | `.dsh/skills/huiji-updater/SKILL.md`    |
</pre>
写入规则：
*使用 HTML marker 包裹
**文件不存在时创建；已存在但没有 marker 时追加，不删除原有内容，不破坏工作区已有文件；已有 marker 时只替换区间。

====Agent Skill====

<code>SKILL.md</code>是专门指导 agent 使用 updater 的技能文档，基于[[user:Kurax|KK]]的huijiwiki Skill改造，包含：

*何时使用updater；
*必读的 AI文档顺序；
*标准流程定义；
*页面预览命令；
*MCP 工具清单；
*权限要求与操作红线。

===页面预览===
{{Mbox
|type=content|border=danger
|text=额外需要权限:开发者或者机长
}}
接口：
<code>
GET http://127.0.0.1:<port>/api/sites/<site>/ai/preview?title=<标题>&format=wikitext|html&refresh=0|1
</code>

*优先走已登录的 `api.php`（与同步同一链路），失败时回退 `curl_cffi` 浏览器指纹直连 `index.php`。
*返回 `{title, format, url, cached, fetched_at, content}`。
*缓存 10 分钟，`refresh=1` 强制刷新，正文上限 2MB。
*遇到 Cloudflare 拦截会给出明确提示，并建议改用 wikitext 或先在桌面端完成验证。
*接受页面标题，不接受任意 URL，避免 SSRF。

===MCP===
{{Mbox
|type=content|border=danger
|text=额外需要权限:开发者或者机长
}}
MCP server是独立控制台进程，由 AI 代理以 stdio 子进程启动，通过本地 HTTP 接口操作 updater：
<pre>
| 工具             | 作用                             |
| -------------- | ------------------------------ |
| `wiki_preview` | 实时预览页面                         |
| `wiki_read`    | 优先读本地页面，否则读远端 wikitext         |
| `wiki_changes` | 本地改动列表                         |
| `wiki_status`  | 运行 status 任务                   |
| `wiki_pull`    | 运行 pull 任务                     |
| `wiki_push`    | 运行 push 任务，`dry_run` 默认 `true` |
</pre>
启动方式：

*源码：<code>python -m huiji_updater.mcp_server</code>
*安装版：<code><安装目录>\mcp\huiji-updater-mcp.exe</code>

MCP 会读取 <code>%LOCALAPPDATA%\HuijiUpdater\runtime.json</code>找到当前 GUI 端口，并用<code>/api/health</code>校验；因此使用 MCP 时必须保持主程序运行。

===CLI命令===
{{Mbox
|type=content|border=danger
|text=额外需要权限:开发者或者机长
}}
<pre>
huiji-updater serve
huiji-updater login
huiji-updater status --site <key>
huiji-updater pull --site <key>
huiji-updater push --site <key> --all --dry-run
huiji-updater push --site <key> --path pages/Foo.wiki --message 说明
huiji-updater ai export --site <key> --all
huiji-updater ai docs --site <key>
huiji-updater ai preview --site <key> --title "Template:Foo"
huiji-updater mcp
</pre>



====已知限制====

*Cloudflare 仍可能拦截 HTML 预览，此时建议使用 wikitext，或先在桌面端完成站点验证。
*Help 命名空间自动识别失败时，可通过 CLI `--help-ns` 指定；界面默认使用主站 www。
*MCP 依赖 `mcp` 1.x；升级到 2.x 需要适配新的 `MCPServer` API。
*客户端令牌只在进程生命周期内有效；重启 GUI 后需要重新打开带令牌的地址（桌面端会自动处理）。
