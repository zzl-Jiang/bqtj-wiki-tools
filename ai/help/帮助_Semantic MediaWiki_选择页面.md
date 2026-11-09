# 帮助:Semantic MediaWiki/选择页面

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3ASemantic%20MediaWiki/%E9%80%89%E6%8B%A9%E9%A1%B5%E9%9D%A2
revid：33394 · 抓取时间：2026-11-09T14:27:10+08:00

---

'''选择页面'''（Selecting pages）是SMW嵌入式查询的第一步，即通过设置一组逻辑查询条件来缩小查询范围。本文将详细介绍相关语法。
==选择分类和属性==
下面都是合法的查询条件
*<code><nowiki>[[category:战士]]</nowiki></code>
*<code><nowiki>[[has fiction::部落]]</nowiki></code>
*<code><nowiki>[[hp::100]]</nowiki></code>
==条件组合==
===逻辑与（AND）===
当然也可以将上述条件同时书写：
*<code><nowiki>[[category:战士]] [[has fiction::部落]] [[hp::100]]</nowiki></code>
这时对于SMW来说，上述写法视为'''逻辑与'''（即AND），将会查询以上条件的合取结果。
===逻辑或（OR）===
可以通过OR来声明析取属性。
*<code><nowiki>[[category:战士]] OR [[category:圣骑士]] OR [[category:法师]]</nowiki></code>
这时SMW会查找分类为“战士”或“圣骑士”或“法师”的结果。

==模糊条件和运算符==
===模糊值===
*<code>+</code>：<nowiki>[[has fiction::+]]</nowiki>中“<code>+</code>”会查找所有has fiction值不为空的属性，不管其数值究竟为何。
*<code>*</code>：匹配任意内容，只在比较符像与不像中使用
*<code>?</code>：匹配一个任意字符，只在比较符像与不像中使用
===比较符===
例如<code><</code> 以及 <code>></code>，用在<code>::</code>之后
*<code>>></code> 和 <code><<</code> （两个>而不是》）：“大于”和“小于”
*<code>></code> 和 <code><</code> ：“大于等于”和“小于等于”，当<code>$smwStrictComparators</code> = true;时变为大于和小于
*<code>≥</code> 和 <code>≤</code> ：“大于等于”和“小于等于”
*<code>!</code>：不等于（非）
*<code>~</code>：“像”（仅限字符串）
*<code>!~</code>：“不像”（仅限字符串）
{{note}} 在比较页面标题时，会受到<code><nowiki>{{DEFAULYSORT}}</nowiki></code>的影响，需要注意

====大于/小于====
在SMW中，通过定义计量单位并定义Quantity type,比较符能够跨单位进行比较，具体参见[[help:Semantic Mediawiki/自定义计量单位]]

例如我们可以直接对长度单位进行筛选
*<code><nowiki>[[Category:Actor]] [[height::>6 ft]] [[height::<7 ft]]</nowiki></code>
即使一个单位的身高数值是<nowiki>[[height::195cm]]</nowiki>仍然可以被选中，因为quantity type会对ft（英尺）和cm（厘米）进行自动转换（需要先进行设置）。

====像/不像====
只对以下类型的属性生效：
*string（SMW1.7.x及之前）
*text、page（SMW1.8.x及之后）
*Email、telephone number、Date

可以与模糊字符“<code>*</code>”和“<code>?</code>”组合使用，例如<code><nowiki>[[Address::~*Park Place*]]</nowiki></code>可以搜寻所有address属性中包括“Park Place”的页面。<code><nowiki>[[Honorific::~M?.]]</nowiki></code>可以匹配到Mr.和Ms.
*在SMW1.7.x及之前的版本，会对String格式下的255个字符全部进行匹配，1.8.x之后只会对新文本格式中，如果字符串长度大于72，则只会对前40个字符进行比对。如果小于等于72则对72个字符进行匹配比对。
*对于属性为Page的属性，255个字符都会进行匹配比对。

====特殊符号的mask====
想查询"n:\path\morepath" 时需要书写为
<code><nowiki>{{#ask:
 [[Path::~n:\\path\\+]]
  ...
}}</nowiki></code>

