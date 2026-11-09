# 帮助:Mustache模板

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3AMustache%E6%A8%A1%E6%9D%BF
revid：41759 · 抓取时间：2026-11-09T14:27:09+08:00

---

{{编辑手册nav}}
{{版本要求|2.1.0}}
'''MediaWiki'''因为安全问题，所支持的HTML标签有限，这造成了一些设计上的困难。为了解决这些困难，并且不放弃安全性，灰机wiki增加了HTML命名空间。该空间只对拥有[[help:用户权限|开发者]]权限的用户开放。

在HTML命名空间内，除了支持撰写原生的HTML5，还额外增加了Mustache模板支持。Mustache模板是一款短小精悍而又灵活多变的Web模板引擎。他的语法和MediaWiki有诸多相似之处，而且可以被Wikitext、PHP、Javascript、Lua同时调用。
<callout class="warning">灰机上的HTML模板的功能和实现类似于MediaWiki社区扩展#Widget，从功能上可以完全取代#Widget，故在灰机不会单独安装#Widget扩展</callout>
为了避免Mustache模板生成的代码被MediaWiki解析器干扰，生成的结果会被压缩为单行，并且在前后加上注释标记。

在灰机上，Mustache可以和[[帮助:MongoDB支持|MongoDB]]配合使用。

