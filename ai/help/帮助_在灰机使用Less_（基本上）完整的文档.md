# 帮助:在灰机使用Less/（基本上）完整的文档

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3A%E5%9C%A8%E7%81%B0%E6%9C%BA%E4%BD%BF%E7%94%A8Less/%EF%BC%88%E5%9F%BA%E6%9C%AC%E4%B8%8A%EF%BC%89%E5%AE%8C%E6%95%B4%E7%9A%84%E6%96%87%E6%A1%A3
revid：41441 · 抓取时间：2026-11-09T14:27:10+08:00

---

本文是[https://lesscss.org/features/ Less官方文档:In-Depth Guide]的译本。其中跳过（或特别标注了）在HuijiLesser中不支持的特性，并且根据灰机的实际情况更改了说明。


==变量==
===基本用法===
通常而言，在Less样式表中几乎不需要书写重复书写属性。例如：
<pre>
/* CSS */
a,
.link {
  color: #428bca;
}
.widget {
  color: #fff;
  background: #428bca;
}</pre>
在Less中可以简写为：
<pre>
// Variables
@link-color:        #428bca; // sea blue
@link-color-hover:  darken(@link-color, 10%);

// Usage
a,
.link {
  color: @link-color;
}
a:hover {
  color: @link-color-hover;
}
.widget {
  color: #fff;
  background: @link-color;
}
</pre>
===变量插值===
====选择器作为变量====
<pre>// Variables
@my-selector: banner;

// Usage
.@{my-selector} {
  font-weight: bold;
  line-height: 40px;
  margin: 0 auto;
}</pre>
编译结果：
<pre>.banner {
  font-weight: bold;
  line-height: 40px;
  margin: 0 auto;
}</pre>
====在url()中使用变量====
<pre>// Variables
@images: "../img";

// Usage
body {
  color: #444;
  background: url("@{images}/white-sand.png");
}</pre>
====在@import语句中使用变量====
略，灰机Lesser不支持<code>@import</code>语法。
====在属性名中使用变量====
<pre>@property: color;

.widget {
  @{property}: #0ee;
  background-@{property}: #999;
}</pre>
编译结果：
<pre>.widget {
  color: #0ee;
  background-color: #999;
}</pre>

====使用变量作为变量====
<pre>@primary:  green;
@secondary: blue;

.section {
  @color: primary;

  .element {
    color: @@color;
  }
}</pre>
编译结果：
<pre>.section .element {
  color: green;
}</pre>

====变量声明的位置====
变量的使用可以在变量声明之前。

例1：
<pre>
.lazy-eval {
  width: @var;
}

@var: @a;
@a: 9%;</pre>
编译结果：
<pre>
.lazy-eval {
  width: 9%;
}
</pre>
在Less编译器寻找变量值时，会从当前的作用域开始向上层搜索。

例2：
<pre>.lazy-eval {
  width: @var;
  @a: 9%;
}

@var: @a;
@a: 100%;</pre>
在例2中，width的属性值为var，编译器首先找到了@var的定义为变量@a，然后从当前作用域（.lazy-eval{}）中寻找@a的定义，因此最后一行的@a不生效，编译结果与例1相同。

===使用同级或上级属性作为变量===
可以使用同级或上一级的css属性作为变量。例如：
<pre>.widget {
  color: #efefef;
  background-color: $color;
}</pre>
这里的background-color引用了color作为变量，输出结果为：
<pre>
.widget {
  color: #efefef;
  background-color: #efefef;
}
</pre>
注意，变量的取值由最邻近的作用于的、某属性的“最终值”决定，与引用的位置无关。例如：
<pre>
.block {
  color: red; 
  .inner {
    background-color: $color; 
  }
  color: blue;  
} 
</pre>
在上例中，$color的值在.block{}作用域中，最终值为blue，因此.inner的background-color值为blue。

===变量的默认值===
可以为@import的样式表中的变量指定默认值。由于HuijiLesser的特性本节略过。

==父选择器==
在选择器中使用<code>&</code>父级选择器的'''整个选择器链'''。
<pre>a {
  color: blue;
  &:hover {
    color: green;
  }
}</pre>
编译结果：
<pre>a {
  color: blue;
}

a:hover {
  color: green;
}</pre>

父选择器也可以用来修饰父级选择器链的最后一个选择器，例如：
<pre>.button {
  &-ok {
    background-image: url("ok.png");
  }
  &-cancel {
    background-image: url("cancel.png");
  }

  &-custom {
    background-image: url("custom.png");
  }
}</pre>
编译结果：
<pre>.button-ok {
  background-image: url("ok.png");
}
.button-cancel {
  background-image: url("cancel.png");
}
.button-custom {
  background-image: url("custom.png");
}</pre>
===多次使用&===
父选择器也可以多次出现。例如：
<pre>.link {
  & + & {
    color: red;
  }
  & & {
    color: green;
  }
  && {
    color: blue;
  }
  &, &ish {
    color: cyan;
  }
}</pre>
编译结果：
<pre>.link + .link {
  color: red;
}
.link .link {
  color: green;
}
.link.link {
  color: blue;
}
.link, .linkish {
  color: cyan;
}</pre>

注意，父选择器代表的是'''整个选择器链'''，例如：
<pre>.grand {
  .parent {
    & > & {
      color: red;
    }

    & & {
      color: green;
    }

    && {
      color: blue;
    }

    &, &ish {
      color: cyan;
    }
  }
}</pre>
编译结果：
<pre>.grand .parent > .grand .parent {
  color: red;
}
.grand .parent .grand .parent {
  color: green;
}
.grand .parent.grand .parent {
  color: blue;
}
.grand .parent,
.grand .parentish {
  color: cyan;
}</pre>
在上例中，&代表的是<code>.grand .parent</code>选择器链，而不是<code>.parent</code>。

===调整父选择器的顺序===
父选择器页可以放在新选择器尾部，例如：
<pre>.header {
  .menu {
    border-radius: 5px;
    .no-borderradius & {
      background-image: url('images/button-background.png');
    }
  }
}</pre>
编译结果：
<pre>.header .menu {
  border-radius: 5px;
}
.no-borderradius .header .menu {
  background-image: url('images/button-background.png');
}</pre>
注意<code>.no-borderradius &</code>最后编译成了<code>.no-borderradius .header .menu</code>。

===枚举所有可能性===
如果父选择器是多个选择器，则输出结果将包含所有可能的组合。见下例：
<pre>p, a, ul, li {
  border-top: 2px dotted #366;
  & + & {
    border-top: 0;
  }
}</pre>
编译结果：
<pre>p,
a,
ul,
li {
  border-top: 2px dotted #366;
}
p + p,
p + a,
p + ul,
p + li,
a + p,
a + a,
a + ul,
a + li,
ul + p,
ul + a,
ul + ul,
ul + li,
li + p,
li + a,
li + ul,
li + li {
  border-top: 0;
}</pre>

==extend()==
extend()是一个less伪类。使'''当前选择器'''继承另一个选择器的样式。
<pre>
nav ul {
  &:extend(.inline);
  background: blue;
}
.inline {
  color: red;
}</pre>
输出结果：
<pre>nav ul {
  background: blue;
}
.inline,
nav ul {
  color: red;
}</pre>
===语法===
<code>extend()</code>可以附着于选择器或放在作用域内。接受1-2个参数，其中第一个参数为所需extend的选择器。第二个参数是一个文本'''all'''，其作用见下文相关章节。

例1-两种语法：
<pre>.a:extend(.b) {}

// 上下两种语法作用方式相同。
.a {
  &:extend(.b);
}</pre>
例2-all参数：
<pre>.c:extend(.d all) {
  // 会应用到与.d相关的所有样式中，例如.d.x和.x.d
}
.c:extend(.d) {
  // 只会应用到.d中
}</pre>
例3-在第一个参数中使用多个选择器：
<pre>
.e:extend(.f) {}
.e:extend(.g) {}

// 合并写法
.e:extend(.f, .g) {}</pre>
===在选择器中使用===
在选择器中使用时，extend语法类似于一个伪类。一个选择器可以跟随多个extend，但extend必须位于所有选择器的最后。例如以下写法都是合法的：
*<code>pre:hover:extend(div pre)</code>
*extend前允许空格：<code>pre:hover :extend(div pre)</code>
*连续使用多个extend:<code>pre:hover:extend(div pre):extend(.bucket tr)</code>，注意可以根据上一节末尾的语法合并成一个。
但以下写法是不合法的：
*extend必须在所有选择器最后：<code>pre:hover:extend(div pre).nth-child(odd)</code>

在多个并列的、同一组选择器中，每一组都可以有自己的extend：
<pre>
.bag {
  content:'bag'
}
.bucket {
  content:'bucket'
}
.big-division,
.big-bag:extend(.bag),
.big-bucket:extend(.bucket) {
  size:big
}</pre>
编译结果：
<pre>.bag,
.big-bag {
  content: 'bag';
}
.bucket,
.big-bucket {
  content: 'bucket';
}
.big-division,
.big-bag,
.big-bucket {
  size: big;
}</pre>
===在样式内使用extend===
在样式内使用<code>&:extend()</code>等同于为这一组样式的所有选择器附着extend。例如：
<pre>pre:hover,
.some-class {
  &:extend(div pre);
}
// 等同于：
pre:hover:extend(div pre),
.some-class:extend(div pre) {}
</pre>
===在嵌套选择器中使用extend===
例1：
<pre>
.bucket {
  tr { 
    color: blue;
  }
}
.some-class:extend(.bucket tr) {} // less能识别上述嵌套选择器
</pre>
例2：
<pre>
.bucket {
  tr & {
    color: blue;
  }
}
.some-class:extend(tr .bucket) {} // 也能识别
</pre>

===extend的精确匹配特性===
extend在默认情况下会完整匹配一整个选择器。例如：
<pre>
.a.class,
.class.a,
.class > .a {
  color: blue;
}
.test:extend(.class) {} // 上述三个选择器中没有.class，因此不会生效。
</pre>
====统配选择器*====
<code>*</code>选择器也会影响结果。
<pre>
*.class {
  color: blue;
}
.noStar:extend(.class) {} // 不会生效，*.class不是.class
</pre>
====伪类顺序====
伪类的顺序也会影响结果。
<pre>
link:hover:visited {
  color: blue;
}
.selector:extend(link:visited:hover) {} // 不会生效。
</pre>
====nth表达式====
在css中，nth-child(n+3)和nth-child(1n+3)作用相同，但extend将他们视为不同的选择器。
====属性选择器====
具有相同选择性质的属性选择器结果一致。
<pre>
[title=identifier] {
  color: blue;
}
[title='identifier'] {
  color: blue;
}
[title="identifier"] {
  color: blue;
}
// 以下三种extend方式作用一致：
.noQuote:extend([title=identifier]) {}
.singleQuote:extend([title='identifier']) {}
.doubleQuote:extend([title="identifier"]) {}
</pre>
===可选参数“all”===
当第二个参数传入all时，上述精确匹配特性即失效，extend将作用于所有最后一个选择器为第一个参数的选择器。例如：
<pre>
.a.b.test,
.test.c {
  color: orange;
}
.test {
  &:hover {
    color: green;
  }
}

.replacement:extend(.test all) {}

// 编译结果：所有包含.test的样式都会复制一份给.replacement 
.a.b.test,
.test.c,
.a.b.replacement,
.replacement.c {
  color: orange;
}
.test:hover,
.replacement:hover {
  color: green;
}</pre>

===extend与选择器的变量插值===
extend无法应用于包含变量的选择器。如：
<pre>
@variable: .bucket;
@{variable} { 
  color: blue;
}
.some-class:extend(.bucket) {} // 无匹配

.bucket {
  color: blue;
}
.some-class:extend(@{variable}) {} // 无匹配
</pre>
但是，被extend的元素可以使用变量。例如：
<pre>
.bucket {
  color: blue;
}
@{variable}:extend(.bucket) {} // 正常匹配
@variable: .selector;
</pre>
===在@media中使用extend===
@media中的extend只会对在同一个@media作用域内的选择器生效：
<pre>
@media print {
  .screenClass:extend(.selector) {} // 可以匹配到下一行的.selector
  .selector { 
    color: black;
  }
}
.selector { // 但是匹配不到media外的.selector
  color: red;
}
@media screen {
  .selector {  // 也匹配不到另一个@media中的.selector
    color: blue;
  }
}</pre>
同样的，外层@media中的extend也不会匹配到内层@media内的选择器。
<pre>
@media screen {
  .screenClass:extend(.selector) {} // 外层media中的extend
  @media (min-width: 1023px) {
    .selector {  // 内层的目标，无法匹配
      color: blue;
    }
  }
}
</pre>
但是，如果extend位于顶层，则可以匹配到所有@media作用域内的选择器。
<pre>@media screen {
  .selector {  // 可以被最后一行匹配
    color: blue;
  }
  @media (min-width: 1023px) {
    .selector {  // 可以被最后一行匹配
      color: blue;
    }
  }
}

.topLevel:extend(.selector) {} // 有效

// 编译结果：
@media screen {
  .selector,
  .topLevel {
    color: blue;
  }
}
@media screen and (min-width: 1023px) {
  .selector,
  .topLevel {
    color: blue;
  }
}
</pre>
===由extend生成的重复选择器===
有可能生成重复的选择器，但less不会专门处理（css仍然有效）：
<pre>
.alert-info,
.widget {
  /* declarations */
}
.alert:extend(.alert-info, .widget) {}

// 上述extend语句会使.alert分别应用.alert-info和.widget的样式，从而生成.alert-info,.alert和.widget,.alert两组选择器，从而造成结果重复。
// 编译结果：
.alert-info,
.widget,
.alert,
.alert {
  /* declarations */
}
</pre>

===Extend的使用场景===
====常见场景====
通常使用extend是为了避免重复书写基础类。例如有一个.animal类：
<pre>
.animal {
  background-color: black;
  color: white;
}
</pre>
假设有一个“熊”元素，他应当具有基础的.animal类：
<pre><a class="animal bear">KUMA!</a></pre>
使用传统CSS和html的情况下，该元素需要写两个class；而使用less时可以只保留一个bear类，然后在该类中使用extend语法：
<pre>
// html
<a class="bear">KUMA!</a>
// less
.animal {
  background-color: black;
  color: white;
}
.bear {
  &:extend(.animal);
  background-color: brown;
}
</pre>
====降低代码量====
首先说明extend与mixin的区别（Mixin会在后面的章节提到）：
*extend会将被extend的选择器添加到原有选择器中；而mixin则会复制原有选择器的所有样式到被mixin的选择器中。
因此，在样式较多的情况下，extend更有利于减小输出样式的大小。例如：
<pre>
// 使用mixin
.my-inline-block() {
  display: inline-block;
  font-size: 0;
}
.thing1 {
  .my-inline-block;
}
.thing2 {
  .my-inline-block;
}
// 输出
.thing1 {
  display: inline-block;
  font-size: 0;
}
.thing2 {
  display: inline-block;
  font-size: 0;
}

// 使用extend
.my-inline-block {
  display: inline-block;
  font-size: 0;
}
.thing1 {
  &:extend(.my-inline-block);
}
.thing2 {
  &:extend(.my-inline-block);
}
// 输出
.my-inline-block,
.thing1,
.thing2 {
  display: inline-block;
  font-size: 0;
}</pre>
可见，复用次数越多，extend的优势也就越大。

====作为高级mixin使用====
下文中会提到，mixin只能作用于一个简单的选择器。而extend功能更强大。例如有两个完全不同的元素，extend可以轻松地使他们共用样式：
<pre>
li.list > a {
  // 列表样式
}
button.list-style {
  &:extend(li.list > a); // 使用和上边儿一样的列表样式
}
</pre>

==Merge==
Merge特性可以将多个作用于中的同名属性使用逗号或空格合并在一起。例如：
<pre>
.shadow {
  box-shadow+:0 0 5px #333;
  box-shadow+:0 5px 15px #000C;
}
// 编译结果：
.shadow {
  box-shadow: 0 0 5px #333, 0 5px 15px #000C;
}
</pre>
在上例中，两个带<code>+</code>的属性名在编译时被合并在了一起，并以逗号分隔。注意，其中任意一个box-shadow+都可以是来自另一个mixin的样式。

===用空格分隔的属性===
对于<code>transform</code>等使用空格分隔的属性，可以使用<code>+_</code>作为属性名后缀。
<pre>
.vortex {
transform+_:rotate(15deg);
transform+_:scale(1.5);
}
// 编译结果
.vortex {
  transform: rotate(15deg) scale(1.5);
}
</pre>
注意，less和HuijiLesser都不会验证CSS属性、属性值的合法性，只会验证语法问题。

==混入（Mixin）==
复制指定选择器的样式到当前作用域。

类选择器和class选择器都可以作为mixin名称。例如：
<pre>
.a, #b {
  color: red;
}
.mixin-class {
  .a();
}
.mixin-id {
  #b();
}

