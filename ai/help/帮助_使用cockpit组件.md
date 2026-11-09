# 帮助:使用cockpit组件

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3A%E4%BD%BF%E7%94%A8cockpit%E7%BB%84%E4%BB%B6
revid：42309 · 抓取时间：2026-11-09T14:27:10+08:00

---

<!-- www:帮助:使用cockpit组件-->

{{编辑手册nav2}}
{{Data Help
|页面名=帮助:使用cockpit组件
|描述文字=使用naive-ui提供的交互组件
|解说=
|symbol=<i class="fa fa-css3" aria-hidden="true"></i>
|主分类=帮助
|子分类=进阶
|tags=编程
|sortkey=255
|关键=no
|catsortkey=1
|guide=no
|难度=进阶
|角色=开发者
|灰机功能=yes
}}

我们在2022年秋季版本中改造了灰机的导航条等组件。改造过程中，我们将一些功能暴露给了window对象，包括：
*<code>$message</code> - toast消息组件
*<code>$dialog</code> - 对话框组件
*<code>$loadingbar</code> - 进度条组件
*<code>$notification</code> - 通知组件（不是mediawiki的通知）
*<code>$modal</code> - 模态框组件
*<code>$popover</code> - 气泡浮层
*<code>$dropdown</code> - 下拉菜单
*<code>$rightMenuToggle</code> - 开关右侧边栏
*<code>$leftMenuToggle</code> - 开关左侧边栏
*<code>$dock</code> - 停靠区（右下角那排按钮）的操作口子
*<code>$cockpitUtil</code> - 工具类

如需在页面加载后立即使用这些组件，请将调用上述组件的代码放在<code>CHP.then()</code>的回调函数中以等待组件加载完成。
*CHP是Component Hook Promise的简称。这个Promise会在上述组件加载完成后兑现（fufill）并执行回调函数。
*在已兑现后再次注册回调函数会立即执行。请参考[https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Promise Promise相关文档]。

<pre>
// 在页面加载后立即调用可能会报错，因为组件可能还没加载完成。
$message.info('爷活了！') // 报错
// 这种情况下需要等待CHP事件完成。
CHP.then(function(tools) {
    $message.info('爷活了！') // 无论如何都会正常运行（除非CHP爆炸而未能正常fufill）
})
// 如果该操作是页面加载后等待了一段时间才触发的（例如用户点了一个按钮），则无需等待CHP。
// 复制以下代码到控制台执行后点击下方按钮以进行测试。
$('#testButton').click(function(){
    $message.info('爷活了！') 
})
</pre>
<div class='label label-success' id='testButton'>#testButton</div> <- 先复制上文最后一段代码到控制台才能点

上文中，CHP的回调函数的tools是一个包含本页所述所有组件的Object（<code>message</code>、<code>dialog</code>、<code>loadingBar</code>、<code>notification</code>、<code>modal</code>、<code>popover</code>、<code>dropdown</code>、<code>util</code>）。<code>$rightMenuToggle</code>、<code>$leftMenuToggle</code>和<code>$dock</code>是例外，它们不在tools里，只在window上（例如<code>window.$rightMenuToggle</code>）。

以下会对上述组件的使用方法做详细介绍。
==message组件==
生成一条toast信息。message预设了几种样式如下：
<pre>
$message.info('info');
$message.success('success');
$message.loading('loading');
$message.error('error');
$message.warning('warning');
// 如果想写一个完全自定义内容的信息，可以使用：
$message.create('没有预设值的消息');
// 一次性隐藏所有消息
$message.destroyAll();
</pre>

