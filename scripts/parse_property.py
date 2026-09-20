"""
爆枪突击属性（Property）数据处理器

从所有 .bin 文件中提取 <pro> 元素，按源文件独立输出 JSON。
不同文件的属性格式差异较大，因此采用"按源隔离 + 统一索引"策略，
每个源文件独立输出，避免跨文件属性覆盖或格式冲突。
"""
import os
import json
import re
import datetime
import xml.etree.ElementTree as ET
from core import XmlCleaner, ValueConverter
from config import SUFFIX_MAP

# --- 配置 ---
XML_DIR = './xml'
OUTPUT_DIR = './data/property'

# 优先用于补全中文名的来源文件
PRIORITY_SOURCES = ('equipRangeClass', 'suitPropertyClass')


def _parse_text_levels(text):
    """将 <pro> 的 text 内容按空白字符拆分为等级数组，尝试转为数字"""
    if not text or not text.strip():
        return None
    parts = text.strip().split()
    result = []
    for v in parts:
        try:
            result.append(int(v))
        except ValueError:
            try:
                result.append(float(v.rstrip('%')))
            except ValueError:
                result.append(v)
    return result if result else None


def _smart_value(v):
    """将字符串转为最合适的 Python 类型"""
    if v is None:
        return None
    v = v.strip()
    if not v:
        return v
    # 布尔
    if v.lower() in ('true', '1'):
        return True
    if v.lower() in ('false', '0'):
        return False
    # 数字
    try:
        return int(v)
    except ValueError:
        try:
            return float(v)
        except ValueError:
            return v


def _fill_cn_name(name, global_map):
    """补全缺失的中文名。带后缀词条（如 dpsMul_rifle）拆成 base + 后缀组合"""
    if name in global_map and global_map[name]:
        return global_map[name]
    # 带后缀：base_suffix
    if '_' in name:
        base, _, suffix = name.rpartition('_')
        if base in global_map and global_map[base] and suffix in SUFFIX_MAP:
            return f"{global_map[base]}/{SUFFIX_MAP[suffix]}"
    return ''


def parse_pro_node(pro_node):
    """解析单个 <pro> 元素，返回数据字典"""
    data = {}
    # 属性
    for k, v in pro_node.attrib.items():
        data[k] = _smart_value(v) if k != 'name' and k != 'cnName' else v

    # 文本内容（等级数据）
    text = pro_node.text.strip() if pro_node.text else ''
    levels = _parse_text_levels(text)
    if levels:
        data['_levels'] = levels

    # 子元素（如 partsPropertyClass 的 effectName/effectCnName/range）
    children = {}
    for child in pro_node:
        tag = child.tag
        if tag == 'range':
            if 'ranges' not in children:
                children['ranges'] = []
            range_data = {k: _smart_value(v) for k, v in child.attrib.items()}
            children['ranges'].append(range_data)
        else:
            # effectName, effectCnName 等
            children[tag] = child.text.strip() if child.text else ''

    for k, v in children.items():
        if v or v == 0:
            data[k] = v

    return data


def run_property_processor():
    """全自动属性处理器：扫描 XML → 按源文件分组提取 <pro> → 输出独立 JSON + 索引"""
    print(f"开始全量扫描目录: {XML_DIR}")

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # file_stem → [pro_dict, ...]
    file_groups = {}
    total_pros = 0

    for root_dir, _, files in os.walk(XML_DIR):
        for file in files:
            if not file.endswith('.bin'):
                continue
            try:
                path = os.path.join(root_dir, file)
                with open(path, 'r', encoding='utf-8') as f:
                    clean_xml = XmlCleaner.clean(f.read())
                root_el = ET.fromstring(clean_xml)

                pros = root_el.findall('.//pro')
                if not pros:
                    continue

                stem = os.path.splitext(file)[0]
                pro_list = []
                for pro_node in pros:
                    pro_data = parse_pro_node(pro_node)
                    if 'name' not in pro_data:
                        continue
                    pro_list.append(pro_data)

                if pro_list:
                    file_groups[stem] = pro_list
                    total_pros += len(pro_list)

            except Exception as e:
                print(f"  [!] 错误文件 {file}: {e}")

    print(f"\n[提取] 共 {total_pros} 个属性定义，分布在 {len(file_groups)} 个源文件中\n")

    # --- 按来源汇总输出 ---
    # 提取源文件名中的人类可读部分（去掉数字前缀和 _XMLOut_）
    def _short_name(stem):
        return re.sub(r'^\d+_XMLOut_', '', stem).replace('__', '_')

    summary = {}
    for stem, pro_list in sorted(file_groups.items()):
        key = _short_name(stem)
        summary[key] = pro_list
        print(f"  {key}: {len(pro_list)} 个属性")

    # 输出汇总 JSON（全量数据）
    summary_path = os.path.join(OUTPUT_DIR, '属性数据汇总.json')
    with open(summary_path, 'w', encoding='utf-8') as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    print(f"\n汇总文件: {summary_path}")

    # 输出对照表（仅 name → cnName，按来源分组）
    # 先建立全局 name → cnName 映射，用于补全缺失的中文名（优先 equipRangeClass/suitPropertyClass）
    global_map = {}
    for stem, pro_list in sorted(file_groups.items()):
        key = _short_name(stem)
        if key not in PRIORITY_SOURCES:
            continue
        for pro in pro_list:
            name = pro.get('name')
            cn = pro.get('cnName', '')
            if name and cn:
                global_map[name] = cn
    for stem, pro_list in sorted(file_groups.items()):
        key = _short_name(stem)
        if key in PRIORITY_SOURCES:
            continue
        for pro in pro_list:
            name = pro.get('name')
            cn = pro.get('cnName', '')
            if name and cn and name not in global_map:
                global_map[name] = cn

    lookup = {}
    filled_count = 0
    for stem, pro_list in sorted(file_groups.items()):
        key = _short_name(stem)
        lookup[key] = {}
        for pro in pro_list:
            name = pro.get('name')
            if not name:
                continue
            cn = pro.get('cnName', '')
            if not cn:
                filled = _fill_cn_name(name, global_map)
                if filled:
                    cn = filled
                    filled_count += 1
            lookup[key][name] = cn
    lookup_path = os.path.join(OUTPUT_DIR, '属性名称对照表.json')
    with open(lookup_path, 'w', encoding='utf-8') as f:
        json.dump(lookup, f, ensure_ascii=False, indent=2)
    print(f"名称对照表: {lookup_path}（补全 {filled_count} 个缺失中文名）")

    print(f"\n处理完成！{len(file_groups)} 个文件，{total_pros} 个属性")


if __name__ == '__main__':
    run_property_processor()
