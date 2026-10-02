"""
爆枪突击黑市（BlackMarket）数据处理器

处理黑市相关数据：
  - blackMarketThingsClass → blackMarketThings.json（黑市商品列表）
  - blackMarketPriceClass  → blackMarketPrice.json（商品基础价格）
"""
import os
import json
import glob as glob_module
import datetime
import xml.etree.ElementTree as ET
from core import XmlCleaner, ValueConverter

# --- 配置 ---
XML_DIR = './xml'
OUTPUT_DIR = './data/blackmarket'

# gift 字段顺序：type;name;num
GIFT_KEYS = ['type', 'name', 'num']


def _parse_price_levels(text):
    """将换行数字拆分为价格数组"""
    if not text or not text.strip():
        return []
    result = []
    for v in text.strip().split():
        try:
            result.append(int(v))
        except ValueError:
            try:
                result.append(float(v))
            except ValueError:
                result.append(v)
    return result


def parse_gift_text(text):
    """解析 gift 文本 'type;name;num'"""
    if not text or not text.strip():
        return None
    parts = text.strip().split(';')
    result = {}
    for i, part in enumerate(parts):
        if i < len(GIFT_KEYS) and part:
            result[GIFT_KEYS[i]] = ValueConverter.to_smart_value(part, GIFT_KEYS[i])
    return result


def run_blackmarket_processor():
    """全自动黑市处理器"""
    print(f"开始处理黑市数据: {XML_DIR}")
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # ======== 1. blackMarketThings ========
    things_files = glob_module.glob(os.path.join(XML_DIR, '*blackMarketThingsClass*'))
    things_list = []
    if things_files:
        with open(things_files[0], 'r', encoding='utf-8') as f:
            clean_xml = XmlCleaner.clean(f.read())
        root_el = ET.fromstring(clean_xml)

        for one_node in root_el.findall('.//one'):
            entry = {}
            for k, v in one_node.attrib.items():
                if k == 'name':
                    entry['name'] = v
                elif k == 'cnName':
                    entry['cnName'] = v
                else:
                    entry[k] = ValueConverter.to_smart_value(v, k)

            gifts = []
            for gift_node in one_node.findall('gift'):
                parsed = parse_gift_text(gift_node.text)
                if parsed:
                    gifts.append(parsed)
            entry['gifts'] = gifts

            things_list.append(entry)

    things_json = {"data": {"father": things_list}}
    things_path = os.path.join(OUTPUT_DIR, 'blackMarketThings.json')
    with open(things_path, 'w', encoding='utf-8') as f:
        json.dump(things_json, f, ensure_ascii=False, indent=2)
    print(f"blackMarketThings JSON: {things_path} ({len(things_list)} 个分类)")

    # ======== 2. blackMarketPrice ========
    price_files = glob_module.glob(os.path.join(XML_DIR, '*blackMarketPriceClass*'))
    price_list = []
    if price_files:
        with open(price_files[0], 'r', encoding='utf-8') as f:
            clean_xml = XmlCleaner.clean(f.read())
        root_el = ET.fromstring(clean_xml)

        for body in root_el.findall('.//body'):
            entry = {}
            for k, v in body.attrib.items():
                if k == 'name':
                    entry['name'] = v
                elif k == 'cnName':
                    entry['cnName'] = v
                else:
                    entry[k] = ValueConverter.to_smart_value(v, k)

            text = body.text.strip() if body.text else ''
            entry['prices'] = _parse_price_levels(text)

            price_list.append(entry)

    price_json = {"data": {"father": price_list}}
    price_path = os.path.join(OUTPUT_DIR, 'blackMarketPrice.json')
    with open(price_path, 'w', encoding='utf-8') as f:
        json.dump(price_json, f, ensure_ascii=False, indent=2)
    print(f"blackMarketPrice JSON: {price_path} ({len(price_list)} 个 body)")

    # ======== 报告 ========
    report = []
    report.append("=" * 50)
    report.append(f" 爆枪突击黑市数据处理报告 - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report.append("=" * 50)
    report.append(f"\n[总体概况]")
    report.append(f" 黑市商品分类: {len(things_list)} 个")
    for t in things_list:
        report.append(f" - {t.get('name', '?'):30} ({t.get('cnName', '')}): {len(t.get('gifts', []))} 件商品")
    report.append(f" 商品价格 body: {len(price_list)} 个")
    for p in price_list:
        report.append(f" - {p.get('name', '?')} ({p.get('cnName', '')}): {len(p.get('prices', []))} 个价格")

    final_report = "\n".join(report)
    print(final_report)
    report_path = os.path.join(OUTPUT_DIR, '处理报告.txt')
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(final_report)
    print(f"\n[报告] 统计报告已保存至: {report_path}")

    print(f"\n处理完成！")


if __name__ == '__main__':
    run_blackmarket_processor()
