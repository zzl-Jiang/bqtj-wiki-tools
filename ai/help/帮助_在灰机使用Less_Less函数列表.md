# 帮助:在灰机使用Less/Less函数列表

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3A%E5%9C%A8%E7%81%B0%E6%9C%BA%E4%BD%BF%E7%94%A8Less/Less%E5%87%BD%E6%95%B0%E5%88%97%E8%A1%A8
revid：41553 · 抓取时间：2026-11-09T14:27:10+08:00

---

本文是[https://lesscss.org/functions/ Less官方文档-函数]的译本，根据灰机和HuijiLess的实际情况有改动。

==逻辑函数==
由于css基本没有true或false的关键字，逻辑函数通常在混入守卫（mixin guard）中使用。
===if()===
根据condition的布尔结果返回第二个或第三个参数值。

参数：
*condition：布尔型表达式
*value1：如果condition为true的返回值
*value2：如果condition为false的返回值

返回：value2或value3

<pre>@some: foo;

div {
    margin: if((2 > 1), 0, 3px);
    color:  if((iscolor(@some)), @some, black); // 如果变量some是色值则原样输出，否则输出black
}</pre>

===boolean()===
输出表达式的计算结果。

参数：
*condition：布尔型表达式

返回：true或false。

<pre>@bg: black;
@bg-light: boolean(luma(@bg) > 50%);

div {
  background: @bg; 
  color: if(@bg-light, black, white);
}</pre>

==字符串函数==
===escape()===
将输入的字符串转义。

参数：需要转义的字符串。

返回：转义后的字符串。
<pre>
.test {
  result:escape('a=1') // result:a%3D1
}
</pre>
===e()===
用于输出CSS不支持、less也不支持的语法（<strike>IE罪大恶极</strike>）

参数：字符串

返回：移除引号的字符串。

<pre>
@mscode: "ms:alwaysHasItsOwnSyntax.For.Stuff()" 
.test {
filter: e(@mscode);
}
//输出filter: ms:alwaysHasItsOwnSyntax.For.Stuff();

</pre>

===%()===
按照一定的规则进行模板字符串替换。

参数：
*参数1：模板字符串。见下文“占位符”。
*其余参数：用于替换模板字符串中的占位符或表达式。

输出：字符串

占位符：
*d,D,a,A - 可以被替换为任意类型的参数。如果使用大写占位符（D和A），则输出文本会被escape。输出文版本将包含引号。
*s,S - 可以被替换为表达式。如果表达式是文本，则文本的引号将不会输出。
<pre>
.test{
  format-a-d: %("repetitions: %a file: %d", 1 + 2, "directory/file.less");
  format-a-d-upper: %('repetitions: %A file: %D', 1 + 2, "directory/file.less");
  format-s: %("repetitions: %s file: %s", 1 + 2, "directory/file.less");
  format-s-upper: %('repetitions: %S file: %S', 1 + 2, "directory/file.less");
}
// 输出
.test {
  format-a-d: "repetitions: 3 file: "directory/file.less"";
  format-a-d-upper: 'repetitions: 3 file: %22directory%2Ffile.less%22';
  format-s: "repetitions: 3 file: directory/file.less";
  format-s-upper: 'repetitions: 3 file: directory%2Ffile.less';
}
</pre>

===replace()===
替换文本。

参数：
*string - 原始文本
*pattern - 需要搜索的词或者正则表达式。
*replacement - 需要替换的文本（如果使用正则，则使用$x代表第x个捕获组）
*flags - 正则匹配的flag，可选参数。

输出：字符串
<pre>
replace("Hello, Mars?", "Mars\?", "Earth!");
replace("One + one = 4", "one", "2", "gi");
replace('This is a string.', "(string)\.$", "new $1.");
replace(~"bar-1", '1', '2'); // 注意这里用~消除了输入字符串的引号

// 输出
"Hello, Earth!";
"2 + 2 = 4";
'This is a new string.';
bar-2;
</pre>

==列表函数==
===length()===
返回列表长度。

参数：一个列表。

返回：数值

<pre>
@list: "banana", "tomato", "potato", "peach";
n: length(@list); // 返回4
</pre>

===extract()===
返回列表指定位置的元素。注意列表位置由1开始。

参数：
*list - 需要检索的列表
*index - 位置，数值
<pre>
extract(8px dotted red, 2); // 返回dotted

@list: apple, pear, coconut, orange;
value: extract(@list, 3); // 返回value:coconut

</pre>


===range()===
生成一个指定范围的列表。

参数：
*start：起始值
*end：最终值
*step：步长，可选参数。

返回：列表

<pre>
value: range(4); // 返回value:1 2 3 4
value:range(5px,10px); //返回value: 5px 6px 7px 8px 9px 10px;
value:range(18em,36em,4); //返回value: 18em 22em 26em 30em 34em;
</pre>

===each()===
依次对列表中每一个元素执行一遍指定规则。
规则中可以使用如下

参数：
*list - 一个列表，可以是逗号或空格分隔的列表。
**样式块也可以用作key-value型的列表。
*rules - 一个样式块或mixin

返回：无，rules将原地输出。

在rules中可以使用如下变量：
*@value:列表中指定项的值
*@index:列表中指定项的序号
*@key:在使用样式块作为列表时，指定项的属性名。
<pre>
@selectors: blue, green, red;

each(@selectors, {
  .sel-@{value} {
    a: b;
  }
});

// 输出
.sel-blue {
  a: b;
}
.sel-green {
  a: b;
}
.sel-red {
  a: b;
}
</pre>
使用样式块作为列表：
<pre>
@set: {
  one: blue;
  two: green;
  three: red;
}
.set {
  each(@set, {
    @{key}-@{index}: @value;
  });
}

// 输出
.set {
  one-1: blue;
  two-2: green;
  three-3: red;
}
</pre>

=====使用“函数”=====
由于第二个参数可以是mixin，而mixin可以作为函数使用，变量@key,@value,@index也可以用这种方法重命名。

这里用到了Less3.7的匿名mixin特性（仅在each()中使用）。

<pre>
.set-2() {
  one: blue;
  two: green;
  three: red;
}
.set-2 {
  each(.set-2(), .(@v, @k, @i) { //注意参数2现在是一个匿名mixin
    @{k}-@{i}: @v;
  });
}
// 输出
.set-2 {
  one-1: blue;
  two-2: green;
  three-3: red;
}
</pre>
如果匿名mixin的参数区域只填写两个或一个参数名，则参数会按照value，key，index的顺序取值。

=====使用each()和range()构建一个for循环=====

<pre>each(range(4), {
  .col-@{value} {
    height: (@value * 50px);
  }
});

// 输出
.col-1 {
  height: 50px;
}
.col-2 {
  height: 100px;
}
.col-3 {
  height: 150px;
}
.col-4 {
  height: 200px;
}
</pre>

==数学函数==
===ceil()===
接受一个数值参数（包括带单位的数值），向上取整。
<pre>
ceil(2.4) // 输出3
ceil(24.5px) // 输出25px
</pre>
===floor()===
与ceil类似，但向下取整。

===percentage()===
将数值转化为百分比。如果数值中带有单位，则单位会被忽略。

===round()===
取特定位的小数。

参数：
*number：需要取小数的数值
*digit：可选参数，保留小数的位数。
<pre>
round(1.6) // 输出2
round(3.1415926,3) // 输出3.142
</pre>

===sqrt()===
计算平方根。单位将保留。
<pre>
sqrt(16) // 输出4
sqrt(28px) // 输出5.29150262px
</pre>

===abs()===
取绝对值。单位会被保留。

===sin()===
取正弦值。

如果传入无单位的数字，则视为rad单位。也可以传入deg和grad为单位的数值。
===asin()===
取反正弦值。输出结果的单位为rad。
===cos()===
取余弦值，见sin()
===acos()===
取反余弦值，见asin()
===tan()===
取正切值，见sin()
===atan()===
取反正切值，见asin()
===pi()===
输出π的值，无单位。
===pow()===
幂运算。

参数：
*base-底数
*exponent-幂数

输出的单位始终与base保持一致。
<pre>
pow(0cm, 0px) // 输出1cm
pow(25, -2) // 输出0.0016
pow(25, 0.5) // 输出5
pow(-25, 0.5) // 输出NaN
pow(-25%, -0.5) //输出NaN%
</pre>

===mod()===
取余数。

参数：
*被除数
*除数

输出单位始终与被除数一致。
<pre>
mod(0cm, 0px); // 输出NaNcm，0不能做除数
mod(11cm, 6px); // 输出5cm，11除6商1余5
mod(-26%, -5); // 输出-1%
</pre>

===min()===
取输入的若干参数中的最小值。

如果参数的单位不一致，将原样输出。

<pre>
min(1px,25px,6px) // 输出1px
min(10%,25px,6em) // 输出min(10%, 25px, 6em)
</pre>

===max()===
取输入的若干参数中的最大值。

如果参数的单位不一致，将原样输出。

见min()

==类型判断函数==
本节中所指的类型为css token的类型。csstoken分为如下几种：
*number：数字或带单位的数字
*color：色值或命名颜色（如red）
*string：由引号包裹的文本，例如grid-area
*keyword：无引号包裹的文本（less不会判断该keyword是否有效）
*url：由url()包裹的文本

对应地，函数分为如下若干个：
*isnumber()
*iscolor()
*isstring()
*iskeyword()
*isurl()
对于number类型，还有如下函数可以用来判断单位：
*ispixel()
*isem()
*ispercentage()
其他单位可以通过以下函数判断：
*isunit(number,unit)

对于样式块变量，还可以通过以下函数判断：
*isruleset(var)

另外，可以通过以下函数判断变量是否已定义：
*isdefined(var)

上述所有函数均输出布尔型结果。

综合前文的'''for循环'''知识，这里使用each和匿名函数进行了一次批量判断：
<pre>.values() {
  number:12;
  unit-number:24px;
  color:#333;
  named-color:red;
  string:'area-51';
  keyword:inset;
  url:url('localhost');
}

each(.values(),.(@v,@k,@i) {
.@{k} {
  rawvalue:@v;
  isnumber:isnumber(@v);
  iscolor:iscolor(@v);
  isstring:isstring(@v);
  iskeyword:iskeyword(@v);
  isurl:isurl(@v)
}    
})</pre>
判断结果：
<pre>
.number {
  rawvalue: 12;
  isnumber: true;
  iscolor: false;
  isstring: false;
  iskeyword: false;
  isurl: false;
}
.unit-number {
  rawvalue: 24px;
  isnumber: true;
  iscolor: false;
  isstring: false;
  iskeyword: false;
  isurl: false;
}
.color {
  rawvalue: #333;
  isnumber: false;
  iscolor: true;
  isstring: false;
  iskeyword: false;
  isurl: false;
}
.named-color {
  rawvalue: red;
  isnumber: false;
  iscolor: true;
  isstring: false;
  iskeyword: false;
  isurl: false;
}
.string {
  rawvalue: 'area-51';
  isnumber: false;
  iscolor: false;
  isstring: true;
  iskeyword: false;
  isurl: false;
}
.keyword {
  rawvalue: inset;
  isnumber: false;
  iscolor: false;
  isstring: false;
  iskeyword: true;
  isurl: false;
}
.url {
  rawvalue: url('localhost');
  isnumber: false;
  iscolor: false;
  isstring: false;
  iskeyword: false;
  isurl: true;
}
</pre>

==颜色定义==
多数函数与CSS中的颜色函数一致，且与CSS3可能有冲突。不建议使用。

==颜色通道函数==
===hue()===
输入一个色值，返回色相角度（0-360）

===saturation()===
输入一个色值，返回色值饱和度（0%-100%）

===lightness()===
输入一个色值，返回色值亮度（0%-100%）

===hsvhue()===
输入一个色值，返回色值在hsv色彩空间中的色相角度（0-360）

===hsvsaturation()===
输入一个色值，返回色值在hsv色彩空间中的饱和度（0%-100%）

===hsvvalue()===
输入一个色值，返回色值在hsv色彩空间中的明度（0%-100%）

===red()===
输入一个色值，返回red通道的数值（0-255）

===blue()===
输入一个色值，返回blue通道的数值（0-255）

===green()===
输入一个色值，返回green通道的数值（0-255）

===alpha()===
输入一个色值，返回alpha通道的数值（0-1）

===luma()===
输入一个色值，返回该色值的[https://handsomeone.gitbooks.io/color-faq-cn/content/docs/11.html 视频亮度（LUMA）]（0-100%）

===luminance()===
同luma()，但不包括gamma矫正。


==颜色运算函数==

以下函数除特别说明，均接受三个参数：
*color：输入色值
*amount：提高或降低的百分比
*method：可选参数，填写relative则按照当前的该属性提高或降低（而不是按照实际值提高或降低）

返回值均为另一个色值。

===saturate()===
提高饱和度。

===desaturate()===
降低饱和度。

===lighten()===
提高亮度。

===darken()===
降低亮度。

===fadein()===
提高不透明度（降低透明度）

===fadeout()===
降低不透明度（提高透明度）

===fade()===
输入一个色值（参数1），并设定不透明度（参数2）。

对原先有/无alpha通道的色值同样有效。不接受参数3。

===spin()===
输入一个色值（参数1），将其色相旋转一定角度（参数2）。

参数2为任意无单位数值，实际单位为度。运算时会对360取模，因此可以输入比360大的数值。

===mix()===
输入两个色值，并按照一定权重混合。

参数：
*参数1和参数2：色值
*参数3：可选参数，两个色值的权重比。默认值为50%。

===tint()===
混合纯白和另一个颜色。

参数1：被混合的颜色。
参数2：可选，被混合颜色的权重（默认值50%）

实际相当于<code>mix(#ffffff, @color, @weight)</code>

===shade()===
混合纯黑和另一个颜色。

参数1：被混合的颜色。
参数2：可选，被混合颜色的权重（默认值50%）

实际相当于<code>mix(#000000, @color, @weight)</code>


===greyscale()===
移除输入色值的饱和度。相当于<code>desaturate(@color, 100%)</code>

注意，使用greyscale()灰度化的颜色看起来比原始颜色要暗。例如<span style="background-color:#80f20d">#80f20d</span>灰度化后会变为<span style="background-color:#808080">#808080</span>。

一个更合适的方法是使用'''luma()'''生成视频亮度（即可感知的灰度），如：
<pre>@c: luma(#80f20d); // 约为68%，而#808080的luma为21%
color: rgb(@c, @c, @c);</pre>

这样，<span style="background-color:#80f20d">#80f20d</span>和使用luma()灰度化的<span style="background-color:#CACACA">#CACACA</span>的可视亮度就基本一致了。

===contrast()===
输出一个与输入颜色对比度最高的颜色（从黑白或参数2，3中选）。

参数：
*color：输入的颜色，被对比的颜色。
*dark：可选参数，默认值为black。
*light：可选参数，默认值为white。
*threshold：可选参数，取值范围为0到100%，默认值43%。决定从dark到light之间哪一个节点是“中间灰”。

==色彩混合函数==
本节的函数均接受两个色彩参数，分别是叠加层（上）和被叠加层（下）的颜色。
===multiply()===
输出正片叠底（multiply）的运算结果。

===screen()===
输出滤色（screen）的运算结果。

===overlay()===
输出叠加（overlay）的运算结果。

===softlight()===
输出柔光（softlight）的运算结果。

===hardlight()===
输出强光（hardlight）的运算结果。

===difference()===
输出差值（difference）的运算结果。

===exclusion()===
输出排除（exclusion）的运算结果。

===average()===
取两个颜色的中间色。

===negation()===
输出与difference()相反的运算结果。

注，不代表反色。




==其他函数==
===color()===
将一个字符串转为色值。
例如，color('#333')将输出#333。

如果输入内容不是字符串，或格式不符合色值要求，则会报错。

===convert()===
将一个带数值的单位转为另一个单位。

只有与原始数据类型相同的单位可以互相转换，相对单位无法转换（例如em、vm等）。

支持转换的类型有：
*长度：m,cm,mm,in,pt,pc
*时间：s,ms
*角度：rad,deg,grad,turn

参数：
*number：原始值
*unit：单位名称。单位名称可以是字符串或无引号的字符串（例如'mm'和mm同义）

如果单位之间无法兼容，将原样输出参数1。

===default()===
仅在混入守卫中使用。在其他的守卫均返回false时返回true以设置混入的默认值。

<pre>
.mixin(1)                   {x: 11}
.mixin(2)                   {y: 22}
.mixin(@x) when (default()) {z: @x}

div {
  .mixin(3);  // 输出z=3，因为前两条都无效
}

div.special {
  .mixin(1); // 输出x:11
}
</pre>
也可以与守卫操作符not共用，以表达“在有匹配的情况下全部适用”
<pre>
.mixin(@value) when (ispixel(@value)) {width: @value}
.mixin(@value) when not(default())    {padding: (@value / 5)}

div-1 {
  .mixin(100px); // 100px是pixel，所以会输出width:100px;且有匹配，所以会输出padding:50px
}

div-2 {
  /* ... */
  .mixin(100%); // 无匹配，所以什么都不会输出
}
</pre>

===unit()===
添加、改变或删除数值的单位。

参数：
*参数1：任意数值
*单位：可选。如果不填写则移除单位。

注意unit函数'''不会进行换算'''，只会添加、删除或改变单位。
<pre>
.test {
  length:5px;
  mod-length1:unit($length);
  mod-length2:unit($length,cm)
}
// 输出
.test {
  color: #333;
  length: 5px;
  mod-length1: 5;
  mod-length2: 5cm;
}
</pre>
===get-unit()===
返回一个数值的单位。如果无单位则什么都不会返回。

===svg-gradient()===
生成一个url字符串，其中是通过本函数生成的svg文档。

参数：
*参数1：方向，例如to bottom等。
*参数2及后续：
**如果参数2传入一个list，则该list代表多个颜色及其拖柄位置；
**如果参数2是一个单一元素，则参数2及剩余所有参数代表展开的颜色及拖柄位置。

输出url(XXXXX)，其中XXXX是生成的svg渐变的代码。

例1：使用list
<pre>
div {
  @list: red, green 30%, blue;
  background-image: svg-gradient(to right, @list);
}
</pre>
例2：使用多个参数
<pre>
div {
  background-image: svg-gradient(to right, red, green 30%, blue);
}
</pre>
上述两例等同，输出如下：
<pre>
div {
  background-image: url('data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3ClinearGradient%20id%3D%22g%22%20x1%3D%220%25%22%20y1%3D%220%25%22%20x2%3D%22100%25%22%20y2%3D%220%25%22%3E%3Cstop%20offset%3D%220%25%22%20stop-color%3D%22%23ff0000%22%2F%3E%3Cstop%20offset%3D%2230%25%22%20stop-color%3D%22%23008000%22%2F%3E%3Cstop%20offset%3D%22100%25%22%20stop-color%3D%22%230000ff%22%2F%3E%3C%2FlinearGradient%3E%3Crect%20x%3D%220%22%20y%3D%220%22%20width%3D%221%22%20height%3D%221%22%20fill%3D%22url(%23g)%22%20%2F%3E%3C%2Fsvg%3E');
}
</pre>
