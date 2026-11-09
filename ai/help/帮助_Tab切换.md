# 帮助:Tab切换

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3ATab%E5%88%87%E6%8D%A2
revid：41762 · 抓取时间：2026-11-09T14:27:10+08:00

---

Tab是wiki中常见的内容折叠收纳方式，这里罗列出灰机wiki支持的tab实现方法
{{编辑手册nav}}

==Tab==
{{Deprecate|2.1.0}}
{{Alternative|templatemanager:Manifest:实用组件集|实用组件集}}
{{HuijiOnly}}
[[File:tab效果.jpg|right|thumb|效果图]]
* 代码:<code><nowiki><tab></nowiki></code>。
* 作用：用于添加多页的标签。
* 示例：<br><code><nowiki>
<tab></nowiki><br /><nowiki>
tab1|一些内容</nowiki><br /><nowiki>
tab2|另一些内容</nowiki><br /><nowiki>
</tab></nowiki><br /><nowiki>
</nowiki></code>
* 效果：[[帮助:解析器扩展标签/Tab|点此查看]]
* 参数：
<div class="table-responsive">
{| class="sortable table table-striped table-bordered"
|-
! 参数 !! 类型 !! 默认值 !! 描述 
|-
| class || class || nav-tabs || 可选值为nav-tabs nav-pills nav-stacked nav-justified
|}
</div>
* 值：每一个tab应该都在一行。形如：<code>tab的名字|tab的内容</code>。其中tab的内容可以是模板。'''请注意：'''这里的模板是没有参数的模板；如果模板带有参数，建议在其外面套上一个没有参数的模板/页面，然后将外面的的模板/页面放入tab的内容。


==零件：简易自定义过滤器==
:安装地址：'''[[templatemanager:Manifest:简易自定义过滤器|简易自定义过滤器]]'''（by [[user:Yuee]]）
[[File:简易自定义过滤器配图3.png|thumb|right|自定义过滤器效果图]]

==零件：Tabber ==
:安装地址：'''[[templatemanager:Manifest:Tabber|Tabber]]'''（by [[user:Yuee]]）
本零件是[[templatemanager:Manifest:简易自定义过滤器|简易自定义过滤器]]的升级版，包含简易自定义过滤器的功能，并且与其使用了不同的class，所以可以共存。

*零件共有三个工作模式，三个模式之间没有任何实际上的关联，一旦决定好工作模式，就会按照对应的逻辑进行执行
*本脚本只使用class和ID作为选择器，不会用到HTML元素作为选择器，所以原则上所有HTML元素都可以作为操作对象
*所有class均为选择器使用，没有配置任何样式，请自行根据需要补充样式
*模式1和模式2，在异步加载内容的等待期间，使用了以下内容作为loading占位，可以通过样式为其设定一张loading图，如果有开发者权限的话也可以自行修改内容
<pre><div class="tabber-loading-block" style="min-height: 140px;text-align: center;"><div class="tabber-loading" style="margin-top:40px;"></div></div></pre>

===模式0===
'''模式0为默认模式'''

该模式下，需要事先在页面中生成切换内容，零件只根据条件控制各元素是否显示

本模式与[[templatemanager:Manifest:简易自定义过滤器|简易自定义过滤器]]完全相同，区别只在检测的class名称不一样

详细文档请参考[[templatemanager:Manifest:Tabber/mode0|模式0详细说明]]

'''效果'''：
<div class="tabber">
	<div class="tabber-filter">
		<div class="tabber-filter-item selected" data-type="test" data-test="1" style="display: inline-block;background: #efb1b1;padding: 1px 5px;margin-right: 3px;cursor: pointer;">选项1</div>
		<div class="tabber-filter-item" data-type="test" data-test="2" style="display: inline-block;background: #b1efcd;padding: 1px 5px;margin-right: 3px;cursor: pointer;">选项2</div>
		<div class="tabber-filter-item" data-type="test" data-test="3" style="display: inline-block;background: #b1bbef;padding: 1px 5px;margin-right: 3px;cursor: pointer;">选项3</div>
	</div>
	<div class="tabber-item" data-test="1" style="background: #efb1b1;width: 200px;height: 50px;padding: 2px 5px;">选项1的内容</div>
	<div class="tabber-item" data-test="2" style="background: #b1efcd;width: 200px;height: 50px;padding: 2px 5px;">选项2的内容</div>
	<div class="tabber-item" data-test="3" style="background: #b1bbef;width: 200px;height: 50px;padding: 2px 5px;">选项3的内容</div>
</div>

'''代码'''：
<pre>
<div class="tabber">
	<div class="tabber-filter">
		<div class="tabber-filter-item selected" data-type="test" data-test="1" style="display: inline-block;background: #efb1b1;padding: 1px 5px;margin-right: 3px;cursor: pointer;">选项1</div>
		<div class="tabber-filter-item" data-type="test" data-test="2" style="display: inline-block;background: #b1efcd;padding: 1px 5px;margin-right: 3px;cursor: pointer;">选项2</div>
		<div class="tabber-filter-item" data-type="test" data-test="3" style="display: inline-block;background: #b1bbef;padding: 1px 5px;margin-right: 3px;cursor: pointer;">选项3</div>
	</div>
	<div class="tabber-item" data-test="1" style="background: #efb1b1;width: 200px;height: 50px;padding: 2px 5px;">选项1的内容</div>
	<div class="tabber-item" data-test="2" style="background: #b1efcd;width: 200px;height: 50px;padding: 2px 5px;">选项2的内容</div>
	<div class="tabber-item" data-test="3" style="background: #b1bbef;width: 200px;height: 50px;padding: 2px 5px;">选项3的内容</div>
