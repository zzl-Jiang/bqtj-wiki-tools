# 帮助:在CSS中使用主题色彩

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3A%E5%9C%A8CSS%E4%B8%AD%E4%BD%BF%E7%94%A8%E4%B8%BB%E9%A2%98%E8%89%B2%E5%BD%A9
revid：17996 · 抓取时间：2026-11-09T14:27:10+08:00

---

本篇帮助主要介绍如何在CSS中使用主题编辑器里配好的颜色。

== 适用场景 ==
* 主题经常变动，CSS希望自动适配。
* 在[[帮助:零件|灰机零件]]中编写CSS代码时，需要考虑不同维基的主题情况。

== 使用CSS变量 ==
如下所示，我们可以将所有的p元素设定为维基的主题色。

<syntaxhighlight lang="css" line="1">
p {
  background-color: var(--brand-primary);
}
</syntaxhighlight>

当一个颜色可能不存在时，还可以设置fallback颜色。例如，我们可以先设置a元素为主题编辑器中的a元素，但是如果该颜色不存在，就使用粉色。

<syntaxhighlight lang="css" line="1">
a {
    color: var(--detail-a, pink);
}
</syntaxhighlight>

灰机提供的CSS变量都是绑定在:root伪元素上的。查看全部CSS变量的列表，请访问[[MediaWiki:CommonStyle]]（只需要将@XXX替换为var(--XXX)即可）。关于CSS变量的详细教程，可以参阅[https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_variables]。最后需要注意的是，只有较新的浏览器才支持CSS变量。

== 使用预设class ==
灰机提供了大量的预设class，可以不写CSS，直接在HTML中调用主题颜色。

* .darken 偏黑的背景色。
* .lighten 偏亮的背景色。
* .secondary 将文字设为次要颜色。
* .text-primary 将文本设为primary颜色。
* .bg-primary将背景设为primary颜色。
* .border-primary将边框设为primary颜色。
* 以上三种表述方式同样适用于warning/danger/success/info这几种语义颜色。
* .quiet a标签会继承父级颜色。
* .badge-ribbon 发光效果。
* .alt-table 将表格设为反色。
* .alt-bg 将元素背景设为反色。
* .image-fit 将元素内的所有图片宽度设为100%，高度自动。
