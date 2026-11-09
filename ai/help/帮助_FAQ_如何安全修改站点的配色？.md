# 帮助:FAQ/如何安全修改站点的配色？

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3AFAQ/%E5%A6%82%E4%BD%95%E5%AE%89%E5%85%A8%E4%BF%AE%E6%94%B9%E7%AB%99%E7%82%B9%E7%9A%84%E9%85%8D%E8%89%B2%EF%BC%9F
revid：12027 · 抓取时间：2026-11-09T14:27:09+08:00

---

修改站点颜色需要先点击左边侧边栏管理员选项中的修改站点CSS按钮

'''注：只有维基管理员可以进入CSS选项修改站点配色。'''

[[file:FAQ2.png|300px]]

然后把这些内容贴入MediaWiki:Common.css 中

/* 放置于这里的CSS将应用于所有皮肤 */<br>
.ns-0{<br>
background-color: #FFF;<br>
}<br>
 
.bottom {<br>
background-color: #FFF;<br>
}


其中的FFF代表Web颜色中的白色，您可以右键审查元素来查看选择颜色代码；<br>
您也可以自己检索“web颜色代码”来寻找自己喜欢的颜色以及其代码；<br>
之后把#后面的代码换成您想要使用的颜色代码就可以了。

[[Category:FAQ]]
