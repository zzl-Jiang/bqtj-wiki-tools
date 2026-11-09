# 帮助:HuijiAgent/事件API

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3AHuijiAgent/%E4%BA%8B%E4%BB%B6API
revid：42446 · 抓取时间：2026-11-09T14:27:09+08:00

---

{{子页面列表|目标页面=帮助:HuijiAgent|隐藏前缀=1}}
{{编辑手册nav}}{{HuijiOnly}}

'''事件API'''(eventAPI)是我们为siteAgent准备的、由开发者捕获并处理流式消息特定片段的接口。

==原理==
用户可通过siteAgent的提示词指定什么时候应当触发什么事件。

agent会根据你的设计，在对话中输出如下形式的markdown片段：
<pre>
[_event:名字]
[_event:名字|数据]
[_event:名字|字段=值|数据]
</pre>
标记可以单独占一行，也可以直接夹在句子里（<code>早上好啊[_event:live2d|happy]，今天……</code>）。

前端对同一份正文有'''两个互不依赖的消费者'''：
*'''渲染'''：markdown-it 把标记换成一个不可见元素 <code>&lt;span class="md-event"&gt;</code>，正文里看不出痕迹；
*'''派发'''：流式收到正文增量时数一遍标记，新出现的就向 <code>window</code> 派发一个 <code>CustomEvent</code>（<code>siteagent:event</code>）。

两者谁也不依赖谁：派发不是在渲染回调里做的，所以渲染还没画出来、甚至这一条渲染失败都不影响派发；反过来，历史消息只走渲染、不走派发。

全程如下：

<pre lang="mermaid">
sequenceDiagram
    autonumber
    participant C as 站点口径（机长提示词）
    participant S as 站点助手（服务端）
    participant M as 大模型
    participant P as 前端 · mdParser
    participant H as eventHandler（站点 JS）

    C->>S: 声明能发哪些事件、参数怎么传、什么时候发
    S->>M: 每轮把这段口径拼进 system 提示
    M->>S: 回答的正文里夹着 [_event:名字|参数1|参数2]
    S->>P: SSE 流式下发正文
    P->>P: 把标记换成不可见 span（正文里看不见）
    P->>H: 每多出一个完整标记，派发一次 siteagent:event
    H->>H: 读 detail.name / detail.payload 自己处理
</pre>

==设计事件==
你可以打开主站siteAgent测试一下，要求他“触发toast，随便写几个字”。agent在答复时，一个toast即会出现在屏幕顶部。

实现这一点需要两个条件：
#在JS里设计了toast事件的捕获器；
#在siteAgent口径里告诉了他“有toast事件可用，参数怎么选”。

以下是我们在这两部分的实现：
<pre lang="javascript">
//// Mediawiki:Common.js

// 20261025 siteAgent eventAPI 示例
// 本站约定参数用“|”分隔。
window.addEventListener('siteagent:event', function (event) {
    if (!event.detail) return;                  // 不是我们派发的（防御）
    var eventName = event.detail.name;
    var payload = event.detail.payload;         // 一定是字符串：没带数据就是空串，不会是 null
    if (eventName === 'toast') {                // [_event:toast|文字|类型]
        var params = payload.split('|').map(function (part) { return part.trim(); });
        var text = params[0];
        var type = params[1];
        if (!text) return;                      // 只有类型没文字就别弹
        var ALLOWED = { info: 1, success: 1, warning: 1, error: 1 }; // 验证type的可用性，无效则fallback到info
        window.$message.create(text, { type: ALLOWED[type] ? type : 'info' });
        return;
    }
    // 这里还可以处理其他事件
});
</pre>
<pre>
//// siteAgent口径
# 正文事件
## toast
格式：`[_event:toast|文字|类型]`，这个事件会在页面顶部显示一个toast，类型的可选值是`info``warning``error``success`。如果你填错了或者不填，它会fallback到`info`。
</pre>

==参数==
<pre>[_event:<eventname>|<payload>]</pre>

