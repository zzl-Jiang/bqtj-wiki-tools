# 帮助:模块/MongoDB函数

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3A%E6%A8%A1%E5%9D%97/MongoDB%E5%87%BD%E6%95%B0
revid：42096 · 抓取时间：2026-11-09T14:27:10+08:00

---

{{LuaNav}}{{HuijiOnly}}
在阅读这篇教程之前，您需要先了解基于JSON——MongoDB——Lua的数据'''[[帮助:MongoDB支持|存储结构]]'''。

==MongoDB基础概念==
===文档（document）===
* MongoDB是一个基于分布式文件存储的数据库，文档是MongoDB储存数据的基本单位。
* 每个文档（document）必须有一个'''唯一'''的“<code>_id</code>”键，用以标识不同的文档。您不需要手动指定其中的内容，对这个概念有印象即可。
**<code>.json</code>页面是一个document，数据id是页面名字，例如"Data:xxxxx.json"。
**<code>.tab</code>或<code>.tabx</code>每一行是一个document，数据id是页面名字+行数。

===键、值（Key, Value）===
* 文档采用键值对的形式储存数据。
* 键名是一个UTF-8编码的字符串，对大小写敏感。
** 以下划线“<code>_</code>”开头的键是保留的，请尽量不要这么命名。
* 一个文档中不能含有重复的键。
* 值可以是多种数据类型。

==数据存储==
在灰机中，MongoDB数据库接受JSON与表格两种形式的数据，存储于站点的Data（3500）[[help:命名空间|命名空间]]下。
===.json===
以JSON格式存储的数据位于页面“<code>Data:xxxxxxx.json</code>”中，不论这个JSON文件有多大，它都会被视为MongoDB中的一个文档，其“<code>_id</code>”值就是页面名“<code>Data:xxxxxxx.json</code>”。

'''上传JSON文件'''

您可以直接在指定的页面创建文件，当然我们并不推荐这样做。
*对于大批量的JSON文件，我们建议通过[[帮助:灰机Wiki数据更新器|灰机Wiki数据更新器]]来批量上载。
*对于单个文件存储的Excel表格或者CSV，可以直接在页面进行上传，或者通过灰机Wiki数据更新器来更新。

'''合理分割JSON文件'''

如果JSON文件超过2M，我们建议将文件按照不同的field进行拆分进行单个上传，您可以自由的使用python或者其他本地语言对JSON文件进行切割。这样可以
*优化页面的阅读体验
*提升页面schema的加载速度
*方便数据的修改和增量更新
由于MongoDB的存储和查询方式，将一个体积巨大的JSON表拆分存储并不会影响数据的查询。

===.tab与.tabx===
灰机的MongoDB还支持直接上传Excel表格或者CSV表格来录入数据，生成后缀为“<code>.tab</code>”、“<code>.tabx</code>”结构的数据文件。对于这类文件，它的每一行都会被MongoDB视为一个以“<code>Data:xxxxxxx.tabx#n</code>”为“<code>_id</code>”的文档（n=行数）。
* 表格中的第一行是表头，必须为英文，首字符不能是空格或下划线。
* 此后的每一行为一条数据，tab/tabx将以第二行数据的类型为基准自动为每列（每个键）建立数据类型。
** 默认为string型，数字为number型，True/False为boolean型。
** 如果Excel中的第二行数据有空白，将会影响类型的判断。对于这种情况，可以调整数据顺序或者在Excel表的第二行录入一组假数据。
** 在当前版本中，即使在本地将Excel中的单元格设置为文本类型，纯数字的单元格还是会被识别成number型。
* 数据中不能出现制表符、换行符等特殊字符。
* tab/tabx具有特殊的数据结构，下面以[[Data:Testdata.tabx]]为例简要介绍灰机中tabx的结构，便于理解上面这几点。
<pre>
{
    "license": "CC0-1.0",    -- 表格数据遵循的共享协议，默认为CC0-1.0
    "description": {         -- 表格描述
        "en": "请输入简要描述"
    },
    "sources": "Imported from file funko统计.xlsx by 用户:SerGawen",
                             -- 表格来源，记录了原始文件的名称和上传该文件的用户ID
    "schema": {              -- 指定了每个键应当采用的数据类型
        "fields": [
            {
                "name": "datatoys",      -- 实际存入的键名
                "type": "string",        -- 键所对应的值的数据类型
                "title": {
                    "en": "Data Toys"    -- 显示的表头
                }
            },
            {
                "name": "wiki_index",
                "type": "number",
                "title": {
                    "en": "wiki_index"
                }
            },
            ...(略)
         ]
    },
    "data": [              -- 具体数据，与schema中指定的键一一对应，当该键没有对应的值时用null填充
        [
            "Data:Funko1", -- 对应键Data Toys
            1,             -- 对应键wiki_index
            ...(略)
        ],
        ...(略)
    ]
}
</pre>

