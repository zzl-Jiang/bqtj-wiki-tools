"""
爆枪突击世界地图（WorldMap）数据处理器

从 XML 提取所有地图定义数据，输出 JSON + Excel。
数据结构：<father> → <place>（两层，place 含多个子元素）
"""
from collections import defaultdict
import os
import json
import datetime
import xml.etree.ElementTree as ET
from core import XmlCleaner, ValueConverter, OutputWriter, ReportGenerator

# --- 配置 ---
XML_DIR = './xml'
OUTPUT_DIR = './data/worldMap'

# 布尔值映射的子标签名
BOOL_KEYS = {'noTaskB', 'noEndlessB', 'mustWinShowB', 'firstShowB'}

# 逗号分隔列表的子标签名
LIST_KEYS = {'labelArr', 'linkArr', 'demSkillArr', 'demBossSkillArr', 'demNoModeArr'}


def parse_coordinate(text):
    """解析坐标字符串 'x,y' → {'x': x, 'y': y}"""
    if not text or not text.strip():
        return {'x': 0, 'y': 0}
    parts = text.strip().split(',')
    try:
        return {'x': int(parts[0]), 'y': int(parts[1]) if len(parts) > 1 else 0}
    except (ValueError, IndexError):
        return {'x': 0, 'y': 0}


def parse_place_node(place_node, father_attrs):
    """解析单个 <place> 节点，返回地图数据字典"""
    place_data = {}
    place_data.update(father_attrs)

    # place 标签自身属性（lv, unlockTask, cnName 等）
    for k, v in place_node.attrib.items():
        place_data[k] = ValueConverter.to_smart_value(v, k)

    # 子元素
    for child in place_node:
        tag = child.tag
        text = child.text.strip() if child.text else ''

        if tag == 'name':
            place_data['name'] = text
        elif tag == 'cnName':
            place_data['cnName'] = text
        elif tag == 'description':
            place_data['description'] = text
        elif tag in ('point', 'pointer'):
            place_data[tag] = parse_coordinate(text)
        elif tag in BOOL_KEYS:
            place_data[tag] = text == '1'
        elif tag in LIST_KEYS:
            place_data[tag] = [v.strip() for v in text.split(',') if v.strip()] if text else []
        elif tag == 'levelArr':
            # 嵌套结构：<levelArr><level><name>xxx</name></level>...
            levels = []
            for level_node in child.findall('level'):
                name_node = level_node.find('name')
                if name_node is not None and name_node.text:
                    levels.append({'name': name_node.text.strip()})
            place_data[tag] = levels
        else:
            place_data[tag] = ValueConverter.to_smart_value(text, tag)

    return place_data


def run_world_map_processor():
    """全自动地图处理器：扫描 XML → 提取 father/place → JSON/Excel 输出"""
    print(f"开始全量扫描目录: {XML_DIR}")

    map_pool = {}

    for root_dir, _, files in os.walk(XML_DIR):
        for file in files:
            if not file.endswith('.bin'):
                continue
            if 'worldMap' not in file:
                continue
            try:
                with open(os.path.join(root_dir, file), 'r', encoding='utf-8') as f:
                    clean_xml = XmlCleaner.clean(f.read())
                root_el = ET.fromstring(clean_xml)

                for father in root_el.findall('father'):
                    father_name = father.get('name', '')
                    father_attrs = {
                        'father': father_name,
                        'fatherCnName': father.get('cnName', ''),
                    }

                    for place_node in father.findall('place'):
                        place_data = parse_place_node(place_node, father_attrs)
                        if not place_data or 'name' not in place_data:
                            continue
                        place_data = ValueConverter.prepare_output(place_data, "爆枪突击", "worldMap")
                        map_pool[place_data['name']] = place_data

            except Exception as e:
                print(f"  [!] 错误文件 {file}: {e}")

    print(f"\n[提取] 共提取 {len(map_pool)} 个地图")

    # 统计
    father_stats = defaultdict(int)
    for data in map_pool.values():
        father_stats[data.get('father', 'unknown')] += 1
    for fn, count in sorted(father_stats.items(), key=lambda x: x[1], reverse=True):
        print(f"  {fn:20} : {count} 个")

    # 生成报告
    ReportGenerator.generate(map_pool, OUTPUT_DIR, report_prefix='世界地图',
                             group_field='fatherCnName')

    # 保存输出
    OutputWriter.write(map_pool, OUTPUT_DIR, 'WorldMap', cn_label='世界地图')

    print(f"\n处理完成！提取地图总数: {len(map_pool)}")


if __name__ == '__main__':
    run_world_map_processor()
