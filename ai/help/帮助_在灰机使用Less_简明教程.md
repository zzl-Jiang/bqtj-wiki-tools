# 帮助:在灰机使用Less/简明教程

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3A%E5%9C%A8%E7%81%B0%E6%9C%BA%E4%BD%BF%E7%94%A8Less/%E7%AE%80%E6%98%8E%E6%95%99%E7%A8%8B
revid：41552 · 抓取时间：2026-11-09T14:27:10+08:00

---

本文档是[[user:Summerset|Summerset]]在经验和Less官方文档的基础上撰写的简明教程。

==阅读理解：CSS的令牌化（tokenize）==
我们可以回顾一下CSS语法中包含的内容，并以程序的方式作出进一步理解：
<pre>
#wiki-body {
  font-size:14px;
  margin:12px 24px 0;
}
</pre>
在上例中，<code>#wiki-body</code>被称为选择器（selector），由花括号包裹的区域称为样式块（ruleset，我忘了正规翻译是什么）。

每个样式块由若干个key-value型数据组成。其中key被称为属性（property），value为该属性的值。

值的基础类型大致分为以下几种：
*数值，如12，50%，14px，1.2em等。值的单位也有如下几种：
**绝对长度：如cm,pt,in
**相对长度：如em,px,vm
**百分比：如50%，100%
*颜色：如#FF5B00。CSS支持多种颜色表达方式，包括：
**六位HEX色号，如#FF5B00
**八位HEX色号，其中最后两位代表alpha通道，如#FF5B00CC
**hsl和hsla色号，如hsl(255,64%,0%)和hsla(255,64%,0%,0.5)
**rgb和rgba色号，如rgb(255,43,25)和rgba(255,43,25,0.5)
*关键字（keyword）。如inset, no-repeat等。
**css和less都不会对属性值中的关键字做有效性判断，所以你可以瞎编一个keyword，只是不会产生作用罢了。
*字符串（string），例如::after伪元素中的content的值、grid-area中用于命名区域的值。
**字符串与关键字的区别是，字符串需要有引号包裹。
*链接，由url()包裹的字符串。例如background-image的值。
在使用中，我们通常会使用多个值以逗号或空格分隔，这种形式在less中被称为列表（list）。
想像一下一个具有多重阴影的文字：
<pre>.neon {
    text-shadow: 0 0 2px white, 0 0 15px #333, 0 0 5px #ff0000;
}</pre>
他的text-shadow包含一个有三个元素的、以逗号分隔的列表，每个列表项又包含一个以空格分隔的子列表。

理解上述内容不会对你使用CSS有太大的影响，但会在使用less函数时更加方便。

在下文中，我们会反复用到本节中提到的术语。

