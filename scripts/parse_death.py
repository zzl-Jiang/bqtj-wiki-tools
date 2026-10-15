"""
爆枪突击肉鸽模式（Death）数据处理器

处理肉鸽模式相关数据：
  - deathUnlockClass → deathUnlock.json（肉鸽模式解锁项）
  - deathMapListClass → deathMapList.json（肉鸽模式地图列表）
"""
import os
import json
import glob as glob_module
import datetime
import xml.etree.ElementTree as ET
from core import XmlCleaner, ValueConverter

# --- 配置 ---
XML_DIR = './xml'
OUTPUT_DIR = './data/death'


def _parse_map_names(text):
    """将换行分隔的地图名拆分为字符串数组"""
    if not text or not text.strip():
        return []
    return [line.strip() for line in text.strip().split('\n') if line.strip()]


def run_death_processor():
    """全自动肉鸽模式处理器"""
    print(f"开始处理肉鸽模式数据: {XML_DIR}")
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # ======== 1. deathUnlock ========
    unlock_files = glob_module.glob(os.path.join(XML_DIR, '*deathUnlockClass*'))
    unlock_list = []
    if unlock_files:
        with open(unlock_files[0], 'r', encoding='utf-8') as f:
            clean_xml = XmlCleaner.clean(f.read())
        root_el = ET.fromstring(clean_xml)

        for father in root_el.findall('.//father'):
            entry = {}
            f_name = father.get('name', '')
            f_text = father.get('text', '')
            entry['name'] = f_name
            if f_text:
                entry['text'] = f_text

            bodys = []
            for body in father.findall('body'):
                body_data = {}
                for k, v in body.attrib.items():
                    body_data[k] = ValueConverter.to_smart_value(v, k)
                bodys.append(body_data)
            entry['bodys'] = bodys

            unlock_list.append(entry)

    unlock_json = {"data": {"father": unlock_list}}
    unlock_path = os.path.join(OUTPUT_DIR, 'deathUnlock.json')
    with open(unlock_path, 'w', encoding='utf-8') as f:
        json.dump(unlock_json, f, ensure_ascii=False, indent=2)
    print(f"deathUnlock JSON: {unlock_path} ({len(unlock_list)} 个解锁项)")

    # ======== 2. deathMapList ========
    maplist_files = glob_module.glob(os.path.join(XML_DIR, '*deathMapListClass*'))
    maplist_list = []
    if maplist_files:
        with open(maplist_files[0], 'r', encoding='utf-8') as f:
            clean_xml = XmlCleaner.clean(f.read())
        root_el = ET.fromstring(clean_xml)

        for father in root_el.findall('.//father'):
            if father.get('name') != 'deathMap':
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
                entry['maps'] = _parse_map_names(text)

                maplist_list.append(entry)

    maplist_json = {"data": {"father": maplist_list}}
    maplist_path = os.path.join(OUTPUT_DIR, 'deathMapList.json')
    with open(maplist_path, 'w', encoding='utf-8') as f:
        json.dump(maplist_json, f, ensure_ascii=False, indent=2)
    print(f"deathMapList JSON: {maplist_path} ({len(maplist_list)} 个地图分组)")

    # ======== 报告 ========
    report = []
    report.append("=" * 50)
    report.append(f" 爆枪突击肉鸽模式数据处理报告 - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report.append("=" * 50)
    report.append(f"\n[总体概况]")
    report.append(f" 肉鸽模式解锁项: {len(unlock_list)} 个")
    for u in unlock_list:
        report.append(f" - {u.get('name', '?'):20}: {len(u.get('bodys', []))} 个等级")
    report.append(f" 肉鸽模式地图分组: {len(maplist_list)} 个")
    for m in maplist_list:
        report.append(f" - {m.get('name', '?'):20} ({m.get('cnName', '')}): {len(m.get('maps', []))} 个地图")

    final_report = "\n".join(report)
    print(final_report)
    report_path = os.path.join(OUTPUT_DIR, '处理报告.txt')
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(final_report)
    print(f"\n[报告] 统计报告已保存至: {report_path}")

    print(f"\n处理完成！")


if __name__ == '__main__':
    run_death_processor()
