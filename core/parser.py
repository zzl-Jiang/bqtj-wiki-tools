import xml.etree.ElementTree as ET
import json
from typing import Any, Dict, Union
from .converter import ValueConverter

class XmlParser:
    '''
    递归 XML 解析器。
    将清洗后的 XML 结构转化为嵌套的 Python 字典，以便生成 JSON。
    针对游戏特有的 <obj> 标签（内嵌 JSON 格式字符串）做了特殊适配。
    '''

    @staticmethod
    def to_dict(element: ET.Element) -> Any:
        '''
        深度优先递归解析 XML 节点。
        
        逻辑说明:
            1. 特殊处理 <obj> 标签：部分数据加密或以 JSON 字符串形式存在于标签文本中，直接解析。
            2. 属性处理：将节点的所有 Attributes 转化为字典键值对。
            3. 列表化处理：如果同级下出现多个重名标签，自动将其转化为列表。
            4. 纯文本处理：如果节点既无属性也无子节点，则直接返回其转换后的 Text。
        '''
        # 处理特殊标签 <obj>，通常其文本是 "{key:value}" 格式
        if element.tag == 'obj' and element.text:
            try:
                return json.loads(f"{{{element.text.strip()}}}")
            except:
                pass

        node_dict = {}

        # 处理当前节点的属性 (Attributes)
        if element.attrib:
            for k, v in element.attrib.items():
                node_dict[k] = ValueConverter.to_smart_value(v, k)

        # 递归处理子节点
        for child in element:
            child_data = XmlParser.to_dict(child)
            tag = child.tag
            
            if tag not in node_dict:
                # 第一次遇到该标签，直接赋值
                node_dict[tag] = child_data
            else:
                # 已经存在该标签，说明需要转化为列表存储 (List)
                if not isinstance(node_dict[tag], list):
                    node_dict[tag] = [node_dict[tag]]
                node_dict[tag].append(child_data)

        # 处理节点自身的文本内容 (Text)
        if element.text and element.text.strip():
            text_val = ValueConverter.to_smart_value(element.text.strip(), element.tag)
            if not node_dict:
                # 如果没有子项和属性，直接返回文本值，不再嵌套字典
                return text_val
            node_dict['_text'] = text_val

        return node_dict if node_dict else None