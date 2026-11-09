# 帮助:SMongo

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3ASMongo
revid：41748 · 抓取时间：2026-11-09T14:27:10+08:00

---

{{编辑手册nav}}
{{infobox
|bodystyle = clear:right;background:#fff;width:240px;color:#000;border:1px solid #333
|titlestyle=color:#fff
|title = 安装SMG
|image = [[File:SMongo logo 2.png|120px|center]]
|label11 = 仓库地址
|data11 = [[templatemanager:Manifest:SMongo|'''SMongo'''零件]]
|label12 = lua源码
|data12 = [[templatemanager:module:Query|核心模块]]
|data13 =为了避免覆盖可能存在的同名模板，零件中的主模板叫做SMongo/ask，您可以根据本站情况将其移动到template:Ask，以使用<nowiki>{{ask}}</nowiki>
}}
{{:templatemanager:Manifest:SMongo/doc}}
{{Data Help
|页面名=帮助:SMongo
|描述文字=SMW风格的Mongo查询
|解说=
|symbol=
|主分类=帮助
|子分类=进阶
|tags=SMW,Lua,数据更新
|sortkey=50700
|关键=no
|catsortkey=3
|guide=no
|难度=进阶
|角色=开发者
|灰机功能=yes
}}
-----------------
{{ask
  |table = Testdata.tabx
  |query = Toy Category::funko; Funko Series::1; Is Released::true;
  |?Has Name = 名字
  |?Funko Franchise = 系列
  |debug=1
}}