所有的事件均会在window上触发，事件名称为<code>siteagent:event</code>。

子事件名称位于<code>event.detail.name</code>，payload位于<code>event.detail.payload</code>。

此外，我们还会提供一些额外的参数用于调试：
*raw：原始标记字符串
*offset：这一段在整个markdown正文里的位置。仅在流式传输时有效，历史记录里手动重放时是-1。
*messageId：包含在哪个message里。手动重放时是空字符串。
*live：布尔型，用于说明是流式传输自动触发的、还是手动重放的。
*at：number型，触发时的时间戳（<code>Date.now()</code>，单位为毫秒）

==限制==
*<code>payload</code>中不可包含换行、不可包含右方括号（<code>]</code>）。因此，我们不建议用JSON格式数据。
**<code><nowiki>[_event:toast]</nowiki></code>、<code><nowiki>[_event:toast|]</nowiki></code>、<code><nowiki>[_event:toast| ]</nowiki></code>这三种情况下payload均为空字符串。
**<code><nowiki>[_event:名字|字段=值|数据]</nowiki></code>的payload为<code>"字段=值|数据"</code>
*仅在流式传输中触发。历史消息不会自动触发，想要调试可以看下一节。
*仅siteAgent具有本功能。在cockpit中打开siteAgent，仅会应用club站的事件处理器。

==调试==
事件标记会输出一个这样的不可见元素：
<pre>
<span class="md-event" data-event="eventname" data-payload="payload" data-raw="[_event:eventname|payload]" role="button" tabindex="0">⚡eventname</span>
</pre>

你可以使用以下调试指令将他们显示出来：
<syntaxhighlight lang="javascript">
$siteAgentEventDebug();        /* 切换 */
$siteAgentEventDebug(true);    /* 只打开 */
$siteAgentEventDebug(false);   /* 只关掉 */
</syntaxhighlight>

显示出来之后，你可以通过点击这个元素再次触发事件。

==口径编写指南==
你需要让siteAgent知道这个站点能使用哪些event。

我们在系统提示里已经告知了他相关语法（使用方括号_event:eventname，第一个pipe后是payload），你只需要告诉他哪些事件可用、参数怎么传就可以了。
*关于无法避免的右方括号，我们建议你告诉siteAgent使用某个特殊符号代表右方括号，并且在eventHandler里完成替换。

你需要包含的信息有：
*有哪些event可用
*参数里填什么，有什么限制
*什么时候发，什么时候不该发
*有没有数量限制

我们以一个live2d形象为例：
<pre>
# 页面上的形象
你可以在回答里用事件让页面上的形象做反应。写法是单独占一行最稳妥，也可以直接跟在句子后面：
    [_event:live2d|名字]

可用名字：
- happy：道喜、夸奖、好消息
- sad：抱歉、坏消息、我查不到
- surprised：需要提醒用户注意
- idle：中性或没把握时用这个

规则：
- 只在情绪明确时发；一条回复最多 2 个，写在相关那句话里、或者它的下一行。
- 正在报错、在解释工具失败时不要发。
- 不要向用户解释这个写法。
</pre>

前端的<code>siteagent:event</code>handler中，通过<code>detail.name</code>过滤live2d，然后处理<code>payload.split("|")[0]</code>拿到相应动作即可。

==事件的硬性要求==
*事件名称只能用英文小写、数字、下划线、连字符（<code><nowiki>[a-z0-9_-]</nowiki></code>），长度1-32位。
*整个事件块会保留在上下文中，agent会读到。因此他需要具有足够的语义。
*事件参数可以用中文，但不建议用中文。
*'''口径中未列出的事件就不发'''这是给agent的要求，不是技术上的限制。你仍可以直接要求agent"发送这么一个事件blablabla"。
*'''非常不建议用JSON当payload'''。JSON数组里必定出现右方括号（会被提前截断），而且有大量冗余字符（花括号、引号、逗号等）。对象虽然不含右方括号，但一样不划算。

