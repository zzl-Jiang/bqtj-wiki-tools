"""
爆枪突击成就（Achieve）数据处理器

从 XML 提取所有成就定义数据，输出独立 JSON + 汇总 JSON + Excel。
数据结构：gather → father → achieve（三层嵌套）
"""
import os
import xml.etree.ElementTree as ET
from core import XmlCleaner, ValueConverter, OutputWriter, ReportGenerator

# --- 配置 ---
XML_DIR = './xml'
OUTPUT_DIR = './data/achieve'

# gift 字段顺序
GIFT_KEYS = ['type', 'name', 'num', 'color', 'lv', 'childType', 'numExtra', 'tipB', 'dropName', 'pro', 'sp']

# 整数属性
INT_ATTRS = {'unlockLv', 'achieveDiff'}


def parse_gift_string(gift_str):
    """解析 <gift> 标签内的分号分隔字符串，返回字典或 None"""
    if not gift_str or not gift_str.strip():
        return None

    parts = gift_str.strip().split(';')
    gift_obj = {}

    for i, prop_name in enumerate(GIFT_KEYS):
        if i >= len(parts):
            break
        value_str = parts[i].strip()
        if not value_str:
            continue

        if prop_name == 'tipB':
            gift_obj[prop_name] = value_str.lower() in ('true', '1')
        elif prop_name in ('num', 'pro', 'sp', 'lv'):
            try:
                gift_obj[prop_name] = float(value_str) if '.' in value_str else int(value_str)
            except ValueError:
                gift_obj[prop_name] = value_str
        else:
            gift_obj[prop_name] = value_str

    return gift_obj if gift_obj else None


def parse_achieve_node(achieve_node, gather_attrs, father_attrs):
    """解析单个 achieve 节点，返回成就数据字典"""
    achieve_data = {}

    # 注入 gather 和 father 信息
    achieve_data.update(gather_attrs)
    achieve_data.update(father_attrs)

    # 处理 achieve 标签属性
    for k, v in achieve_node.attrib.items():
        if k == 'name':
            achieve_data['name'] = v
            continue
        if k in INT_ATTRS:
            achieve_data[k] = int(v)
            continue
        achieve_data[k] = ValueConverter.to_smart_value(v, k)

    # 子节点处理
    desc_node = achieve_node.find('description')
    if desc_node is not None and desc_node.text and desc_node.text.strip():
        achieve_data['description'] = desc_node.text.strip()

    gift_node = achieve_node.find('gift')
    if gift_node is not None and gift_node.text:
        parsed_gift = parse_gift_string(gift_node.text)
        if parsed_gift:
            achieve_data['gift'] = parsed_gift

    condition_node = achieve_node.find('condition')
    if condition_node is not None and condition_node.attrib:
        achieve_data['condition'] = {}
        for k, v in condition_node.attrib.items():
            achieve_data['condition'][k] = ValueConverter.to_smart_value(v, k)

    return achieve_data


def run_achieve_processor():
    """全自动成就处理器：扫描 XML → 提取 gather/father/achieve → JSON/Excel 输出"""
    print(f"开始全量扫描目录: {XML_DIR}")

    achieve_pool = {}

    for root_dir, _, files in os.walk(XML_DIR):
        for file in files:
            if not file.endswith('.bin'):
                continue
            try:
                with open(os.path.join(root_dir, file), 'r', encoding='utf-8') as f:
                    clean_xml = XmlCleaner.clean(f.read())
                root_el = ET.fromstring(clean_xml)

                for gather in root_el.findall('.//gather'):
                    gather_name = gather.get('name', '')
                    gather_cn = gather.get('cnName', '')

                    gather_attrs = {
                        'gather': gather_name,
                        'gatherCnName': gather_cn,
                    }

                    for father in gather.findall('father'):
                        father_name = father.get('name', '')
                        father_attrs = {
                            'father': father_name,
                            'fatherCnName': father.get('cnName', ''),
                        }
                        # father 上的其他属性（如 autoLowB）
                        for k, v in father.attrib.items():
                            if k not in ('name', 'cnName'):
                                father_attrs[k] = ValueConverter.to_smart_value(v, k)

                        for achieve_node in father.findall('achieve'):
                            achieve_data = parse_achieve_node(achieve_node, gather_attrs, father_attrs)
                            if not achieve_data or 'name' not in achieve_data:
                                continue

                            achieve_data = ValueConverter.prepare_output(achieve_data, "爆枪突击", "achieve")
                            achieve_pool[achieve_data['name']] = achieve_data

            except Exception as e:
                print(f"  [!] 错误文件 {file}: {e}")

    print(f"\n[提取] 共提取 {len(achieve_pool)} 个成就")

    # 清理空的 medelProArr
    for data in achieve_pool.values():
        if not data.get('medelProArr'):
            data.pop('medelProArr', None)

    # 生成报告
    ReportGenerator.generate(achieve_pool, OUTPUT_DIR,
                             report_prefix='成就',
                             group_field='gatherCnName',
                             extra_checks={'gift 奖励': 'gift'})

    # --- 保存输出 ---
    OutputWriter.write(achieve_pool, OUTPUT_DIR, 'Achieve', cn_label='成就')

    # --- 附：勋章属性对照表 ---
    # 成就系统通过 medelProArr 字段引用勋章属性名（如 "dpsMul"），
    # 该数据极轻量（约 40 条键值对，无层级结构），不适合独立成模块，
    # 故以轻量步骤挂在此处，仅输出单个 JSON 文件。
    medel_path = _extract_medel_properties()
    if medel_path:
        print(f"勋章属性表: {medel_path}")

    print(f"\n处理完成！提取成就总数: {len(achieve_pool)}")


# ============================================================
#  勋章属性对照表提取（轻量步骤，不独立成模块）
# ============================================================

def _extract_medel_properties():
    """
    从 medelPropertyClass.bin 提取勋章属性对照表。

    数据格式：<data> → <pro name="属性名" v="数值"/>
    用途：成就的 medelProArr 字段引用这些属性名，Wiki 端通过此表
          将属性名解析为具体加成数值。

    注意：
    - 仅扫描文件名含 "medelProperty" 的 .bin 文件，避免误抓其他模块的 <pro> 元素。
    """
    import json as _json

    output_path = os.path.join(OUTPUT_DIR, 'medelProperty.json')
    medel_list = []

    for root_dir, _, files in os.walk(XML_DIR):
        for file in files:
            if not file.endswith('.bin') or 'medelProperty' not in file:
                continue
            try:
                with open(os.path.join(root_dir, file), 'r', encoding='utf-8') as f:
                    clean_xml = XmlCleaner.clean(f.read())
                root_el = ET.fromstring(clean_xml)

                # 勋章属性 <pro> 直接挂在 <data> 下，无 gather/father 包裹
                for pro_node in root_el.findall('pro'):
                    name = pro_node.get('name')
                    if not name:
                        continue
                    v = pro_node.get('v', '0')
                    medel_list.append({
                        'name': name,
                        'v': float(v) if '.' in v else int(v)
                    })

            except Exception:
                continue

    if medel_list:
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            _json.dump(medel_list, f, ensure_ascii=False, indent=2)
        return output_path

    return None


if __name__ == '__main__':
    run_achieve_processor()