====以特定符号开头的属性====
特定属性的取值可能出现以下列符号开头的情况：<、≤、>、≥、=、!以及~。 SMW会将这些符号与内置的比较操作符相混淆。为了确保并不发生这种情况，属性因而对空白敏感（white-space sensitive）。 为避免混淆，在::之后要插入一个空格。 例如，<code><nowiki>[[property:: <br>]]</nowiki></code>实际上搜索的是那些特定属性的取值为"<nowiki><br></nowiki>"的页面

==析取（disjunctions）查询的联合书写==
上文介绍了逻辑或的书写方法，例如：
*<code><nowiki>[[category:战士]] OR [[category:圣骑士]] OR [[category:法师]]</nowiki></code>
亦可以书写为
*<code><nowiki>[[category:战士||圣骑士||法师]]</nowiki></code>
===注意事项===
*联合书写仅限于同类型的属性查询，例如category和category，property与property，category和property之间不可进行联合
*由于在MySQL5.6环境下的bug，当前版本的SMW可能在灰机环境下无法正常使用联合书写语法，请静候官方升级修正这一bug
*对于一些特殊的逻辑条件，例如查询“出生在暴风城的人类或出生在铁炉堡的人类”要书写为<code><nowiki>[[category:人类]][[born in::暴风城]]OR[[category:人类]][[born in::铁炉堡]]</nowiki></code>而不是<code><nowiki>[[category:人类]][[born in::暴风城]]OR[[born in::铁炉堡]]</nowiki></code>

==描述页面==
*<code><nowiki>[[萨尔||吉安娜||User:SerGawen]]</nowiki></code>可以用来选择三个页面
*<code><nowiki>[[~Test页面/*]]</nowiki></code>可以用来选择<nowiki>Test页面/萨尔</nowiki>、<nowiki>Test页面/吉安娜</nowiki>、<nowiki>Test页面/罗宁</nowiki>等页面。
*自SMW2.1.0开始，可以通过“范围”来选择页面，例如
**<code><nowiki>[[>Test页面|1]][[<Test页面|9]]</nowiki></code>具体案例可以参考：[http://sandbox.semantic-mediawiki.org/wiki/Issue/1291 SMW官网案例]

==限定页面的命名空间（Namespace）==
*<code><nowiki>[[Help:+]]</nowiki></code>：会选择所有help（帮助）命名空间的页面
*主空间没有前缀，因此这样书写：<code><nowiki>[[:+]]</nowiki></code>
*<code><nowiki>[[:+||User:+]]</nowiki></code>：表示主空间或用户空间的所有页面

==查询嵌套==
SMW允许在查询条件中嵌套查询条件：
<code><nowiki>[[Category:Actor]] [[born in::<q>[[Category:City]] [[located in::Italy]]</q>]]</nowiki></code>
*限制：在q标签中不能出现超过1个分类，除非是析取（OR）
===.的用法===
<pre>
[[Category:Cities]]
[[located in::<q>[[member of::European Union]]</q>]]
</pre>
等价于
<pre>
[[Category:Cities]] [[located in.member of::European Union]]
</pre>
==使用模板和变量==
<pre>
 [[Category:Event]]
 [[end date::>{{CURRENTYEAR}}-{{CURRENTMONTH}}-{{CURRENTDAY}}]]
 </pre>
 
==无法实现的功能==
*查询不存在的值
*查询特殊属性：例如"Has type", "Allows value" 或者 "Equivalent URI".
*不能在分类（category）或者（concepts）中使用：<code><nowiki>{{#ask: [[Category:!City]] }}</nowiki></code>只会查询一个名为!City的分类，而不是查询所有不是City的分类。
*Subqueries for properties：It is not possible to use a subquery to obtain a list of properties that is then used in a query. One can, however, use a query that returns a list of properties, and copy and paste the result into another query. Alternatively, one can use the template results format to pass properties directly to another query.（其实我没看懂= =！）
{{navboxSMW}}
