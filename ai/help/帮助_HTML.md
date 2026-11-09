# 帮助:HTML

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3AHTML
revid：39552 · 抓取时间：2026-11-09T14:27:09+08:00

---

{{编辑手册nav}}
要使用HTML代码，无需额外处理，直接输入HTML标记即可。
==HTML与CSS基础==
我们强烈推荐您前往以下页面进行基础学习：
*[https://www.w3schools.com/ W3school]
**[http://www.w3school.com.cn/css/css_index.asp CSS基础教程]
**[http://www.w3school.com.cn/cssref/index.asp CSS手册]
**[http://www.w3school.com.cn/html/index.asp HTML基础教程]
*[[css:首页|灰机CSS维基]]
另请参见：[[h:帮助:站点CSS编辑|站点CSS编辑]]

==HTML与CSS的嵌入==
在灰机和其他mediawiki搭建的站点中，您可以通过如下几种手段自定义css
*<s>页面层：使用<code><nowiki>{{#css:}}</nowiki></code>解析器函数</s>&nbsp;已过时，不再支持
*站点层：通过<code>Mediawiki:CSS</code>页面来添加css样式表（需要[[帮助:用户权限|管理员]]权限）

==灰机允许使用的HTML元素==
灰机继承了MediaWiki支持的html元素，总体来说除了<a>标签之外大部分的CSS、CSS3效果您都可以直接在本站使用。
以下是明显被支持的HTML元素（除此之外的元素，尤其是CSS3标准的您可以自行在沙盒测试）：
{{clear}}
{| class="wikitable"
|-
! HTML元素
! 作用
! 您所看到的
! 您所输入的
|-
| <pre><big></pre>
| 文字字号加一
| 正常大小 <big>字号加一</big>
| 
<pre>
<big>示例</big>
</pre>
|-
| <pre><blockquote></pre>
| 块状引用文本
| <blockquote>这次需要长一点的示例</blockquote>
| <pre><blockquote>这次需要长一点的示例</blockquote></pre>
|-
|<pre><br></pre>
| 另起一行
| 这次需要<br>
长一点的<br>
示例
|
<pre>
这次需要<br>
长一点的<br>
示例
</pre>
|-
| <pre><center></pre>
| 文字居中
| <center>示例</center>
| <pre><center>示例</center></pre>
|-
| <pre><font></pre>
| 定义文字的大小、颜色和字体
|
默认字样<br>
<font size="150%">文字大小</font><br>
<font color="red">文字颜色1</font><br>
<font color="#0000ff">文字颜色2</font><br>
<font face="楷体">文字字体</font>
|
<pre>
默认字样
<font size="150%">文字大小</font>
<font color="red">文字颜色1</font>
<font color="#0000ff">文字颜色2</font>
<font face="楷体">文字字体</font>
</pre>
|-
| <pre><h1><h2><h3><h4><h5><h6></pre>
| 标题1到标题6字体逐次减小
|
<h1>标题1</h1><br>
<h2>标题2</h2><br>
<h3>标题3</h3><br>
<h4>标题4</h4><br>
<h5>标题5</h5><br>
<h6>标题6</h6><br>
|
<pre>
<h1>标题1</h1><br>
<h2>标题2</h2><br>
<h3>标题3</h3><br>
<h4>标题4</h4><br>
<h5>标题5</h5><br>
<h6>标题6</h6><br>
</pre>
|-
| <pre><p></pre>
| 定义一个内文段落
|
|
|-
| <pre><pre></pre>
| 显示源代码
| 
|
|-
| <pre><small></pre>
| 文字字号减一
| 正常大小 <small>字号减一</small>
|
<pre>
<small>示例</small>
</pre>
|-
| <pre><strike>或<del></pre>
| 给文字添加删除线
| 
<strike>示例</strike><br>
<del>示例</del>
| 
<pre>
<strike>示例</strike>
<del>示例</del>
</pre>
|-
| <pre><strong></pre>
| 文字加粗
| <strong>示例</strong>
| 
<pre>
<strong>示例</strong>
</pre>
|-
| <pre><sub></pre>
| 给文字添加下角标
| 灰机<sub>示例</sub>
|
<pre>
灰机<sub>示例</sub>
</pre>
|-
| <pre><sup></pre>
| 给文字添加上角标
| 灰机<sup>示例</sup>
|
<pre>
灰机<sup>示例</sup>
</pre>
|-
| <pre><table></pre>
| 定义表格
|
|
|-
| <pre><u></pre>
| 给文字添加下划线
| <u>示例</u>
| 
<pre>
<u>示例</u>
</pre>
|-
| <pre><tt></pre>
| typewriter字体
| 
default font <br>
<tt>typewriter font</tt>
|
<pre>
default font 
<tt>typewriter font</tt>
</pre>
|-
|<pre><!-- ... --></pre>
| 给其他编辑者的注释，<br>
仅在编辑页面可见
| 
本维基由灰机粉丝共同维护
<!-- 此处还可以留下QQ群，微博等信息 -->
| 
<pre>
本维基由灰机粉丝共同维护

<!-- 此处还可以留下QQ群，微博等信息 -->
</pre>
|-
| <pre><div></pre>
| 定义网页文件的一个区块，让多组文字用同一格式显示。
|  <div style="color:#09c; text-align:center; font-family:宋体; font-size:small">
这组字体都是天蓝色，
居中，
宋体，
小号字体的样式。
</div>
|
<pre>
<div style="color:#09c; text-align:center; 
font-family:宋体; font-size:small">
这组字体都是天蓝色，
居中，
宋体，
小号字体的样式。
</div>
</pre>
|-
|}
==预设类==
预设类指的是集成在灰机皮肤样式表内预定义好样式的“类”（class），可以在页面上直接引用生效，而无需在common.css中定义。
*语法：<code>class="<预设1> <预设2>"</code>
*在本地common.css可以补充样式，重合部分本地优先级更高，会覆盖皮肤中的预设值。
{| class="wikitable"
|-
! 预设类 !! 解释说明 !! 示例代码 !! 效果
|-
| style="width:200px"| <code>well</code> || 内容容器 || <pre><div class="well">示例</div></pre>|| <div class="well">示例</div>
|-
| <code>darken/lighten</code> || 内容容器 || <pre><div class="darken">示例</div></pre>|| <div class="darken">示例</div>
|-
| <code>bg-<语义颜色></code> || 为元素指定背景色 || <pre><div class="bg-primary">示例</div></pre><pre><div class="bg-info">示例</div></pre><pre><div class="bg-success">示例</div></pre><pre><div class="bg-warning">示例</div></pre><pre><div class="bg-danger">示例</div></pre> || <div class="bg-primary">示例</div><div class="bg-info">示例</div><div class="bg-success">示例</div><div class="bg-warning">示例</div><div class="bg-danger">示例</div>
|-
| <code>text-<语义颜色></code> || 为元素指定文字颜色 || <pre><div class="text-primary">示例</div></pre><pre><div class="text-info">示例</div></pre><pre><div class="text-success">示例</div></pre><pre><div class="text-warning">示例</div></pre><pre><div class="text-danger">示例</div></pre> || <div class="text-primary">示例</div><div class="text-info">示例</div><div class="text-success">示例</div><div class="text-warning">示例</div><div class="text-danger">示例</div>
|-
| <code>border-<语义颜色></code> || 为元素指定边框颜色 || <pre><div class="border-primary" style="border-style:solid;border-width:2px;">示例</div></pre><pre><div class="border-info" style="border-style:solid;border-width:2px;>示例</div></pre><pre><div class="border-success" style="border-style:solid;border-width:2px;>示例</div></pre><pre><div class="border-warning" style="border-style:solid;border-width:2px;>示例</div></pre><pre><div class="border-danger" style="border-style:solid;border-width:2px;>示例</div></pre> || <div class="border-primary" style="border-style:solid;border-width:2px;>示例</div><div class="border-info" style="border-style:solid;border-width:2px;>示例</div><div class="border-success" style="border-style:solid;border-width:2px;>示例</div><div class="border-warning" style="border-style:solid;border-width:2px;>示例</div><div class="border-danger" style="border-style:solid;border-width:2px;>示例</div>
|-
| <code>wikitable</code> || 使表格带有默认的维基表格样式（自动插入表格默认带有此类） || 参考本表格 || 参考本表格
|-
| <code>table</code> || 使表格带有bootstrap的表格样式 || <pre><table class="table"><tr><th>th</th><td>td</td></tr></table></pre> || <table class="table"><tr><th>th</th><td>td</td></tr></table>
|-
| <code>table-striped</code> || 使表格带有条纹样式，可以和wikitable\table同时使用|| <pre><table class="table table-striped"><tr><th>th</th></tr><tr><td>td</td></tr></table></pre> || <table class="table table-striped"><tr><th>th</th></tr><tr><td>td</td></tr></table>
|-
| <code>table-hover</code> || 使表格带有hover效果，可以和wikitable\table同时使用|| <pre><table class="table table-hover"><tr><th>th</th></tr><tr><td>td</td></tr></table></pre> || <table class="table table-hover"><tr><th>th</th></tr><tr><td>td</td></tr></table>
|-
| <code>hidden-<屏幕尺寸></code> || 使元素在预设的屏幕尺寸上被隐藏（display:none）<br>可选项：hidden-lg/hidden-md/hidden-sm/hidden-xs|| <pre><div class="hidden-xs">123</div></pre> || <div class="hidden-xs">123</div>
|-
| <code>visible-<屏幕尺寸>-block</code><br><code>visible-<屏幕尺寸>-inline</code><br><code>visible-<屏幕尺寸>-inline-block</code>  || 使元素在预设的屏幕尺寸上被显示<br>同样有可选项<ref>[http://v3.bootcss.com/css/#responsive-utilities BOOTSTRAP3 文档]</ref>：visible-lg-*/visible-md-*/visible-sm-*/visible-xs-*|| <pre><div class="visible-xs-block">123</div></pre> || <div class="visible-xs-block">123</div>
|-
|<code>badge</code> || 使元素带有bootstrap默认的badge样式|| <pre><div class="badge bg-primary">123</div></pre> || <div class="badge bg-primary">123</div>
|-
|<code>label</code> || 使元素带有bootstrap默认的label样式|| <pre><div class="label bg-primary">123</div></pre> || <div class="label bg-primary">123</div>
|-
|<code>btn</code> || 使元素带有bootstrap默认的btn样式|| <pre><div class="btn bg-primary">123</div></pre> || <div class="btn bg-primary">123</div>
|}
除此之外大部分的bootstrap3预设类均可以在灰机直接引用，在此不再一一赘述，可以参考bootstrap3的文档：'''[[help:BOOTSTRAP|BOOTSTRAP]]'''
===通过零件封装类===
通过灰机的workshop功能,对于一些常见的样式功能,可以封装成为零件并发布,供其他使用者一键导入到本站
*[[help:灰机workshop]]

==HTML模板与Mustache==
参见'''[[帮助:Mustache模板]]'''
==引用==
{{Reflist|2}}
{{Data Help
|页面名=帮助:HTML
|描述文字=在维基使用HTML
|解说=
|symbol=<i class="fa fa-html5" aria-hidden="true"></i>
|主分类=帮助
|子分类=进阶
|tags=HTML,编程
|sortkey=47
|关键=no
|catsortkey=3
|guide=no
|难度=进阶
|角色=模板制作
|灰机功能=no
}}
