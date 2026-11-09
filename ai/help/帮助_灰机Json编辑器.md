# 帮助:灰机Json编辑器

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3A%E7%81%B0%E6%9C%BAJson%E7%BC%96%E8%BE%91%E5%99%A8
revid：42604 · 抓取时间：2026-11-09T14:27:11+08:00

---

{{编辑手册nav}}
灰机Json编辑器是一个辅助编辑Json的工具，需要配合[[帮助:模块/挂载数据|模块]]、[[帮助:MongoDB支持|MongoDB]]或[[帮助:SMongo|SMongo]]来使用这些数据。

==创建Schema==
于Data命名空间（3500），以<code>Data:xxxx.schema</code>创建新内容，以默认内容保存即可创建新的Schema。

==修改Schema==
访问一个Schema页面时，将会加载灰机Json编辑器，通过'''“编辑Schema”'''功能，即可修改和调整Schema的配置。

如果不希望Schema可以被普通用户编辑，可以通过保护的方式进行锁定。

Schema中，根节点表示最终生成Json文件的第一层级，块则是定义Object的格式。块可以嵌套，但不可循环嵌套。

修改后可以通过“验证定义”的方式来确认是否有问题。

==编辑Json==
在灰机Json编辑器中可以通过'''“编辑Json”'''功能来按照Schema的定义创建或编辑Json文件。

编辑时
*源Json有没被Schema定义的节点的情况，不会被删除
*如果被Schema定义的节点，但源Json已有不同类型的值时，会被重置为默认值（一般为空）。

创建的Json除了Schema定义的字段外，在根节点会有额外的<code>_hjschema</code>属性，该属性表示该文件是由哪个Schema文件创建或最后编辑过。

根节点拥有<code>_hjschem</code>属性的Json文件，会在<code>action=view</code>时出现'''“通过 HuijiJsonEditor 编辑”'''按钮，点击后会跳转到<code>_hjschem</code>属性所指的Schema页面进行编辑。

在Schema页面可以添加地址参数<code>?target=<pagename></code>来编辑一个Data命名空间下的<code>.json</code>条目。

==更新历史==
===v2.0.2（2023年7月1日）===
*大幅调整了编辑器的样式，使得编辑界面更紧凑以便同时显示更多内容
*Schema根节点新增“页名”字段，用以描述该Schema对应的Data页面命名的规则，会在Json编辑界面输入保存文件名的地方显示
*Schema的所有项目添加“提示（tips）”字段，填写该字段后，Json编辑界面对应项目的名字可以通过鼠标hover的方式显示提示。功能与原本的“描述”类似，都是用来提醒编写者该字段应该如何填写，但不那么占用界面空间
*Schema配置文本（Input）、数字（Input Number）和标签（Tags）这三类项目时，新增“选项”部分，这三类项目的“选项”会作为Json编辑时的快捷输入显示
*修复了可以使用空条目名进行保存的错误

===v1.4.5（2023年3月31日）===
*调整了备注的颜色，之前的颜色过于刺眼

===v1.4.4（2023年3月19日）===
*移除了保存条目时，目标条目的条目名输入按键限制，改为在保存时检查条目名的合法性。该限制会导致无法使用粘贴功能

===v1.4.2（2023年3月16日）===
*添加了Select Number，Radio Number，Checkbox Number三个控件，以对应形式进行选择，但值为数字
*优化了样式和控件布局

==示例==
===演示===
{| class="wikitable"
!Schema||[[danteng:Data:演示.schema]]
|-
!数据页面||[[danteng:Data:小和尚.json]]
|}
这是一个为了展示本工具功能特意编写的演示，示例生成一个类似游戏角色的Schema，并通过该Schema生成了一个测试数据

===FF14手工副本数据===
{| class="wikitable"
!Schema||[[ff14:Data:Instance.schema]]
|-
!数据页面||[[ff14:Data:Instance/36001.json]]
|-
!使用数据的页面||[[ff14:多变迷宫_希拉狄哈水道]]
|}
最终幻想XIV维基中大部分副本的数据来自于抓取官方网站进行整理，但也有一些特殊的副本并无可抓取的来源，需要编辑手工制作，该Schema用于协助编辑手工编写副本数据页。

[[分类:帮助文档]]
