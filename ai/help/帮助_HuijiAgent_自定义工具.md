# 帮助:HuijiAgent/自定义工具

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3AHuijiAgent/%E8%87%AA%E5%AE%9A%E4%B9%89%E5%B7%A5%E5%85%B7
revid：42440 · 抓取时间：2026-11-09T14:27:09+08:00

---

{{子页面列表|目标页面=帮助:HuijiAgent|隐藏前缀=1}}
{{编辑手册nav}}{{HuijiOnly}}

从2026年10月24日开始，站点可以为自己的站点助手（siteAgent）注入'''额外的前端工具'''。

站点助手在回答时会像调用内置工具（查知识库、读页面）一样调用它们，但有一些区别：'''这些工具的执行发生在浏览器里'''，用的是本站自己的JS。也就是说，怎么查数据、字段怎么翻译成人话，都由站点自己决定。



==它解决什么问题==
我们已收到大量反馈，希望siteAgent能访问本站的mongoDB。但目前的困难是：
*我们不知道站点的数据结构是什么样，比如武器在哪，装备在哪；
*Data空间下可能混有一些配置文件；
*结果中的大部分字段可能都是无用字段。

因此，我们决定将自定义工具开放给站点开发者，由开发者在js中自行定义工具行为。
*能实现的功能不限于mongoDB，只要JS能做、当前用户有权限，则都能实现。

==执行流程==

<pre lang="mermaid">
sequenceDiagram
    autonumber
    participant F as 前端（本站 JS）
    participant S as 站点助手（服务端）
    participant M as 大模型

    F->>F: 每次发送时读 __hjsSiteTools
    F->>S: 发送内容 + 本轮工具清单
    S->>M: 提问 + 工具清单
    M->>S: 决定调用 site_xxx
    S->>F: 请求执行前端工具(id和参数)
    Note over F JS: execute(param)
    F->>S: 发送前端执行结果(ok+result/error+message)
    S->>M: 发送工具返回值
    M->>M: 生成回答
</pre>

* '''工具只在页面开着时可用'''。刷新、跳转、关闭页面时，LLM会受到工具调用错误的答复，但他会自己继续执行。
* '''执行身份是用户本人'''。你的 <code>execute</code> 里发的请求带的是当前访客的会话，所以能不能执行这一步操作决于'''访客自己的权限'''。
* '''工具清单每一轮都会重新拉取'''，所以站点改了定义、或者懒加载的零件后来才注册都会在下一次用户点击发送时生效。

==定义方法==

在<code>MediaWiki:Common.js</code>或js零件里用如下方式注册工具（向window.__hjsSiteTools数组里push）：

<syntaxhighlight lang="javascript">
/* 使用这种fallback来保证数组存在 */
(window.__hjsSiteTools = window.__hjsSiteTools || []).push({
    id: 'queryitem',  // 工具ID，需要本站唯一
    description: '查询本站物品，最多返回 10 条。', // 工具描述
    parameters: { // 传入参数的schema，参考下文写Schema那一节
        type: 'object', // 这一层必须是object
        properties: {
            query: { type: 'string', description: '关键词' }, // 参数query的定义和说明
        },
        required: ['query'], // query必填
        additionalProperties: false, // 不允许添加其他参数
    },
    execute: function (args) { // args就是上面定义的{query:string}，只接受一个参数。可以返回Promise
        return [];
    },
});
</syntaxhighlight>


===字段===

{| class="wikitable"
! 字段 !! 必填 !! 说明
|-
| <code>id</code> || 是 || 工具标识，只允许小写字母/数字/下划线（<code><nowiki>^[a-z0-9_]{1,48}$</nowiki></code>）。模型看到的工具名是<code>site_&lt;id&gt;</code>
|-
| <code>description</code> || 是 || '''给模型看的全部说明'''：干什么、什么时候该用、每个参数是什么、返回什么。超过 600 字会被截断，而且越长越烧燃料
|-
| <code>parameters</code> || 否 || 入参的 JSON Schema。不写就是「无参数」，详见下文“怎么写schema”
|-
| <code>execute</code> || 是 || <code>function (args) { ... }</code>，返回值就是工具结果。可以返回Promise。promise在Reject的时候会被视为错误，错误文本LLM可见。
|-
| <code>debug</code> || 否 || <code>true</code> 时每次调用都往浏览器控制台打日志。'''只在前端生效'''，不会上送给模型
|}