// 编译结果：
.a,
#b {
  color: red;
}
.mixin-class {
  color: red; // 由.a混入
}
.mixin-id {
  color: red; // 由#b混入
}
</pre>

===使用括号===
如果被引用的选择器后跟随了括号（<code>()</code>），则该选择器将被视为一个mixin变量，从而不会出现在输出的css中（但仍然会被混入元素中）。
<pre>
.my-mixin { // 不使用括号时属于正常选择器
  color: black; 
}
.my-other-mixin() { // 使用括号时视为mixin变量
  background: white;
}
.class {
  .my-mixin();
  .my-other-mixin();
}
// 输出结果
.my-mixin {
  color: black;
}
.class {
  color: black;
  background: white;
}
</pre>
===在混入中使用其他选择器===
如果混入的选择器中包含其他选择器，则混入后这些选择器仍然会保留。
<pre>
.my-hover-mixin() {
  &:hover {
    border: 1px solid red;
  }
}
button {
  .my-hover-mixin();
}
// 输出结果
button:hover {
  border: 1px solid red;
}
</pre>


===命名空间===
命名空间是包含多个子选择器的mixin变量，本质上和上一节相同。但使用时可以进一步定义混入变量中的哪一个子选择器。
<pre>
#outer() {
  .inner {
    color: red;
  }
}

