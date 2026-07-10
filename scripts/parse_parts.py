"""
爆枪突击零件（Parts）数据处理器

从 *_XMLOut_partsClass.bin 提取零件数据，按零件名分组输出独立 JSON。
同名的不同等级零件（如 shockParts_1 / shockParts_2）合并为同一个文件。
"""
import os
import re
import ast
import json
import glob as glob_module
import pandas as pd
import datetime
import xml.etree.ElementTree as ET
from collections import defaultdict
from core import XmlCleaner, ValueConverter, OutputWriter

# --- 配置 ---
XML_DIR = './xml'
OUTPUT_DIR = './data/parts'
REPORT_OUT = './data/parts/处理报告.txt'


def parse_o_attr(value):
    """解析 o 属性中的 Python 字典字面量（兼容 JSON 风格 true/false/null）"""
    if not value or not value.strip():
        return {}
    text = value.strip()
    # 将 JSON 风格的布尔/null 转为 Python 字面量
    text = re.sub(r'\btrue\b', 'True', text)
    text = re.sub(r'\bfalse\b', 'False', text)
    text = re.sub(r'\bnull\b', 'None', text)
    try:
        return ast.literal_eval(text)
    except (ValueError, SyntaxError):
        return {}


def parse_things_node(things_node):
    """解析单个 <things> 节点"""
    item = {}

    # things 标签自身属性
    for k, v in things_node.attrib.items():
        if k == 'o':
            item['o'] = parse_o_attr(v)
        elif k == 'cnName':
            # 优先级低于子元素 <cnName>，先暂存
            item['_attrCnName'] = v
        else:
            item[k] = ValueConverter.to_smart_value(v, k)

    # 子元素
    for child in things_node:
        tag = child.tag
        text = child.text.strip() if child.text else ''
        if tag == 'name':
            item['name'] = text
        elif tag == 'cnName':
            item['cnName'] = text
        elif tag == 'baseLabel':
            item['baseLabel'] = text
        elif tag == 'description':
            item['description'] = text
        else:
            item[tag] = ValueConverter.to_smart_value(text, tag)

    # 如果没有子元素 cnName，用标签 cnName
    if 'cnName' not in item:
        item['cnName'] = item.pop('_attrCnName', '')
    else:
        item.pop('_attrCnName', None)

    # 默认 itemsLevel = 1
    if 'itemsLevel' not in item:
        item['itemsLevel'] = 1

    return item


def get_group_key(name):
    """从 name 中提取分组键：去掉尾部的 _数字 后缀"""
    return re.sub(r'_\d+$', '', name)


