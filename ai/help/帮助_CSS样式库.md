# 帮助:CSS样式库

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3ACSS%E6%A0%B7%E5%BC%8F%E5%BA%93
revid：39549 · 抓取时间：2026-11-09T14:27:09+08:00

---

{{编辑手册nav}}
<callout>本页面的内容已经过时，当前版本不再支持<hover.css/>但相关库仍然可以通过零件gadget导入，请自行判断</callout>
灰机整合了一些备受好评的第三方开源CSS样式库，以方便用户自行调用，免去手写/搬运之苦。

本文的一些内容需要一些入门级的CSS知识基础，如果您还不太明白“CSS样式表”、“class”和相关html知识，请另行参见以下内容：
*[[h:帮助:HTML|HTML]]
*[http://www.w3school.com.cn/css/css_syntax_class_selector.asp class（类）]
==工作原理==
[[File:css库示意图.png|400px|right]]灰机在站点资源层打包整合了一些第三方开源的样式库，在这些不同的样式库中包含了若干个Class，用户可以在自己的站点中任意页面里的任意元素中插入class="<想要引用的class名称>"即可获得对应的样式效果。例如：

<code>
<nowiki><div class="hover-buzz"></div></nowiki>
</code>

但是请务必注意两点：
*必须在源代码模式下操作
*必须先在页面中声明想要引用的库，才可以成功引用，否则不会加载。开启方法详见：'''[[h:help:CSS样式库#开启方法|开启方法]]'''

==开启方法==
为了减少预加载，提高页面浏览速度，样式库是默认关闭的，只有在声明引用的时候才会加载，具体方式是在您想要使用样式库的页面中的'''任意位置'''输入：
<code>
<样式表名称.css/>
</code>

例如我想调用“ihover”这个样式库，就在页面的任意位置写入“<nowiki><ihover.css/></nowiki>”即可

==样式的调用与修改方法==
===调用===
<hover.css/>
举个例子，比如您的页面中有这么一段话：

“[[user:SerGawen|点我]]”

源代码编辑器下是

<code><nowiki>[[user:SerGawen|点我]]</nowiki></code>

这是我想给这句话添加一个悬浮效果，我觉得使用来自“hover”样式库的“buzz”样式（我们在hover的手册中找到这一样式的class ID是“hvr-buzz”）
那么操作过程如下：

<code><nowiki><span class="hvr-buzz">[[user:SerGawen|点我]]</span></nowiki></code>

效果是：<span class="hvr-buzz">[[user:SerGawen|点我]]</span>

这里我使用的是“<nowiki><span></nowiki>”标签，类似的您也可以在div、table、li等其他元素中使用。

与class的属性一样，样式可以叠加，比如

<code><nowiki><span class="hvr-buzz hvr-sweep-to-left">[[user:SerGawen|点我]]</span></nowiki></code>，效果：<span class="hvr-buzz hvr-sweep-to-left">[[user:SerGawen|点我]]</span>

===修改===
您可以在站点层对class样式进行修改，站点的class属性会覆盖默认的class属性，比如如果您认为默认的蓝色不合适，可以在本地将对应的background字段改为其他颜色，再进行引用。更改方法有两种
*在站点css页面中修改，需要管理员权限，效果不会马上生效，要等后服务器缓存最近一次更新，亦可以手动使用“调试”功能看到效果；
<code>.hvr-buzz {background:#333;}</code>
*在页面中使用<nowiki>{{#css:}}</nowiki>解析器函数，<code><nowiki>{{#css:.hvr-buzz {background:#333;}}</nowiki></code>可以立刻生效，但是使用不当会增加页面加载内容，慎用。

==支持的样式库表==
===Hover.css===
[[File:hovercss.png|300px]]一款简洁、实用的悬浮效果样式库，支持与Fontawesome图标库一起实用：
*源链接地址：[http://ianlunn.github.io/Hover/ Hover.css @Github]（有效果预览）
*代码库地址：[https://github.com/IanLunn/Hover github代码库]
*教程地址：[http://ianlunn.co.uk/articles/hover-css-tutorial-introduction/ hovercss教程]（英文）
*huiji开启方法：任意位置输入<nowiki><hover.css/></nowiki>
*class命名规则：“hvr”+“class类名”。如果您想使用的效果是“Grow”，那么只需在本站开启<hover.css/>后，调用“hvr-grow”class即可。

===iHover.css===
[[File:ihovercss.png|300px]]比起hover更加酷炫的一套 悬浮效果库。
*源链接地址:[http://gudh.github.io/ihover/dist/index.html  iHover.css @Github]（有效果预览）
*代码库地址：[https://github.com/gudh/ihover github代码库]
*huiji开启方法：任意位置输入<nowiki><ihover.css/></nowiki>
*class命名规则：ihover使用的是样式组合的方法，具体请参见源链接地址上的代码效果和说明。
===纯css背景图案===
一些好看的纯CSS背景素材。
http://lea.verou.me/css3patterns/
==其他推荐==
如果您有其他优秀的样式库向我们推荐，请在本页面下留言或者发邮件到support@huiji.wiki告知我们！
{{Data Help
|页面名=帮助:CSS样式库
|描述文字=CSS样式库
|解说=
|symbol=
|主分类=帮助
|子分类=进阶
|tags=设计,编程,CSS
|sortkey=65
|关键=no
|catsortkey=3
|guide=no
|难度=进阶
|角色=设计者
|灰机功能=no
}}
