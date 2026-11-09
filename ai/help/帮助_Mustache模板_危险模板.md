# 帮助:Mustache模板/危险模板

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3AMustache%E6%A8%A1%E6%9D%BF/%E5%8D%B1%E9%99%A9%E6%A8%A1%E6%9D%BF
revid：41797 · 抓取时间：2026-11-09T14:27:10+08:00

---

在Mustache模板中使用类似<code>{{{arg}}}</code>的方式接收参数，会导致任意非开发者用户，可以执行任意JavaScript代码，这对没有相关知识的普通用户而言是非常危险的。

因此我们决定采取以下措施
*于2023年2月6日起，灰机把使用了<code>{{{arg}}}</code>的HTML模板生成的页面，标记为[[:分类:使用危险模板的页面]]
*预计在2023年3月的某一天，启用以下新的限制：在wikitext和lua调用方式下，不再支持<code>{{{arg}}}</code>这样的参数调用方法，这样写的代码将会被视为<code><nowiki>{{arg}}</nowiki></code>

==已知有问题的模板列表==

以下是初步筛查后，Template Manager中涉及该问题的功能：
*[[templatemanager:Manifest:Accordion|Accordion]]：可使用[[templatemanager:Manifest:AccordionGreen|AccordionGreen]]替代
*[[templatemanager:Manifest:Alert|Alert]]
*[[templatemanager:Manifest:Carousel|Carousel]]：可使用[[templatemanager:Manifest:CarouselGreen|CarouselGreen]]替代
*[[templatemanager:Manifest:Dropdown|Dropdown]]
*[[templatemanager:Manifest:Pop|Pop]]
*[[templatemanager:Manifest:RichTab|RichTab]]：可使用[[templatemanager:Manifest:RichTabGreen|RichTabGreen]]或[[templatemanager:Manifest:RichTabOrange|RichTabOrange]]替代
*[[templatemanager:Manifest:Tip|Tip]]：已更新，请重新安装。也可以考虑使用[[templatemanager:Manifest:TipGreen|TipGreen]]或[[templatemanager:Manifest:鼠标提示框|鼠标提示框]]替代

[[分类:使用危险模板的页面]]
