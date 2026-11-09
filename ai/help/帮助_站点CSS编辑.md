# 帮助:站点CSS编辑

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3A%E7%AB%99%E7%82%B9CSS%E7%BC%96%E8%BE%91
revid：39615 · 抓取时间：2026-11-09T14:27:11+08:00

---

{{编辑手册nav}}
'''层叠样式表'''（‘‘CSS’’）是一种用来表现HTML（标准通用标记语言的一个应用）或XML（标准通用标记语言的一个子集）等文件样式的计算机语言。
CSS目前最新版本为CSS3，是能够真正做到网页表现与内容分离的一种样式设计语言。相对于传统HTML的表现而言，CSS能够对网页中的对象的位置排版进行像素级的精确控制，支持几乎所有的字体字号样式，拥有对网页对象和模型样式编辑的能力，并能够进行初步交互设计，是目前基于文本展示最优秀的表现设计语言。CSS能够根据不同使用者的理解能力，简化或者优化写法，针对各类人群，有较强的易读性。

CSS知识由浅入深，大致由下列要点构成：
*层叠作用规则
*选择器与类（class）、伪类
*CSS属性与默认值
*实际应用

我们推荐您前往以下页面进行基础学习：
*[http://www.runoob.com/css/css-tutorial.html CSS教程（站外链接）]

== 在灰机wiki使用CSS ==
在灰机，所有管理员以上级别的用户可以在一定条件下自定义站点CSS。具体方法是将站点需要使用的CSS文件添加到所在站点的CSS页面：

*'''方法一'''：[[Mediawiki:Common.css]]（灰机不支持针对特定用户的css页面编辑），该页面的脚本会在全站点默认加载，但会被CDN缓存，回源时间最长不超过24h，可以通过?debug=1指令暂时绕过进行调试，详情参考：[[帮助:Huiji缓存]]
*'''方法二'''：通过'''[[帮助:零件|零件]]'''挂载的Gadget:xxx.css页面添加，这里的脚本是'''按需加载'''，即只有满足了零件本身的加载逻辑才会生效，与方法一类似，这里的脚本会被CDN缓存。
*'''方法三'''（需要[[help:开发者101|开发者]]权限）：通过'''[[帮助:Mustache模板|html模板]]'''中的<code><nowiki><style></style></nowiki></code>标签插入一段CSS代码,这里的脚本只会在调用嵌套了html模板的页面加载生效，但不会被CDN缓存，因此无需调试或等待刷新缓存。
**注意，如果在template模板中嵌套html模板来装载CSS，如果该模板被多次加载，CSS也会被多次加载，因此最好在嵌入方式仅被加载一次的情况下使用这种方法。

{| class="wikitable"
|-
! 方法 !! 加载方式 !! 会否被CDN缓存 !! 特性
|-
| 一 || 全局加载 || 会 ||MediaWiki默认
|-
| 二 || 按需加载 || 会 ||MediaWiki零件提供<br><span class="text-primary">未安装Gadget扩展无法使用</span>
|-
| 三 || 按需加载 || 不会 ||灰机wiki提供<br><span class="text-primary">非灰机wiki平台无法使用</span>
|}

:参考：'''[[帮助:站点JS编辑]]'''

==需要注意的问题==
在修改CSS的过程中，您需要注意以下问题：
* 请不要使用CSS修改属于灰机wiki的皮肤区域，包括但不限于头部、页脚、侧边栏、广告等。请确保您的编辑符合用户协议的约定。
* 请不要过度修改CSS，以免造成读者阅读困难。（比如将背景设为半透明可能会造成阅读障碍。）
* 修改CSS后，测试时应在url后加上?debug=1来绕过服务器缓存。
* 修改CSS后，应尽可能在更多的浏览器上测试（其表现可能完全不同），并且需要照顾手机浏览器。

== 外部库 ==
为了您的方便，下列外部库已经全局加载，可以直接使用。
* [http://fortawesome.github.io/Font-Awesome/icons/ Fontawesome 4.4]
* [http://getbootstrap.com/ Bootstrap 3.2]

== 模块化 ==
MediaWiki:Common.css中的CSS代码将会全局加载。但是当开发者试图编写一套复杂的CSS代码时，单页显然是不够的。请参阅[[帮助:零件]]学习如何编写高扩展性的前端模块。考虑到复用等情况，编写CSS模块时，应当避免硬编码（hard code）颜色，[[帮助:在CSS中使用主题色彩|尽量调用主题中预设好的色彩。]]

== 常用代码 ==
在进行大规模的修改颜色时，应注意选择器的书写，灰机默认埋下了名为<code>.huiji-css-hook</code>的类，您可以善加利用，以下面的代码为例，可以避免过度选择，影响到talkpage和special页面、ns-0以外的[[help:命名空间|命名空间]]页面样式。
===修改背景颜色===
<pre lang="css">
#wiki-outer-body.huiji-css-hook {
  background-color: #F4F0E7;
  color: #000;
}
</pre>

===使用背景图片===
<pre lang="css">
#wiki-outer-body.huiji-css-hook{
    background:url(https://huiji-public.huijistatic.com/xinglugu/uploads/a/a2/13.jpg);
    background-repeat:no-repeat;
    background-attachment: fixed;
    background-position: center;
}
</pre>

===修改字体===
<pre lang="css">
body {
    font-family: "Lantinghei SC","Open Sans",Arial,"Hiragino Sans GB","Microsoft YaHei","微软雅黑","STHeiti","WenQuanYi Micro Hei",SimSun,sans-serif;
}
</pre>
{{Data Help
|页面名=帮助:站点CSS编辑
|描述文字=站点CSS编辑
|解说=
|symbol=
|主分类=帮助
|子分类=进阶
|tags=编程,维基化,设计,JS
|sortkey=62
|关键=no
|catsortkey=3
|guide=no
|难度=进阶
|角色=设计者
|灰机功能=no
}}
