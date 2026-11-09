# 帮助:使用CSS变量

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3A%E4%BD%BF%E7%94%A8CSS%E5%8F%98%E9%87%8F
revid：42092 · 抓取时间：2026-11-09T14:27:10+08:00

---

{{编辑手册nav}}
在灰机，你可以为自己的站点编写CSS变量，使其能在之后的样式表（或style属性）中被重复使用，从而解决同一配色在样式表中出现多次产生的维护不便问题。

目前大多数主流浏览器均对CSS变量有良好支持。

灰机的[[帮助:主题编辑器|主题编辑器]]会将部分配色写入CSS变量，因而可以直接使用。

==用法==
使用<code>--*</code>语法声明一个变量。CSS变量遵从一般CSS属性的书写规范，因而必须位于一个选择器之下。

为了方便阅读，下文中使用gtr<strike>（即狗头人的缩写）</strike>作为变量前缀。
<pre>:root {
--gtr-white:#C0C0C0;
--gtr-border:2px solid #000000;
}</pre>
上述例子中在根元素下生成了两组变量，所有<code>:root</code>下的元素均可以使用这两个变量编写样式。
<pre>.avatarbox {
background-color:var(--gtr-white);
border:var(--gtr-border);
}</pre>
变量可以是CSS属性值的全部或一部分，但无法连同属性名称一同定义（即不支持mixin）。
<pre>.avatarbox2 {
border-left:4px solid var(--gtr-white);
}</pre>
===变量的继承===
前文中提到了CSS变量需要位于一个选择器之下，此时该变量可被此选择器的所有子元素继承。因此，我们建议尽可能在<code>:root</code>选择器下定义变量。
===变量的级联性===
如果同一个变量在不同的选择器内被定义，则实际使用时将根据级联关系的远近选择所应用的变量值。
<pre>:root {
--gtr-font:Arial;
}
.mono {
--gtr-font:Consolas;
}</pre>
在以上的例子中，对于一般元素引用<code>var(--gtr-font)</code>将输出Arial，而对于<code>class="mono"</code>的元素及其子元素引用则会输出Consolas。

===代码检查和代码高亮===
CSS编辑器会对变量的定义和使用报错。这是由于CodeEditor插件较旧导致的。此时正常提交即可，不影响变量功能的使用。

==使用主题编辑器配色==
主题编辑器配色会将所选颜色输出到CSS变量中。下表中列出了大部分变量的名称和在当前站点的颜色。

下表中初始值为false的变量一开始不会被定义。用户在主题编辑器里修改了相应颜色后，该变量即变为可用。

此外，并非所有的预设变量都由主题编辑器定义，也并非所有主题编辑器定义的变量都会成为CSS变量。

下表中最后一列“实时颜色”直接在style属性中引用了相应的CSS变量（<code>style="color:var(--main-base)"</code>）。将该表格复制到其他站点即可看到该站点中的配色。

{{mbox|type=delete|border=danger|text=灰机的mediawiki升级到1.38之后，在行内（style属性内）书写css变量会被认为不安全，因此下表的实时颜色一列处于失效状态。但是这不影响CSS变量在css文件中的使用。
}}

