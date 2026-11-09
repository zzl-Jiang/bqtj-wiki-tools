# 帮助:Tailwind CSS参考

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3ATailwind%20CSS%E5%8F%82%E8%80%83
revid：42224 · 抓取时间：2026-11-09T14:27:10+08:00

---

{{编辑手册nav}}
'''Tailwind CSS'''是一个著名的CSS框架，它最大的特点是使用声明式的方式来为页面添加样式。它改变了传统对于应用页面样式的思路，很多人可能不是很适应这种风格来定义页面样式，尤其是已经适应传统在wiki定义样式方式的编辑者。但是，一旦接受了Tailwind这种设定，构建复杂版式的页面会变得乐趣无穷。

Tailwind的主要优点是：
* 声明式的响应式class，页面适配手机和桌面不再是个痛苦的事情。
* 使用CSS3的布局系统，抛弃table，排版更为灵活容易。
* 使用规范的单位，很容易统一站点里的间距、字号等风格。

== 应用原理 ==
Tailwind本身定义了相当多的class名称，每个class都有对应的样式。借助于常用的<code><nowiki><div></nowiki></code>标签（或者其他mediawiki允许使用的标签），可以在<code>class</code>属性上写上想要的名称，便可以实现对div应用样式效果。

而你要做的，就是熟练掌握各名称及其对应的样式效果。

== 为站点启用Tailwind ==
默认情况下，站点是没有启用Tailwind功能的，需要管理员前往驾驶室页面，在机长室中可以开启。

灰机的Tailwind由于需要对现有皮肤样式的兼容，所以有一定的修改，但整体上不影响使用。

===配置===

由于Tailwind CSS的默认样式与灰机皮肤中使用的[[帮助:BOOTSTRAP|Bootstrap]]样式冲突，所以会默认加载了以下Tailwind CSS配置
<pre>
tailwind.config = {
    corePlugins: { preflight: false, container: false },
    theme: {
        screens: {
            sm: '576px',
            md: '768px',
            lg: '992px',
            xl: '1200px',
            '2xl': '1366px',
            '3xl': '1600px',
        },
    },
};
</pre>

如需自定义配置，请在自己站点的<code>Common.js</code>中，添加以下代码
<pre>
window.tailwindconfig = {
    ...
}
</pre>
注意：这里添加的是<code>tailwindconfig</code>，而不是<code>tailwind.config</code>。这是由于脚本加载顺序的缘故，当Common.js加载到页面时，Tailwind CSS还没有加载，导致tailwind对象不存在，无法使用<code>tailwind.config</code>进行配置。当加载Tailwind CSS完成后，会检查是否存在<code>tailwindconfig</code>，如果存在则使用<code>tailwindconfig</code>作为配置（此时不会加载默认配置，如需包含请复制一份），否则使用上面的默认配置。

除此之外还有其他样式会发生冲突，发生冲突时，可以使用<code>tailwind</code>的important语法（在class名之前加<code>!</code>），例如<code>!text-black</code>

===已知冲突===
以下为目前已知的因为huiji自身样式表导致冲突的部分
{| class="wikitable"
!class名称||冲突说明
|-
|<code>hidden</code>||huiji的样式表中定义该class的样式为<code>display: none !important</code>，导致Tailwind的切换display无法生效，解决办法为同时使用Tailwind的important（在原class前加<code>!</code>），例如<code>class="hidden md:!block"</code>可以让元素在移动端下隐藏并在768px以上时显示成block元素
|-
|<code>collapse</code>||已知会与MediaWiki的collapse冲突，导致Mediwiki的collapse的内容被隐藏，解决办法为自行添加以下样式来禁用Tailwind的样式：<code>.collapse {visibility: visible !important;}</code>
|}

