# 帮助:在灰机使用Vue.js

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3A%E5%9C%A8%E7%81%B0%E6%9C%BA%E4%BD%BF%E7%94%A8Vue.js
revid：42102 · 抓取时间：2026-11-09T14:27:10+08:00

---

{{编辑手册nav}}
本文仅供了解如何在灰机wiki使用[https://cn.vuejs.org/ Vue.js]框架进行开发

关于如何使用Vue.js的问题，请参考[https://cn.vuejs.org/v2/guide/ 官方教程]

另外还可以阅读[[帮助:使用SPA|如何在MediaWiki上开发单页应用]]获得更多信息

== 加载Vue.js ==
灰机皮肤在使用Vue.js (v3) 的同时，也将其暴露给了全局环境，使用 <code>window.cockpitVue</code> 即可访问Vue.js的API，使用方法与UMD引入相同。

在零件运行时，Vue可能尚未加载完毕。加载完毕后皮肤会持续发送 <code>externalLibsLoaded</code> 自定义事件，零件中可以监听此事件后执行相关代码。

例如：

<syntaxhighlight lang="javascript">
$(function() {
    window.addEventListener(
        "externalLibsLoaded",
        function () {
            // 此时可访问 window.cockpitVue
            cockpitVue.createApp(/* ... */).mount("#app");
        },
        { once: true } // 只执行一次
    );
});
</syntaxhighlight>

=== 旧方法 ===
由于目前使用的MediaWiki版本不支持ES6语法，在非调试模式下会直接报错，因此无法将Vue.js直接作为[[帮助:零件|零件]]加载。一种解决方案是：在零件中使用JavaScript引入Vue.js，绕过MediwWiki的解析。

例如：

<syntaxhighlight lang="javascript">
$(function() {
    // 使用jQuery从灰机CDN引入
    $.getScript("https://fs.huijiwiki.com/vue/3.5.26/vue.global.js")
        .then(function() {
            // 此时可访问 window.Vue
        });
});
</syntaxhighlight>

[[User:Honestleaf|{{#avatar:Honestleaf|sm}}Honestleaf]]提供的[[templatemanager:Manifest:Vue|Vue零件]]使用类似方法加载了Vue v2.6.10。

== 使用Vue.js ==
=== 使用构建工具 ===
使用Vite等构建工具，将Vue App构建为单个JavaScript脚本，然后通过零件引用。由于一般情况下的构建结果会包含ES6语法（而且Vue3的ref在非兼容模式下依赖Proxy实现），因此生成结果需要通过其他零件在JavaScript中引入。<small>或者通过Webpack + Babel等构建工具将生成结果限制在ES5，不推荐。</small>

一些体积较大的第三方库可以配置为external，排除在打包范围外，使用灰机皮肤内置或通过CDN单独引入，大幅减小生成结果的体积。参考的Vite配置如下，示例中使用了灰机皮肤提供的Vue，并（搭配零件）从CDN中引入NaiveUI：

<syntaxhighlight lang="typescript">
// vite.config.ts
export default defineConfig({
  // ......
  build: {
    rollupOptions: {
      external: ["vue", "naive-ui"], // 将指定依赖从构建结果排除
      output: {
        format: "iife",
        entryFileNames: "Vue_Sandbox.js", // 指定生成的文件名称
        globals: { // 指定全局变量名，代替构建时排除的依赖
          "vue": "cockpitVue",
          "naive-ui": "naive",
        },
      },
    },
  },
});
</syntaxhighlight>

构建后会生成独立的 <code>Vue_Sandbox.js</code> 文件，将该文件保存为一个零件。在另一个入口零件中使用<code>$.getScript</code>先加载NaiveUI的CDN，再加载该零件即可。例如：

<syntaxhighlight lang="javascript">
// 判断Vue零件需要加载时
$.getScript("https://fs.huijiwiki.com/naiveui/2.43.2/index.prod.js") // 从CDN加载NaiveUI
    .then(function () {
        $.getScript("/wiki/Gadget:Vue_Sandbox.js?action=raw"); // 加载完成后，加载Vue_Sandbox.js
    });
</syntaxhighlight>

在实际使用时，建议更改Vue的挂载目标元素（默认的<code>#app</code>），以便于将不同Vue零件通过统一入口零件加载、通过统一模板调用。见Workshop中的[[templatemanager:Manifest:VueEntries|VueEntries]]（还没写）。

=== 使用Mustache模板 ===
搭配[[帮助:Mustache模板|Mustache模板]]，也可以直接在Wiki中编写HTML模板。但需要做出一定调整，修改Mustache模板中的定界符<code><nowiki>{{ }}</nowiki></code>：

<pre>
<!-- {{=<% %>=}} -->
</pre>

在HTML模板的行首添加此注释，即可将模板的定界符更换为<code><nowiki><% %></nowiki></code>；<code><nowiki>{{ }}</nowiki></code>则会保留在生成的页面上，供Vue使用。

使用时可能会遇到以下问题：
{| class="wikitable"
! 问题 !! 说明
|-
| ES6语法 || 直接执行的零件不能包含ES6语法
|-
| HTML模板中出现<code><nowiki> :</nowiki></code>
| 半角空格+半角冒号的组合会解析错误，需要回避，常见情况包括：
* 使用了v-bind的缩写形式，例如<code><nowiki><div :title="xxx"></nowiki></code>
* 使用了对象，例如<code>v-bind:class="{ enable : isOK() }"</code>，需要删除半角冒号前的空格
|}
{{Data Help
|页面名=帮助:在灰机使用Vue.js
|描述文字=使用Vue.js
|解说=
|symbol=
|主分类=帮助
|子分类=复杂
|tags=开发,编程,JS
|sortkey=51800
|关键=no
|catsortkey=4
|guide=no
|难度=复杂
|角色=开发者
|灰机功能=yes
}}