<table class="wikitable">
<tr><th>变量名</th><th>主题编辑器位置</th><th>说明</th><th>实时颜色</th></tr>
<tr><td>--main-base</td><td>快捷配色-主配色</td><td></td><td><span style='color:var(--main-base);font-weight:bold'>--main-base</span></td></tr>
<tr><td>--bg</td><td>快捷配色-辅配色-外部背景</td><td></td><td><span style='color:var(--bg);font-weight:bold'>--bg</span></td></tr>
<tr><td>--bg-inner</td><td>快捷配色-辅配色-内部背景</td><td></td><td><span style='color:var(--bg-inner);font-weight:bold'>--bg-inner</span></td></tr>
<tr><td>--a</td><td>快捷配色-链接颜色</td><td></td><td><span style='color:var(--a);font-weight:bold'>--a</span></td></tr>
<tr><td>--sub-bg</td><td>快捷配色-导航主色</td><td></td><td><span style='color:var(--sub-bg);font-weight:bold'>--sub-bg</span></td></tr>
<tr><td>--sub-a</td><td>快捷配色-导航辅色</td><td></td><td><span style='color:var(--sub-a);font-weight:bold'>--sub-a</span></td></tr>
<tr><td>--modal</td><td>快捷配色-模板色调</td><td></td><td><span style='color:var(--modal);font-weight:bold'>--modal</span></td></tr>
<tr><td>--brand-default</td><td>语义配色-无语义</td><td></td><td><span style='color:var(--brand-default);font-weight:bold'>--brand-default</span></td></tr>
<tr><td>--brand-primary</td><td>语义配色-主要</td><td></td><td><span style='color:var(--brand-primary);font-weight:bold'>--brand-primary</span></td></tr>
<tr><td>--brand-success</td><td>语义配色-成功</td><td></td><td><span style='color:var(--brand-success);font-weight:bold'>--brand-success</span></td></tr>
<tr><td>--brand-info</td><td>语义配色-信息</td><td></td><td><span style='color:var(--brand-info);font-weight:bold'>--brand-info</span></td></tr>
<tr><td>--brand-warning</td><td>语义配色-警示</td><td></td><td><span style='color:var(--brand-warning);font-weight:bold'>--brand-warning</span></td></tr>
<tr><td>--brand-danger</td><td>语义配色-危险</td><td></td><td><span style='color:var(--brand-danger);font-weight:bold'>--brand-danger</span></td></tr>
<tr><td>--detail-bg</td><td>区域细节-外部背景</td><td></td><td><span style='color:var(--detail-bg);font-weight:bold'>--detail-bg</span></td></tr>
<tr><td>--detail-inner-bg</td><td>区域细节-内部背景</td><td></td><td><span style='color:var(--detail-inner-bg);font-weight:bold'>--detail-inner-bg</span></td></tr>
<tr><td>--detail-color</td><td>文字细节-文字</td><td></td><td><span style='color:var(--detail-color);font-weight:bold'>--detail-color</span></td></tr>
<tr><td>--detail-h1</td><td>标题-H1</td><td>初始值false</td><td><span style='color:var(--detail-h1);font-weight:bold'>--detail-h1</span></td></tr>
<tr><td>--detail-h2</td><td>标题-H2</td><td>初始值false</td><td><span style='color:var(--detail-h2);font-weight:bold'>--detail-h2</span></td></tr>
<tr><td>--detail-h3</td><td>标题-H3</td><td>初始值false</td><td><span style='color:var(--detail-h3);font-weight:bold'>--detail-h3</span></td></tr>
<tr><td>--detail-h4</td><td>标题-H4</td><td>初始值false</td><td><span style='color:var(--detail-h4);font-weight:bold'>--detail-h4</span></td></tr>
<tr><td>--detail-h5</td><td>标题-H5</td><td>初始值false</td><td><span style='color:var(--detail-h5);font-weight:bold'>--detail-h5</span></td></tr>
<tr><td>--detail-a</td><td>文字细节-蓝链</td><td>初始值false</td><td><span style='color:var(--detail-a);font-weight:bold'>--detail-a</span></td></tr>
<tr><td>--detail-new</td><td>文字细节-红链</td><td>初始值false</td><td><span style='color:var(--detail-new);font-weight:bold'>--detail-new</span></td></tr>
<tr><td>--detail-border</td><td>文字细节-边框和分割线</td><td>初始值false</td><td><span style='color:var(--detail-border);font-weight:bold'>--detail-border</span></td></tr>
<tr><td>--detail-secondary</td><td>文字细节-辅助文字</td><td>初始值false</td><td><span style='color:var(--detail-secondary);font-weight:bold'>--detail-secondary</span></td></tr>
<tr><td>--detail-toc-a</td><td>文字细节-目录-未选中状态</td><td>初始值false</td><td><span style='color:var(--detail-toc-a);font-weight:bold'>--detail-toc-a</span></td></tr>
<tr><td>--detail-toc-a-hover</td><td>文字细节-目录-选中状态</td><td>初始值false</td><td><span style='color:var(--detail-toc-a-hover);font-weight:bold'>--detail-toc-a-hover</span></td></tr>
<tr><td>--detail-sub-bg</td><td>导航-背景</td><td>初始值false</td><td><span style='color:var(--detail-sub-bg);font-weight:bold'>--detail-sub-bg</span></td></tr>
<tr><td>--detail-sub-a</td><td>导航-文字</td><td>初始值false</td><td><span style='color:var(--detail-sub-a);font-weight:bold'>--detail-sub-a</span></td></tr>
<tr><td>--detail-sub-a-hover-bg</td><td>导航-文字选中</td><td>初始值false</td><td><span style='color:var(--detail-sub-a-hover-bg);font-weight:bold'>--detail-sub-a-hover-bg</span></td></tr>
<tr><td>--detail-sub-site-count</td><td>导航-统计文字颜色</td><td>初始值false</td><td><span style='color:var(--detail-sub-site-count);font-weight:bold'>--detail-sub-site-count</span></td></tr>
<tr><td>--detail-contentsub</td><td>文字细节-副标题</td><td>初始值false</td><td><span style='color:var(--detail-contentsub);font-weight:bold'>--detail-contentsub</span></td></tr>
<tr><td>--detail-bottom-bg</td><td>页面底部-背景</td><td>初始值false</td><td><span style='color:var(--detail-bottom-bg);font-weight:bold'>--detail-bottom-bg</span></td></tr>
<tr><td>--detail-bottom-color</td><td>页面底部-文字</td><td>初始值false</td><td><span style='color:var(--detail-bottom-color);font-weight:bold'>--detail-bottom-color</span></td></tr>
<tr><td>--detail-quote-bg</td><td>模板细节-quote-背景</td><td>初始值false</td><td><span style='color:var(--detail-quote-bg);font-weight:bold'>--detail-quote-bg</span></td></tr>
<tr><td>--detail-quote-color</td><td>模板细节-quote-文字</td><td>初始值false</td><td><span style='color:var(--detail-quote-color);font-weight:bold'>--detail-quote-color</span></td></tr>
<tr><td>--detail-quote-a</td><td>模板细节-quote-链接</td><td>初始值false</td><td><span style='color:var(--detail-quote-a);font-weight:bold'>--detail-quote-a</span></td></tr>
<tr><td>--detail-quote-border</td><td></td><td>不在主题编辑器中</td><td><span style='color:var(--detail-quote-border);font-weight:bold'>--detail-quote-border</span></td></tr>
<tr><td>--detail-wikitable-bg</td><td>表格-背景</td><td>初始值false</td><td><span style='color:var(--detail-wikitable-bg);font-weight:bold'>--detail-wikitable-bg</span></td></tr>
<tr><td>--detail-wikitable-color</td><td>表格-文字</td><td>初始值false</td><td><span style='color:var(--detail-wikitable-color);font-weight:bold'>--detail-wikitable-color</span></td></tr>
<tr><td>--detail-wikitable-a</td><td>表格-链接</td><td>初始值false</td><td><span style='color:var(--detail-wikitable-a);font-weight:bold'>--detail-wikitable-a</span></td></tr>
<tr><td>--detail-wikitable-border</td><td>表格-边框</td><td>初始值false</td><td><span style='color:var(--detail-wikitable-border);font-weight:bold'>--detail-wikitable-border</span></td></tr>
<tr><td>--detail-infobox-bg</td><td>模板细节-infobox-背景</td><td>初始值false</td><td><span style='color:var(--detail-infobox-bg);font-weight:bold'>--detail-infobox-bg</span></td></tr>
<tr><td>--detail-infobox-color</td><td>模板细节-infobox-文字</td><td>初始值false</td><td><span style='color:var(--detail-infobox-color);font-weight:bold'>--detail-infobox-color</span></td></tr>
<tr><td>--detail-infobox-a</td><td>模板细节-infobox-链接</td><td>初始值false</td><td><span style='color:var(--detail-infobox-a);font-weight:bold'>--detail-infobox-a</span></td></tr>
<tr><td>--detail-infobox-border</td><td>模板细节-infobox-边框</td><td>初始值false</td><td><span style='color:var(--detail-infobox-border);font-weight:bold'>--detail-infobox-border</span></td></tr>
<tr><td>--detail-infobox-title-bg</td><td>模板细节-infobox-title-背景</td><td>初始值false</td><td><span style='color:var(--detail-infobox-title-bg);font-weight:bold'>--detail-infobox-title-bg</span></td></tr>
<tr><td>--detail-infobox-title-color</td><td>模板细节-infobox-title-文字</td><td>初始值false</td><td><span style='color:var(--detail-infobox-title-color);font-weight:bold'>--detail-infobox-title-color</span></td></tr>
<tr><td>--detail-infobox-item-title-bg</td><td>模板细节-infobox-header-背景</td><td>初始值false</td><td><span style='color:var(--detail-infobox-item-title-bg);font-weight:bold'>--detail-infobox-item-title-bg</span></td></tr>
<tr><td>--detail-infobox-item-title-color</td><td>模板细节-infobox-header-文字</td><td>初始值false</td><td><span style='color:var(--detail-infobox-item-title-color);font-weight:bold'>--detail-infobox-item-title-color</span></td></tr>
<tr><td>--detail-infobox-item-label-bg</td><td>模板细节-infobox-label-背景</td><td>初始值false</td><td><span style='color:var(--detail-infobox-item-label-bg);font-weight:bold'>--detail-infobox-item-label-bg</span></td></tr>
<tr><td>--detail-infobox-item-label-color</td><td>模板细节-infobox-label-文字</td><td>初始值false</td><td><span style='color:var(--detail-infobox-item-label-color);font-weight:bold'>--detail-infobox-item-label-color</span></td></tr>
<tr><td>--detail-infobox-item-label-a</td><td>模板细节-infobox-label-链接</td><td>初始值false</td><td><span style='color:var(--detail-infobox-item-label-a);font-weight:bold'>--detail-infobox-item-label-a</span></td></tr>
<tr><td>--detail-infobox-item-label-border</td><td>模板细节-infobox-label-边框</td><td>初始值false</td><td><span style='color:var(--detail-infobox-item-label-border);font-weight:bold'>--detail-infobox-item-label-border</span></td></tr>
<tr><td>--detail-infobox-item-detail-bg</td><td></td><td>不在主题编辑器中</td><td><span style='color:var(--detail-infobox-item-detail-bg);font-weight:bold'>--detail-infobox-item-detail-bg</span></td></tr>
<tr><td>--detail-infobox-item-detail-color</td><td></td><td>不在主题编辑器中</td><td><span style='color:var(--detail-infobox-item-detail-color);font-weight:bold'>--detail-infobox-item-detail-color</span></td></tr>
<tr><td>--detail-infobox-item-detail-a</td><td></td><td>不在主题编辑器中</td><td><span style='color:var(--detail-infobox-item-detail-a);font-weight:bold'>--detail-infobox-item-detail-a</span></td></tr>
<tr><td>--detail-infobox-item-detail-border</td><td></td><td>不在主题编辑器中</td><td><span style='color:var(--detail-infobox-item-detail-border);font-weight:bold'>--detail-infobox-item-detail-border</span></td></tr>
<tr><td>--detail-navbox-bg</td><td>模板细节-navbox-背景</td><td>初始值false</td><td><span style='color:var(--detail-navbox-bg);font-weight:bold'>--detail-navbox-bg</span></td></tr>
<tr><td>--detail-navbox-color</td><td>模板细节-navbox-文字</td><td>初始值false</td><td><span style='color:var(--detail-navbox-color);font-weight:bold'>--detail-navbox-color</span></td></tr>
<tr><td>--detail-navbox-a</td><td>模板细节-navbox-链接</td><td>初始值false</td><td><span style='color:var(--detail-navbox-a);font-weight:bold'>--detail-navbox-a</span></td></tr>
<tr><td>--detail-navbox-title-bg</td><td>模板细节-navbox-title-背景</td><td>初始值false</td><td><span style='color:var(--detail-navbox-title-bg);font-weight:bold'>--detail-navbox-title-bg</span></td></tr>
<tr><td>--detail-navbox-title-color</td><td>模板细节-navbox-title-文字</td><td>初始值false</td><td><span style='color:var(--detail-navbox-title-color);font-weight:bold'>--detail-navbox-title-color</span></td></tr>
<tr><td>--detail-navbox-title-a</td><td>模板细节-navbox-title-链接</td><td>初始值false</td><td><span style='color:var(--detail-navbox-title-a);font-weight:bold'>--detail-navbox-title-a</span></td></tr>
<tr><td>--detail-navbox-group-bg</td><td>模板细节-navbox-group-背景</td><td>初始值false</td><td><span style='color:var(--detail-navbox-group-bg);font-weight:bold'>--detail-navbox-group-bg</span></td></tr>
<tr><td>--detail-navbox-group-color</td><td>模板细节-navbox-group-文字</td><td>初始值false</td><td><span style='color:var(--detail-navbox-group-color);font-weight:bold'>--detail-navbox-group-color</span></td></tr>
<tr><td>--detail-navbox-group-a</td><td>模板细节-navbox-group-链接</td><td>初始值false</td><td><span style='color:var(--detail-navbox-group-a);font-weight:bold'>--detail-navbox-group-a</span></td></tr>
<tr><td>--detail-navbox-list-bg</td><td>模板细节-navbox-list-背景</td><td>初始值false</td><td><span style='color:var(--detail-navbox-list-bg);font-weight:bold'>--detail-navbox-list-bg</span></td></tr>
<tr><td>--detail-navbox-list-color</td><td>模板细节-navbox-list-文字</td><td>初始值false</td><td><span style='color:var(--detail-navbox-list-color);font-weight:bold'>--detail-navbox-list-color</span></td></tr>
<tr><td>--detail-navbox-list-a</td><td>模板细节-navbox-list-链接（活链）</td><td>初始值false</td><td><span style='color:var(--detail-navbox-list-a);font-weight:bold'>--detail-navbox-list-a</span></td></tr>
<tr><td>--detail-navbox-list-new</td><td>模板细节-navbox-list-链接（死链）</td><td>初始值false</td><td><span style='color:var(--detail-navbox-list-new);font-weight:bold'>--detail-navbox-list-new</span></td></tr>
<tr><td>--detail-navbox-list-odd-bg</td><td>模板细节-navbox-list-奇数背景</td><td>初始值false</td><td><span style='color:var(--detail-navbox-list-odd-bg);font-weight:bold'>--detail-navbox-list-odd-bg</span></td></tr>
<tr><td>--detail-navbox-list-even-bg</td><td>模板细节-navbox-list-偶数背景</td><td>初始值false</td><td><span style='color:var(--detail-navbox-list-even-bg);font-weight:bold'>--detail-navbox-list-even-bg</span></td></tr>
<tr><td>--detail-navbox-abovebelow-bg</td><td>模板细节-navbox-abovebelow-背景</td><td>初始值false</td><td><span style='color:var(--detail-navbox-abovebelow-bg);font-weight:bold'>--detail-navbox-abovebelow-bg</span></td></tr>
<tr><td>--detail-navbox-abovebelow-color</td><td>模板细节-navbox-abovebelow-文字</td><td>初始值false</td><td><span style='color:var(--detail-navbox-abovebelow-color);font-weight:bold'>--detail-navbox-abovebelow-color</span></td></tr>
<tr><td>--detail-navbox-abovebelow-a</td><td>模板细节-navbox-abovebelow-链接</td><td>初始值false</td><td><span style='color:var(--detail-navbox-abovebelow-a);font-weight:bold'>--detail-navbox-abovebelow-a</span></td></tr>
</table>

==相关技巧==
*变量可以反过来在style属性中声明，在样式表中引用，从而让页面来控制样式表中的特定属性。实际效果是一样的，但是有时候能玩儿出花来。
*变量值可以不受CSS属性的取值限制。例如可以声明一个整数值，引用时通过CSS<code>calc()</code>函数更改为所需单位。
**例如声明<code>--intvar</code>为50，实际使用时写<code>width:calc(1px * var(--intvar))</code>来获取50px的宽度样式。
**访问[https://developer.mozilla.org/zh-CN/docs/Web/CSS/calc 这里]获取关于calc()函数的文档。
==相关资料==
*[https://developer.mozilla.org/zh-CN/docs/Web/CSS/Using_CSS_custom_properties MDN:使用CSS变量]
*灰机workshop上有[[templatemanager:Manifest:Tbui-color|一个现成的CSS变量调色板]]可供使用。
{{Data Help
|页面名=帮助:使用CSS变量
|描述文字=使用CSS变量
|解说=
|symbol=
|主分类=帮助
|子分类=进阶
|tags=编程,维基化,设计,CSS
|sortkey=63
|关键=no
|catsortkey=3
|guide=no
|难度=进阶
|角色=设计者
|灰机功能=no
}}
