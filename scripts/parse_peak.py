"""
爆枪突击巅峰等级（Peak）数据处理器

处理巅峰等级相关数据：
  - peakExpClass → peakExp.json（各巅峰等级所需经验）
  - peakProClass → peakPro.json（巅峰可提升的属性词条）
"""
import os
import json
import glob as glob_module
import datetime
import xml.etree.ElementTree as ET
from core import XmlCleaner, ValueConverter
from config import is_skipped_xml

# --- 配置 ---
XML_DIR = './xml'
OUTPUT_DIR = './data/others/peak'


def _find_xml(pattern):
    """按文件名片段定位 XML（自动排除屏蔽文件）"""
    for path in glob_module.glob(os.path.join(XML_DIR, pattern)):
        if not is_skipped_xml(os.path.basename(path)):
            return path
    return None


def _parse_exp_values(text):
    """将换行分隔的经验数值拆分为数组（支持科学计数法），整数值转为 int"""
    if not text or not text.strip():
        return []
    result = []
    for token in text.strip().split():
        try:
            num = float(token)
            result.append(int(num) if num.is_integer() else num)
        except ValueError:
            result.append(token)
    return result


def run_peak_processor():
    """全自动巅峰等级处理器"""
    print(f"开始处理巅峰等级数据: {XML_DIR}")
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # ======== 1. peakExp ========
    exp_file = _find_xml('*peakExpClass*')
    exp_list = []
    if exp_file:
        with open(exp_file, 'r', encoding='utf-8') as f:
            clean_xml = XmlCleaner.clean(f.read())
        root_el = ET.fromstring(clean_xml)

        for father in root_el.findall('.//father'):
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
                entry['exps'] = _parse_exp_values(text)

                exp_list.append(entry)

    exp_json = {"data": {"father": exp_list}}
    exp_path = os.path.join(OUTPUT_DIR, 'peakExp.json')
    with open(exp_path, 'w', encoding='utf-8') as f:
        json.dump(exp_json, f, ensure_ascii=False, indent=2)
    exp_total = sum(len(e.get('exps', [])) for e in exp_list)
    print(f"peakExp JSON: {exp_path} ({len(exp_list)} 个 body / {exp_total} 条经验)")

    # ======== 2. peakPro ========
    pro_file = _find_xml('*peakProClass*')
    pro_list = []
    if pro_file:
        with open(pro_file, 'r', encoding='utf-8') as f:
            clean_xml = XmlCleaner.clean(f.read())
        root_el = ET.fromstring(clean_xml)

        for father in root_el.findall('.//father'):
            for body in father.findall('body'):
                entry = {}
                for k, v in body.attrib.items():
                    if k == 'name':
                        entry['name'] = v
                    elif k == 'cnName':
                        entry['cnName'] = v
                    else:
                        entry[k] = ValueConverter.to_smart_value(v, k)
                pro_list.append(entry)

    pro_json = {"data": {"father": pro_list}}
    pro_path = os.path.join(OUTPUT_DIR, 'peakPro.json')
    with open(pro_path, 'w', encoding='utf-8') as f:
        json.dump(pro_json, f, ensure_ascii=False, indent=2)
    print(f"peakPro JSON: {pro_path} ({len(pro_list)} 个属性)")

    # ======== 报告 ========
    report = []
    report.append("=" * 50)
    report.append(f" 爆枪突击巅峰等级数据处理报告 - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report.append("=" * 50)
    report.append(f"\n[总体概况]")
    report.append(f" 经验表 body: {len(exp_list)} 个")
    for e in exp_list:
        exps = e.get('exps', [])
        first = exps[0] if exps else '-'
        last = exps[-1] if exps else '-'
        report.append(f" - {e.get('name', '?')} ({e.get('cnName', '')}): {len(exps)} 条经验"
                      f"（{first} → {last}）")
    report.append(f" 属性词条: {len(pro_list)} 个")
    for p in pro_list:
        extra = f" add={p.get('add')}" if 'add' in p else ''
        if p.get('skill'):
            extra += f" skill={p['skill']}"
        report.append(f" - {p.get('name', '?'):20} ({p.get('cnName', '')}): max={p.get('max')}{extra}")

    final_report = "\n".join(report)
    print(final_report)
    report_path = os.path.join(OUTPUT_DIR, '处理报告.txt')
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(final_report)
    print(f"\n[报告] 统计报告已保存至: {report_path}")

    print(f"\n处理完成！")


if __name__ == '__main__':
    run_peak_processor()
