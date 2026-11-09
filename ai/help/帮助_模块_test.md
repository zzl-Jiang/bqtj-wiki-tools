# 帮助:模块/test

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3A%E6%A8%A1%E5%9D%97/test
revid：34623 · 抓取时间：2026-11-09T14:27:11+08:00

---

==1==
{{ask
|table = Testdata.tabx
|query = Toy Category::funko,Year::2012
|?Has Name = y
|?Year = Year
|?Funko Franchise = y
|limit =20
|class= sortable
|mainlabel = funko!
}}

==2==
{{ask
|table = Testdata.tabx
|query = Toy Category::funko,Year::2012,Is Released::true,Funko Series::1
|?Has Name = y
|?Funko Franchise = y
|limit =20
|template = test/1
|format =template
|named args = yes
|introtemplate =test/0
|outrotemplate =test/3
}}

==3==
{{ask
|table = Testdata.tabx
|query = Is Released::true
|?Has Name = y
|?Funko Franchise = y
|limit =20
|mainlabel = -
}}
==4==
{{ask
|table = Testdata.tabx
|query = Year::!2011
|?Has Name = y
|?Funko Franchise = y
|?Funko Series = Funko Series
|limit =20
|mainlabel = -
}}