==使用wikitext调用==
===准备===
调用之前需要在，在HTML命名空间下创建一个页面[[Html:Test]]，其内容为：
<pre class="lang-html">
Hello {{name}}
You have just won {{value}} dollars!
{{#in_ca}}
Well, {{taxed}} dollars, after taxes.
{{/in_ca}}
</pre>

===调用===
<callout class="warning">自2.2.1起，原有的[[帮助:Mustache模板/dot写法|dot写法]]已经被[https://www.runoob.com/json/json-syntax.html json语法]取代。</callout>
页面调用示例：
<pre>{{#html:Test
|{"name":"Chris", "value":10000, "taxed":{{#expr:10000 - (10000 * 0.4)}}, "in_ca":true}
}}</pre>
'''注意：'''在使用inline样式编写代码时，应避免结尾处出现<code>}}}</code>，因为这会导致代码无法被正常解析。下面这段代码就会造成解析异常。
<pre>{{#html:Test|{"name":"Chris", "value":10000, "taxed":{{#expr:10000 - (10000 * 0.4)}}, "in_ca":true}}}</pre>
正确的写法是使用'''空格'''或'''换行'''来将<code>}}}</code>分隔开，例如：
<pre>{{#html:Test|{"name":"Chris", "value":10000, "taxed":{{#expr:10000 - (10000 * 0.4)}}, "in_ca":true} }}</pre>

===效果===
{{#html:Test
|{"name":"Chris", "value":10000, "taxed":{{#expr:10000 - (10000 * 0.4)}}, "in_ca":true}
}}
===其他功能===
====在Mustache模板中使用wikitext====
在V2.1.0更新后，Mustache模板中可以使用wikitext，代码如下：

<pre>{{#wt}}在这里添加wikitext{{/wt}}</pre>
'''注意：'''由于Mustache的<nowiki>{{}}</nowiki>依然会优先于wikitext解析，最好不要在Mustache模板中添加wikitext模板，这种方法可以用于添加内链或图片。
*如需要内嵌其他模板，可以使用Mustache的partial方式，内嵌另一个Mustache模板，调用方法是<nowiki>{{>模板名称}}</nowiki>。

==使用Javascript调用==

===调用===
<pre class="lang-javascript">
mw.loader.load('mediawiki.template.mustache');
$.get('//www.huijiwiki.com/wiki/Html:Test?action=raw').done(
	function(raw){
		var template = mw.template.compile(raw, 'mustache');
		var html = template.render({
			name: 'Chris',
			value: 10000,
			taxed: 10000 - (10000 * 0.4),
			in_ca: true
		});
		$('#mw-content-text').append(html);
	}
);
</pre>
在浏览器的控制台粘贴部分代码，就可以在本页看到结果。

===处理loader的延迟===
少数情况下，mw.loader.load可能会产生延迟、从而导致后续函数无法识别mw.template.compile。为此可以使用以下方法强制要求函数在loader加载完成后执行：
<pre class="lang-javascript">
mw.loader.using('mediawiki.template.mustache').then(function () {
    $.get('//www.huijiwiki.com/wiki/Html:Test?action=raw').done(
        function (raw) {
            var template = mw.template.compile(raw, 'mustache');
            var html = template.render({
                name: 'Chris',
                value: 10000,
                taxed: 10000 - (10000 * 0.4),
                in_ca: true
            });
            $('#mw-content-text').append(html);
        }
    );
});

</pre>

==使用Lua调用==
灰机打包的函数<code>mw.ext.mustache</code>可以处理Mustache模板，并且直接生成HTML，不会再被Parser处理，因此可以直接生成某些Wikitext禁止的标签。
<pre class="lang-lua">
local p = {}
 
function p.render(frame)
	view_model = {
	  name = "Chris",
	  value = 10000,
	  in_ca = true,
	  taxed = 10000 - (10000 * 0.4)
	}
 
	return mw.ext.mustache.render('Test', view_model)
end

return p
 
</pre>
'''<code>mw.ext.mustache.render(templateName, args, flag)</code>'''
:！注意，是高开销函数
mw.ext.mustache.render的第3个参数是一个flag（可不填，默认为false）。

;mw.ext.mustache.PERSERVE_KEY
如果该flag未填写，则自动将第二个参数'''args'''从1开始的数组（''欢迎来到Lua!''）转换成0开始的数组，以符合mustache需要。如果你需要手动处理args的键值，应该将此参数设为mw.ext.mustache.PERSERVE_KEYS。

;mw.ext.mustache.PARSE_ARGS 
如果未填写此flag，则所有args中的参数不会经过维基parser处理，也就是<nowiki>[[ABC]]</nowiki>将不会被转换成A标签。如果填写的话，<nowiki>[[ABC]]</nowiki>会变为<nowiki><a href="/wiki/ABC">ABC</a></nowiki>。

==案例==
可参阅[[Html:Table]]和[[Module:Table]]，通过Mustache模板定义了数据和表格的对应关系。

==已知的限制==
* <nowiki><a>标签内不能直接插入div，这是MediaWiki的限制，建议用span替代。即使不用Mustache模板，使用[[Link|<div>link</div>]]和[[Link|<span>link</span>]]的结果也不相同。</nowiki>
* 如果在HTML中直接使用<script>标签，那么内容中的代码会在DOM ready之前执行，该时刻JQuery还没有加载。如果想用JQuery，可以使用
<pre class="lang-js">
<script type="text/javascript">
RLQ.push(function () {
    console.log('This runs with jQuery support', $);
});
</script>
</pre>
* 不能用阿拉伯数字作为Mustache模板的参数名。

==额外限制==
2023年2月6日：以下限制暂缓执行，具体请参考[[/危险模板|危险模板]]
*<del>为了保证代码安全，灰机的Mustache模板在wikitext和lua调用方式下，不支持<code>{{{arg}}}</code>这样的参数调用方法，这样写的代码将会被视为<code><nowiki>{{arg}}</nowiki></code></del>

==Mustache官方说明文档==
[https://mustache.github.io/mustache.5.html https://mustache.github.io/mustache.5.html]
{{Data Help
|页面名=帮助:Mustache模板
|描述文字=HTML模板
|解说=Mustache
|symbol=
|主分类=帮助
|子分类=复杂
|tags=编程,维基化,设计,JS,CSS,HTML
|sortkey=51600
|关键=no
|catsortkey=4
|guide=no
|难度=复杂
|角色=开发者
|灰机功能=no
}}