你可以在复制上述代码在控制台中查看效果。
===参数===
以<code>$message.info</code>为例，该方法接受两个参数。第一个参数为消息本身（字符串），第二个参数为消息设置，可选。设置参数的节点如下：
{|class='wikitable'
!节点名!!类型!!说明
|-
|closable||boolean||是否显示一个关闭按钮
|-
|duration||number||消息多长时间会自动关闭，毫秒
|-
|keepAliveOnHover||boolean||在鼠标悬停在消息上时是否停止计时
|-
|onLeave||回调函数||信息开始消失时执行的回调
|-
|onAfterLeave||回调函数||信息完全消失（销毁）时执行的回调
|-
|onClose||回调函数||用户手工点击关闭按钮时的回调
|}

===返回值===
上述方法均返回该消息的实例。你可以使用destroy方法销毁该实例。
<pre>
// 创建一个永久不消失的消息
var testmsg = $message.info('永远不消失（不可能）',{duration:999999})
// 然后销毁它
testmsg.destroy()
</pre>

==dialog组件==
创建一个对话框组件，类似confirm，但是不会中断页面中其他脚本的运行。

和message类似，dialog也自带若干种预设样式：
<pre>
$dialog.info({
    title: '我是标题',
    content: 'info'
});
$dialog.success(); // 太长了不想写，下同
$dialog.warning();
$dialog.error();
$dialog.create();
</pre>

===参数===
dialog接受一个object作为参数，该object的节点如下：
{|class='wikitable'
!节点名!!类型!!说明
|-
|title||string||标题
|-
|content||string||内容
|-
|closable||boolean||是否显示一个关闭按钮
|-
|blockScroll||boolean||是否在弹出时禁用后边元素的滚动
|-
|closeOnEsc||boolean||是否在点击esc的时候关闭
|-
|maskClosable||boolean||点击模态浮层时是否关闭
|-
|positiveText||string||确认按钮的文本，如果不填则不显示该按钮
|-
|onPositiveClick||eventHandler(MouseEvent)||点击确认按钮的行为。该函数执行完成之后对话框会关闭。如果该函数返回false、resolve(false)、或者一个被reject的Promise对象，则不会关闭。
|-
|negativeText||string||取消按钮的文本，如果不填则不显示该按钮
|-
|onNegativeClick||eventHandler(MouseEvent)||点击取消按钮的行为。该函数执行完成之后对话框会关闭。如果该函数返回false、resolve(false)、或者一个被reject的Promise对象，则不会关闭。
|-
|onMaskClick||回调函数||点击浮层时的回调
|-
|onClose||回调函数||点击关闭按钮的行为。该函数执行完成之后对话框会关闭。如果该函数返回false、resolve(false)、或者一个被reject的Promise对象，则不会关闭。
|}
示例：
<pre>
$dialog.info({
    title: '给我来一个中杯的拿铁',
    content: '你这儿不是大中小三个杯子吗',
    positiveText: '我就要这个中杯',
    onPositiveClick: function () {
        $message.error('对不起先生那个是大杯');
        // return false时dialog不会关闭
        return false
    },
    negativeText: '抽脸',
    onNegativeClick: function () {
        $message.success('罗老师别这样');
        // 因为没有返回false或者resolve(false)或者reject，对话框会关闭
    }
})
</pre>
复制代码到控制台查看效果。

===返回值===
上述方法会返回dialog实例。使用destroy()方法可以销毁该实例。

==loadingbar组件==
在页面顶部返回一个进度条（虽然这个进度和实际进度无关）。提供三个方法，分别是：
*<code>$loadingbar.start()</code>开始
*<code>$loadingbar.finish()</code>结束
*<code>$loadingbar.error()</code>报个错
上述方法均不需要参数，也不提供返回值。