==LESS的嵌套语法==
相对于CSS，Less的最大特色就是嵌套语法。该语法可以使你不用反复写同一个上级选择器。
<pre>
#wiki-body {
  font-size:14px;
  #firstHeading {
    display:flex;
    >h1 {
      flex:1;
      font-size:24px;
    }
    &:hover {
      font-weight:bold;
    }
  }
}
// 编译结果
#wiki-body {
  font-size: 14px;
}
#wiki-body #firstHeading {
  display: flex;
}
#wiki-body #firstHeading > h1 {
  flex: 1;
  font-size: 24px;
}
#wiki-body #firstHeading:hover {
  font-weight: bold;
}
</pre>
上例中，位于父级样式块(#wiki-body的样式块)中的其他选择器（#firstHeading），和位于#firstHeading样式块中的其他选择器（>h1,&:hover）会在编译为CSS的时候逐级展开。

这里用到的<code>&</code>称为父选择器。父选择器可以完整复现当前所在样式块的选择器链，例如<code>&:hover</code>中的<code>&</code>会被编译为<code>#wiki-body #firstHeading</code>。注意如果你写成了<code>& :hover</code>，则解析结果会变为<code>#wiki-body #firstHeading :hover</code>。

如果父选择器是多个选择器的组合，则编译时会尝试所有的组合可能性。设想一个“调整所有列表项缩进”的例子：
<pre>
ul>li,ol>li {
  margin-left:12px;
  >ul>li,>ol>li {
  margin-left:24px;
    >ul>li,>ol>li {
      margin-left:36px;
    }
  }
}
// 编译结果
ul > li,
ol > li {
  margin-left: 12px;
}
ul > li > ul > li,
ol > li > ul > li,
ul > li > ol > li,
ol > li > ol > li {
  margin-left: 24px;
}
ul > li > ul > li > ul > li,
ol > li > ul > li > ul > li,
ul > li > ol > li > ul > li,
ol > li > ol > li > ul > li,
ul > li > ul > li > ol > li,
ol > li > ul > li > ol > li,
ul > li > ol > li > ol > li,
ol > li > ol > li > ol > li {
  margin-left: 36px;
}
</pre>

==less的混入（mixin）语法==
有时候我们会碰到这样的情况，有很多个元素共用一组样式。在CSS中我们需要为每个元素都写一遍相同的样式、或者至少为他们添加一个共用的class：
<pre>
.button-default,
.button-primary,
.button-secondary {
  display:inline-block;
  padding:6px 12px;
  background:#aaa;
}
.button-primary {
  background:blue;
}
.button-secondary {
  background:green;
}
</pre>
在less中则可以使用“混入”特性直接将另一个样式块“塞进”当前样式块：
<pre>
.button-mixin { 
  display:inline-block;
  padding:6px 12px;
  background:#aaa;
}
.button-primary {
  .button-mixin();
  background:blue;
}
.button-secondary {
  .button-mixin();
  background:green;
}
</pre>
虽然看上去代码量并没有减少，但是'''mixin可以作为函数使用'''，从而使其能实现更复杂的功能。例如我们可以让按钮自动生成hover的背景色：
<pre>
.button-mixin(@bg) {
  display:inline-block;
  padding:6px 12px;
  background:@bg;
  &:hover {
    background:lighten(@bg,25%)
  }
}
.button-primary {
  .button-mixin(blue);
}
.button-secondary {
  .button-mixin(green);
}

// 编译结果
.button-primary {
  display: inline-block;
  padding: 6px 12px;
  background: blue;
}
.button-primary:hover {
  background: #8080ff;
}
.button-secondary {
  display: inline-block;
  padding: 6px 12px;
  background: green;
}
.button-secondary:hover {
  background: #00ff00;
}
</pre>
这里将<code>.mixin</code>从一个选择器样式转换为了一个函数（在后边加了括号），并且接受一个<code>@bg</code>参数。在运算时，<code>@bg</code>会被另一个less函数<code>lighten()</code>处理成相对较浅的另一个颜色。

===关于括号===
上文中提到，可以通过一个选择器构建mixin。如果在选择器后不加括号（如.button-mixin {}），则该mixin视为一个普通的样式块，会被输出到css中。而如果加了括号（如.button-mixin(){}），则无论括号里是否定义了参数，该mixin本身不会输出到css，仅在被调用时输出到调用所在的位置。

==变量==
在上一节中，我们将background作为一个颜色变量传递给了mixin。实际上变量支持任意类型的数据（见'''CSS的令牌化'''一节）。并且，变量也可以在全局或者任意样式块中声明，但需要注意变量的作用域：
<pre>
@default-shadow:0 0 5px #000; // 全局声明
.button {
  box-shadow:@default-shadow; // 可以拿到全局变量
  @hover-weight:bold; // 局部声明
  &:hover {
  font-weight:@hover-weight; // 可以拿到局部变量
  }
}
.another-button {
  box-shadow:@default-shadow; // 可以拿到全局变量
  &:hover {
  font-weight:@hover-weight; // 报错，因为本级和所有上级样式块中没有@hover-weight
  }
}
</pre>
===变量声明先后不影响使用===
变量可以在使用后声明。如果多次声明，则该样式块中最后一次声明该变量有效。
<pre>
.button {
  &:hover {
  font-weight:@hover-weight; // 可以拿到局部变量，输出thin
  }
  @hover-weight:bold; // 后置局部声明
  @hover-weight:thin; // 第二次局部声明
}
</pre>
===使用其他属性作为变量===
样式块中的其他属性也可以作为变量使用。
<pre>
.button {
  color:#FFF;
  text-shadow:0 0 5px fadeout($color,50%);
}
// 编译结果
.button {
  color: #FFF;
  text-shadow: 0 0 5px rgba(255, 255, 255, 0.5);
}
</pre>
上例中使用了一个fadeout函数，使#FFF变为50%透明的#FFF。

如果当前样式块中没有该属性，则less会向上查找，与@变量类似。
<pre>
.set {
  color:#FFF;
  .button {
    text-shadow:0 0 5px fadeout($color,50%); // 有效，上一层.set中有$color
  }
}
</pre>
===选择器变量===
keyword、string、number型变量均可以在选择器中调用，语法如下（注意@符号后的大括号）：
<pre>
@selector-var1:test;
@selector-var2:'test';
@selector-var3:5px;
.query {
  @{selector-var1} {value:true}
  @{selector-var2} {value:true}
  @{selector-var3} {value:true}
}
// 编译结果
.query test {
  value: true;
}
.query 'test' {
  value: true;
}
.query 5px {
  value: true;
}
</pre>
less不会判断选择器是否有效，因此'test'和5px均正常输出。

===在url()的参数中使用变量===
<pre>
@root-path:'https://my-image.bed';
// Usage
body {
  color: #444;
  background: url("@{root-path}/white-sand.png");
}

// 编译结果
body {
  color: #444;
  background: url("https://my-image.bed/white-sand.png");
}
</pre>
===在属性名中使用变量===
<pre>
@property: color;
 
.widget {
  @{property}: #0ee;
  background-@{property}: #999;
}
</pre>
===使用变量作为变量===
如果引用的变量值本身是另一个变量，则需要添加多个@符号：
<pre>
@primary:  green;
@secondary: blue;
 
.section {
  @color: primary; // primary是一个变量，而不是变量的值
 
  .element {
    color: @@color; // color是变量的变量
  }
}
</pre>
===列表变量===
请参考[[帮助:在灰机使用Less/Less函数列表]]中'''列表函数'''一节。

==merge特性==
merge特性适用于接受列表的css属性。例如：
<pre>
.neon-button {
  box-shadow+:0 0 5px #FFBB00;
  box-shadow+:0 0 15px #FFCC66;
}
// 输出结果
.neon-button {
  box-shadow: 0 0 5px #FFBB00, 0 0 15px #FFCC66;
}
</pre>
如果属性是以空格做分隔的，则可以使用<code>+_</code>作为属性后缀：
<pre>
.grid {
  grid-template-columns+_:24px 64px 12px;
  grid-template-columns+_:1fr;
}
// 输出结果：
.grid {
  grid-template-columns: 24px 64px 12px 1fr;
}
</pre>
注意，截至目前（less 4.1.3），merge特性无法拿到选择器不一致的样式块中的属性（包括当前和父级样式块），因此以下的例子是无法正常运作的：
<pre>
.neon-button {
  box-shadow+:0 0 5px #FFBB00;
  &:hover {
    box-shadow+:0 0 15px #FFCC66; // 只会输出0 0 15px #FFCC66，因为&:hover定义的是另一个样式块。
  }
}
</pre>
但是，如果前一条属性是通过mixin导入的，那之后的merge样式可以正常生效，因为他们位于同一个样式块：
<pre>
.basic-box-shadow() {
  box-shadow+:0 0 5px #FFBB00;
}

.neon {
  .basic-box-shadow();
  box-shadow+:0 0 15px #FFCC66; // 输出0 0 5px #FFBB00, 0 0 15px #FFCC66;
}

</pre>

==extend语法==
extend语法可以将当前选择器并列附加到另一个选择器中，以继承另一个选择器的样式。

与mixin不同的是，a extend(b)会将a选择器添加到b上，而a {.b()}则会将b的样式全部添加到a的样式中。因此，extend虽然看起来奇怪但是会大幅减少编译后的代码长度。我们将mixin一节中的例子换为extend：
<pre>
// 使用mixin ===================
.button-mixin{ 
  display:inline-block;
  padding:6px 12px;
  background:#aaa;
}
.button-primary {
  .button-mixin();
  background:blue;
}
.button-secondary {
  .button-mixin();
  background:green;
}

// 编译结果
.button-mixin {
  display: inline-block;
  padding: 6px 12px;
  background: #aaa;
}
.button-primary {
  display: inline-block;
  padding: 6px 12px;
  background: #aaa;
  background: blue;
}
.button-secondary {
  display: inline-block;
  padding: 6px 12px;
  background: #aaa;
  background: green;
}

// 使用extend ===================
.button-mixin{ 
  display:inline-block;
  padding:6px 12px;
  background:#aaa;
}
.button-primary {
  background:blue;
}
.button-secondary {
  background:green;
}

// 编译结果：
.button-mixin,
.button-primary,
.button-secondary {
  display: inline-block;
  padding: 6px 12px;
  background: #aaa;
}
.button-primary {
  background: blue;
}
.button-secondary {
  background: green;
}
</pre>
extend的使用有如下限制：
*extend的语法类似于一个伪类（selector:extend(b)）。如果selector中本身包含伪类，则<code>:extend()</code>必须位于最后。
*extend接受第二个参数“all”，与第一个参数以空格分隔，例如<code>selector:extend(b all)</code>。
*可以连续使用多个extend，或在第一个参数中以逗号分隔多个选择器，例如<code>selector:extend(a):extend(b)</code>与<code>selector:extend(a,b)</code>等效。
*如果extend的选择器位于一个@media规则内，则只会extend同一个@media内的另一个选择器。

===all参数===
extend的第一个参数默认为精确匹配。例如:extend(button)不会extend到button.primary，也不会extend到group > button.

但如果第二个参数添加了all，则所有和button有关的选择器都会extend。
<pre>
.button {
  value:'顶层button';
  &:hover {
  value:'hover的button'
  }
}
.group.button {
  value:'有父选择器的button'
}

.test1:extend(.button) {caller:'test1'}

.test2:extend(.button all) {caller:'test2'}

// 输出结果
.button,
.test1,
.test2 { // test1的extend没有填写all，所以只会附加到精确匹配的.button
  value: '顶层button';
}
.button:hover,
.test2:hover { //test2的extend写了all，所以会延伸到.button:hover和.group.button
  value: 'hover的button';
}
.group.button,
.group.test2 {
  value: '有父选择器的button';
}
.test1 {
  caller: 'test1';
}
.test2 {
  caller: 'test2';
}
</pre>
===extend和@media===
如果在一个@media内填写extend，则只会extend到同一个@media内的选择器上。
<pre>
@media screen {
  .button {
    font-size:24px;
  }
  .button-extend:extend(.button) {}
}
.button {
  color:#FFF;
}
// 编译结果
@media screen {
  .button,
  .button-extend {
    font-size: 24px;
  }
}
.button {
  color: #FFF; // @media内的extend不会延伸到这里
}
</pre>
但如果在顶层extend，则会延伸到所有的@media。
<pre>
@media screen {
  .button {
    font-size:24px;
  }

}
.button {
  color:#FFF;
}
.button-extend:extend(.button) {} // 在顶层extend

// 编译结果
@media screen {
  .button,
  .button-extend { // 延伸到了@media内
    font-size: 24px;
  }
}
.button,
.button-extend {
  color: #FFF;
}
</pre>

==变量==
我们在前文用到了两种变量：值变量（@XXX）和属性变量（$xxx）。本节将对变量部分做进一步延伸说明。
===值变量（@）===
值变量可以是任意css接受的值（见第一节）。
<pre>
@default-font-size:14px;
@default-color:#FFF;
@default-content:'test content';
@default-shadow:0 0 5px #000;
</pre>
===样式块变量===
此外，值变量还可以是一个样式块，只是调用方式不同（类似mixin）：
<pre>
@default-hover: {
  box-shadow:0 0 5px #000;
  &:hover {
    box-shadow:0 0 15px #000;
  }
};
.hover-item {
 @default-hover();
}

// 编译结果
.hover-item {
  box-shadow: 0 0 5px #000;
}
.hover-item:hover {
  box-shadow: 0 0 15px #000;
}
</pre>
需要注意的是，如果样式块内包含一个变量，则该变量仅限内部使用。
<pre>
@private-variable-block: {
  @color-var:#FFF;
  color:@color-var; // 在内部使用变量
}
.test-block {
  @private-variable-block();
  background:@color-var; // 拿不到私有变量
}
</pre>
样式块变量也可以当做一个映射表使用，甚至可以嵌套：
<pre>
@default-values: {
  color:#FFF;
  background:#000;
  @font-families: {
    serif:'Times New Roman','Simsun',serif;
    sans-serif:'Tahoma','Arial','Microsoft Yahei',sans-serif;
  }  
}
.text-lines {
  .serif {
  font-family:@default-values[@font-families][serif];
  }
  .sans-serif {
  font-family:@default-values[@font-families][sans-serif];
  }
}
// 编译结果
.text-lines .serif {
  font-family: 'Times New Roman', 'Simsun', serif;
}
.text-lines .sans-serif {
  font-family: 'Tahoma', 'Arial', 'Microsoft Yahei', sans-serif;
}
</pre>
注意，嵌套的节点必须是一个变量节点（以@开头）。上文中如果将@font-families换成font-families，则会报错。

另外，如果调用嵌套内容时的节点名本身由一个变量生成，则调用时需要填写两个@：
<pre>
@default-values: {
  color:#FFF;
  background:#000;
  @font-families: {
    serif:'Times New Roman','Simsun',serif;
    sans-serif:'Tahoma','Arial','Microsoft Yahei',sans-serif;
  }  
}
.use-var-as-node-name {
  @font-node-name:font-families;
  font-family: @default-values[@@font-node-name][serif]
}
</pre>
===属性变量($)===
属性变量的调用以<code>$</code>开头，其取值会从当前样式块向上寻找同名属性。如果找不到同名属性则会在编译时报错。
<pre>
.set {
  color:#FFF;
  .button {
    text-shadow:0 0 5px fadeout($color,50%); // 有效，上一层.set中有$color
  }
}
</pre>

===转义变量===
属于一个特殊用法。
<pre>
@min768: ~'min-width: 768px'; 
.element {
  @media (@min768) {
    font-size: 1.2rem;
  }
}

// 编译结果
@media (min-width: 768px) {
  .element {
    font-size: 1.2rem;
  }
}
</pre>
我们在[[博客:灰机2022秋季攻势|2022秋季更新]]中使用转义变量优化了cockpit和皮肤的移动端兼容性，它是这么写的：
<pre>
// 定义media-query字符串
@xs: ~'(max-width:767px)';
@sm: ~'(min-width:768px) and (max-width:991px)';
@md: ~'(min-width:992px) and (max-width:1199px)';
@lg: ~'(min-width:1200px)';

// 使用mediaw-query字符串
.skinroot-links {
    gap: 6px;

    @media @sm,
    @xs {
        display: none;
    }
}

// 由于@media规则的嵌套特性，上述代码会被编译为：
.skinroot-links {
    gap: 6px;
}

@media (min-width:768px) and (max-width:991px),
(max-width:767px) {
    .skinroot-links {
        display: none;
    }
}
</pre>

==高级用法==
===命名空间===
命名空间实际上是一个嵌套mixin，可以用来成组管理样式。
<pre>
#bundle() { // 定义#bundle为一个命名空间
  .button {
    display: block;
    border: 1px solid black;
    background-color: grey;
    &:hover {
      background-color: white;
    }
  }
}
#header a {
  color: orange;
  #bundle.button();  // 混入#bundle的.button()样式
}
</pre>
===运算===
数值类的变量和数值均可参与运算。支持基本的加、减、乘、除运算符。
<pre>
@grid-width:12%;
.col-2 {
  width:@grid-width * 2; // 输出24%
}
</pre>
如果运算符前后的单位不一致，则只有第一个、带单位的数值有效。
<pre>
.calculate {
  different-unit:5m * 2m; // 输出10m。怎么，还想有平方米？
  first-unit-only:5* 2m * 7s; // 输出70m。
  divide-test:20m / 2; // 输出20m/2，原因未知
}
</pre>
另外，less不会处理calc中的运算符。
<pre>
.calculate {
  operator-in-calc:calc(100% - 25cm); // 输出calc(100% - 25cm)
}
</pre>
===@media的冒泡===
在CSS中，@media规则必须写在顶层。而在less中，@media可以作为子选择器使用。编译时会自动把整个选择器链移动到顶层。
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
===结合字符串变量使用@media===
我们在写响应式样式时往往需要反复书写查询字符串以定义最大和最小宽度。结合上文中的字符串变量，我们可以在less中实现如下写法：
<pre>
// 先定义四个尺寸区间
@xs: ~'(max-width:767px)';
@sm: ~'(min-width:768px) and (max-width:991px)';
@md: ~'(min-width:992px) and (max-width:1199px)';
@lg: ~'(min-width:1200px)';