==注册eventHandler的方法==

除了上文例子里的<code>window.addEventListener</code>（方法1），你还可以用以下两种方式处理事件。

===方法2：$siteAgentEvent===
<syntaxhighlight lang="javascript">
// 处理live2d事件
var off = window.$siteAgentEvent('live2d', function (detail) { /* 示例，自己实现 */ });
// 之后想取消注册时
off();
// 处理全部事件
window.$siteAgentEvent('*', function (detail) { /* 通过detail.name判断后处理 */ });
</syntaxhighlight>
该方法的缺陷是<code>$siteAgentEvent</code>需要等皮肤加载完才会生效，会和你的脚本产生先后顺序问题。
*在<code>window.CHP.then()</code>之后注册可保证生效。

===方法3：排队===
<syntaxhighlight lang="javascript">

var live2dHandler = function (detail) {
    /* 示例，自己实现 */
};
// 注意push的形状：二元数组，字符串+函数
(window.__hjsSiteAgentEventHandlers = window.__hjsSiteAgentEventHandlers || []).push(['live2d', live2dHandler]);

</syntaxhighlight>
这种方法可以保证window.__hjsSiteAgentEventHandlers一定存在，名字也可以填<code>*</code>表示处理所有事件。
*皮肤加载时、以及'''每次派发事件前'''，都会把数组里排队的条目接管进注册表并清空数组（所以皮肤加载之后再 push 的，也能在下一次事件里生效）。
*用这个方法无法取消注册。

==常见问题==

'''我让它写事件，但它从来不写？'''

*先确认机长口径里真的列了名字和时机（模型不知道你要什么就不会写）；再确认名字符合 <code><nowiki>[a-z0-9_-]</nowiki></code>。
*在控制台输入<code>$siteAgentEventDebug()</code>会在正文冒出事件处出现一个卡片，表示这个时候发送了事件。你可以点击这个小卡片重新发出事件。

'''写了但没反应？'''

依序排查：
#是不是写在'''markdown表格'''里（表格按竖线分列，标记会被拆开）；
#是不是写在代码块或者反引号里；
#名字和你 handler 里认的对不对得上（大小写、空格）；
#数据里是不是有右方括号（会被提前截断）；
#handler是不是挂在那条消息所在的页面上。

'''控制台报 <code>window.$siteAgentEvent is not a function</code>？'''

*你的脚本比皮肤跑得快。建议更换为方法一或方法三。

'''能在 <code>site_*</code> 工具里发事件吗？'''

*你都能用工具了为什么还要用event
*理论上你的工具发出同一个事件也没问题，就是有一些上下文字段会缺失，自己注意处理。
*但是event比工具要省一些，见下文“燃料消耗”。

关于tool发出同一个事件的示例：
<syntaxhighlight lang="javascript">
// 等同于agent发送[_event:emote|字段=值|数据]
let e = new CustomEvent("siteagent:event", {
    detail: {
        name:"emote",
        payload:"字段=值|数据" 
    }
});
// 这种方法下，detail里只会包含name和payload
window.dispatchEvent(e);
</syntaxhighlight>

*注意：这么发只走<code>window.addEventListener</code>这一条路。用<code>$siteAgentEvent</code>或<code>__hjsSiteAgentEventHandlers</code>注册的handler'''收不到'''——那两个是我们内部的注册表，只有正文触发的派发才会调它们。

'''事件会存进对话历史吗？'''

*会。标记是正文的一部分。但历史记录不会自动触发事件。
*使用调试功能可以手动触发历史事件。
*由于他是正文的一部分，我们建议整体上具有充分的语义以便agent理解。

==燃料消耗==
和siteAgent的工具不同，eventAPI没有额外的一次模型往返，所以燃料消耗几乎可以忽略。会有零星消耗的点在：
*siteAgent口径中需要额外描述event；
*正文答复时需要占用额外的字符数；
*如果开了思考模式，则会在思考中考虑额外的输出逻辑。