.c {
  #outer.inner();
}

// 输出结果
.c {
  color: red;
}
</pre>

命名空间可有效减少样式冲突的情况。同样也是一种组织混入样式的手段。
<pre>
#my-library() {
  .my-mixin() {
    color: black;
  }
}
// 使用方式
.class {
  #my-library.my-mixin();
}
</pre>

===以函数方式使用Mixin===
在定义Mixin时可以定义传入参数。例如：
<pre>
// 定义Mixin
.average(@x, @y) {
  @result: ((@x + @y) / 2);
}

// 调用Mixin，传入参数
div {
  // 调用average mixin，传入16px和50px两个参数，并以@result变量作为输出结果。
  padding:.average(16px,50px)[@result]
}
// 编译结果
div {
  padding: 33px;
}
</pre>
定义mixin时也可以指定某参数的默认值。
<pre>
.roundbox(@radius: 6px) {
          border-radius: @radius;
}

// 调用
.card {
  .roundbox();
  &-biground {
  .roundbox(12px)
  }
}
// 编译结果
.card {
  border-radius: 6px;
}
.card-biground {
  border-radius: 12px;
}
</pre>

===Mixin守卫===
Mixin可以使用<code>when</code>操作符以定义生效方式。如下例：
<pre>
// 定义mixin
.mixin(@a) when (lightness(@a) >= 50%) {
  background-color: black;  // 亮度高于50%时，输出黑色背景
}
.mixin(@a) when (lightness(@a) < 50%) {
  background-color: white;  //亮度低于50%时，输出白色背景
}
.mixin(@a) {
  color: @a; // 无论何时都输出color:@a
}