==notification组件==
在右上方显示一个或多个通知。提供多种预设样式如下：
<pre>
$notification.info({ content: '测一下' }); // 下同，懒得写了
$notification.warning({ content: '测一下' });
$notification.success({ content: '测一下' });
$notification.error({ content: '测一下' });
$notification.create({ content: '测一下' });
// 隐藏所有消息
$notification.destroyAll();
</pre>
===参数===
上述方法（除了destroyAll）接受一个参数作为配置项。该配置项的节点如下：
{|class='wikitable'
!节点名!!类型!!说明
|-
|closable||boolean||是否显示一个关闭按钮
|-
|title||string||标题
|-
|content||string||内容
|-
|description||string||描述
|-
|meta||string||额外信息
|-
|keepAliveOnHover||boolean||悬停时是否停止关闭计时。
|-
|duration||number/undefined||自动关闭时间。如果不设置则不会自动关闭。
|-
|onClose||返回布尔型或resolve为布尔型的peromise的函数||关闭通知的回调。返回false或resolve(false)则不会关闭。
|-
|onLeave||回调函数||通知关闭时的回调
|-
|onAfterLeave||回调函数||通知完全关闭（动画完成）时的回调
|-
|onAfterEnter||回调函数||通知显示时的回调
|}
示例：
<pre>
$notification.success({
    title: '我是title',
    content: '我是content',
    meta: '我是meta',
    duration: 20000,
    onAfterEnter: function () { $message.info('您有新的短消息') },
    onClose: function () { $message.error('呵，男人') },
})
</pre>
===返回值===
上述方法（除了destroyAll()）均返回通知实例。你可以用destroy()方法销毁单个通知。


==modal组件==
{{cockpit version|add|2.0.54}}
即naive-ui的modal组件，用于生成模态框。与dialog的区别是它不限于「一问一答」，可以承载任意内容，并且可以选用预设布局。
<pre>
$modal.create({
    title: '我是标题',
    content: '我是内容',
    preset: 'card', // 可选dialog / card。不填就是一张干净的浮层
    positiveText: '好',
    onPositiveClick: function () {
        $message.success('点了确认');
        return false; // 返回false则不会关闭
    }
});
// 关闭所有由$modal创建的模态框
$modal.destroyAll();
</pre>
create()会返回模态框实例，使用其<code>destroy()</code>方法可以关闭它。其余参数与naive-ui的modal一致，请参考本文底部的参考资料。

==popover组件==
{{cockpit version|add|2.0.54}}
气泡浮层。和上面几个组件不同，它需要你先提供一个'''锚点'''（浮层挂在哪个元素旁边），再决定何时显示。
<pre>
CHP.then(function (tools) {
    var pop = tools.popover.create({
        target: '#someButton',   // 锚点：CSS选择器 / DOM元素 / Vue组件实例
        placement: 'left',       // 摆在锚点的哪一侧，默认left
        content: function () {   // 浮层内容：字符串 / VNode / Vue组件
            return tools.util.h('div', '你好');
        }
    });
    pop.show();
});
</pre>
===create(options)===
{|class='wikitable'
!节点名!!类型!!说明
|-
|target||选择器 / DOM元素 / Vue组件实例||'''必填'''。锚点。到show()的时候才去量，所以给还没上屏的元素（比如ref）也行——量不出来就不显示，不会报错
|-
|placement||string||摆在锚点的哪一侧：left / right / top / bottom，以及带对齐的top-start、top-end、bottom-start、bottom-end。默认left
|-
|distance||number||离锚点多远，默认为12像素
|-
|duration||number||显示多少毫秒后自动关闭。不填则不会自动关闭
|-
|closeOnClickOutside||boolean||点击浮层外面（且不是锚点自己）时是否关闭。默认为true
|-
|destroyOnAnchorRemoved||boolean||锚点被移出DOM时是否自动销毁。默认为true
|-
|content||字符串 / VNode / Vue组件||浮层内容
|-
|width||number||浮层宽度，默认为250像素
|-
|onClose||回调函数||浮层关闭（或销毁）时的回调
|}
===返回值===
create()返回浮层实例：
*<code>show()</code>显示。每次都重新量一次锚点；锚点量不出来时返回false并且不显示
*<code>hide()</code>隐藏。实例仍然保留，可以再次show()
*<code>destroy()</code>销毁该实例
*<code>shown</code>当前是否正在显示
也可以使用<code>$popover.destroyAll()</code>销毁所有气泡。