</div>
</pre>

===模式1===
模式1在用户交互的感受上，与模式0相同（通过切换过滤器显示不同内容）

区别在于，模式0的内容需要提前渲染在页面中，而模式1是通过API异步解析模板或是读取页面来加载内容

例如下面的例子中
*在class=tabber的元素上，指定了data-mode=1表示使用模式1，指定了data-template=TabberTest表示解析[[templatemanager:模板:TabberTest]]的内容，指定了data-param="a=共用文字"作为参数
*在每个选择器（tabber-filter-item）子项中，指定了data-param作为参数
*执行时会将tabber的param和每个filter中被选中项目的param连在一起，例如点击“选项1”后，会通过API请求解析'''<nowiki>{{TabberTest|a=共用文字|选项1|你好|c=efb1b1}}</nowiki>'''这个模板，并将结果内容更新到tabber的子元素tabber-content中
*选项3则指向了一个页面，会异步将这个页面的内容加载过来

详细文档请参考[[templatemanager:Manifest:Tabber/mode1|模式1详细说明]]

'''效果'''：
<div class="tabber" data-mode="1" data-template="TabberTest" data-param="a=共用文字" data-pagename="Manifest:Tabber/doc"><!-- 源代码中的data-pagename="Manifest:Tabber/doc"是因为解析模板时会使用当前页面名来解析，但Manifest这个命名空间不支持解析模板，会报错，所以手工指定了别的页面名，一般使用时不需要加此参数-->
	<div class="tabber-filter">
		<div class="tabber-filter-item selected" data-param="选项1|你好|c=efb1b1" style="display: inline-block;background: #efb1b1;padding: 1px 5px;margin-right: 3px;cursor: pointer;">选项1</div>
		<div class="tabber-filter-item" data-param="选项2|我好|c=b1efcd" style="display: inline-block;background: #b1efcd;padding: 1px 5px;margin-right: 3px;cursor: pointer;">选项2</div>
		<div class="tabber-filter-item" data-page="Manifest:Tabber/测试页" style="display: inline-block;background: #b1bbef;padding: 1px 5px;margin-right: 3px;cursor: pointer;">选项3</div>
	</div>
	<div class="tabber-content"></div>
</div>

'''代码'''：
<pre>
<div class="tabber" data-mode="1" data-template="TabberTest" data-param="a=共用文字">
	<div class="tabber-filter">
		<div class="tabber-filter-item selected" data-param="选项1|你好|c=efb1b1" style="display: inline-block;background: #efb1b1;padding: 1px 5px;margin-right: 3px;cursor: pointer;">选项1</div>
		<div class="tabber-filter-item" data-param="选项2|我好|c=b1efcd" style="display: inline-block;background: #b1efcd;padding: 1px 5px;margin-right: 3px;cursor: pointer;">选项2</div>
		<div class="tabber-filter-item" data-page="Manifest:Tabber/测试页" style="display: inline-block;background: #b1bbef;padding: 1px 5px;margin-right: 3px;cursor: pointer;">选项3</div>
	</div>
	<div class="tabber-content"></div>
</div>
</pre>

'''调用的模板内容'''：
<pre>
<div style="background: #{{{c}}};width: 200px;padding: 2px 5px;">这是TabberTest，内容
*{{{1|第1个参数的内容}}}
*{{{2|第2个参数的内容}}}
*{{{a|参数a的内容}}}
</div>
</pre>

'''调用的页面'''：
[[templatemanager:Manifest:Tabber/测试页]]

===模式2===
模式2是一个简化版的模式1，通过异步解析模板或是读取页面来加载内容，显示元素中

该模式主要用来将页面中的一部分内容改为异步加载，来减轻页面的渲染压力

该内容会在脚本加载后，就自动执行进行解析

详细文档请参考[[templatemanager:Manifest:Tabber/mode2|模式2详细说明]]

'''效果'''：
<div class="tabber" data-mode="2" data-template="TabberTest" data-param="自动加载|异步|c=fba030" data-pagename="Manifest:Tabber/doc"></div><!-- 源代码中的data-pagename="Manifest:Tabber/doc"是因为解析模板时会使用当前页面名来解析，但Manifest这个命名空间不支持解析模板，会报错，所以手工指定了别的页面名，一般使用时不需要加此参数-->
'''代码'''：
<pre>
<div class="tabber" data-mode="2" data-template="TabberTest" data-param="自动加载|异步|c=fba030"></div>
</pre>

==零件：RichTab==
{{templatemanager:危险模板}}
:安装地址：'''[[templatemanager:Manifest:RichTab|RichTab]]'''（by [[user:honestleaf]]）
===相关说明===
* 与原生<code><nowiki><tab></nowiki></code>相比，RichTab的优点在于可以使用wikitext或模板等较为复杂的内容作为分页标题和内容。
* 分页标题和内容必须依照顺序成对出现，如果其中一项为空则这一组标题和内容都会被略去。
* 由于零件使用了灰机的html功能，在可视化编辑器中可能会出现渲染异常，这个问题有待修正

===示例===
<pre>
{{RichTab
|[[File:中国.png|150px|link=]]
|中国
|[[File:美国.png|150px|link=]]
|美国
|[[File:日本.png|150px|link=]]
|日本
|class=nav-pills
}}</pre>

==另行参见==
*[[h:help:搜索器与检索工具|搜索器与检索工具]]
*[[h:帮助:折叠|折叠]]