==数据查询==
对于JSON的查询，必须使用'''Lua'''编写的[[help:模块|模块]]来进行。核心是四个已经封装好的函数：
{| class="wikitable"
|-
! 封装的Lua函数 !! MongoDB操作及含义
|-
| <code>mw.huiji.db.find( filter, options )</code> || Find操作：查询文档，默认返回所有符合条件的数据。
|-
| <code>mw.huiji.db.findOne( filter, options )</code> || FindOne操作：查询文档，但只返回第一个符合条件的数据。
|-
| <code>mw.huiji.db.count( filter, options )</code> || Count操作：返回符合查询条件的文档总数，这是一种简单的聚合操作。
|-
| <code>mw.huiji.db.aggregate( pipeline, options )</code> || Aggregate操作：聚合操作，用于实现数据的粘合以及初步的统计功能。
|}
注意，上述参数filter、options和pipeline的书写方法均与MongoDB在PHP中的语法保持一致，'''但必须遵照Lua中关于table的语法进行转写'''，直接复制[https://docs.mongodb.com/php-library/current/tutorial/ MongoDB Tutorial]官方文档中的PHP代码是无法在Lua中运行的。


'''例[1]'''：从PHP到Lua的转写

PHP中用下面的形式表示一个数组（array）：
<pre>
[
    'cuisine' => 'Italian',
    'borough' => 'Manhattan'
]
</pre>
在Lua中需要转换成这样的table类型：
<pre>
{
    ['cuisine']  =  'Italian',
    ['borough']  = 'Manhattan'
}
</pre>
或者简写成（不推荐，如果key中存在单引号或者空格，会导致mw的lua编辑器报错）：
<pre>
{
    cuisine  =  'Italian',
    borough  = 'Manhattan'
}
</pre>
总结要点：
*Lua中"<code>[]</code>"需要转写成“<code>{}</code>”
*Lua中table的key需要套上“<code>[]</code>”
*Lua中的单引号<nowiki>''</nowiki>与双引号<nowiki>""</nowiki>通用

<callout>下面我们着重介绍<code>mw.huiji.db.find( filter, options )</code>、和<code>mw.huiji.db.aggregate( pipeline, options )</code> 这两个最具代表性的函数，findOne()和count()相对简单，参数的书写语法与find()差别不大，您可以参考官方文档自行摸索。下面的示例代码同样采用[[Data:Testdata.tabx]]作例子。</callout>

==mw.huiji.db.find()==
函数定义：<code>mw.huiji.db.find( filter, options )</code>

返回值类型：table
{| class="wikitable"
|-
! 参数名 !! 参数类型 !! 描述
|-
| filter || table || 可选，使用查询操作符指定文件查询的过滤条件。
|-
| options || table || 可选，使用投影操作符指定查询结果的返回规则。如需返回结果中的所有键值， 只需省略此参数即可。
|}

===简单查询===
'''例[2]'''：简单的filter和option组合查询

目标：查询所有丹妮莉丝·坦格利安的Funko玩具，并按照wiki_index键从小到大排序

上述需求可用find语句这样实现：
<pre>
local data = mw.huiji.db.find( { ['hasname'] = '丹妮莉丝·坦格利安' }, { ['sort'] = { ['wiki_index'] = 1 } } )
</pre>
其中，filter参数中指出了我们要查询<code>hasname</code>键对应的值为<code>'丹妮莉丝·坦格利安'</code>的文档。options参数用sort字段指出了我们要将所有符合filter参数的查询结果按照<code>wiki_index</code>的大小进行排序，因为是正序（从小到大）所以赋值为1，若需要反序则令该值为-1。

鉴于Lua中<code>{}</code>的出现频率较高，为了便于阅读和修改，上述代码可以改写为：
<pre>
local query = {
    ['hasname'] = '丹妮莉丝·坦格利安'
}
local options = {
    ['sort'] = {
        ['wiki_index'] = 1
    }
}
local data = mw.huiji.db.find(query, options)
</pre>

===AND逻辑===
'''例[3]'''：带有AND逻辑的查询

目标：查询所有在2012年发布的丹妮莉丝·坦格利安的Funko玩具
<pre>
local query = {
    ['hasname'] = '丹妮莉丝·坦格利安',
    ['year'] = 2012
}
local data = mw.huiji.db.find(query)
</pre>
利用Lua对table的操作语法，可以通过以下方式添加查询条件：
<pre>
local query = {
    ['hasname'] = '丹妮莉丝·坦格利安'
}

query['year'] = 2012    -- 添加的条件

local data = mw.huiji.db.find(query)
</pre>

===OR逻辑===
'''例[4]'''：相同键的OR逻辑

目标：查询所有卓耿、韦赛利昂及雷哥的Funko玩具
<pre>
local query = {
    ['hasname'] = {
        ['$in'] = {
            '卓耿',
            '韦赛利昂',
            '雷哥'
        }
    }
}
local data = mw.huiji.db.find(query)
</pre>
注：
*使用$in操作符时，所赋的值必须是一个array类型的参数（即lua中只能是连续的序号索引，不能有字符串作索引的情况）

'''例[5]'''：不同键的OR逻辑

目标：查询hasname和haslink键中，所有包含兰尼斯特字样的Funko玩具
<pre>
local query = {
    ['$or'] = {
        {
            ['hasname'] = { ['$regex'] = '兰尼斯特' }
        },
        {
            ['haslink'] = { ['$regex'] = '兰尼斯特' }
        }
    }
}
local data = mw.huiji.db.find(query)
</pre>
注：
*使用$regex操作符，所赋的值必须是一个string类型的参数，可将该字段的值视为正则表达式进行搜索。
*相同键的OR逻辑也可用不同键的OR逻辑写法实现，但从方便的角度考虑我们通常采取上面的写法。

===缩小查询范围===
我们之前提到过每个文档都有一个'''唯一'''的“<code>_id</code>”键，这在关系型数据库中被称为'''主键'''（Primary Key）。JSON类文档的<code>_id</code>是对应的页面名“<code>Data:xxxxxxx.json</code>”，而tabx的每行文档的<code>_id</code>是“<code>Data:xxxxxxx.tabx#n</code>”（n为行数）。在MongoDB的查询中，我们可以通过设置条件限制<code>_id</code>的取值，达到缩小查询范围的目的。这么做可以：
*避免Lua的运行内存被占满 -- 如不加以限制，则默认在该站的整个MongoDB进行查询。这对于一些数据体量非常大的站点是很有必要的。
*加快页面加载速度 -- 查询范围缩小了自然速度会快些。


'''例[6]'''：在指定的单个文档中查询

以下的代码可以在单个文档中进行查询：
<pre>
local query = {
    ['_id'] = 'Data:Testdata.tabx#32'    -- JSON文档写成 ['_id'] = 'Data:xxxxxxxx.json'
}
local data = mw.huiji.db.find(query)
</pre>
注：
* 对于tab/tabx页面，必须指明行号，因为每一行才是MongoDB中的一个文档。
* 这种写法只能在单个文档中进行查询，适用场景并不多。通常在一个较大的json文档中才会这样使用。

在指定的多个文档中查询，可以根据实际情况使用以下两种方法：

假设[[Data:Testdata.tabx]]被分成了116个json，页面名为<code>Data:FunkoXX.json</code>（其中XX代表原tabx中的行号）。


'''例[7]'''：使用正则表达式<code>$regex</code>，在指定的多个文档中查询

目标：在所有<code>Data:FunkoXX.json</code>文档中查询
<pre>
local query = {
    ['_id'] = { ['$regex'] = 'Data:Funko.*\.json' }
    -- 也可以写成 ['_id'] = { ["$regex"] = '^Data:Funko.*\.json$' }
    -- ^ 表示以……开头
    -- $ 表示以……结尾
}
local data = mw.huiji.db.find(query)
</pre>
注：在上传数据的时候，设置一个合适的前缀有利于数据的管理。


'''例[8]'''：使用包含操作符<code>$in</code>，通过设置一个已知的List来进行查找

目标：在<code>Data:Funko1.json</code>、<code>Data:Funko2.json</code>、<code>Data:Funko3.json</code>中查询
<pre>
local queryList = {
    'Data:Funko1.json',
    'Data:Funko2.json',
    'Data:Funko3.json'
}

local query = {
    ['_id'] =  { ['$in'] = queryList }
}
local data = mw.huiji.db.find(query)
</pre>

===使用操作符===
'''例[9]'''：用'''比较操作符'''进行查询

目标：查询在2013年至2017年之间发布的丹妮莉丝·坦格利安Funko玩具
<pre>
local query = {
    ['hasname'] = '丹妮莉丝·坦格利安',
    ['year'] = {
        ['$gte'] = 2013,
        ['$lte'] = 2017
    }
}
local data = mw.huiji.db.find(query)
</pre>

'''完整的比较操作符列表'''
{| class="wikitable"
|-
! 运算符 !! 描述
|-
| $eq || 相等（equal）
|-
| $gt || 大于（greater than）
|-
| $gte || 大于等于（greater than or equal）
|-
| $in || 在list中（in）
|-
| $lt || 小于（lower than）
|-
| $lte || 小于等于（lower than or equal）
|-
| $ne || 不相等（not equal）
|-
| $nin || 不在list中（not in）
|}

'''例[10]'''：用'''元素操作符'''进行查询
*比较操作符不会对不存在的字段进行比较，此时可以使用元素操作符<code>['$exists'] = true</code>来判断
目标：查询所有特殊版本的Funko玩具
<pre>
local query = {
    ['special'] = {
        ['$exists'] = true
    }
}
local data = mw.huiji.db.find(query)
</pre>

===使用options参数===
默认情况下，MongoDB的查询会返回匹配所有符合query条件的文档，并且查询结果中会呈现这些文档中包含的所有键值，按照<code>_id</code>。若想限制查询的结果，需要灵活使用options参数。

'''例[11]'''：使用<code>limit</code>限制结果个数

目标：查询在2012年发布的Funko玩具，并返回前5条记录。
<pre>
local query = {
    ['year'] = 2012
}
local options = {
    ['limit'] = 5    -- 返回符合条件查询结果的前5个
}
local data = mw.huiji.db.find(query, options)
</pre>
'''例[12]'''：使用<code>sort</code>对结果排序

目标：查询在2012年发布的Funko玩具，并返回按照角色名称升序排序后的前5条记录。
<pre>
local query = {
    ['year'] = 2012
}
local options = {
    ['limit'] = 5,
    ['sort'] = {
        ['hasname'] = 1    -- 升序为1，降序为-1
    }
}
local data = mw.huiji.db.find(query, options)
</pre>
'''例[13]'''：使用<code>projection</code>限制返回特定键值

目标：查询在2012年发布的Funko玩具，返回按照角色名称升序排序后的前5条记录，且只显示它们的wiki_index和hasname属性。
<pre>
local query = {
    ['year'] = 2012
}
local options = {
    ['limit'] = 5,
    ['sort'] = {
        ['hasname'] = 1
    },
    ['projection'] = {
        ['wiki_index'] = 1,    -- 该值为0时，表示返回除此字段之外的其他字段
        ['hasname'] = 1
    }
}
local data = mw.huiji.db.find(query, options)
</pre>
在数据体量较大时，灵活运用<code>projection</code>可以丢弃不必要的结果，'''避免lua运行内存不足'''

'''例[14]'''，使用<code>skip</code>来切割结果

目标：查询在2012年发布的Funko玩具，返回按照角色名称升序排序后的第6-10条记录
<pre>
local query = {
    ['year'] = 2012
}
local options = {
    ['limit'] = 5,
    ['sort'] = {
        ['hasname'] = 1
    },
    ['skip'] = 5    -- 跳过前5条记录
}
local data = mw.huiji.db.find(query, options)
</pre>
使用<code>skip</code>跳过前5个文档，配合<code>limit</code>限制返回5个文档，得到的就是第6-10号文档。

==mw.huiji.db.aggregate()==
:<code>mw.huiji.db.aggregate(pipeline,options )</code>
aggregate(聚合)是mongoDB非常强大的一个功能，在这里简单介绍一下如何通过mw.huiji.db.aggregate()进行数据粘合以及初步处理。

===pipeline===
*'''[https://docs.mongodb.com/manual/core/aggregation-pipeline/ aggregation-pipeline]'''：完整的aggregation-pipeline文档（英文）
*'''[https://docs.mongodb.com/manual/reference/operator/aggregation-pipeline/#aggregation-pipeline-operator-reference Stages]'''：stage的文档（英文）
pipeline可以抽象为若干个依次进行的“stage”，以下列代码为例：

'''例[15]'''
<pre>
local pipeline = {
  {["$match"] = {                                  --------------stage.$match
    ['main_category'] = 'Activity',
    ['isPlaylist'] = false,
    ['activityLightLevel'] = 750,
    ['pgcrImage'] = { ["$regex"] = '.{2,}' }
  }},
-------------------------------------------------------------------
  {["$group"] = {                                                            --------------stage.$group
    ['_id'] = '$activityTypeHash',                                     --------------“activityTypeHash”是目标数据中的字段key
    ['count'] = {['$sum'] = 1},
    ['rewards'] = {['$addToSet'] = '$rewards'},                ------“rewards”是目标数据中的字段key
    ['hash'] = {['$push'] = '$hash'},                                 ------“hash”是目标数据中的字段key
    ['name'] = {['$push'] = '$name'},                               ------“name”是目标数据中的字段key
    ['image'] = {['$push'] = '$pgcrImage'},                      ------“pgcrImage”是目标数据中的字段key
    ['aLv'] = {['$push'] = '$activityLevel'},                        ------“activityLevel”是目标数据中的字段key
    ['matchmaking'] = {['$push'] = '$matchmaking'}        ------“matchmaking”是目标数据中的字段key                   
  }}
} 
</pre>
该段代码由两个stage组成，一个是<code>$match</code>，一个是<code>$group</code>。
*<code>$match</code>类似find()中的filter语句，用来书写查询条件
*<code>$group</code>是聚合规则，对本例而言，由<code>$match</code>查询到的结果，会按照<code>$activityTypeHash</code>进行聚合，相同的结果会被按照指定的规则粘合到一起。
**数据的聚合规则需要逐个字段指定，不指定的字段结果会被丢弃。
**常用聚合规则包括，<code>$push</code>、<code>$addToSet</code>、<code>$merge</code>、<code>$sum</code>、<code>$max</code>、<code>$min</code>等，完整的运算符参考：[https://docs.mongodb.com/manual/reference/operator/aggregation/group/#pipe._S_group group运算符文档（英文）]

除了<code>$match</code>、<code>$group</code>以外，还有包括<code>$addFields</code>、<code>$count</code>等不同的stage。

'''注意'''：除了 <code>$out</code>， <code>$merge</code>, 和<code>$geoNear</code>之外，其他stage均可以在pipeline中多次出现。

mw.huiji.db.aggregate()所能实现的功能非常复杂，因此在这里很难逐一进行讲解，按照上述范例，您可以使用本站数据进行实际操作，通过不断尝试来提高对mw.huiji.db.aggregate()函数的认知和掌握程度。（相关文档已经在上面对应位置给出）。

==查询语句的调试==
在实际操作中，可以频繁的使用<code>mw.dumpObject()</code>来查看查询语句的结果，来修正自己的代码，例如
<pre>
local data  = mw.huiji.db.find(query,options)
  for _i,v in ipairs(data) do
    res = res .. mw.dumpObject(v)  ----- dump出循环中的所有内容
  end
return res
</pre>

==查询语句的优化==
如果查询语句书写不当，极有可能造成如下几种情况：

===lua运行内存爆满===
:'''表现'''：页面返回lua红字异常，提示memory已满。
:'''成因分析'''：一般来说，这是因为查询返回数据量过大导致的
:'''解决方法'''：通过limit、slice、projection等手段缩减查询结果的体积，将不用的数据丢弃掉。亦可以通过slice来进行分割查询。

===页面长度超限===
:'''表现'''：页面停止解析#invoke函数，页面自动获得对应的异常分类。
:'''成因分析'''：这是因为通过lua渲染得出的内容（或是mw.dumpObject返回的dump内容）超过了MediaWiki对于单个页面内容长度的限制所导致的。
:'''解决方法'''：
:*将内容进行合理拆分，通过归类的细化进行分流。
:*对于mw.dumpObject()导致的情况，查看是否在循环中进行dump，如果是，可以将dump提出循环或者进行覆盖。

===过多的高开销函数===
:'''表现'''：too much expensive function calls红字提示。
:'''成因分析'''：前述的四种<code>mw.huiji.db</code>函数均被注册为'''高开销'''函数，根据MediaWiki的约束，同个页面内最多出现的高开销函数（包括lua中和普通的解析器函数例如#ifexist）不得超过100个。
:'''解决方法'''：一般来说，一个页面内（通过嵌套模块的调用）远远用不到100个<code>find()</code>或者<code>aggregate()</code>函数。如果出现了这种情况，说明您的代码过于破费，有很大的优化余地。对于由一张表内存储了超过100个id或hash索引，需要进一步显示对应内容，从而导致大量二次查询（<code>find()</code>或者<code>aggregate()</code>）引发的高开销超限问题，有如下两种方法可以解决：
:#将索引指向的详细内容（物品信息，任务信息）等通过鼠标浮层的方式进行展示（参考[[templatemanager:Manifest:鼠标提示框|鼠标提示框零件]]），这种浮层是通过js进行异步加载，并且有缓存，因此可以有效的避免在单个页面加载过多内容导致高开销超限。
:#将索引进行预收纳，例如在for循环中通过<code>table.insert()</code>函数，将待查询的id、index或者hash预先存放在一个list中（table类型变量），然后使用在<code>mw.huiji.db.find()</code>的filter中的<code>$in</code>语法进行合并查询。例如
<pre>
...<data block>

local itemList = {}            -----初始化一个空table（list），用来记录待查的物品hash
  for _i,v in ipairs(data.rewardItems) do            ---------循环已有的数据table，来获取待查物品的hash
    table.insert(itemList,v.itemHash)                  ---------使用table.insert()来收纳hash
  end
  
local query =  {                                    --------准备查询
  ['hash'] = {['$in'] = itemList}                ---------读取已经装满待查物品hash的table（list）
}

local rewardData  =  mw.huiji.db.find(query)                 ---------返回查询结果

...<data block>

</pre>
上述代码只是在最简形态下的示范，您还可以通过aggregate可以对结果进行更多的预处理，来减轻查询压力，提升效率，原本需要100+次的查询，可以合并到1次查询进行，从而避免了高开销超限。

除此之外，还可以将一些层级不那么复杂的数据实现准备好，放在一个文件里作为索引，省去查找的必要，这些文件可以使用python生成。
例如：[[hearthstone:module:hearthstone/data]]

==常见问题==
===table索引返回的内容为nil===
这种情况通常是因为查询返回的内容为空表导致的，或者是由于返回了多个内容，没有对结果进行正确的索引。以下面代码为例
<pre>
local query = {
  ['_id'] = { ["$regex"] = range },
  ['main_category'] = 'InventoryItem'
}
local data = mw.huiji.db.find(query)

local res = data.name
</pre>
通过使用<code>mw.dumpObject()</code>发现data实际上由N个table组成，因此我们需要制定一个下级table的序号，或者是使用循环进行操作
<pre>
local query = {
  ['_id'] = { ["$regex"] = range },
  ['main_category'] = 'InventoryItem'
}
local data = mw.huiji.db.find(query)
data = data[1]            ----------操作第一个结果
local res = data.name
</pre>

===在ipairs循环中通过value索引table时返回nil===
这通常是由于value=0 时导致的，在json中，序号或者hash等为0的情况非常常见，而lua的table则不允许key值为0（最小为1）
这种情况需要手动+1
<pre>
for _i,v in ipairs(data) do
   local res = res .. table[tostring(v+1)]
end
return res
</pre>

'''注意'''：在lua中大部分提示为nil的错误，均是由于类型不匹配，或者查询结果索引不当导致的，善用<code>mw.dumpObject()</code>来查看表结构，并注意使用<code>tostring()</code>、<code>tonumber()</code>来正确处理数据类型可以解决大部分的问题。