// 调用mixin
.class1 { .mixin(#ddd) }
.class2 { .mixin(#555) }

// 输出结果
.class1 {
  background-color: black;
  color: #ddd;
}
.class2 {
  background-color: white;
  color: #555;
}
</pre>
====Mixin守卫的运算符====
在<code>when</code>操作符后的括号中支持这些比较运算符：<code>></code>，<code>>=</code>，<code>=</code>，<code><=</code>，<code><</code>。

如果不填写运算符，则视为truthy判断，但只有传入字符串<code>true</code>时才视为true。其他任何值都视为false。
<pre>
// 以下两个定义相同。
.truth(@a) when (@a) { ... }
.truth(@a) when (@a = true) { ... }

.class {
  .truth(40) // 该调用不生效，因为40不等于true
  .truth(true) // 生效
}
</pre>
可以比较传入的多个参数，也可以比较其他变量。
<pre>
// 比较传入的两个参数
.compare(@a; @b) when (@a > @b) { width: @a }
.compare(@a; @b) when (@a < @b) { width: @b }

// 比较变量
@defaultmedia:mobile; // 注意这里是定义变量而不是@规则
.mixin(@a) when (@media = mobile) { ... }
.mixin(@a) when (@media = desktop) { ... }
</pre>
====多个运算结果的逻辑运算====
可以使用<code>and</code>、<code>,</code>、<code>not</code>对守卫的初步运算结果做进一步比较：
<pre>
// @a是数字且大于0时有效
.mixin(@a) when (isnumber(@a)) and (@a > 0) { ... }

// @a大于10或小于-10时生效
.mixin(@a) when (@a > 10), (@a < -10) { ... }

// b不大于0时生效
.mixin(@b) when not (@b > 0) { ... }
</pre>
上例中使用了isnumber()函数。此外还有以下可用函数：
*iscolor(@a)，判断@a是否是任意合法色值
*isnumber(@a)，判断@a是否是数值，包括带单位后缀的数值，如<code>16px</code>也属于数值。
*isstring(@a)，判断@a是否是字符串（由引号包裹的字符）
*iskeyword(@a)，判断@a是否是关键字（无引号包裹的字符）
*isurl(@a)，判断@a是否是url（是否符合<code>url('...')</code>）
对于任意数值类型，还可以进一步判断单位：
*ispixel(@a)，判断@a是否使用px作为单位
*ispercentage(@a)，判断@a是否使用百分比作为单位
*isem(@a)，判断@a是否使用em作为单位
*isunit(@a,@b)，判断@a的单位是否是@b。@b必须为一个字符串（需要用引号包裹））

===调用mixin时使用important===
如果在调用mixin时后面加!important，则该mixin中所有引入的样式均视为important。
<pre>
.foo (@bg: #f5f5f5; @color: #900) {
  background: @bg;
  color: @color;
}
.unimportant {
  .foo();
}
.important {
  .foo() !important;
}
// 输出结果
.unimportant {
  background: #f5f5f5;
  color: #900;
}
.important {
  background: #f5f5f5 !important;
  color: #900 !important;
}
</pre>
==使用样式块作为变量==
样式块（花括号之间的区域）也可以作为变量使用。
<pre>
// 声明
@rulegroup: {background:red;};

// 调用
.redblock {
    @rulegroup();
}
</pre>
由于mixin接受变量，样式块也可以作为参数传入mixin。例如：
<pre>
.desktop-and-old-ie(@a) {
  @media screen and (min-width: 1200px) { @a(); }
  html.lt-ie9 &                         { @a(); }
}

header {
  background-color: blue;
  // 这里将{background-color:red}作为参数传给了.desktop-and-old-ie()
  .desktop-and-old-ie({
    background-color: red;
  });
}
// 编译结果
header {
  background-color: blue;
}
@media screen and (min-width: 1200px) {
  header {
    background-color: red;
  }
}
html.lt-ie9 header {
  background-color: red;
}
</pre>
样式块引入后，该样式块中的其他mixin可以正常使用：
<pre>
@detached-ruleset: { 
    .sub-mixin() {
        color: blue;
    }
};

.caller {
    @detached-ruleset();  //这一行运行后，.caller也具有一个mixin叫sub-mixin，因此可以在下一行调用
    .sub-mixin();
}
</pre>
但是，样式块中的变量无法在被调用的代码块中使用。
<pre>
@detached-ruleset: {
  @color:blue;
  background-color:@color; // 可以内部使用
};
.caller {
  @detached-ruleset(); // 输出background-color:blue，但是不会输出@color
  color:@color; // 报错， 因为@color是私有变量
}
</pre>
相反地，调用代码块变量时，代码块能拿到调用位置的其他属性和变量。
<pre>
@detached-ruleset: {
  caller-variable: @caller-variable; // 未定义
  .caller-mixin(); // 未定义
};

selector {
  @detached-ruleset();    // 调用代码块。代码块可以拿到瞎编的@caller-variable和.caller-mixin
  @caller-variable: value; // 调用者的变量
  .caller-mixin() { // 调用者的mixin
    variable: declaration;
  }
}

// 输出
selector {
  caller-variable: value;
  variable: declaration;
}
</pre>

和一般代码规则不同，在全局中定义的变量会覆盖局部变量，而直接调用变量则相反。
<pre>
@variable: global; // 定义全局变量
@detached-ruleset: {
  ruleset-output: @variable;
}
;
selector {
  @variable: local; // 定义了局部同名变量
  local-output:@variable; // 输出直接调用变量的结果
  @detached-ruleset(); // 输出通过调用代码块的结果
}
// 输出
selector {
  local-output: local;
  ruleset-output: global;
}
</pre>

===访问样式块的特定属性===
由于样式块变量的特性，样式块可以作为配置表使用。
<pre>
@config: {
  option1: true;
  option2: false;
}

.mixin() when (@config[option1] = true) {
  selected: value;
}

.box {
  .mixin();
}

// 输出
.box {
  selected: value;
}
</pre>
样式块可以像object一样嵌套：
<pre>
@config: {
  @colors: {
    primary: blue;
  }
}
.box {
  color: @config[@colors][primary];
}
</pre>
查询key如果是另一个变量，则需要使用两个@符号：
<pre>
@config: {
  @dark: {
    primary: darkblue;
  }
  @light: {
    primary: lightblue;
  }
}

.box {
  @lookup: dark; //局部变量
  color: @config[@@lookup][primary]; // 在@config里找局部变量@lookup的值，再找下一级的primary
}
</pre>
