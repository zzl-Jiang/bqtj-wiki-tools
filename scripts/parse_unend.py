"""
爆枪突击虚天塔（Unend）数据处理器

从 unendEnemyClass 提取每层出场角色（father name="unend" 下的 body），
从 unendProClass 提取虚天塔点数 pro 数据。
输出 unendEnemy.json + unendPro.json。
"""
import os
import json
import glob as glob_module
import datetime
import xml.etree.ElementTree as ET
from core import XmlCleaner, ValueConverter

# --- 配置 ---
XML_DIR = './xml'
OUTPUT_DIR = './data/unend'


def _smart_number(v):
    """将字符串转为数字（int/float），失败则返回原字符串"""
    try:
        if '.' in v:
            return float(v)
        return int(v)
    except (ValueError, TypeError):
        return v


def parse_enemy_bodys(text):
    """解析敌人 body 文本为对象数组：每行 '名称[:权重[:权重]]'"""
    if not text or not text.strip():
        return []
    result = []
    for line in text.strip().split('\n'):
        line = line.strip()
        if not line:
            continue
        parts = line.split(':')
        name = parts[0].strip()
        if not name:
            continue
        if len(parts) == 1:
            result.append({'name': name})
        else:
            weights = [_smart_number(w.strip()) for w in parts[1:] if w.strip() != '']
            if weights:
                result.append({'name': name, 'weights': weights})
            else:
                result.append({'name': name})
    return result


def parse_map_bodys(text):
    """解析地图 body 文本为字符串数组"""
    if not text or not text.strip():
        return []
    return [line.strip() for line in text.strip().split('\n') if line.strip()]


def run_unend_processor():
    """全自动虚天塔处理器"""
    print(f"开始处理虚天塔数据: {XML_DIR}")

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # ======== 1. unendEnemy ========
    enemy_files = glob_module.glob(os.path.join(XML_DIR, '*unendEnemyClass*'))
    enemy_list = []
    if enemy_files:
        with open(enemy_files[0], 'r', encoding='utf-8') as f:
            clean_xml = XmlCleaner.clean(f.read())
        root_el = ET.fromstring(clean_xml)

        for father in root_el.findall('.//father'):
            if father.get('name') != 'unend':
                continue
            for body in father.findall('body'):
                entry = {}
                for k, v in body.attrib.items():
                    if k == 'name':
                        entry['name'] = v
                    elif k == 'cnName':
                        entry['cnName'] = v
                    else:
                        entry[k] = ValueConverter.to_smart_value(v, k)

                text = body.text.strip() if body.text else ''
                if entry.get('name') == 'unendMap':
                    entry['bodys'] = parse_map_bodys(text)
                else:
                    entry['bodys'] = parse_enemy_bodys(text)

                enemy_list.append(entry)

    enemy_json = {"data": {"father": enemy_list}}
    enemy_path = os.path.join(OUTPUT_DIR, 'unendEnemy.json')
    with open(enemy_path, 'w', encoding='utf-8') as f:
        json.dump(enemy_json, f, ensure_ascii=False, indent=2)
    print(f"unendEnemy JSON: {enemy_path} ({len(enemy_list)} 个 body)")

    # ======== 2. unendPro ========
    pro_files = glob_module.glob(os.path.join(XML_DIR, '*unendProClass*'))
    pro_list = []
    if pro_files:
        with open(pro_files[0], 'r', encoding='utf-8') as f:
            clean_xml = XmlCleaner.clean(f.read())
        root_el = ET.fromstring(clean_xml)

        for father in root_el.findall('.//father'):
            father_name = father.get('name', '')
            for body in father.findall('body'):
                entry = {'father': father_name}
                for k, v in body.attrib.items():
                    if k == 'name':
                        entry['name'] = v
                    elif k == 'cnName':
                        entry['cnName'] = v
                    else:
                        entry[k] = ValueConverter.to_smart_value(v, k)
                pro_list.append(entry)

    pro_json = {"data": {"father": pro_list}}
    pro_path = os.path.join(OUTPUT_DIR, 'unendPro.json')
    with open(pro_path, 'w', encoding='utf-8') as f:
        json.dump(pro_json, f, ensure_ascii=False, indent=2)
    print(f"unendPro JSON: {pro_path} ({len(pro_list)} 条)")

    # ======== 3. Excel ========
    import pandas as pd
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    excel_path = os.path.join(OUTPUT_DIR, f'虚天塔数据更新_{timestamp}.xlsx')
    excel_data = [
        {"PageName": "Data:unendEnemy.json", "Content": json.dumps(enemy_json, ensure_ascii=False)},
        {"PageName": "Data:unendPro.json", "Content": json.dumps(pro_json, ensure_ascii=False)},
    ]
    pd.DataFrame(excel_data).to_excel(excel_path, index=False, header=False)
    print(f"Excel: {excel_path} ({len(excel_data)} 行)")

    # ======== 报告 ========
    report = []
    report.append("=" * 50)
    report.append(f" 爆枪突击虚天塔数据处理报告 - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report.append("=" * 50)
    report.append(f"\n[总体概况]")
    report.append(f" 出场角色 body: {len(enemy_list)} 个")
    report.append(f" 点数 pro: {len(pro_list)} 条")

    report.append("\n[出场角色分类]")
    for e in enemy_list:
        body_count = len(e.get('bodys', []))
        report.append(f" - {e.get('name', '?'):20} ({e.get('cnName', '')}): {body_count} 个")

    report.append("\n[点数 pro 分类 (father)]")
    from collections import defaultdict
    pro_stats = defaultdict(int)
    for p in pro_list:
        pro_stats[p.get('father', 'unknown')] += 1
    for f_name, count in sorted(pro_stats.items()):
        report.append(f" - {f_name:12} : {count} 条")

    final_report = "\n".join(report)
    print(final_report)
    report_path = os.path.join(OUTPUT_DIR, '处理报告.txt')
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(final_report)
    print(f"\n[报告] 统计报告已保存至: {report_path}")

    print(f"\n处理完成！")


if __name__ == '__main__':
    run_unend_processor()