== 参考手册 ==
Tailwind的内容十分庞大，本页面无法涵盖到全部内容，只会列出常用且有用的class，如果想了解更多的内容，可以直接访问[https://v3.tailwindcss.com/docs/ 官方文档（英文）]。

=== 优先级 ===
CSS样式类是有优先级的，优先级高的样式类会覆盖掉低优先级的样式。优先级的规则十分复杂，但基本的规则是，描述的越具体的选择符（css selector）优先级越高。本帮助不会涉及CSS本身的知识，这里只举一个简单的例子：在<code>.toolbox .title</code>里定义的样式会覆盖掉在<code>.toolbox</code>里定义的同名样式。

灰机基础皮肤很多的样式类都描述的很具体，这些样式通常会比你直接写在<code>class</code>属性里的类优先级要高，通常这不会有问题。但在一些特殊的情况下，你必须要覆盖灰机应用的样式，则可以在Tailwind的样式类名前加一个<code>!</code>前缀，这将给对应的css样式设置<code>!important</code>标记，带这个标记的样式优先级会高于任何不带这个标记的。比如使用<code>!text-lg</code>则代表你需要覆盖任何其他和字体大小相关的样式，而使用你的大小定义。

=== 响应式设计 ===
辅助响应式设计是Tailwind最大的价值所在。

响应式布局用于适配各种不同大小（宽度）的屏幕下，页面的显示效果。如果你想让页面在手机、平台以及PC桌面上都能完整呈现的话，则需要掌握响应式设计的知识。如果你计划站点只支持在电脑上呈现，或者只能在手机上呈现，则可以跳过这部分。

在CSS中，设计响应式界面是一个十分复杂的过程，不过在Tailwind的帮助下，我们可以很轻松地达到以往要调试很久的效果。

Tailwind遵循手机优先的响应式定义，也就是你的默认样式应该为手机屏幕设计，然后再一层层补充更宽屏幕下的效果。

在响应式设计中，为了规范和实现标准，我们会给指定的宽度取一个名字（前缀），这个名字又称为“断点”。灰机覆盖了Tailwind默认的断点宽度，下表是灰机定义的前缀及其对应的屏幕宽度：
{| class="wikitable"
|-
! 类名前缀
| <code>sm:</code>
| <code>md:</code>
| <code>lg:</code>
| <code>xl:</code>
| <code>2xl:</code>
| <code>3xl:</code>
|-
! 屏幕宽度
| <code>576px</code>
| <code>768px</code>
| <code>992px</code>
| <code>1200px</code>
| <code>1366px</code>
| <code>1600px</code>
|}
这个表格的意思是说，当浏览网页的设备屏幕宽度大于等于指定的宽度时，应用带有指定前缀指定的样式类效果。

比如，以下的HTML：
<pre><div class="bg-yellow-200 w-full lg:w-1/2">这个黄色的方块默认占据整行，但是如果你的设备宽度大于992像素则占据页面一半的宽度。</div></pre>

会呈现为：
<div class="bg-yellow-200 w-full lg:w-1/2">这个黄色的方块默认占据整行，但是如果你的设备宽度大于992像素则占据页面一半的宽度。</div>

你可以通过调整浏览器窗口大小来看看具体的效果。

我们可以看到这里使用了3个class：<code>bg-yellow-200</code>、<code>w-full</code>以及<code>lg:w-1/2</code>。<code>bg-yellow-200</code>定义了这个<code>div</code>的背景色，<code>w-full</code>是说默认宽度占满其父容器的100%，而<code>w-1/2</code>代表占满父容器的二分之一，也就是50%。前缀<code>lg:</code>代表只有在屏幕宽度大于992像素时，这一条才会生效。

上面各样式类名称的意义会在下面有进一步解释，此时只需要了解响应式前缀的使用方法。没有前缀的样式为默认样式，可以理解为页面在所支持的最小屏幕宽度上的样式。

=== 颜色表 ===
Tailwind自带一套颜色调色板，由两个部分组成：颜色和亮度，其中颜色是一个英文单词，亮度是一个数字，范围从50-950，除了50和950之外，剩余的都是100的倍数，数字越小，颜色越亮，反之越暗，500为原始亮度。Tailwind所有定义颜色的类名都支持这个调色板，比如<code>text-red-700</code>代表给文字应用<span class="text-red-700">亮度值为700的red色</span>，而<code>bg-red-700</code>使用了同一个颜色，<span class="bg-red-700 text-white">但是作用于背景色</span>。

以下是具体的调色板：
{| class="wikitable"
|-
!
! style="width: 50px" | 50
! style="width: 50px" | 100
! style="width: 50px" | 200
! style="width: 50px" | 300
! style="width: 50px" | 400
! style="width: 50px" | 500
! style="width: 50px" | 600
! style="width: 50px" | 700
! style="width: 50px" | 800
! style="width: 50px" | 900
! style="width: 50px" | 950
|-
! slate
| class="bg-slate-50" |
| class="bg-slate-100" |
| class="bg-slate-200" |
| class="bg-slate-300" |
| class="bg-slate-400" |
| class="bg-slate-500" |
| class="bg-slate-600" |
| class="bg-slate-700" |
| class="bg-slate-800" |
| class="bg-slate-900" |
| class="bg-slate-950" |
|-
! gray
| class="bg-gray-50" |
| class="bg-gray-100" |
| class="bg-gray-200" |
| class="bg-gray-300" |
| class="bg-gray-400" |
| class="bg-gray-500" |
| class="bg-gray-600" |
| class="bg-gray-700" |
| class="bg-gray-800" |
| class="bg-gray-900" |
| class="bg-gray-950" |
|-
! zinc
| class="bg-zinc-50" |
| class="bg-zinc-100" |
| class="bg-zinc-200" |
| class="bg-zinc-300" |
| class="bg-zinc-400" |
| class="bg-zinc-500" |
| class="bg-zinc-600" |
| class="bg-zinc-700" |
| class="bg-zinc-800" |
| class="bg-zinc-900" |
| class="bg-zinc-950" |
|-
! neutral
| class="bg-neutral-50" |
| class="bg-neutral-100" |
| class="bg-neutral-200" |
| class="bg-neutral-300" |
| class="bg-neutral-400" |
| class="bg-neutral-500" |
| class="bg-neutral-600" |
| class="bg-neutral-700" |
| class="bg-neutral-800" |
| class="bg-neutral-900" |
| class="bg-neutral-950" |
|-
! stone
| class="bg-stone-50" |
| class="bg-stone-100" |
| class="bg-stone-200" |
| class="bg-stone-300" |
| class="bg-stone-400" |
| class="bg-stone-500" |
| class="bg-stone-600" |
| class="bg-stone-700" |
| class="bg-stone-800" |
| class="bg-stone-900" |
| class="bg-stone-950" |
|-
! red
| class="bg-red-50" |
| class="bg-red-100" |
| class="bg-red-200" |
| class="bg-red-300" |
| class="bg-red-400" |
| class="bg-red-500" |
| class="bg-red-600" |
| class="bg-red-700" |
| class="bg-red-800" |
| class="bg-red-900" |
| class="bg-red-950" |
|-
! orange
| class="bg-orange-50" |
| class="bg-orange-100" |
| class="bg-orange-200" |
| class="bg-orange-300" |
| class="bg-orange-400" |
| class="bg-orange-500" |
| class="bg-orange-600" |
| class="bg-orange-700" |
| class="bg-orange-800" |
| class="bg-orange-900" |
| class="bg-orange-950" |
|-
! amber
| class="bg-amber-50" |
| class="bg-amber-100" |
| class="bg-amber-200" |
| class="bg-amber-300" |
| class="bg-amber-400" |
| class="bg-amber-500" |
| class="bg-amber-600" |
| class="bg-amber-700" |
| class="bg-amber-800" |
| class="bg-amber-900" |
| class="bg-amber-950" |
|-
! yellow
| class="bg-yellow-50" |
| class="bg-yellow-100" |
| class="bg-yellow-200" |
| class="bg-yellow-300" |
| class="bg-yellow-400" |
| class="bg-yellow-500" |
| class="bg-yellow-600" |
| class="bg-yellow-700" |
| class="bg-yellow-800" |
| class="bg-yellow-900" |
| class="bg-yellow-950" |
|-
! lime
| class="bg-lime-50" |
| class="bg-lime-100" |
| class="bg-lime-200" |
| class="bg-lime-300" |
| class="bg-lime-400" |
| class="bg-lime-500" |
| class="bg-lime-600" |
| class="bg-lime-700" |
| class="bg-lime-800" |
| class="bg-lime-900" |
| class="bg-lime-950" |
|-
! green
| class="bg-green-50" |
| class="bg-green-100" |
| class="bg-green-200" |
| class="bg-green-300" |
| class="bg-green-400" |
| class="bg-green-500" |
| class="bg-green-600" |
| class="bg-green-700" |
| class="bg-green-800" |
| class="bg-green-900" |
| class="bg-green-950" |
|-
! emerald
| class="bg-emerald-50" |
| class="bg-emerald-100" |
| class="bg-emerald-200" |
| class="bg-emerald-300" |
| class="bg-emerald-400" |
| class="bg-emerald-500" |
| class="bg-emerald-600" |
| class="bg-emerald-700" |
| class="bg-emerald-800" |
| class="bg-emerald-900" |
| class="bg-emerald-950" |
|-
! teal
| class="bg-teal-50" |
| class="bg-teal-100" |
| class="bg-teal-200" |
| class="bg-teal-300" |
| class="bg-teal-400" |
| class="bg-teal-500" |
| class="bg-teal-600" |
| class="bg-teal-700" |
| class="bg-teal-800" |
| class="bg-teal-900" |
| class="bg-teal-950" |
|-
! cyan
| class="bg-cyan-50" |
| class="bg-cyan-100" |
| class="bg-cyan-200" |
| class="bg-cyan-300" |
| class="bg-cyan-400" |
| class="bg-cyan-500" |
| class="bg-cyan-600" |
| class="bg-cyan-700" |
| class="bg-cyan-800" |
| class="bg-cyan-900" |
| class="bg-cyan-950" |
|-
! sky
| class="bg-sky-50" |
| class="bg-sky-100" |
| class="bg-sky-200" |
| class="bg-sky-300" |
| class="bg-sky-400" |
| class="bg-sky-500" |
| class="bg-sky-600" |
| class="bg-sky-700" |
| class="bg-sky-800" |
| class="bg-sky-900" |
| class="bg-sky-950" |
|-
! blue
| class="bg-blue-50" |
| class="bg-blue-100" |
| class="bg-blue-200" |
| class="bg-blue-300" |
| class="bg-blue-400" |
| class="bg-blue-500" |
| class="bg-blue-600" |
| class="bg-blue-700" |
| class="bg-blue-800" |
| class="bg-blue-900" |
| class="bg-blue-950" |
|-
! indigo
| class="bg-indigo-50" |
| class="bg-indigo-100" |
| class="bg-indigo-200" |
| class="bg-indigo-300" |
| class="bg-indigo-400" |
| class="bg-indigo-500" |
| class="bg-indigo-600" |
| class="bg-indigo-700" |
| class="bg-indigo-800" |
| class="bg-indigo-900" |
| class="bg-indigo-950" |
|-
! violet
| class="bg-violet-50" |
| class="bg-violet-100" |
| class="bg-violet-200" |
| class="bg-violet-300" |
| class="bg-violet-400" |
| class="bg-violet-500" |
| class="bg-violet-600" |
| class="bg-violet-700" |
| class="bg-violet-800" |
| class="bg-violet-900" |
| class="bg-violet-950" |
|-
! purple
| class="bg-purple-50" |
| class="bg-purple-100" |
| class="bg-purple-200" |
| class="bg-purple-300" |
| class="bg-purple-400" |
| class="bg-purple-500" |
| class="bg-purple-600" |
| class="bg-purple-700" |
| class="bg-purple-800" |
| class="bg-purple-900" |
| class="bg-purple-950" |
|-
! fuchsia
| class="bg-fuchsia-50" |
| class="bg-fuchsia-100" |
| class="bg-fuchsia-200" |
| class="bg-fuchsia-300" |
| class="bg-fuchsia-400" |
| class="bg-fuchsia-500" |
| class="bg-fuchsia-600" |
| class="bg-fuchsia-700" |
| class="bg-fuchsia-800" |
| class="bg-fuchsia-900" |
| class="bg-fuchsia-950" |
|-
! pink
| class="bg-pink-50" |
| class="bg-pink-100" |
| class="bg-pink-200" |
| class="bg-pink-300" |
| class="bg-pink-400" |
| class="bg-pink-500" |
| class="bg-pink-600" |
| class="bg-pink-700" |
| class="bg-pink-800" |
| class="bg-pink-900" |
| class="bg-pink-950" |
|-
! rose
| class="bg-rose-50" |
| class="bg-rose-100" |
| class="bg-rose-200" |
| class="bg-rose-300" |
| class="bg-rose-400" |
| class="bg-rose-500" |
| class="bg-rose-600" |
| class="bg-rose-700" |
| class="bg-rose-800" |
| class="bg-rose-900" |
| class="bg-rose-950" |
|}

除此之外，还有没有亮度部分的黑白两色分别以<code>black</code>和<code>white</code>代表，比如<code>class="text-white bg-black"</code>会呈现为<span class="text-white bg-black">黑底白字的效果</span>。

你也可以使用不在默认颜色表里的自定义颜色，只需要使用一对<code>[]</code>即可。比如使用<code>class="text-[#50d71e]"</code>便可<span class="text-[#50d71e]">以 #50d71e 为文字设定颜色</span>。

=== 大小长度 ===
CSS中有非常多的单位定义，其中最有名的可能是<code>px</code>，<code>1px</code>代表一个像素的长度，这样的单位被称为绝对单位。但由于现在设备类型众多，你并不知道你的页面会在什么样的终端设备上显示。在电脑屏幕和手机屏幕上，1个像素的宽度对于眼睛来说是不一样的，因为通常手机屏幕的单位面积里像素密度更高。面对多样的屏幕设备，使用相对单位会是一个更为合理的选择。在CSS里，最有名的相对单位应该是<code>%</code>，但是粒度不够细，我们有一个更细致的单位：<code>rem</code>。<code>1rem</code>代表根节点定义的字体中大写字母M的宽度，<code>2rem</code>就是两倍宽度，不过很不幸目前这个根单位的长度定义依然还是<code>px</code>，在灰机站点的默认设置上，<code>1rem = 16px</code>。

大部分情况下Tailwind使用<code>rem</code>来定义长度，但也保留<code>1px</code>这样的绝对长度。基本上，1个tailwind单位相当于<code>0.25rem</code>。以下是对照表：
{| class="wikitable" style="font-family: monospace"
|-
! 后缀 !! rem !! px !! 视觉宽度 !! 后缀 !! rem !! px !! 视觉宽度
|-
| <code>0</code> || class="text-right" | 0 || class="text-right" | 0 || || <code>14</code> || class="text-right" | 3.5rem || class="text-right" | 56px || <div class="h-4 bg-cyan-400 w-14"></div>
|-
| <code>px</code> || class="text-right" | - || class="text-right" | 1px || <div class="h-4 bg-cyan-400 w-px"></div> || <code>16</code> || class="text-right" | 4rem || class="text-right" | 64px || <div class="h-4 bg-cyan-400 w-16"></div>
|-
| <code>0.5</code> || class="text-right" | 0.125rem || class="text-right" | 2px || <div class="h-4 bg-cyan-400 w-0.5"></div> || <code>20</code> || class="text-right" | 5rem || class="text-right" | 80px || <div class="h-4 bg-cyan-400 w-20"></div>
|-
| <code>1</code> || class="text-right" | 0.25rem || class="text-right" | 4px || <div class="h-4 bg-cyan-400 w-1"></div> || <code>24</code> || class="text-right" | 6rem || class="text-right" | 96px || <div class="h-4 bg-cyan-400 w-24"></div>
|-
| <code>1.5</code> || class="text-right" | 0.375rem || class="text-right" | 6px || <div class="h-4 bg-cyan-400 w-1.5"></div> || <code>28</code> || class="text-right" | 7rem || class="text-right" | 112px || <div class="h-4 bg-cyan-400 w-28"></div>
|-
| <code>2</code> || class="text-right" | 0.5rem || class="text-right" | 8px || <div class="h-4 bg-cyan-400 w-2"></div> || <code>32</code> || class="text-right" | 8rem || class="text-right" | 128px || <div class="h-4 bg-cyan-400 w-32"></div>
|-
| <code>2.5</code> || class="text-right" | 0.625rem || class="text-right" | 10px || <div class="h-4 bg-cyan-400 w-2.5"></div> || <code>36</code> || class="text-right" | 9rem || class="text-right" | 144px || <div class="h-4 bg-cyan-400 w-36"></div>
|-
| <code>3</code> || class="text-right" | 0.75rem || class="text-right" | 12px || <div class="h-4 bg-cyan-400 w-3"></div> || <code>40</code> || class="text-right" | 10rem || class="text-right" | 160px || <div class="h-4 bg-cyan-400 w-40"></div>
|-
| <code>3.5</code> || class="text-right" | 0.875rem || class="text-right" | 14px || <div class="h-4 bg-cyan-400 w-3.5"></div> || <code>44</code> || class="text-right" | 11rem || class="text-right" | 176px || <div class="h-4 bg-cyan-400 w-44"></div>
|-
| <code>4</code> || class="text-right" | 1rem || class="text-right" | 16px || <div class="h-4 bg-cyan-400 w-4"></div> || <code>48</code> || class="text-right" | 12rem || class="text-right" | 192px || <div class="h-4 bg-cyan-400 w-48"></div>
|-
| <code>5</code> || class="text-right" | 1.25rem || class="text-right" | 20px || <div class="h-4 bg-cyan-400 w-5"></div> || <code>52</code> || class="text-right" | 13rem || class="text-right" | 208px || <div class="h-4 bg-cyan-400 w-52"></div>
|-
| <code>6</code> || class="text-right" | 1.5rem || class="text-right" | 24px || <div class="h-4 bg-cyan-400 w-6"></div> || <code>56</code> || class="text-right" | 14rem || class="text-right" | 224px || <div class="h-4 bg-cyan-400 w-56"></div>
|-
| <code>7</code> || class="text-right" | 1.75rem || class="text-right" | 28px || <div class="h-4 bg-cyan-400 w-7"></div> || <code>60</code> || class="text-right" | 15rem || class="text-right" | 240px || <div class="h-4 bg-cyan-400 w-60"></div>
|-
| <code>8</code> || class="text-right" | 2rem || class="text-right" | 32px || <div class="h-4 bg-cyan-400 w-8"></div> || <code>64</code> || class="text-right" | 16rem || class="text-right" | 256px || <div class="h-4 bg-cyan-400 w-64"></div>
|-
| <code>9</code> || class="text-right" | 2.25rem || class="text-right" | 36px || <div class="h-4 bg-cyan-400 w-9"></div> || <code>72</code> || class="text-right" | 18rem || class="text-right" | 288px || <div class="h-4 bg-cyan-400 w-72"></div>
|-
| <code>10</code> || class="text-right" | 2.5rem || class="text-right" | 40px || <div class="h-4 bg-cyan-400 w-10"></div> || <code>80</code> || class="text-right" | 20rem || class="text-right" | 320px || <div class="h-4 bg-cyan-400 w-80"></div>
|-
| <code>11</code> || class="text-right" | 2.75rem || class="text-right" | 44px || <div class="h-4 bg-cyan-400 w-11"></div> || <code>96</code> || class="text-right" | 24rem || class="text-right" | 384px || <div class="h-4 bg-cyan-400 w-96"></div>
|-
| <code>12</code> || class="text-right" | 3rem || class="text-right" | 48px || <div class="h-4 bg-cyan-400 w-12"></div>
|}

{{Data Help
|页面名=帮助:Tailwind_CSS参考
|描述文字=Tailwind参考手册
|解说=
|symbol=
|主分类=帮助
|子分类=进阶
|tags=设计,CSS
|sortkey=62
|关键=no
|catsortkey=3
|guide=no
|难度=进阶
|角色=设计者
|灰机功能=yes
}}
