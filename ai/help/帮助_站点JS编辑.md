# 帮助:站点JS编辑

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3A%E7%AB%99%E7%82%B9JS%E7%BC%96%E8%BE%91
revid：41830 · 抓取时间：2026-11-09T14:27:11+08:00

---

{{编辑手册nav}}
JavaScript，简称JS，一种直译式脚本语言，是一种动态类型、弱类型、基于原型的语言，内置支持类型。它的解释器被称为JavaScript引擎，为浏览器的一部分，广泛用于客户端的脚本语言，在HTML网页上使用，用来给HTML网页增加动态功能。

==在灰机wiki使用JavaScript==
:在灰机，编辑JavaScript功能需至少满足下列条件中的一条：
::*具有[[帮助:用户权限|机长]]权限<ref>根据MediaWiki 1.32对于commonJS权限的改动匹配而来，除了editinterface之外对common.JS增加了单独的权限组editsitejs，而admin用户组不带editsitejs权限。新增了一个名为interface-admin的用户组，而该用户组因为和灰机原有的开发者权限（developer）高度相似故而没有启用。相关权限自动合并到developer和sys-op（机长）组生效。综上，自灰机2023年3.0版本上线之后起，[[帮助:用户权限|管理员]]不再有编辑commonJS页面的豁免。</ref>
::*具有[[帮助:用户权限|开发者权限]]
:换言之，拥有[[帮助:用户权限|开发者权限]]是编辑JavaScript的<span class="text-danger">充分不必要条件</span>。

用户可以在一定条件下自定义站点JavaScript。具体方法包括：
*'''方法一'''：将站点需要使用的js文件添加到所在站点的[[Mediawiki:Common.js]]页面。该页面的脚本会在全站点默认加载，但会被CDN缓存，回源时间最长不超过24h，可以通过?debug=1指令暂时绕过进行调试，详情参考：[[帮助:Huiji缓存]]
*'''方法二'''：通过'''[[帮助:零件|零件]]'''挂载的Gadget:xxx.js页面添加，这里的脚本是'''按需加载'''，即只有满足了零件本身的加载逻辑才会生效，与方法一类似，这里的脚本会被CDN缓存。
*'''方法三'''（需要[[help:开发者101|开发者]]权限）：通过'''[[帮助:Mustache模板|html模板]]'''中的<code><nowiki><script></script></nowiki></code>标签插入一段JavaScript脚本,这里的脚本只会在调用嵌套了html模板的页面加载生效，但不会被CDN缓存，因此无需调试或等待刷新缓存。
**注意，如果在template模板中嵌套html模板来装载CSS，如果该模板被多次加载，CSS也会被多次加载，因此最好在嵌入方式仅被加载一次的情况下使用这种方法。

{| class="wikitable"
|-
! 方法 !! 加载方式 !! 会否被CDN缓存 !! 特性!! 需要权限
|-
| 一 || 全局加载 || 会 ||MediaWiki默认||机长，开发者中任一<br><span class="text-danger">*无需成为开发者</span>
|-
| 二 || 按需加载 || 会 ||MediaWiki零件提供<br><span class="text-primary">未安装Gadget扩展无法使用</span>||必须是开发者
|-
| 三 || 按需加载 || 不会 ||灰机wiki提供<br><span class="text-primary">非灰机wiki平台无法使用</span>||必须是开发者
|}
:参考：'''[[帮助:站点CSS编辑]]'''

==需要注意的问题==
在修改Javascript的过程中，您需要注意以下问题：
* 请不要使用JavaScript修改属于灰机wiki的皮肤区域，包括但不限于头部、页脚、侧边栏、广告等。请确保您的编辑符合用户协议的约定。
* 请不要过度修改JavaScript，以免造成读者阅读困难或网页卡顿。（比如过度使用alert命令。）
* 修改JavaScript后，测试时应在url后加上<code>?debug=1</code>来绕过服务器缓存。
* 修改JavaScript后，应尽可能在更多的浏览器上测试（其表现可能完全不同），并且需要照顾手机浏览器。
* 请不要加载不明外部脚本，他们可能具有侵害性。
* 请注意代码的可读性，撰写必要的注释和文档。

== 外部库 ==
为了您的方便，下列外部库已经全局加载，可以直接使用。
* [https://doc.wikimedia.org/mediawiki-core/master/js/ MediaWiki]
** 如果你要认真的写一段JavaScript, 这个库是必看的。它提供了众多MediaWiki相关API的封装，没有必要重新发明轮子。
* jQuery
* [http://fortawesome.github.io/Font-Awesome/icons/ Fontawesome 4.7]
* [http://getbootstrap.com/ Bootstrap 3.2]

=== 可选库 ===
* OOjs — 一套面向对象的JS库，由Wikimedia设计。另有OOjs-UI，可视化编辑器中使用的UI系统。

== 模块化 ==
<code>MediaWiki:Common.js</code>中的JavaScript代码将会全局加载。但是当开发者试图编写一套复杂的JavaScript代码时，单页显然是不够的。请参阅[[帮助:零件]]学习如何编写高扩展性的前端模块。
*<code>gadget:xxxx.js</code>中的JavaScript文件可以设置为按需加载
*<code>gadget:xxxx.js</code>中的JavaScript文件可以通过[[帮助:灰机Wiki数据更新器|灰机数据更新器]]同步，方便在本地配合零件和module模块同时修改上传更新
*<code>gadget:xxxx.js</code>中的JavaScript文件方便集成、打包、搬运

==常用代码==
===在js中获取指定fileName的图片url===
<pre>
// 计算MD5
window.calcHexMD5 = function(){for(var m=[],l=0;64>l;)m[l]=0|4294967296*Math.abs(Math.sin(++l));return function(c){var e,g,f,a,h=[];c=unescape(encodeURI(c));for(var b=c.length,k=[e=1732584193,g=-271733879,~e,~g],d=0;d<=b;)h[d>>2]|=(c.charCodeAt(d)||128)<<8*(d++%4);h[c=16*(b+8>>6)+14]=8*b;for(d=0;d<c;d+=16){b=k;for(a=0;64>a;)b=[f=b[3],(e=b[1]|0)+((f=b[0]+[e&(g=b[2])|~e&f,f&e|~f&g,e^g^f,g^(e|~f)][b=a>>4]+(m[a]+(h[[a,5*a+1,3*a+5,7*a][b]%16+d]|0)))<<(b=[7,12,17,22,5,9,14,20,4,11,16,23,6,10,15,21][4*b+a++%4])|f>>>32-b),e,g];for(a=4;a;)k[--a]=k[a]+b[a]}for(c="";32>a;)c+=(k[a>>3]>>4*(1^a++&7)&15).toString(16);return c}}();

// 拼图片url
window.getImageUrl = function(filename) {
    var hex = window.calcHexMD5(filename)
    return [
      'https://huiji-public.huijistatic.com/'+mw.config.get('wgHuijiPrefix')+'/uploads',
      hex[0],
      hex[0] + hex[1],
      filename
    ].join('/')
}
</pre>

使用案例
<pre>
// fileName = '图片.png'
var url = getImageUrl(fileName)
</pre>
{{Data Help
|页面名=帮助:站点JS编辑
|描述文字=站点JS编辑
|解说=
|symbol=
|主分类=帮助
|子分类=进阶
|tags=编程,JS
|sortkey=50100
|关键=no
|catsortkey=3
|guide=no
|难度=进阶
|角色=开发者
|灰机功能=no
}}
