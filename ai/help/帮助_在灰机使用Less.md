# 帮助:在灰机使用Less

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3A%E5%9C%A8%E7%81%B0%E6%9C%BA%E4%BD%BF%E7%94%A8Less
revid：41550 · 抓取时间：2026-11-09T14:27:10+08:00

---

{{编辑手册nav2}}
{{Data Help
|页面名=帮助:在灰机使用Less
|描述文字=使用Less语法编辑灰机样式。
|解说=
|symbol=<i class="fa fa-css3" aria-hidden="true"></i>
|主分类=帮助
|子分类=进阶
|tags=编程,维基化,设计,CSS
|sortkey=255
|关键=no
|catsortkey=1
|guide=no
|难度=进阶
|角色=设计者
|灰机功能=yes
}}

从2022年7月26日开始，你可以通过安装[[templatemanager:manifest:huijiLesser|HuijiLesser]]零件来使用less语法为站点编辑样式。

其他文档：
*[[/简明教程|简明语法教程]]
*[[/（基本上）完整的文档|（基本上）完整的文档]]
*[[/Less函数列表|函数列表]]

==灰机皮肤更新==
从2022年9月26日开始，具有开发者权限、且相应站点已安装[[templatemanager:manifest:huijiLesser|HuijiLesser]]的用户可以直接从左边栏唤起huijiLesser。

==简介==
Less是一种需要预处理的CSS语法。

===与CSS的差异===
*Less无法在浏览器中直接运行。在HuijiLesser零件中，Less样式会被编译为CSS样式然后提交到零件（或是临时插入到当前页面）。
*Less支持双斜杠单行注释（<code>// 单行注释</code>）和块注释语法（<code>/* 多行注释 */</code>）

===与SASS的差异===
*具体说，与SCSS的差异不大。如果你能熟练地写SCSS，那使用less就完全没难度。
===HuijiLesser与less.js的差异===
*由于运作方式原因，HuijiLesser不支持<code>@import</code>语法。
*HuijiLesser的less编译器版本为<code>4.1.3</code>，该版本号会在你查询less官方文档时用到。

==Less特性==
===嵌套===
在CSS中，我们通常需要反复书写嵌套元素的选择器。该方法非常不利于维护。但在less中源生支持嵌套功能。例如：
<pre>
/* less */
.content-entry {
    display:block;
    >.content-entry-title {font-weight:bold;}
    a {color:red}
}
/* 编译结果 */
.content-entry {
  display: block;
}
.content-entry > .content-entry-title {
  font-weight: bold;
}
.content-entry a {
  color: red;
}
</pre>
嵌套中支持多数CSS选择器。另外，Less支持一个“父选择器”的符号<code>&</code>。

“父选择器”代表的是从根选择器到当前选择器的选择器链。因此该符号可以加在新选择器的前面或后面，或在该选择器上扩展其他选择器。

示例如下：
<pre>
/* less */
.buttongroup {
  .buttonlink {
    background:#333;
    &.primary { // 添加同级的class选择器
      background:red;
    }
    &:hover { // 添加同级伪类
      background:#666;
    }
    &-nobg { // 变更选择器（即将buttonlink变为buttonlink-nobg）
      background:transparent;
    }
    .quote & { // 在选择器链前加.quote
      background:unset;
    }
  }
}

/* 编译结果 */

.buttongroup .buttonlink {
  background: #333;
}
.buttongroup .buttonlink.primary {
  background: red;
}
.buttongroup .buttonlink:hover {
  background: #666;
}
.buttongroup .buttonlink-nobg {
  background: transparent;
}
.quote .buttongroup .buttonlink {
  background: unset;
}
</pre>

===变量===
和[[帮助:使用CSS变量|CSS变量]]类似，Less也有自己的变量定义。不同之处在于，Less变量将会在编译后消失，从而无法被其他less项目（及其他CSS）使用。例如：
<pre>
/* less */
@main-color:#333;
#huiji-body {
    color:@main-color;
}
/* 编译结果 */
#huiji-body {
  color: #333;
}
</pre>
在多数情况下，我们不建议使用Less变量语法，而建议使用[[帮助:使用CSS变量|CSS变量]]代替。但请注意，CSS变量无法参与less函数和运算功能。

===混入(mixin)===
可以将另一个选择器中的所有样式混入当前选择器。例如：
<pre>
/* less */
.button-default {
    display:inline-block;
    padding:12px 6px;
    color:#FFF;
    background-color:#333;
}
.button-primary {
    .button-default();
    background-color:#FF5B00;
    font-weight:bold;
}
/* 编译结果 */
.button-default {
  display: inline-block;
  padding: 12px 6px;
  color: #FFF;
  background-color: #333;
}
.button-primary {
  display: inline-block;
  padding: 12px 6px;
  color: #FFF;
  background-color: #333;
  background-color: #FF5B00;
  font-weight: bold;
}
</pre>
===@规则的嵌套===
在Css中，@规则通常需要写在样式表的顶层，这样对于嵌套深层的元素很难维护（需要完整写一遍选择器路径）。在Less中可以使用类似选择器的方式使用@规则。例如：
<pre>
/* less */
.container {
    width:720px;
    .component {
      width:320px;
      font-size:14px;
      @media (max-width:320px) {
          font-size:12px;
          >span {
          padding:4px;
          }
    }
  }
}
/* 编译结果 */
.container {
  width: 720px;
}
.container .component {
  width: 320px;
  font-size: 14px;
}
@media (max-width: 320px) {
  .container .component {
    font-size: 12px;
  }
  .container .component > span {
    padding: 4px;
  }
}
</pre>
===更多特性===
请参考[[/简明教程|简明语法教程]]

==示例==
灰机的多个单页APP（例如上述HuijiLesser零件、[[fnd:模型查看器|朱雀青龙模型查看器]]和新版[[h:首页|灰机首页]]）样式均使用Less编写（虽然你看到的是编译结果）。

在本页面的[[/example|这个子页面]]中列出了在[[wandao:首页|部落与弯刀Wiki]]中一个组件的Less样式和编译结果。

==迁移==
HuijiLesser本质上是在站点样式表（Mediawiki:Common.css）的基础上增加了一个零件样式表（Gadget:HuijiLesser.css），因此不存在迁移的必要。但是如果你想将现有的CSS转换为等价的Less样式表（以在未来通过Less维护），以下工具可能可以帮到你：
*[https://beautifytools.com/css-to-less-converter.php CSS to LESS Converter]
