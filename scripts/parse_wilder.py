"""
爆枪突击秘境（Wilder）数据处理器

从 XML 提取所有秘境首领定义数据，输出 JSON + Excel。
数据结构：<father> → <body> → <drop> → <gift>（四层嵌套）
"""
from collections import defaultdict
import os
import datetime
import xml.etree.ElementTree as ET
from core import XmlCleaner, ValueConverter, OutputWriter, ReportGenerator

# --- 配置 ---
XML_DIR = './xml'
OUTPUT_DIR = './data/wilder'

# Wilder 特有的数值属性（需转换为 int/float）
INT_ATTRS = {'id', 'day', 'limitAll'}
FLOAT_ATTRS = {'lifeMul', 'dpsMul'}
BOOL_ATTRS = {'noMoreB', 'hideB', 'noExchangeB', 'noBuyB'}


def parse_gift_text(gift_str):
    """解析 gift 子标签的文本（格式: type;name;num）"""
    if not gift_str or not gift_str.strip():
        return None
    parts = gift_str.strip().split(';')
    if len(parts) >= 3:
        return {
            'type': parts[0].strip(),
            'name': parts[1].strip(),
            'num': int(parts[2].strip()) if parts[2].strip().isdigit() else parts[2].strip(),
        }
    return None


def parse_body_node(body_node, father_attrs):
    """解析单个 <body> 节点，返回秘境数据字典"""
    body_data = {}
    body_data.update(father_attrs)

    # body 标签属性
    for k, v in body_node.attrib.items():
        if k == 'name':
            body_data['name'] = v
        elif k == 'cnName':
            body_data['cnName'] = v
        elif k in INT_ATTRS:
            body_data[k] = int(v)
        elif k in FLOAT_ATTRS:
            body_data[k] = float(v)
        elif k in BOOL_ATTRS:
            body_data[k] = v == '1'
        else:
            body_data[k] = ValueConverter.to_smart_value(v, k)

    # 子元素：drop → gift
    drops = []
    for drop_node in body_node.findall('drop'):
        drop_entry = {}
        for gift_node in drop_node.findall('gift'):
            parsed = parse_gift_text(gift_node.text)
            if parsed:
                drop_entry['gift'] = parsed
                break
        if drop_entry:
            drops.append(drop_entry)
    if drops:
        body_data['dropArr'] = drops

    return body_data


def run_wilder_processor():
    """全自动秘境处理器：扫描 XML → 提取 father/body → JSON/Excel 输出"""
    print(f"开始全量扫描目录: {XML_DIR}")

    wilder_pool = {}

    for root_dir, _, files in os.walk(XML_DIR):
        for file in files:
            if not file.endswith('.bin'):
                continue
            if 'wilderClass' not in file:
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
                    # father 上的其他属性
                    for k, v in father.attrib.items():
                        if k not in ('name', 'cnName'):
                            father_attrs[k] = ValueConverter.to_smart_value(v, k)

                    for body_node in father.findall('body'):
                        body_data = parse_body_node(body_node, father_attrs)
                        if not body_data or 'name' not in body_data:
                            continue
                        body_data = ValueConverter.prepare_output(body_data, "爆枪突击", "wilder")
                        wilder_pool[body_data['name']] = body_data

            except Exception as e:
                print(f"  [!] 错误文件 {file}: {e}")

    print(f"\n[提取] 共提取 {len(wilder_pool)} 个秘境首领")

    # 分类统计
    father_stats = defaultdict(int)
    for data in wilder_pool.values():
        father_stats[data.get('father', 'unknown')] += 1
    for fn, count in sorted(father_stats.items(), key=lambda x: x[1], reverse=True):
        print(f"  {fn:20} : {count} 个")

    # 生成报告
    ReportGenerator.generate(wilder_pool, OUTPUT_DIR, report_prefix='秘境',
                             group_field='fatherCnName')

    # 保存输出
    OutputWriter.write(wilder_pool, OUTPUT_DIR, 'Wilder', cn_label='秘境')

    print(f"\n处理完成！提取秘境首领总数: {len(wilder_pool)}")


if __name__ == '__main__':
    run_wilder_processor()