工具个数'''不设上限'''，但你需要考虑到燃料消耗问题：
*'''工具烧燃料，而且就算没有调用也烧燃料。''' 工具清单会在'''每一次'''模型请求时附加到请求定义上、并且每一个请求可能会执行若干步，所以N个工具 = 每一步都要多烧这N份description和schema的燃料。一次都没调用、整轮只问了一句话，这笔燃料也会被消耗。所以：'''能合并就合并、能删就删，宁可一个参数多一点的工具，也不要五个参数少一点的工具。'''

不合法（id 不合规 / description 为空 / 没有 execute）的定义会被'''静默忽略'''——不报错、也不会让对话发不出去，所以定义完要确认助手认得这个工具。你可以直接向siteAgent询问这一轮都有哪些工具可用。

===工具定义的加载顺序与替换===

* 无论你的脚本加载快还是siteAgent加载快，工具注入仅在点击发送时生效；
* 要'''替换'''一个已定义的工具，再 push 一份'''同 id''' 的即可，'''后出现的覆盖前面的'''；
* 要临时停用一个工具：覆盖一个同id但description为空的工具即可，你也可以自己设法写一个filter来处理__hjsSiteTools数组。

==示例==
此处以一个主站查询fonko信息的需求为例（数据在<code>Data:Testdata.tabx</code>）。
===准备===
请首先考虑以下问题：
*这类数据有统一的标识吗？
**有，他们的<code>Toy Category</code>都为<code>funko</code>
*我要开放哪些查询条件？
**需要按名字模糊搜索(<code>$regex</code>)
*结果需要排序、限制数量吗？
**按<code>wiki_index</code>排序
**限制返回10条
*结果中哪些信息要提供给Agent？
**<code>Has Name</code>，<code>Year</code>，<code>Funko Franchise</code>，<code>Funko Series</code>，<code>Is Released</code>，<code>In Bundle</code>，<code>Has Image</code>
*结果中有Agent看不懂的吗？
**有，<code>Is Released</code>，<code>In Bundle</code>现在是数字型，需要翻译为人话。

===设计执行函数===
根据上一节的设计，我们开始设计执行函数。

执行函数的参数必须是一个Object。在我们的场景下，这个object只具有一个字符串型<code>name</code>字段。

执行的行为则是：
*filter参数：限定<code>Toy Category</code>为<code>"funko"</code>，<code>Has Name</code>则需要使用正则实现模糊搜索；
*sort参数：按<code>wiki_index</code>排序；
*limit参数：限制返回10条。

这样，我们可以设计出请求参数（注意restAPI要求请求参数为string，所以我们要对Object做JSON.stringify）：
<syntaxhighlight lang="javascript">
{
    filter: JSON.stringify({
        'Toy Category': 'funko',
        'Has Name': { $regex: args.name },
    }),
    sort_by: JSON.stringify({ wiki_index: 1 }),
    pagesize: 10
}
</syntaxhighlight>

下一步是设计处理函数。我们拿到数据后'''不能一次塞给agent'''，因为多数信息可能是对他没用的。我们要选出工具实际需要的字段，并且“翻译成人话”。

<syntaxhighlight lang="javascript">
// jquery ajax then的处理函数
function (response) {
    var docs = (response && response._embedded) || [];
    // 如果没查到，可以用Error告诉Agent
    if (docs.length === 0) throw new Error('未找到匹配的 Funko');
    // 选出所需字段，并且翻译成人话
    // 你也可以用restapi的keys字段提前限制返回哪些字段
    return docs.map(function (doc) {
        return {
            'Has Name': doc['Has Name'],
            'Year': doc['Year'],
            'Funko Franchise': doc['Funko Franchise'],
            'Funko Series': doc['Funko Series'],
            'Is Released': doc['Is Released'] === 1 ? '已发售' : '未发售',
            'In Bundle': doc['In Bundle'] === 1 ? '套装' : '单品',
            'Has Image': doc['Has Image']
        };
    });
}
</syntaxhighlight>

