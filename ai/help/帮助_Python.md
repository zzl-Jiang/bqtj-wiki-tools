# 帮助:Python

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3APython
revid：42223 · 抓取时间：2026-11-09T14:27:10+08:00

---

{{编辑手册nav}}
'''Python'''是一种简明、易学的解释型语言，运行Python脚本不需要编译，因此可以方便的部署和使用。本教程着重介绍如何在MediaWiki的场景下使用'''Python 3.x'''语言。
==关于Python==
自2020 年 1 月 1 日起， Python 2 的更新已经停止，因此我们在这里只讨论Python 3版本的相关内容。关于在灰机使用Python，需要明确：
*出于安全考虑，灰机无法在线上运行Python脚本，线上的逻辑编译我们推荐使用MediaWiki内建支持的Lua进行编程。
*Python在本地使用时，可以搭配各种bot工具，比如[[帮助:AWB机器人|AWB]]或者[[帮助:灰机Wiki数据更新器|灰机数据更新器]]，但我们不推荐使用PyWikibot（太麻烦）。
===Python能做什么？===
Python的作用主要在于为线上准备编辑材料，比如文学翻译类维基的译名表，游戏类维基的结构化数据，<s>甚至制作镜像wiki</s>。概括来说，Python最擅长的功能主要包括：
*提取、拆分结构化数据，实现包文件、文本文件（txt、hex等）、结构化数据之间（XML、JSON、CSV）的互转；
*将Excel表格（xls，xlsx）以CSV的形式与XML、JSON、txt进行互转；
*将数据按照你想要的结构进行重构，比如多语言字段的merge、大体积JSON文件（超过2M）的切割等等；
*快速的备份灰机或其他MediaWiki网站的文字和图片内容（请注意节操！）；
*将预处理的内容直接更新到灰机（与[[帮助:灰机Wiki数据更新器|灰机数据更新器]]、[[帮助:AWB机器人|AWB]]存在一定程度上的重合，请自行判断用哪个方法）。

