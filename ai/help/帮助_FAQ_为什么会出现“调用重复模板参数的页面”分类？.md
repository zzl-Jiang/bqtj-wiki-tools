# 帮助:FAQ/为什么会出现“调用重复模板参数的页面”分类？

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3AFAQ/%E4%B8%BA%E4%BB%80%E4%B9%88%E4%BC%9A%E5%87%BA%E7%8E%B0%E2%80%9C%E8%B0%83%E7%94%A8%E9%87%8D%E5%A4%8D%E6%A8%A1%E6%9D%BF%E5%8F%82%E6%95%B0%E7%9A%84%E9%A1%B5%E9%9D%A2%E2%80%9D%E5%88%86%E7%B1%BB%EF%BC%9F
revid：12041 · 抓取时间：2026-11-09T14:27:09+08:00

---

通常，这是由于在模板中给同一个参数赋予不同的值造成的，常见于类infobox模板。

如infobox模板中预设
*|data14=<nowiki>{{{灰机id}}}</nowiki>
*|data14=<nowiki>{{{灰机昵称|}}}</nowiki>
那么在引用了infobox模板页面中分别赋予
*|灰机id=12345
*|灰机昵称=下河捉泥鳅
时，该页面即会被归类于“调用重复模板参数的页面”分类下。此时需要回到infobox模板中进行修改，刷新词条页面即可。
[[Category:FAQ]]