==dropdown组件==
{{cockpit version|add|2.0.54}}
命令式的下拉菜单。用法与popover一致，只是内容换成菜单项、并且多了选中回调。默认摆在锚点下方并且左边缘对齐（即placement为bottom-start）。
<pre>
CHP.then(function (tools) {
    var menu = tools.dropdown.create({
        target: '#someButton',
        options: [
            { label: '选项一', key: 'a' },
            { label: '选项二', key: 'b' },
            { type: 'divider', key: 'd' }
        ],
        onSelect: function (key) {
            $message.info('选中了' + key);
            menu.hide();
        }
    });
    menu.show();
});
</pre>
options的写法与naive-ui的dropdown一致（支持label、key、disabled、type:'divider'、children等），请参考本文底部的参考资料。可用参数、返回值与popover相同，另外多一个<code>size</code>参数（small / medium / large）。销毁全部用<code>$dropdown.destroyAll()</code>。

==leftMenuToggle / rightMenuToggle==
{{cockpit version|add|2.0.54}}
两个无参数的函数，分别用于打开/收起皮肤左侧的边栏（标题栏左上角那个菜单按钮）和右侧的边栏（右上角头像那个抽屉）。
左抽屉里是当前页面的相关操作，右抽屉里是用户相关的操作；右抽屉是懒加载的，第一次打开时会顺带拉取当前用户的关注列表。
<pre>
window.$rightMenuToggle();
window.$leftMenuToggle();
</pre>


==dock - 停靠区==
{{cockpit version|add|2.0.58}}
页面右下角那一列悬浮按钮叫「停靠区」，里面的按钮由各个功能自己挂上去（评论、站点评分、站内消息、站点管理器、分享……）。
如果你觉得其中几个用不上，可以自己把它们藏起来 —— 藏起来的状态记在'''当前站点'''的cookie里（永久），
所以只影响你藏的那个站，别的站点照旧。

用法是在控制台里执行。第一层是「哪个停靠区」，目前只有右下角这一个，叫<code>bottom-right</code>：
<pre>
// 看这个区现在有哪些按钮（返回按钮id的数组）
$dock['bottom-right'].list()

// 看自己藏过哪些
$dock['bottom-right'].hidden()

// 藏掉其中几个（可以一次藏多个）
$dock['bottom-right'].hide(['site-rating', 'new-message'])

// 把某个再放出来
$dock['bottom-right'].show(['site-rating'])

// 全部恢复（清掉这个站点上所有藏按钮的记录）
$dock['bottom-right'].resetHide()
</pre>

说明：
*<code>list()</code>返回的是'''当前真的会显示'''的按钮id（藏掉的不在里面），所以藏完再<code>list()</code>就能确认生效了。
*<code>hidden()</code>返回的是你藏过的id（cookie里存的那份），里面可能有当前页面上本来就没登记的按钮 —— 那种藏了也没关系。
*<code>hide()</code>是'''累加'''的：多次调用会把id一个个添进去，不会把之前的覆盖掉；<code>show()</code>只管把自己传进去的那几个删掉。
*藏按钮的那个cookie叫<code>dock-hide-bottom-right</code>（本网站的普通cookie，想手动改或删也行）。
*把手（右下角那个折叠开关）藏不掉；如果所有按钮都被藏光了，整个停靠区会一起消失，这时用<code>resetHide()</code>恢复。

我们未来会考虑为站点零件开放停靠区注入功能。

==cockpitUtil - 工具==
cockpitUtil包括了若干个工具。你可以通过<code>$cockpitUtil</code>访问到cockpitUtil节点。
*从2022年11月15日开始，你也可以通过mw.huijiApi获取到这个节点。