def run_parts_processor():
    """全自动零件处理器：提取 → 按 name 分组 → JSON + Excel"""
    # 按文件名匹配 partsClass，兼容版本号前缀变动
    xml_files = glob_module.glob(os.path.join(XML_DIR, '*partsClass*'))

    XML_FILE = xml_files[0]
    print(f"开始处理零件数据: {XML_FILE}")

    with open(XML_FILE, 'r', encoding='utf-8') as f:
        clean_xml = XmlCleaner.clean(f.read())

    root_el = ET.fromstring(clean_xml)

    # 按 name（去 _N 后缀）分组
    groups = defaultdict(list)

    for father in root_el.findall('.//father'):
        if father.get('name') != 'parts':
            continue
        for things_node in father.findall('things'):
            item = parse_things_node(things_node)
            if not item or 'name' not in item:
                continue
            group_key = get_group_key(item['name'])
            groups[group_key].append(item)

    print(f"[提取] 共提取 {sum(len(v) for v in groups.values())} 个零件条目，{len(groups)} 个 baseLabel 分组")

    # --- 构建分组数据 ---
    parts_pool = {}
    for group_key, items in groups.items():
        first = items[0]
        group_data = {
            "game": "爆枪突击",
            "moduleType": "parts",
            "name": group_key,
            "cnName": first.get('cnName', ''),
            "baseLabel": group_key,
            "objType": first.get('objType', ''),
        }
        # 收集共有属性（取第一个非空值）
        for key in ('maxLevel', 'skillArr', 'iconUrl', 'o', 'description'):
            for item in items:
                if key in item and item[key]:
                    group_data[key] = item[key]
                    break

        # 按 itemsLevel 排序
        items_sorted = sorted(items, key=lambda x: x.get('itemsLevel', 1))
        group_data['items'] = [{k: v for k, v in it.items()
                                if k not in ('baseLabel', '_attrCnName')}
                               for it in items_sorted]

        # 补齐缺失等级 + 统一 _N 后缀（对应 AS3 createSpecialPartsDefine：
        #   XML 仅定义基础条目，运行时按 maxLevel 生成 1..maxLevel 的副本。
        #   所有条目（含 level 1）的 name/skillArr/iconUrl 均追加 "_N" 后缀。）
        max_level = group_data.get('maxLevel', 1)
        base_item = group_data['items'][0]  # 以 level 1 原始数据为模板
        # 保存原始值，用于生成所有等级（避免被 level 1 修改污染）
        base_icon = base_item.get('iconUrl', '')
        base_skills = base_item.get('skillArr', [])
        existing_levels = {it['itemsLevel'] for it in group_data['items']}
        for lv in range(1, max_level + 1):
            if lv in existing_levels:
                # 已有条目：用 base_* 重建（避免 XML 中已有后缀导致重复追加）
                item = next(it for it in group_data['items'] if it['itemsLevel'] == lv)
                item['name'] = f'{group_key}_{lv}'
                if base_icon:
                    item['iconUrl'] = f'{base_icon}_{lv}'
                if base_skills:
                    item['skillArr'] = [f'{s}_{lv}' for s in base_skills]
                continue
            new_item = dict(base_item)
            new_item['name'] = f'{group_key}_{lv}'
            new_item['itemsLevel'] = lv
            if base_icon:
                new_item['iconUrl'] = f'{base_icon}_{lv}'
            else:
                new_item['iconUrl'] = f'ThingsIcon/{group_key}_{lv}'
            if base_skills:
                new_item['skillArr'] = [f'{s}_{lv}' for s in base_skills]
            if lv != 1:
                new_item.pop('addDropDefineB', None)
            group_data['items'].append(new_item)
        # 重新排序
        group_data['items'] = sorted(group_data['items'], key=lambda x: x['itemsLevel'])

        # 同步 group 级 iconUrl/skillArr 为归一化后的 _1 版本
        first_item = group_data['items'][0]
        if 'iconUrl' in first_item:
            group_data['iconUrl'] = first_item['iconUrl']
        if 'skillArr' in first_item:
            group_data['skillArr'] = first_item['skillArr']

        # 精简 items：移除与 group 级相同或为空的冗余字段
        _SHARED_KEYS = {'cnName', 'objType', 'iconUrl', 'skillArr', 'description', 'o', 'maxLevel'}
        for it in group_data['items']:
            for key in _SHARED_KEYS:
                if key not in it:
                    continue
                val = it[key]
                # 空值：移除
                if not val and val != 0:
                    del it[key]
                # 与 group 级相同：移除
                elif key in group_data and val == group_data[key]:
                    del it[key]

        parts_pool[group_key] = group_data

    # --- 统一键序（OutputWriter 按 dict 插入顺序输出，此处确保可读性）---
    for group_key, data in parts_pool.items():
        ordered = {}
        for k in ['game', 'moduleType', 'name', 'cnName', 'baseLabel', 'objType', 'maxLevel']:
            if k in data:
                ordered[k] = data[k]
        for k, v in data.items():
            if k not in ordered:
                ordered[k] = v
        parts_pool[group_key] = ordered

    # --- 保存独立 JSON + 汇总 JSON + Excel ---
    ts = OutputWriter.write(parts_pool, OUTPUT_DIR, 'Part', cn_label='零件')
    EXCEL_NAME = f'{OUTPUT_DIR}/零件数据更新_{ts}.xlsx'

    # --- 生成 PartsItemData（精简查询 JSON） ---
    item_data = []
    for group_key, data in parts_pool.items():
        entry = {}
        for k in ('name', 'cnName', 'iconUrl'):
            val = data.get(k)
            if val is not None and val != '':
                entry[k] = val
        item_data.append(entry)

    parts_item_json = {
        "data": {
            "father": {
                "@name": "PartsItem",
                "@cnName": "零件标签",
                "item": item_data
            }
        }
    }

    item_json_path = os.path.join(OUTPUT_DIR, 'PartsItemData.json')
    with open(item_json_path, 'w', encoding='utf-8') as f:
        json.dump(parts_item_json, f, ensure_ascii=False, indent=2)
    print(f"PartsItemData JSON: {item_json_path} ({len(item_data)} 条)")

    # 追加 PartsItemData 到 Excel
    existing_df = pd.read_excel(EXCEL_NAME, header=None)
    new_row = pd.DataFrame([{
        0: "Data:PartsItemData.json",
        1: json.dumps(parts_item_json, ensure_ascii=False)
    }])
    pd.concat([existing_df, new_row], ignore_index=True).to_excel(EXCEL_NAME, index=False, header=False)

    # --- 生成报告 ---
    report = []
    report.append("=" * 50)
    report.append(f" 爆枪突击零件数据处理报告 - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report.append("=" * 50)
    report.append(f"\n[总体概况] 提取零件分组: {len(parts_pool)} 个")
    report.append(f"           零件条目总数: {sum(len(v.get('items', [])) for v in parts_pool.values())} 个")

    obj_stats = defaultdict(int)
    for data in parts_pool.values():
        obj_stats[data.get('objType', 'unknown')] += 1
    report.append("\n[分类统计 (objType)]")
    for t, c in sorted(obj_stats.items(), key=lambda x: x[1], reverse=True):
        report.append(f" - {t:12} : {c} 个")

    multi_level = [(n, d) for n, d in parts_pool.items() if len(d.get('items', [])) > 1]
    report.append(f"\n[多等级零件] 共 {len(multi_level)} 组")
    for n, d in multi_level:
        levels = [it.get('itemsLevel', '?') for it in d['items']]
        report.append(f" - {n} ({d.get('cnName','')}) : {len(d['items'])} 级 [{', '.join(str(l) for l in levels)}]")

    report.append("\n[异常数据检测]")
    missing_cn = [n for n, d in parts_pool.items() if not d.get('cnName')]
    if missing_cn:
        report.append(f" [X] 缺少中文名的零件 ({len(missing_cn)}个): {', '.join(missing_cn)}")
    else:
        report.append(" [OK] 所有零件均包含中文名。")

    missing_icon = [n for n, d in parts_pool.items() if not d.get('iconUrl')]
    if missing_icon:
        report.append(f" [X] 缺少 iconUrl 的零件 ({len(missing_icon)}个): {', '.join(missing_icon)}")
    else:
        report.append(" [OK] 所有零件均包含 iconUrl。")

    final_report = "\n".join(report)
    print(final_report)
    with open(REPORT_OUT, "w", encoding="utf-8") as f:
        f.write(final_report)
    print(f"\n[报告] 统计报告已保存至: {REPORT_OUT}")
    print(f"\n处理完成！提取零件分组: {len(parts_pool)}")


if __name__ == '__main__':
    run_parts_processor()
