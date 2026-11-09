# 帮助:使用echarts

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3A%E4%BD%BF%E7%94%A8echarts
revid：42617 · 抓取时间：2026-11-09T14:27:10+08:00

---

{{编辑手册nav}}
在2022年10月9日的更新之后，你可以使用全新的解析器函数<code><nowiki>{{#echarts}}</nowiki></code>来生成echarts图表，并且不需要安装任何零件。

如果你的站点之前用过零件版echarts，请参阅本文底部的迁移指南。

==语法==
与一般解析器函数语法相同，即<code><nowiki>{{#echarts:参数1|参数2|参数3}}</nowiki></code>。在本解析器函数中，该功能将扩展为<code><nowiki>{{#echarts:参数1=值1|参数2=值2|参数3=值3}}</nowiki></code>。支持的参数如下：
===option===
表单选项，包括坐标轴定义、值的系列、标题、图例等配置项。请参考[https://echarts.apache.org/zh/option.html echarts配置项手册]。

该字段的值<span style="font-size:1em;font-weight:bold;">必须为一个可解析的JSON字符串</span>。
===theme===
表单的样式。可以是字符串"dark"（echarts自带的暗色样式）或者一个代表theme的JSON字符串。你可以通过[https://echarts.apache.org/zh/theme-builder.html echarts主题编辑器]生成一个主题，导出配置后复制<code>theme</code>节点的内容作为主题。如果不填写该参数，则使用echarts的默认样式。

如果需要复用一组样式，你可以将该字符串封装到模板中。

===id===
为图表实例分配一个ID。如果不填写，则会自动生成一个ID。参考下文“开发者”相关段落。

===style===
图表容器的style。请务必至少指定一个宽高：
*width或min-width，如不指定则为100%（因为他是一个block）
*height或min-height，如不指定则高度为0，图表将无法正常显示。

===class===
图表的额外class。

==示例==
===最简单的写法===
使用echarts自带样式。
<pre>{{#echarts:option={
    "title": {
        "text": "ECharts 入门示例"
    },
    "legend": {
        "data": ["销量"]
    },
    "xAxis": {
        "data": ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    },
    "yAxis": {
	    "type": "value"
    },
    "series": [{
        "name": "销量",
        "type": "bar",
        "data": [5, 20, 36, 10, 10, 20]
    }]
}
|style=min-height:240px}}</pre>
{{#echarts:option={
    "title": {
        "text": "ECharts 入门示例"
    },
    "legend": {
        "data": ["销量"]
    },
    "xAxis": {
        "data": ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    },
    "yAxis": {
	    "type": "value"
    },
    "series": [{
        "name": "销量",
        "type": "bar",
        "data": [5, 20, 36, 10, 10, 20]
    }]
}
|style=min-height:240px}}

===使用dark样式===
<pre>{{#echarts:option={
    "title": {
        "text": "ECharts 入门示例"
    },
    "legend": {
        "data": ["销量"]
    },
    "xAxis": {
        "data": ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    },
    "yAxis": {
	    "type": "value"
    },
    "series": [{
        "name": "销量",
        "type": "bar",
        "data": [5, 20, 36, 10, 10, 20]
    }]
|theme=dark}}</pre>
{{#echarts:option={
    "title": {
        "text": "ECharts 入门示例"
    },
    "legend": {
        "data": ["销量"]
    },
    "xAxis": {
        "data": ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    },
    "yAxis": {
	    "type": "value"
    },
    "series": [{
        "name": "销量",
        "type": "bar",
        "data": [5, 20, 36, 10, 10, 20]
    }]
}
|style=min-height:240px|theme=dark}}
===使用调色板===
调色板配置较为复杂，建议通过[https://echarts.apache.org/zh/theme-builder.html echarts样式编辑器]生成样式，并将输出文件中的"theme"节点复制到theme参数中。
<pre>{{#echarts:option={
    "title": {
        "text": "ECharts 入门示例"
    },
    "legend": {
        "data": ["销量"]
    },
    "xAxis": {
        "data": ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    },
    "yAxis": {
	    "type": "value"
    },
    "series": [{
        "name": "销量",
        "type": "bar",
        "data": [5, 20, 36, 10, 10, 20]
    }]
}
|style=min-height:240px
|theme={
        "seriesCnt": 4,
        "backgroundColor": "rgba(254,248,239,1)",
        "titleColor": "#333333",
        "subtitleColor": "#aaaaaa",
        "textColorShow": false,
        "textColor": "#333",
        "markTextColor": "#eee",
        "color": [
            "#d87c7c",
            "#919e8b",
            "#d7ab82",
            "#6e7074",
            "#61a0a8",
            "#efa18d",
            "#787464",
            "#cc7e63",
            "#724e58",
            "#4b565b"
        ],
        "borderColor": "#ccc",
        "borderWidth": 0,
        "visualMapColor": [
            "#bf444c",
            "#d88273",
            "#f6efa6"
        ],
        "legendTextColor": "#333333",
        "kColor": "#c23531",
        "kColor0": "#314656",
        "kBorderColor": "#c23531",
        "kBorderColor0": "#314656",
        "kBorderWidth": 1,
        "lineWidth": 2,
        "symbolSize": 4,
        "symbol": "emptyCircle",
        "symbolBorderWidth": 1,
        "lineSmooth": false,
        "graphLineWidth": 1,
        "graphLineColor": "#aaa",
        "mapLabelColor": "#000000",
        "mapLabelColorE": "rgb(100,0,0)",
        "mapBorderColor": "#444444",
        "mapBorderColorE": "#444444",
        "mapBorderWidth": 0.5,
        "mapBorderWidthE": 1,
        "mapAreaColor": "#eeeeee",
        "mapAreaColorE": "rgba(255,215,0,0.8)",
        "axes": [
            {
                "type": "all",
                "name": "通用坐标轴",
                "axisLineShow": true,
                "axisLineColor": "#333",
                "axisTickShow": true,
                "axisTickColor": "#333",
                "axisLabelShow": true,
                "axisLabelColor": "#333",
                "splitLineShow": true,
                "splitLineColor": [
                    "#ccc"
                ],
                "splitAreaShow": false,
                "splitAreaColor": [
                    "rgba(250,250,250,0.3)",
                    "rgba(200,200,200,0.3)"
                ]
            },
            {
                "type": "category",
                "name": "类目坐标轴",
                "axisLineShow": true,
                "axisLineColor": "#333",
                "axisTickShow": true,
                "axisTickColor": "#333",
                "axisLabelShow": true,
                "axisLabelColor": "#333",
                "splitLineShow": false,
                "splitLineColor": [
                    "#ccc"
                ],
                "splitAreaShow": false,
                "splitAreaColor": [
                    "rgba(250,250,250,0.3)",
                    "rgba(200,200,200,0.3)"
                ]
            },
            {
                "type": "value",
                "name": "数值坐标轴",
                "axisLineShow": true,
                "axisLineColor": "#333",
                "axisTickShow": true,
                "axisTickColor": "#333",
                "axisLabelShow": true,
                "axisLabelColor": "#333",
                "splitLineShow": true,
                "splitLineColor": [
                    "#ccc"
                ],
                "splitAreaShow": false,
                "splitAreaColor": [
                    "rgba(250,250,250,0.3)",
                    "rgba(200,200,200,0.3)"
                ]
            },
            {
                "type": "log",
                "name": "对数坐标轴",
                "axisLineShow": true,
                "axisLineColor": "#333",
                "axisTickShow": true,
                "axisTickColor": "#333",
                "axisLabelShow": true,
                "axisLabelColor": "#333",
                "splitLineShow": true,
                "splitLineColor": [
                    "#ccc"
                ],
                "splitAreaShow": false,
                "splitAreaColor": [
                    "rgba(250,250,250,0.3)",
                    "rgba(200,200,200,0.3)"
                ]
            },
            {
                "type": "time",
                "name": "时间坐标轴",
                "axisLineShow": true,
                "axisLineColor": "#333",
                "axisTickShow": true,
                "axisTickColor": "#333",
                "axisLabelShow": true,
                "axisLabelColor": "#333",
                "splitLineShow": true,
                "splitLineColor": [
                    "#ccc"
                ],
                "splitAreaShow": false,
                "splitAreaColor": [
                    "rgba(250,250,250,0.3)",
                    "rgba(200,200,200,0.3)"
                ]
            }
        ],
        "axisSeperateSetting": true,
        "toolboxColor": "#999999",
        "toolboxEmphasisColor": "#666666",
        "tooltipAxisColor": "#cccccc",
        "tooltipAxisWidth": 1,
        "timelineLineColor": "#293c55",
        "timelineLineWidth": 1,
        "timelineItemColor": "#293c55",
        "timelineItemColorE": "#a9334c",
        "timelineCheckColor": "#e43c59",
        "timelineCheckBorderColor": "#c23531",
        "timelineItemBorderWidth": 1,
        "timelineControlColor": "#293c55",
        "timelineControlBorderColor": "#293c55",
        "timelineControlBorderWidth": 0.5,
        "timelineLabelColor": "#293c55",
        "datazoomBackgroundColor": "rgba(47,69,84,0)",
        "datazoomDataColor": "rgba(47,69,84,0.3)",
        "datazoomFillColor": "rgba(167,183,204,0.4)",
        "datazoomHandleColor": "#a7b7cc",
        "datazoomHandleWidth": "100",
        "datazoomLabelColor": "#333333"
    }
}}</pre>
{{#echarts:option={
    "title": {
        "text": "ECharts 入门示例"
    },
    "legend": {
        "data": ["销量"]
    },
    "xAxis": {
        "data": ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    },
    "yAxis": {
	    "type": "value"
    },
    "series": [{
        "name": "销量",
        "type": "bar",
        "data": [5, 20, 36, 10, 10, 20]
    }]
}
|style=min-height:240px
|theme={
        "seriesCnt": 4,
        "backgroundColor": "rgba(254,248,239,1)",
        "titleColor": "#333333",
        "subtitleColor": "#aaaaaa",
        "textColorShow": false,
        "textColor": "#333",
        "markTextColor": "#eee",
        "color": [
            "#d87c7c",
            "#919e8b",
            "#d7ab82",
            "#6e7074",
            "#61a0a8",
            "#efa18d",
            "#787464",
            "#cc7e63",
            "#724e58",
            "#4b565b"
        ],
        "borderColor": "#ccc",
        "borderWidth": 0,
        "visualMapColor": [
            "#bf444c",
            "#d88273",
            "#f6efa6"
        ],
        "legendTextColor": "#333333",
        "kColor": "#c23531",
        "kColor0": "#314656",
        "kBorderColor": "#c23531",
        "kBorderColor0": "#314656",
        "kBorderWidth": 1,
        "lineWidth": 2,
        "symbolSize": 4,
        "symbol": "emptyCircle",
        "symbolBorderWidth": 1,
        "lineSmooth": false,
        "graphLineWidth": 1,
        "graphLineColor": "#aaa",
        "mapLabelColor": "#000000",
        "mapLabelColorE": "rgb(100,0,0)",
        "mapBorderColor": "#444444",
        "mapBorderColorE": "#444444",
        "mapBorderWidth": 0.5,
        "mapBorderWidthE": 1,
        "mapAreaColor": "#eeeeee",
        "mapAreaColorE": "rgba(255,215,0,0.8)",
        "axes": [
            {
                "type": "all",
                "name": "通用坐标轴",
                "axisLineShow": true,
                "axisLineColor": "#333",
                "axisTickShow": true,
                "axisTickColor": "#333",
                "axisLabelShow": true,
                "axisLabelColor": "#333",
                "splitLineShow": true,
                "splitLineColor": [
                    "#ccc"
                ],
                "splitAreaShow": false,
                "splitAreaColor": [
                    "rgba(250,250,250,0.3)",
                    "rgba(200,200,200,0.3)"
                ]
            },
            {
                "type": "category",
                "name": "类目坐标轴",
                "axisLineShow": true,
                "axisLineColor": "#333",
                "axisTickShow": true,
                "axisTickColor": "#333",
                "axisLabelShow": true,
                "axisLabelColor": "#333",
                "splitLineShow": false,
                "splitLineColor": [
                    "#ccc"
                ],
                "splitAreaShow": false,
                "splitAreaColor": [
                    "rgba(250,250,250,0.3)",
                    "rgba(200,200,200,0.3)"
                ]
            },
            {
                "type": "value",
                "name": "数值坐标轴",
                "axisLineShow": true,
                "axisLineColor": "#333",
                "axisTickShow": true,
                "axisTickColor": "#333",
                "axisLabelShow": true,
                "axisLabelColor": "#333",
                "splitLineShow": true,
                "splitLineColor": [
                    "#ccc"
                ],
                "splitAreaShow": false,
                "splitAreaColor": [
                    "rgba(250,250,250,0.3)",
                    "rgba(200,200,200,0.3)"
                ]
            },
            {
                "type": "log",
                "name": "对数坐标轴",
                "axisLineShow": true,
                "axisLineColor": "#333",
                "axisTickShow": true,
                "axisTickColor": "#333",
                "axisLabelShow": true,
                "axisLabelColor": "#333",
                "splitLineShow": true,
                "splitLineColor": [
                    "#ccc"
                ],
                "splitAreaShow": false,
                "splitAreaColor": [
                    "rgba(250,250,250,0.3)",
                    "rgba(200,200,200,0.3)"
                ]
            },
            {
                "type": "time",
                "name": "时间坐标轴",
                "axisLineShow": true,
                "axisLineColor": "#333",
                "axisTickShow": true,
                "axisTickColor": "#333",
                "axisLabelShow": true,
                "axisLabelColor": "#333",
                "splitLineShow": true,
                "splitLineColor": [
                    "#ccc"
                ],
                "splitAreaShow": false,
                "splitAreaColor": [
                    "rgba(250,250,250,0.3)",
                    "rgba(200,200,200,0.3)"
                ]
            }
        ],
        "axisSeperateSetting": true,
        "toolboxColor": "#999999",
        "toolboxEmphasisColor": "#666666",
        "tooltipAxisColor": "#cccccc",
        "tooltipAxisWidth": 1,
        "timelineLineColor": "#293c55",
        "timelineLineWidth": 1,
        "timelineItemColor": "#293c55",
        "timelineItemColorE": "#a9334c",
        "timelineCheckColor": "#e43c59",
        "timelineCheckBorderColor": "#c23531",
        "timelineItemBorderWidth": 1,
        "timelineControlColor": "#293c55",
        "timelineControlBorderColor": "#293c55",
        "timelineControlBorderWidth": 0.5,
        "timelineLabelColor": "#293c55",
        "datazoomBackgroundColor": "rgba(47,69,84,0)",
        "datazoomDataColor": "rgba(47,69,84,0.3)",
        "datazoomFillColor": "rgba(167,183,204,0.4)",
        "datazoomHandleColor": "#a7b7cc",
        "datazoomHandleWidth": "100",
        "datazoomLabelColor": "#333333"
    }
}}
为了使用方便，你可以将theme单独封装一个模板。

封装模板时可以使用<code><nowiki><includeonly></nowiki></code>。

==开发者==
===限制===
*配置项会被JSON化，因此配置项中如果有函数则不会生效。
*多表联动等功能理论上可以实现，请自行查阅相关文档。
===检查配置项===
你可以使用<code>mw.config.get('hjEChartsConfig')</code>获取当前页面中的所有通过本方法生成的echarts实例的配置信息（通过此前的echarts零件生成的图表将不算在内）。这个object的每一个key均为解析器函数传入的id（或自动生成的id），值为对应的配置项（option）。

===实例操作===
echarts自带一个通过DOM元素反查实例的方法，因此你可以这样写：
<pre>
echarts.getInstanceByDom(document.getElementById('echarts-289409'))
</pre>
上述语句会返回echarts-289409的图表实例，你可以进行添加数据等操作。参考：[https://echarts.apache.org/zh/api.html#echartsInstance echartsAPI手册 - echartsInstance]。
===通过lua调用echarts===
你可以通过lua二次封装echarts解析器函数，语法如下：
<pre>
frame:callParserFunction('#echarts',{
    'theme=dark',
    'option=...'
})
--记得return
</pre>
注意，解析器函数的参数是一个数组table且每一个元素均为字符串，因此你需要将参数名及等号添加在原始字符串之前。

你可以使用<code>mw.text.jsonDecode</code>和<code>mw.text.jsonEncode</code>来进行JSON字符串到table的双向转换。请参考[https://www.mediawiki.org/wiki/Extension:Scribunto/Lua_reference_manual#mw.text.jsonDecode scribunto相关文档]。

==从echarts零件中迁移==
除非你在同一个页面使用了零件和本解析器函数，否则没有迁移的必要。迁移指南如下：
<pre>
// 零件的写法
{{ECharts
|id=example2
|title=ECharts demo (wikitext)
|width=890px
|option=
{
    "title": {
        "text": "ECharts 入门示例"
    },
    "legend": {
        "data": ["销量"]
    },
    "xAxis": {
        "data": ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    },
    "yAxis": {
	    "type": "value"
    },
    "series": [{
        "name": "销量",
        "type": "bar",
        "data": [5, 20, 36, 10, 10, 20]
    }]
}
}}

// 解析器函数的写法
{{#echarts:id=example2
|style=width:890px;height:240px;
|option={
    "title": {
        "text": "ECharts 入门示例"
    },
    "legend": {
        "data": ["销量"]
    },
    "xAxis": {
        "data": ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    },
    "yAxis": {
	    "type": "value"
    },
    "series": [{
        "name": "销量",
        "type": "bar",
        "data": [5, 20, 36, 10, 10, 20]
    }]
}
}}
</pre>
差异如下：
*title参数将弃用，折叠功能失效。请使用其他方式实现折叠功能。
*width参数弃用，合并到style参数中，并且必须指定高度或最小高度（否则会看不见）
*新增了theme参数。
