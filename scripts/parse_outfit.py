"""
爆枪突击套件（Outfit）数据处理器

从 outfitClass 提取套件定义，输出 Outfit.json。
数据结构：<data> → <one>（套件）→ <must>（装备要求）
"""
import os
import json
import glob as glob_module
import datetime
import xml.etree.ElementTree as ET
from core import XmlCleaner, ValueConverter, clean_str
from config import is_skipped_xml

# --- 配置 ---
XML_DIR = './xml'
OUTPUT_DIR = './data/outfit'


def _find_xml(pattern):
    """按文件名片段定位 XML（自动排除屏蔽文件）"""
    for path in glob_module.glob(os.path.join(XML_DIR, pattern)):
        if not is_skipped_xml(os.path.basename(path)):
            return path
    return None


def run_outfit_processor():
    """全自动套件处理器"""
    print(f"开始处理套件数据: {XML_DIR}")
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    outfit_file = _find_xml('*outfitClass*')
    outfit_list = []

    if outfit_file:
        with open(outfit_file, 'r', encoding='utf-8') as f:
            clean_xml = XmlCleaner.clean(f.read())
        root_el = ET.fromstring(clean_xml)

        for one in root_el.findall('.//one'):
            entry = {}
            for k, v in one.attrib.items():
                if k == 'index':
                    continue
                elif k == 'name':
                    entry['name'] = v
                elif k == 'cnName':
                    entry['cnName'] = clean_str(v)
                else:
                    entry[k] = ValueConverter.to_smart_value(v, k)

            musts = []
            for must in one.findall('must'):
                must_obj = {}
                for k, v in must.attrib.items():
                    must_obj[k] = ValueConverter.to_smart_value(v, k)
                musts.append(must_obj)
            entry['musts'] = musts

            outfit_list.append(entry)

    outfit_json = {"data": {"father": outfit_list}}
    outfit_path = os.path.join(OUTPUT_DIR, 'Outfit.json')
    with open(outfit_path, 'w', encoding='utf-8') as f:
        json.dump(outfit_json, f, ensure_ascii=False, indent=2)
    print(f"Outfit JSON: {outfit_path} ({len(outfit_list)} 个套件)")

    # ======== 报告 ========
    report = []
    report.append("=" * 50)
    report.append(f" 爆枪突击套件数据处理报告 - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report.append("=" * 50)
    report.append(f"\n[总体概况] 提取套件总数: {len(outfit_list)} 个")

    total_musts = sum(len(o.get('musts', [])) for o in outfit_list)
    report.append(f" 装备要求总数: {total_musts} 条")

    report.append("\n[套件列表]")
    for o in outfit_list:
        skill = o.get('skill', '')
        hurt = ' [无双]' if o.get('hurtB') else ''
        report.append(f" - {o.get('name', '?'):20} ({o.get('cnName', '')}){hurt}: "
                      f"{len(o.get('musts', []))} 条要求, skill={skill}")

    report.append("\n[异常数据检测]")
    missing_cn = [o.get('name') for o in outfit_list if not o.get('cnName')]
    if missing_cn:
        report.append(f" [X] 缺少中文名的套件 ({len(missing_cn)}个): {', '.join(missing_cn)}")
    else:
        report.append(" [OK] 所有套件均包含中文名。")

    final_report = "\n".join(report)
    print(final_report)
    report_path = os.path.join(OUTPUT_DIR, '处理报告.txt')
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(final_report)
    print(f"\n[报告] 统计报告已保存至: {report_path}")

    print(f"\n处理完成！")


if __name__ == '__main__':
    run_outfit_processor()