// 然后这样使用
.element {
    color: red;

    @media @xs {
        color: blue;
    }

    @media @sm,
    @md {
        // 逗号代表“或”逻辑
        color: green;
    }
}

// 编译结果
.element {
    color: red;
}

@media (max-width:767px) {
    .element {
        color: blue;
    }
}

@media (min-width:768px) and (max-width:991px),
(min-width:992px) and (max-width:1199px) {
    .element {
        color: green;
    }
}
</pre>

===使用“守卫”===
可以在定义mixin时增加一个守卫，用来判断该mixin是否应当生效。
<pre>
.mixin(@a) when (lightness(@a) >= 50%) {
  background-color: black;  // 亮度高于50%时，输出黑色背景
}
.mixin(@a) when (lightness(@a) < 50%) {
  background-color: white;  //亮度低于50%时，输出白色背景
}
.mixin(@a) {
  color: @a; // 无论何时都输出color:@a
}
.class1 { .mixin(#ddd) }
.class2 { .mixin(#555) }
</pre>
在上例中，调用mixin时需要传入一个色号参数。该mixin的三组定义中的when即为守卫标识，任意一组mixin仅在守卫条件返回true时生效。例如#ddd的亮度大于50%，则背景色将为black。第三组定义没有守卫，则始终生效。

===使用“守卫”的默认值===
在守卫条件中使用when(default())，则该定义会在没有其他守卫匹配的情况下生效。
<pre>
.mixin(1)                   {x: 11}
.mixin(2)                   {y: 22}
.mixin(@x) when (default()) {z: @x}
 
div {
  .mixin(3);  // 输出z=3，因为前两条都无效，default()将返回true
}
</pre>

也可以使用when not(default())以使该定义在任意有匹配的情况下生效，而无匹配的时候不生效。
<pre>
.mixin(1)                   {x: 11}
.mixin(2)                   {y: 22}
.mixin(@x) when not(default()) {z: @x}
 
div {
  .mixin(2);  // 输出y:22;z:2;因为有匹配，会应用第二条和第三条规则
}
</pre>


===使用函数===
我们在[[帮助:在灰机使用Less/Less函数列表|这个页面]]中列出了几乎所有less函数，欢迎查阅。
