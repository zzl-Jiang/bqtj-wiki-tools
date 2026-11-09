# 帮助:使用SPA

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3A%E4%BD%BF%E7%94%A8SPA
revid：41243 · 抓取时间：2026-11-09T14:27:10+08:00

---

{{编辑手册nav}}
本文所述内容意在指导开发者如何在MediaWiki上开发单页应用（Single Page Application），而不是做水疗。教程文字整理自[[user:Pa001024|{{#avatar:Pa001024|sm}}Pa001024]]的技术博客


== 准备 ==
需要先申请[[h:博客:吹响灰机开发者的号角|开发者权限]]：因为需要编辑js和common.css页面

==API==
{{expand|另行参见：[[API]]}}
=== PHP的api ===

https://arknights.huijiwiki.com/api.php 或者 https://cdn.huijiwiki.com/arknights/api.php

灰机的这个页面是可以跨域的，可以处理维基相关的操作 如果你做的开发是与维基内容有关。这个页面必须啃透。

:需要注意的是后面带cdn的是只读的，也就是只能用GET请求，一般用于读取Data数据或者其他页面内容。

===RESTful的api ===
https://arknights.huijiwiki.com/api/rest_v1/
同样是跨域的api，这个API没有缓存所以使用时需要注意请求频次和其他对于服务器性能的影响，由于保护设置可能会经常504，所以不推荐作为核心功能使用，与PHP的API相比多了一个把wikitext转换成html的功能。（下面会用到）

=== 主域的api ===
https://arknights.huijiwiki.com/index.php?title=xxx&action=xxx

这个其实也不算api，也不能跨域，不过在不需要跨域的时候还是比较好用的，常用的指令有action=raw和action=render，前者是输出wikitext后者是输出HTML。

=== JS的api ===
也就是所有页面中都有的mw对象。说明文档[https://doc.wikimedia.org/mediawiki-core/master/js/#!/api/mw.Api 在这里]，如果要写与wiki本身交互功能，这里大部分都可以直接调用。

== 开发 ==
在了解基础架构并且选择自己喜欢的框架之后就可以开始开发了，这里我用的是Vue+Typescript。

===需要注意的点===
====1. CSS兼容性====

这里的兼容不光是你的代码不会受wiki定义的css影响，同时你的代码也不能对wiki的样式造成影响。

根据不同wiki的不同，你最好复制一份wiki渲染出的css（比如 https://cdn.huijiwiki.com/arknights/load.php?debug=true&lang=zh-cn&modules=skins.bootstrapmediawiki.top&only=styles&skin=bootstrapmediawiki<）到你的项目里以防发生兼容性问题（解决这个问题的最好方法是使用css混淆，或者使用styled-component之类的CSS-in-JS框架）

在Vue中解决这个问题可以使用scoped style，开启之后默认是CSS-in-JS，开autoprefixer则还是CSS，这样做的好处是可以确保你的类名绝对不会影响到wiki中同名的类，不过你的类还是有一定几率会受到wiki中同名类的影响（尽管你优先级更高，但也架不住未定义啊）。

====2. JS兼容性====

一般通过webpack打包出来已经解决了大部分的JS冲突问题，不过如果Typescript需要调用JSapi，需要自己写一个定义。

====3. 图片====

一般来说运行应用需要考虑效率，所以调用wiki上图片肯定不是调用API取html然后放上去这样的，这里提供一种实现方式：[https://github.com/pa001024/arkwiki-hr/blob/master/src/components/WikiImage.vue WikiImage.vue]

主要思路就是解析图片文件名直接生成最终的地址，将首字母大写之后取md5前两位就是图片地址中的前缀

同时也分为原图和缩略图，其中缩略图在你访问之前是不存在的，所以这个组件处理了这种情况。具体原理就是如果一个图片加载失败，就调用RESTful-api来渲染一个指定大小的图片，等于告诉服务器，我现在用了这个大小的图片，你先缓存一下，然后再次加载就能正常读出缩略图了（这里还有一个移动端不同dpi图片的fix，有兴趣可以看代码）。

== 部署 ==
一般js可以写在[[MediaWiki:Common.js]]里，不过实际项目编译出来的文件往往较大，除非这个是全站UI改动，否则不推荐放在这里。

我们推荐使用零件来部署，请查看官方教程[[h:帮助:零件|帮助:零件]]，这里不赘述。

:'''[[templatemanager:Manifest:Vue|Vue零件]]'''：由Honestleaf提供的VUE零件

一般来说我们开发的都是'''SPA'''，也就是只有特定页面才需要加载的，所以零件定义（Gadget_definition）里面的'''default'''就写成'''false'''，表示不默认加载，同时'''hide'''也为'''true'''，表示不能在设置手动勾选。这样这个零件就只能通过代码来手动加载了，也就保证了只有特定页面才会加载。

这里的加载方式可以参考[[Html:VueTpl]]，通过调用<code>mw.loader.load("ext.gadget.零件名")</code>来实现异步加载。

=== 需要注意的点 ===
如果你是用webpack这种打包工具打包的，你基本会有99%概率遇到如下报错问题，如图
[[File:blog-pa1.png]]

为什么呢？明明在本地都可以运行啊。那是因为mw的解析器只认识ES3（IE8）的语法，只要他不认识就会报这个Parse error。

当然是有办法解决的，办法就是在webpack打包之后再对他进行一个转换，这里虽然找到了es3ify-loader或者es3ify-webpack-plugin，然而这个只能转换a.default到a["default"]而不能转{default:0}这种，实际上后者只要转换成{"default":0}在ES3也并不报错，但是我们神奇的mw不认，只好再给他治一治。为此我专门魔改了一个转换器出来[https://github.com/pa001024/es3ify-mw es3ify-mw]，已经放到npm，使用例子见[https://github.com/pa001024/arkwiki-hr/blob/master/mwtransform.js 此处]。

===避难措施===
如果你没有折腾成功，那么也可以使用第三方的cdn来提供脚本的加载，这种加载方式的示例在[[arknights:html:Hr]]，缺点是可能会产生一定成本费用。

至此大功告成，总算是可以在WIKI上开发大型SPA了，可喜可贺可喜可贺。

==实例==
*<s>[[arknights:HR|明日方舟探员招募选择器]]</s>