==学习Python==
Python的文档和教程可以前往[https://www.runoob.com/python3/python3-tutorial.html 菜鸟教程]自行阅读。
*注意，请勿死记硬背，尽量在具体项目中实践摸索。

==安装Python==
安装和部署Python环境，主要是要安装Python本体，和JB家的Python编译工具，下面是地址
*[https://www.python.org/ 官网]
*[https://www.python.org/doc/ 英文文档]
*[https://www.jetbrains.com/pycharm/download/#section=windows pycharm]

===配置解释器===
#File——Other Settings——Setting for New Project ——
#Project Interpreter ——下拉选择编译器，通过右侧的“+”安装需要的库（lib）——
#运行脚本——Edit Configuration——选择之前配置完毕的interpreter——运行
<gallery>
File:配置编译器1.jpg
File:配置编译器2.jpg
File:配置编译器3.jpg
File:配置编译器4.jpg
</gallery>

===常用库===
{| class="wikitable"
|-
! 库 !! 用途 !! 类型 !!文档
|-
| beautifulsoup4 || 爬虫和网页内容处理 || 外部库，需要安装 || [https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/#id41be 中文]
|-
| mwclient || MW的API通信 || 外部库，需要安装 ||[https://mwclient.readthedocs.io/en/latest/index.html 英文]
|-
| requests || 网络请求 || 外部库，需要安装 ||[https://requests.readthedocs.io/zh_CN/latest/ 中文]
|-
| urllib3 || 网络请求 || 外部库，需要安装  ||[https://urllib3.readthedocs.io/en/latest/ 英文]
|-
| json || JSON编码 || 内部库，直接导入 || [https://docs.python.org/3/library/json.html 英文]
|-
| csv || CSV编码 || 内部库，直接导入 || [https://docs.python.org/3/library/csv.html 英文]
|-
| re || 正则表达式 || 内部库，直接导入 || [https://docs.python.org/3/library/re.html 英文]
|-
| os || 本地文件操作 || 内部库，直接导入 || [https://docs.python.org/3/library/os.html 英文]
|-
| time || 时间 || 内部库，直接导入 || [https://docs.python.org/3/library/time.html 英文]
|-
| slpp || lua编码 || 外部库，需要安装 || [https://github.com/SirAnthony/slpp 英文]
|-
| xmltodict || XML编码 || 外部库，需要安装 || [https://github.com/martinblech/xmltodict 英文]
|}

==方法一，非直接交互==
顾名思义，您的Python脚本无需直接和灰机服务器进行通信，而是通过灰机数据更新器将您的本地资料上传到灰机的服务器，典型使用场景：
#本地解包，Python将包文件编译为JSON文件，通过灰机数据更新器同步到灰机wiki的Data命名空间下，存入MongoDB，然后使用Lua在线上进行查询。
#本地使用Python爬取目标网站的图片或者特定信息（请确认您的爬虫行为符合网络礼仪且合法！），在本地预处理成新增信息，通过灰机数据更新器更新到页面模板中。

==方法二：直接交互==
这里主要用到一个Python的库，叫做<code>[https://mwclient.readthedocs.io/en/latest/user mwclient]</code>
{{Mbox
|border=danger
|type=content
|text=需要额外的authkey<br>
目前因为较严格的反爬虫策略，需要向职员申请authkey才可以通过自定义请求访问api。
点击链接加入群聊[http://qm.qq.com/cgi-bin/qm/qr?_wv=1027&k=YMvgLLlDBvbaIimfg-XLxCFCyLzAt5F4&authKey=y4thITCFxunWXGf67ReZIbH%2BtsoPEMVvx1lkEPVceaovHB2qENMeWjTcIxRBQ91i&noverify=0&group_code=286359271 灰机WIKI动物园]
}}

===连接===

<pre> from mwclient import Site</pre>
<pre>site = Site('test.huijiwiki.com', scheme="https")</pre>

===声明自己的ua===
<code>{tool_name}/{tool_version} ({contact})</code>.非强制，但推荐
<pre>
ua = 'MyCoolTool/0.2 (ga@huiji.wiki)'
site = Site('test.huijiwiki.com', clients_useragent=ua)
</pre>

===登录===
<pre>
site.login('my_username', 'my_password')
</pre>

===操作页面===
拿到特定页面的内容，代码如下
<pre>
from mwclient import Site
site = Site('www.huijiwiki.com', scheme="https")

page = site.pages['help:Python']
text = page.text()
</pre>

===编辑页面===
通过<code>page.exists</code>可以对指定页面是否存在进行判断
<pre>page.exists</pre>

在指定的字符串内装载完毕更新内容后，使用

<pre>page.save(text, 'Edit summary')</pre>

来进行更新，页面存在进行编辑，不存在则进行创建。

===获取分类===
<code>Site.categories()</code>获取站点的分类信息，同时可以使用 <code>members()</code>列出分类中的内容。

Category object本身就是一个iterator，用法如下

<pre>
category = site.categories['Python']
for page in category:
    print(page.name)
</pre>

===处理文件===
获取指定文件的信息

<pre>
file = site.images['Example.jpg']
</pre>

<pre>
print(file.imageinfo)

{'comment': 'Reverted to version as of 17:58, 12 March 2010',
 'descriptionshorturl': 'https://commons.wikimedia.org/w/index.php?curid=6428847',
 'descriptionurl': 'https://commons.wikimedia.org/wiki/File:Example.jpg',
 'height': 178,
 'metadata': [{'name': 'MEDIAWIKI_EXIF_VERSION', 'value': 1}],
 'sha1': 'd01b79a6781c72ac9bfff93e5e2cfbeef4efc840',
 'size': 9022,
 'timestamp': '2010-03-14T17:20:20Z',
 'url': 'https://upload.wikimedia.org/wikipedia/commons/a/a9/Example.jpg',
 'user': 'SomeUser',
 'width': 172}
</pre>

获取使用目标图片的条目

<pre>
for page in image.imageusage():
     print('Page:', page.name, '; namespace:', page.namespace)
</pre>

注意：通过共享的图片不被视为物理存在

===下载文件===
<code>Image.download()</code> 

例子:
<pre>
file = site.images['Example.jpg']
    with open('Example.jpg', 'wb') as fd:
...     image.download(fd)
</pre>

===上传文件===
<pre>
site.upload(open('file.jpg'), 'destination.jpg', 'Image description')
</pre>

===页面（Page Object）===
通过<code>Page</code>、<code>Category</code> 、 <code>Image</code>进行操作，一般用<code>Site.pages</code> 作为generator生成迭代器遍历。

<pre>
page = site.Pages['Template:Stub']   # a Page object
image = site.Pages['Image:Wiki.png'] # an Image object
image = site.Images['Wiki.png']      # the same Image object
cat = site.Pages['Category:Python']  # a Category object
cat = site.Images['Python']          # the same Category object</pre>

===手册索引===
[https://mwclient.readthedocs.io/en/latest/reference/index.html mwclient完全索引]

==搜索替换的代码实例==
<pre>
import re
from mwclient import Site

site = Site('asdasd.huijiwiki.com, scheme="https"')
site.login('SerGawen', '123123123123')

category = site.categories['categoryxxx']


def find_and_replace():
    for page in category:
        change = 0

        # 获取页面内容（str）
        text = page.text()

        # find 1 使用普通的文本替换
        obj = re.search('regex', text)
        if obj:
            new = '123123123123'

            # use replace
            text = text.replace('{{ShowCardText}}', new)
            change += 1

        # find 2 使用正则表达式
        obj2 = re.search('regex', text)
        if obj2:
            new = '13123123'

            # 使用正则表达式capture并返回\1
            text = re.sub(r'(\=\=\=)', '\1', text)

            # 使用程序作为re.sub的repl
            text = re.sub('("[a-zA-Z]+":\s[\w\[,\s]+)', processValue, text)
            change += 1

        if change > 0:
            page.save(text, summary='fix', minor=False, bot=True, section=None)
            print("changed : %s" % page)
            
# 如果使用程序作为re.sub的repl部分：           
def processValue(m):
    res = ''
    n = str(m.group(1)).split(':')
    # 切片
    for slice in n:
        # 没有引号的
        if re.search('"',slice) is None:
            # 有英文字符串的
            match = re.findall('[\w\._]+',slice)
            if match is not None:
                # 每个正确的匹配
                if match != 'true' and match != 'false':
                    slice = re.sub('([\w\._]+)', r'"\1"', slice)
        res = res + slice + ':'
    res = res[0:len(res)-1]
    return res

find_and_replace()
</pre>

==从MediaWiki站点备份图片代码实例==
<pre>
import os
import requests
from mwclient import Site
root_path = 'H:\\download'  # file path


# 这里的实例为Fandom，注意，Fandom没有采用默认的api路径，需要手动指定一个path。
def getFandomSite(prefix):
    site = Site(prefix + '.fandom.com', path='/')
    
    # 获取所有图片文件
    allImages = site.allimages()

    for img in allImages:
        file = img.name
        url = img.imageinfo['url']
        r = requests.get(url, stream=True)
        name = file.replace("File:", '')
        
        # 防雷补丁
        name = name.replace("/", '%2F')
        name = name.replace(":", '%3A')
        name = name.replace("*", '%2A')
        name = name.replace("?", '%3F')
        name = name.replace('"', '%22')

        path = root_path + '\\' + prefix
        if not os.path.exists(path):
            os.mkdir(path)
        path = path + '\\' + name
        
        # 保存文件
        if not os.path.exists(path):
            try:
                with open(path, 'wb') as fd:
                    fd.write(r.content)
                    print(path)
            except Exception:
                    print("erro: %s" % path)
                pass

# 指定站点为 avatar.fandom.com
getFandomSite('avatar')

</pre>

==从灰机shareduploads备份国旗图片实例==
<pre>
import os
import requests
from mwclient import Site
root_path = 'H:\\download'  # file path


def getHuijiSiteFlags(prefix):
    site = Site('shareduploads.huijiwiki.com', scheme='https')
    allImages = site.categories['国旗和区旗']

    for img in allImages:
        file = img.name
        if 'url' in img.imageinfo:
            url = img.imageinfo['url']
            if 'url' in img.imageinfo:
                r = requests.get(url, stream=True)
                name = file.replace("文件:", '')
                # 防雷
                name = name.replace("/", '%2F')
                name = name.replace(":", '%3A')
                name = name.replace("*", '%2A')
                name = name.replace("?", '%3F')
                name = name.replace('"', '%22')

                path = root_path + '\\' + prefix
                if not os.path.exists(path):
                    os.mkdir(path)
                path = path + '\\' + name
                if not os.path.exists(path):
                    try:
                        with open(path, 'wb') as fd:
                            fd.write(r.content)
                            print(path)
                    except Exception:
                        pass


getHuijiSiteFlags('flags')

</pre>
{{Data Help
|页面名=帮助:Python
|描述文字=在灰机使用Python
|解说=
|symbol=
|主分类=帮助
|子分类=复杂
|tags=编程,维基化,数据更新
|sortkey=51400
|关键=no
|catsortkey=4
|guide=no
|难度=复杂
|角色=开发者
|灰机功能=no
}}