以下是列表：
===axios===
即<code>axios</code>库，用于包装请求。访问[https://axios-http.com/zh/docs/intro 官方文档]获取说明。

你可以通过$cockpitUtil.axios或直接访问axios获取该组件，但必须位于CHP之后。

使用<code>axios.create()</code>来创建一个axios副本以避免与cockpit业务产生潜在冲突。

===hotkeys===
即<code>hotkeys-js</code>库，可用于注册快捷键。访问[https://www.npmjs.com/package/hotkeys-js 官方文档]获取使用说明。

'''hotkeys会在CHP事件之后挂载到window，你不需要通过$cockpitUtil.hotkeys访问。'''

hotkeys()接受两个或三个参数。
*第一个参数是需要注册的快捷键列表，字符串。
*第二个参数是回调函数，该函数会提供event和handler两个参数用于处理事件。
**从event可以拿到触发该时间的元素。从handler可以拿到实际触发事件的快捷键组合（因为快捷键可以是多个）。
*如果指定了第三个参数，则第三个参数为回调函数，而第二个参数则是参数配置。参数配置的可选节点如下：
<pre>
{
    // 快捷键的“作用域”。使用hotkeys.setScope()来设置当前激活的作用域。除了'all'之外只能有一个生效的作用域。
    scope:'all', 
    // 触发事件的元素
    element:document.getElementById('someId'),
    // 是否在keyup时触发
    keyup:true,
    // 是否在keydown时触发
    keydown:true,
    // 组合快捷键中的连接符，默认为加号
    splitKey:'+',
    // 这个我也不知道是干嘛的
    capture:false,    
}
</pre>
====注册快捷键列表====
hotkeys()的第一个参数是快捷键列表，多组快捷键使用逗号分隔，组合快捷键使用加号或者上文中提到的splitKey分隔。
<pre>
hotkeys('a,b,c,ctrl+a',function(e,handler){
    $message.info('bingo!')
})
</pre>
组合键支持以下参数：
*⇧, shift, option, ⌥, alt, ctrl, control, command,⌘
*backspace, tab, clear, enter, return, esc, escape, space, up, down, left, right, home, end, pageup, pagedown, del, delete, f1 through f19, num_0 through num_9, num_multiply, num_add, num_enter, num_subtract, num_decimal, num_divide

也可以使用通配符<code>*</code>代表所有按键事件，但你可以通过访问hotkeys[按键名称]判断该键是否被按下，从而进行后续判断。
<pre>
hotkeys('*', function() {
  if (hotkeys.shift) {
    console.log('shift is pressed!');
  }

  if (hotkeys.ctrl) {
    console.log('ctrl is pressed!');
  }

  if (hotkeys.alt) {
    console.log('alt is pressed!');
  }
});</pre>
====关于scope====
使用<code>hotkeys.setScope()</code>来设置当前生效的作用域。设置完成后，所有作用域不为all、且不为被设置的作用域的快捷键绑定均不会生效。
<pre>
// 绑定一个带作用域的快捷键组合
hotkeys('ctrl+o, ctrl+alt+enter', 'issues', function(){
  console.log('do something');
});
hotkeys('o, enter', 'files', function(){
  console.log('do something else');
});

// 设置作用域为issues，此时只有作用域为all和issues的快捷键生效。
hotkeys.setScope('issues');
// 如果需要恢复则将作用域换回all。

// 还有这些方法可以用：
hotkeys.getScope(); // 获得当前作用域
hotkeys.deleteScope('issues'); // 删除所有作用域为issues的快捷键
hotkeys.deleteScope('issues','nobug'); // 将issues作用域的快捷键迁移到nobug作用域
</pre>

====删除快捷键绑定====
<pre>
hotkeys.unbind('a'); // 解除所有按键为a的快捷键绑定。如果不提供第二个参数，则解除的是当前作用域的绑定。
hotkeys.unbind('a','issues'); // 解除issues作用域、按键为a的绑定。
hotkeys.unbind('o,enter'); // 解除当前作用域的o和enter绑定
hotkeys.unbind(); // 解除所有绑定，BY FIRE BE PURGED
</pre>


===parseForm(data)===
将一个object处理成<code>FormData</code>对象以用于post请求。
<pre>
var formRaw = {
    inputText: 1,
    inputBoolean: true,
    inputArray: [1, 2, 3]
}
var formOutput = $cockpitUtil.parseForm(formRaw)
</pre>
===parseFormPlain(data)===
{{cockpit version|add|2.0.54}}
与parseForm相同，但数组类型的值会原样输出，不额外加上方括号。
===getSiteAvatar(prefix,size,modified?)===
生成站点头像地址。
*prefix：站点前缀
*size: 尺寸，l/ml/m/s。默认值为l
*modified：站点头像的更改时间，用于更新浏览器缓存。可选。
===getUserAvatar(userId,size,modified?)===
生成用户头像地址。
*userid：用户ID。
*size: 尺寸，l/ml/m/s。默认值为l
*modified：用户头像的更改时间，用于更新浏览器缓存。可选。
===getUserAvatarFromFileName(filename)===
通过实际文件名生成用户头像地址，不建议使用。
===getSiteUrl(prefix)===
生成一个站点的url。
===getUserUrl(username,prefix)===
生成指向用户页的url。prefix为所在站点的前缀。

不建议使用，用户页即将废弃。
===getPageUrl(title,prefix)===
通过标题生成页面链接。title为完整页面标题。prefix为站点前缀。
===getPageUrlById(pid,prefix)===
同上，但是是通过pageId生成的链接。
===getMedalAvatar(medalId,size)===
生成成就图标的URL。medalId为成就ID，size为尺寸（l/ml/m/s。默认值为l）。
===getGiftAvatar(giftId,size)===
同上，但是是礼物。
===jumpTo(url,target)===
跳转到指定url。target为目标窗体名称，默认值为_blank，即新标签页。设置为_self可在当前标签页打开。
===jumpToSite(prefix,target)===
跳转到指定站点。
===jumpToPage(title,target,prefix)===
跳转到指定站点的指定页面。
===jumpToPageId(pid,target,prefix)===
跳转到指定站点的指定页面，但是使用pageId。
===numberFriendly(value)===
输入数字，生成数字的友好形式。例如大于1024显示为1K，两百万显示为2M。

如果不输入数字，则返回一个“-”
===timestampToUTC8Date(timestamp)===
输入时间戳（秒），返回东八区的时间，YY-MM-dd格式。
===parseText(text)===
将输入文本中的换行符替换为br以用于html输出。
===sleep(t)===
返回一个在t毫秒后resolve的promise。

注意，灰机的js加载器可能暂时不支持es6语法，因此请使用then进行后续操作。
<pre>
async function wakeUp() {
    await $cockpitUtil.sleep(500);
    console.log('睡醒了');
    // 报错，因为mw不认得async也不认得await
}
// 替代写法
function wakeUp() {
    $cockpitUtil.sleep(500).then(function () {
        console.log('睡醒了');
    })
}
</pre>
===isMobile()===
{{cockpit version|add|2.0.54}}
判断当前访问设备是否为移动端，返回布尔值。

===timeRelativeFriendly(time)===
{{cockpit version|add|2.0.54}}
输入时间戳（'''秒'''），返回「3分钟前」「2小时前」这样的相对时间。注意本方法与下面的getRelTime所要求的时间戳单位不同。

===getRelTime(ts)===
{{cockpit version|add|2.0.54}}
输入时间戳（'''毫秒'''），返回聊天里那种相对时间：24小时内显示<code>hh:mm</code>，48小时内显示「昨天 hh:mm」，一周内显示「星期X」，一年内显示<code>MM/DD</code>，更早则显示<code>yyyy年MM月</code>。一律按访问者的本地时区计算。

===setCookie(key,value,options) / getCookie(key) / removeCookie(key,options)===
{{cockpit version|add|2.0.54}}
读写cookie。如果要写「所有子站共享」的cookie，需要把父域带上，可以直接用cookieDomainOption()：
<pre>
var options = Object.assign({ path: '/' }, $cockpitUtil.cookieDomainOption());
$cockpitUtil.setCookie('key', 'value', options);
$cockpitUtil.getCookie('key');
$cockpitUtil.removeCookie('key', options);
</pre>
cookieDomainOption()在线上返回<code>{domain:'.huijiwiki.com'}</code>，在本地开发环境返回空对象（因为localhost写不了父域cookie）。
===getCockpitUserUrl(userId)===
生成指向指定用户的灰机驾驶室链接。
===getCockpitSiteUrl(prefix)===
生成指向指定站点的灰机驾驶室链接。

===getCockpitUrl(route)===
{{cockpit version|add|2.0.54}}
生成指向灰机驾驶室的链接。route为驾驶室内部的路由（例如<code>'user/123'</code>、<code>'site/www'</code>），不填则指向驾驶室首页。

===isCockpitPage()===
{{cockpit version|add|2.0.54}}
判断当前页面是不是「特殊:驾驶室」，返回布尔值。不在mediawiki环境下时返回false。

===getImageUrl(fileName,prefix)===
生成指向图片的原始地址的链接。例如：
<pre>
$cockpitUtil.getImageUrl('Cockpit-logo-png.png','www')
// 返回：'https://huiji-public.huijistatic.com/www/uploads/b/b9/Cockpit-logo-png.png'
</pre>
===getImageThumb(fileName,prefix,width)===
生成一张图片的指定尺寸的缩略图，返回地址。

注意，如果width大于图片的原始尺寸，则接口可能报错。

注意2，返回数据的contentType目前已知有问题。

===clipImage(fileName,params)===
裁切一张当前站点的图片并返回Blob。

fileName为文件名，首字母需要大写，不用加命名空间。

params中需要包括起始点（x、y）裁切尺寸（w、h）四个参数，均为数字型。

返回<code>Promise<Blob | null></code>。

===generateClippedImage(parent)===
{{cockpit version|add|2.0.54}}
把裁切好的图片直接填进某个元素里。参数parent是这个元素，函数会从它的下列data属性读取参数并调用clipImage：
*data-clip-name：图片文件名
*data-clip-x、data-clip-y、data-clip-w、data-clip-h：裁切的起始点与尺寸
*data-target-width、data-target-height：输出图片的尺寸，默认与裁切尺寸相同
*data-target-class：输出图片额外的class，多个class用空格分隔
图片加载完成后会插入parent中（parent原有的子节点会被清空）。

==高级功能==
在$cockpitUtil中还包含了vue的<code>h()</code>函数。请参阅[https://cn.vuejs.org/api/render-function.html#h vue官方文档]获取使用方式。

另外$cockpitUtil中还有一个renderIcon函数，可用于将图标组件包装成VNode。

实际上在上文中提到的配置项中，部分配置项接受VNode作为参数以进行更高级的内容渲染（比如在通知正文中添加html），请参考本文底部的naive-ui文档获取使用方式。

==参考资料==
*[https://www.naiveui.com/zh-CN/os-theme/components/message message] - naive-ui message组件
*[https://www.naiveui.com/zh-CN/os-theme/components/dialog dialog] - naive-ui dialog组件
*[https://www.naiveui.com/zh-CN/os-theme/components/modal modal] - naive-ui modal组件
*[https://www.naiveui.com/zh-CN/os-theme/components/popover popover] - naive-ui popover组件
*[https://www.naiveui.com/zh-CN/os-theme/components/dropdown dropdown] - naive-ui dropdown组件
*[https://www.naiveui.com/zh-CN/os-theme/components/notification notification] - naive-ui notification组件
*[https://www.naiveui.com/zh-CN/os-theme/components/loading-bar loadingbar] - naive-ui loadingbar组件
*[https://www.naiveui.com/zh-CN/os-theme/components/icon icon] - naive-ui icon组件
*[https://cn.vuejs.org/api/render-function.html h()] - vue3 渲染函数