这样，我们就得到了一个完整的执行函数：
<syntaxhighlight lang="javascript">
function executeFunkoQuery(args) {
    if (typeof args.name !== 'string' || args.name === '') throw new Error('name必填');
    return $.ajax({
        url: '/api/rest_v1/namespace/data',
        data: {
            filter: JSON.stringify({
                'Toy Category': 'funko',
                'Has Name': { $regex: args.name },
            }),
            sort_by: JSON.stringify({ wiki_index: 1 }),
            pagesize: 10
        }
    }).then(function (response) {
        var docs = (response && response._embedded) || [];
        if (docs.length === 0) throw new Error('未找到匹配的 Funko');
        return docs.map(function (doc) {
            return {
                'Has Name': doc['Has Name'],
                'Year': doc['Year'],
                'Funko Franchise': doc['Funko Franchise'],
                'Funko Series': doc['Funko Series'],
                'Is Released': doc['Is Released'] === 1 ? '已发售' : '未发售',
                'In Bundle': doc['In Bundle'] === 1 ? '套装' : '单品',
                'Has Image': doc['Has Image']
            };
        });
    });
}
</syntaxhighlight>

===设计Schema===
我们还需要告诉agent“这个工具怎么传参数”。可参考的文档：
* [https://json-schema.org/learn/getting-started-step-by-step 官方入门教程]
* [https://json-schema.org/draft/2020-12/json-schema-validation 关键字总览]

由于各家LLM用的是不同的JSON Schema子集，我们应当尽量使用标准字段：
*type - 指定这个节点的数据类型(<code>string</code>、<code>number</code>、<code>boolean</code>、<code>object</code>、<code>array</code> 等)
*description - 对这个节点的描述，通常用于告诉agent这个参数的用途
*required - 指定这个节点是否为必填项，值为布尔类型
**type为object时，required可以填写这个对象中哪些属性是必填的，值为属性名数组。
*additionalProperties - 指定对象是否允许出现未在properties中声明的属性，值为boolean。
*properties - 指定该对象的下一级属性，值为一个对象，键为属性名，值为该属性的JSON Schema定义。
**为了防止Schema过于复杂，我们建议尽量使用一层参数。

另外，我们还有一个限制“函数只能有一个参数”，也就是上文的args。

根据上例的要求，我们可以得出一个schema:
<syntaxhighlight lang="json">
{
    "type": "object",
    "properties": {
        "name": {
            "type": "string",
            "description": "Funko 的名称"
        }
    },
    "required": ["name"],
    "additionalProperties": false
}
</syntaxhighlight>

===设计工具提示===
我们还需要一个字段来描述'''这个工具有什么用'''。
<syntaxhighlight lang="javascript">
    '查询 Funko 玩偶（只看玩具分类 funko 的那批数据，最多 10 条）。' +
    '参数 name 是名称关键词，如「琼恩」「布兰」。' +
    '返回数组，每条含 name（名称）/ year（年份）/ franchise（作品系列）/ series（Funko 系列）/ ' +
    'released（是否已发售）/ bundle（套装还是单只）/ image（图片文件名）。',
</syntaxhighlight>

===注册工具===
最后，我们生成一个包含上述信息的对象，并给定一个工具id即可。
*<code>id</code>：需要在当前站点唯一。如果不唯一则最后注册的生效。
*<code>description</code>：描述这个工具的用途。
*<code>parameters</code>：工具的参数 schema，遵循 JSON Schema 规范。
*<code>execute</code>：工具的执行函数，接收一个参数对象 args，返回结果或 Promise。

完成后，将他push到<code>window.__hjsSiteTools</code>。由于脚本加载顺序的原因，此时的hjsSiteTools可能还没有出现，因此需要做一次判断，如果没有则新建一个。

<syntaxhighlight lang="javascript">
(window.__hjsSiteTools = window.__hjsSiteTools || []).push({
    id: 'queryfunko',
    description:
        '查询 Funko 玩偶（只看玩具分类 funko 的那批数据，最多 10 条）。' +
        '参数 name 是名称关键词，如「琼恩」「布兰」。' +
        '返回数组，每条含 name（名称）/ year（年份）/ franchise（作品系列）/ series（Funko 系列）/ ' +
        'released（是否已发售）/ bundle（套装还是单只）/ image（图片文件名）。',
    parameters: {
        type: 'object',
        properties: {
            name: { type: 'string', description: '玩偶名称里的关键词，中文即可，如「琼恩」' },
        },
        required: ['name'],
        additionalProperties: false,
    },
    execute: function (args) {
        if (typeof args.name !== 'string' || args.name === '') throw new Error('name 必填');
        return $.ajax({
            url: '/api/rest_v1/namespace/data',
            dataType: 'json',
            data: {
                filter: JSON.stringify({
                    'Toy Category': 'funko',
                    'Has Name': { $regex: args.name },
                }),
                sort_by: JSON.stringify({ wiki_index: 1 }),
                pagesize: 10,
            },
        }).then(function (response) {
            var docs = (response && response._embedded) || [];
            if (docs.length === 0) throw new Error('没有名字含「' + args.name + '」的 Funko 玩偶');
            return docs.map(function (doc) {
                return {
                    name: doc['Has Name'],
                    year: doc['Year'],
                    franchise: doc['Funko Franchise'],
                    series: doc['Funko Series'],
                    released: doc['Is Released'] === 1 ? '已发售' : '未发售',
                    bundle: doc['In Bundle'] === 1 ? '套装' : '单只',
                    image: doc['Has Image'],
                };
            });
        });
    },
});
</syntaxhighlight>

===测试===
*想测试工具是否能跑通：可以直接在控制台用<code>__hjsSiteTools</code> 查看已注册的工具，找到execute 函数并调用。
*想测试工具是否注册成功：可以直接问siteAgent“有没有site_开头的工具”。site_开头的工具均为当前站点注册的工具。
*想做量化测试，可以给工具定义加上<code>debug:true</code>，他会在控制台给你返回一些有用的信息。

上例已在灰机主站的siteAgent实现，你可以在右下角打开siteAgent并请他“查找名字包含琼恩的funko”。

==执行函数==
你可以在执行函数中返回任意thenable对象，包括Promise、jquery的jqXHR，也可以直接同步返回数据。

需要注意的是，'''mediawiki'''的代码压缩器不支持ES6语法，比如async、await等。这种情况下可能会出现多层then嵌套的情况：但你可以在最外面包一个Promise。

<syntaxhighlight lang="javascript">
{
    execute:function (args) {
        return new Promise(function (resolve, reject) {
        // 这里不管嵌套多少层，最终调最外层的resolve(result)或者reject(error)即可
        // reject则会被认为工具调用失败，agent能看到reject(error)的error。        
            });
        }    
    }
}
</syntaxhighlight>

此外，在[[帮助:使用cockpit组件|window.CHP]]兑现后，你可以用其中的<code>axios</code>作为<code>$.ajax</code>的替代品。

==工具链的设计==
对于需要agent依次调用工具才能实现的业务，你需要在工具的description或站点提示词里给他足够的指引。

以官方知识库查询工具链为例，我们在后端已经明确给出了这些工具的调用顺序：
*用<code>kb_search_wiki</code>找知识库条目；
*用<code>kb_get_wiki_section</code>找相应章节；
*用<code>kb_get_nearby_sections</code>找相邻章节；
*如果知识库没有，用<code>wiki_search_live</code>直接搜维基；
*拿到了页面标题或pid后用<code>wiki_rendered_bytitle</code>取内容。

siteAgent每次对话具有六轮的工具调用限制（每轮可以同时发出多个请求），设计工具链时务必注意。


* '''链上每一环都是一次完整的模型往返'''，也就意味着清单每次都重发：三步的工具链 ≈ 三倍的固定开销。能从工具内部搞定的别拆成两步。
* '''两步之间不需要模型做判断就别拆'''。
* '''中途出错很正常'''：某一环如果出了问题（灰机网络问题、本地JS问题等）是很正常的。agent会看到错误信息以决定后续操作。
* '''输出要照顾下一步'''：既然结果会被拿去接着用，就把下一步需要的东西（id、英文名、可选的枚举值）放在返回对象里，别只给整段文案。
* '''description 里不用写“必须在 X 之后调用”'''：模型不保证照做，那句话还占字数。把名字和参数写清楚、在 prompt 里给顺序，比下命令可靠，除非你在前端确实有先后顺序逻辑。

==注意事项==

===返回值===

由于没有针对返回值类型的硬性限制，我们建议返回值尽可能用属性名就能看懂。例如，如果坐标字段的原始数据为<code><nowiki>[253,622]</nowiki></code>，则提供给agent时应当转换为<code><nowiki>{x: 253, y: 622}</nowiki></code>。

* '''必须是 JSON 能表达的东西'''：字符串、数字、布尔、数组、对象、<code>null</code>皆可。对象最常见，但'''不是强制要对象'''。
* '''不要返回''' <code>Date</code>、函数、DOM 节点、循环引用的对象。它们进不了模型的消息，会让这一轮直接失败。
* 返回 <code>undefined</code>会被当成<code>null</code>。
* '''返回结果也占燃料'''。根据自己站点的情况截断结果、筛选字段，或选用更合适的查询语句。


===怎么省燃料===
对于工具定义，最大的燃料开销就是工具定义本身。因为即使工具没有被调用，他也会出现在每一轮请求中，并且同一轮对话的每一个步骤也会包含这些定义。

因此，工具要少、并且语义化。能共用参数的工具可以合并成一个。
*例如一个“查询物品”、但带有物品类型参数的工具，好过“查询武器”“查询防具”等多个工具。

一个工具里能实现的工具就不要拆成多个。
*例如按名字搜物品、按稀有度搜物品可以合并成带有两个可选参数、但description里限制二选一的工具。

工具的描述只要足够让agent“知道他能干什么”就可以。

返回结果也应当尽量精简。


===错误处理===
*怎么告诉agent“代码报错了”
**在execute中使用throw new Error、在promise中reject皆可。agent能看到错误文案。
**错误文案应当说人话，这样agent方便判断下一步怎么做。
*验证参数
**在execute函数里对参数进行必要的验证。服务端不会处理参数校验问题，schema是给Agent看的，他不一定会听话。

===其它===

* '''30 秒超时'''：一次执行超过 30 秒，模型会收到前端没响应的提示。
* '''页面一走就没了'''：访客刷新 / 跳转 / 关页面，执行体随页面消失，这一轮调用失败。
* 页面关掉之后，'''这一轮不会立刻停'''。模型会把手上的信息整理完（结果照样存进会话），并且被要求'''不再调用任何 <code>site_</code> 工具'''。所以不会出现等 30 秒-再试一个-再等 30 秒的干烧现象。就算agent依然这么做了，服务端也不会让它干等：前端一断，后续每次站点工具调用都会'''立刻'''返回'''前端连接已断开（页面被刷新或关掉了）'''。
* '''只做查询'''：不要在里面保存编辑、发消息。执行身份是访客，做这些出了问题极难排查。


==常见问题==

'''为什么助手好像根本不知道我有这个工具？'''

: 三种可能：
*定义不合法（id 不合规 / description 为空 / 没有 execute）被静默丢掉；
*你的 JS 在这条消息'''之后'''才跑（下一轮才带上）；
*撞了 id、被同名的那份盖掉了（后 push 的赢）。加 <code>debug: true</code> 看控制台有没有调用日志，是最快的判断方式。

'''工具定义多了会不会很贵？'''

*会，而且'''不用也贵''' —— 清单每步重发，数量直接变成固定开销。详见上面「怎么省燃料」和「工具之间怎么配合」。

'''工具名里为什么多了个 <code>site_</code> 前缀？'''

*那是「前端工具」的标记，也顺手防止和内置工具撞名。你只写 <code>id</code>，模型看到的是 <code>site_&lt;id&gt;</code>。
*注意：模型看到的是带 <code>site_</code> 前缀的 id，但你在 JS 里仍然用原始 id 注册和调用工具。

'''能在工具里再调别的站的数据吗？'''

*技术上可以（就是个普通请求），但那是跨站行为，请先确认你有权限、且访客能理解。
*此外，请求其他站点的api会造成本站csrf丢失。

'''为什么我在驾驶室里跟助手说话时，它说查不了站内数据？'''

*因为驾驶室从属于灰机俱乐部(club.huijiwiki.com)，站点工具实际上是club的工具。因此，我们决定在驾驶室不应用这种功能。

'''没开知识库的站能用吗？'''

: : 不能用。站点助手本身要求这个站开了知识库；自定义工具是它的扩展，不是替代。
