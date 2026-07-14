"""
爆枪突击物品数据处理器（含补丁水合）

一步完成：XML 提取 → 武器碎片数据补全 → JSON/Excel 输出
"""
from collections import defaultdict
import os
import re
import json
import glob
import datetime
import xml.etree.ElementTree as ET
from typing import Dict, Any
from core import XmlCleaner, XmlParser, ValueConverter, OutputWriter, clean_game_description

# ============================================================
#  配置
# ============================================================

XML_DIR = './xml'
OUTPUT_DIR = './data/things'
ARMS_JSON_DIR = './data/arms/json'
SUIT_JSON_DIR = './data/suit/json'

# Things 特有的 gift 标签字段映射
GIFT_KEYS = ["type", "name", "num", "color", "lv", "childType", "numExtra", "tipB", "dropName"]


# ============================================================
#  XML 解析工具
# ============================================================

def parse_gift_element(element):
    """解析 gift 标签的内容和属性"""
    obj = {}
    if element.attrib:
        for k, v in element.attrib.items():
            obj[k] = ValueConverter.to_smart_value(v, k)
    if element.text and element.text.strip():
        parts = element.text.strip().split(';')
        for i, part in enumerate(parts):
            if i < len(GIFT_KEYS) and part:
                obj[GIFT_KEYS[i]] = ValueConverter.to_smart_value(part, GIFT_KEYS[i])
    return obj


def process_element(element):
    """通用函数：处理 XML 叶子元素，根据属性/文本/子节点情况返回对应数据类型"""
    if element.attrib and not element.text and not len(element):
        return {k: ValueConverter.to_smart_value(v, k) for k, v in element.attrib.items()}
    if element.attrib:
        obj = {k: ValueConverter.to_smart_value(v, k) for k, v in element.attrib.items()}
        if element.text and element.text.strip():
            obj['value'] = ValueConverter.to_smart_value(element.text.strip(), element.tag)
        return obj
    if element.text and element.text.strip():
        text = element.text.strip()
        if element.tag == 'description':
            return clean_game_description(text)
        return ValueConverter.to_smart_value(text, element.tag)
    return None


def parse_things_node(things_node, father_attrs):
    """解析单个 <things> 节点，返回物品数据字典"""
    item_obj = {}
    item_obj.update(father_attrs)
    if things_node.attrib:
        for k, v in things_node.attrib.items():
            item_obj[k] = ValueConverter.to_smart_value(v, k)
    children_dict = {}
    for child in things_node:
        tag = child.tag
        if tag not in children_dict:
            children_dict[tag] = []
        if tag == 'gift':
            children_dict[tag].append(parse_gift_element(child))
        else:
            processed_value = process_element(child)
            if processed_value is not None:
                children_dict[tag].append(processed_value)
    for tag, values in children_dict.items():
        if len(values) > 1:
            item_obj[tag] = values
        elif len(values) == 1:
            if tag in ['gift']:
                item_obj[tag] = values
            else:
                item_obj[tag] = values[0]
    return item_obj


# ============================================================
#  Smelt 熔炼配置
# ============================================================

def _get_smelt_config(items_level: int, color: str) -> Dict[str, Any]:
    """武器碎片 smeltD 配置"""
    config = {"type": "armsChip", "grade": 1, "price": 2, "maxNum": None, "addType": None}
    if items_level < 86:
        config["price"] = 2
        config["grade"] = 1
    elif items_level < 91:
        config["price"] = 10
        config["grade"] = 2
        config["maxNum"] = 1
        config["addType"] = "armsEquip"
    else:
        config["price"] = 1
    if items_level >= 90 or color in ["darkgold", "purgold", "yagold"]:
        config["grade"] = -1
    return config

# ============================================================
#  数据加载（外部 JSON）
# ============================================================

def _load_arms_data() -> Dict[str, Dict[str, Any]]:
    """加载武器数据，按名称索引"""
    arms_index = {}
    if not os.path.exists(ARMS_JSON_DIR):
        print(f"\n[补丁] 武器数据目录不存在: {ARMS_JSON_DIR}，跳过补丁阶段")
        print("       请先运行 parse_arms.py 生成武器数据")
        return arms_index
    for json_file in glob.glob(os.path.join(ARMS_JSON_DIR, '*.json')):
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                name = data.get('name')
                if name:
                    arms_index[name] = data
        except Exception as e:
            print(f"[补丁] 加载武器文件失败 {json_file}: {e}")
    print(f"[补丁] 已加载 {len(arms_index)} 个武器定义")
    return arms_index


def _load_suit_data() -> Dict[str, list]:
    """加载套装数据，提取黑色套装的部件列表。返回 {suit_name: [part_dict, ...]}"""
    suit_parts = {}
    if not os.path.exists(SUIT_JSON_DIR):
        print(f"\n[补丁] 套装数据目录不存在: {SUIT_JSON_DIR}，跳过装备碎片补丁")
        print("       请先运行 parse_suit.py 生成套装数据")
        return suit_parts
    for json_file in glob.glob(os.path.join(SUIT_JSON_DIR, '*.json')):
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            if data.get('color') != 'black':
                continue
            suit_name = data.get('name', '')
            parts = data.get('image', [])
            if suit_name and parts:
                suit_parts[suit_name] = parts
        except Exception as e:
            print(f"[补丁] 加载套装文件失败 {json_file}: {e}")
    if suit_parts:
        total_parts = sum(len(v) for v in suit_parts.values())
        print(f"[补丁] 已加载 {len(suit_parts)} 个黑色套装（共 {total_parts} 个部件）")
    return suit_parts


# ============================================================
#  补丁：武器碎片
# ============================================================

def _patch_black_chip(thing_data: dict, arms_data: dict) -> bool:
    """修补黑色武器碎片数据"""
    name = thing_data.get('name')
    if name not in arms_data:
        return False
    arm = arms_data[name]
    compose_lv = arm.get('composeLv', 0)
    if compose_lv <= 0:
        return False

    thing_data['secType'] = 'arms'
    thing_data['itemsLevel'] = compose_lv
    if not thing_data.get('iconUrl'):
        thing_data['iconUrl'] = arm.get('iconUrl') or f"ThingsIcon/{name}Icon"

    smelt_config = _get_smelt_config(compose_lv, arm.get('color', ''))
    existing_smelt = thing_data.get('smeltD', {})
    if isinstance(existing_smelt, dict):
        for key, value in smelt_config.items():
            if key not in existing_smelt or existing_smelt[key] is None:
                existing_smelt[key] = value
        thing_data['smeltD'] = existing_smelt
    else:
        thing_data['smeltD'] = smelt_config

    thing_data['btnList'] = ['compose']
    thing_data['_patched'] = True
    return True


def _patch_rare_chip(thing_data: dict, arms_data: dict) -> bool:
    """修补稀有武器碎片数据"""
    name = thing_data.get('name')
    cn_name = thing_data.get('cnName', '')
    if not cn_name.endswith('稀有碎片'):
        return False
    if name not in arms_data:
        return False
    arm = arms_data[name]
    if arm.get('chipNum', 0) <= 0:
        return False

    thing_data['secType'] = 'arms'
    if not thing_data.get('description'):
        thing_data['description'] = f"合成{arm.get('cnName', '')}所需物品。"
    if 'itemsLevel' not in thing_data:
        thing_data['itemsLevel'] = arm.get('rareDropLevel', 1)
    thing_data['smeltD'] = {"type": "armsChip", "grade": 1, "price": 10}
    thing_data['btnList'] = ['compose']
    if not thing_data.get('iconUrl'):
        thing_data['iconUrl'] = arm.get('iconUrl') or f"ThingsIcon/{name}Icon"
    thing_data['_patched'] = True
    return True


def _generate_missing_chips(things_pool: dict, arms_data: dict) -> dict:
    """为 chipNum > 0 但尚无 things 条目的武器生成碎片（黑色/稀有分类处理）"""
    rare_template = things_pool.get('rareChip', {}).copy() if 'rareChip' in things_pool else {
        'father': 'rareChip', 'fatherCnName': '稀有碎片', 'hideB': True, 'addDropDefineB': True,
    }
    black_template = things_pool.get('blackChip', {}).copy() if 'blackChip' in things_pool else {
        'father': 'blackChip', 'fatherCnName': '黑色碎片', 'hideB': True, 'addDropDefineB': True,
    }

    stats = {'black_generated': 0, 'rare_generated': 0}
    for arm_name, arm_data in arms_data.items():
        if arm_data.get('chipNum', 0) <= 0:
            continue
        if arm_name in things_pool:
            continue

        weapon_cn = arm_data.get('cnName', '')
        is_black = arm_data.get('color') == 'black'

        if is_black:
            template = black_template.copy()
            template.update({
                'name': arm_name,
                'cnName': f'{weapon_cn}碎片',
                'secType': 'arms',
                'description': f'合成{weapon_cn}所需物品。',
                'itemsLevel': arm_data.get('composeLv', 1),
                'iconUrl': arm_data.get('iconUrl') or f'ThingsIcon/{arm_name}Icon',
                'smeltD': {'type': 'armsChip', 'grade': 1, 'price': 2},
                'btnList': ['compose'],
                '_generated': True,
            })
            things_pool[arm_name] = template
            stats['black_generated'] += 1
            print(f"  [补丁/生成] 黑色碎片: {arm_name} ({template['cnName']})")
        else:
            template = rare_template.copy()
            template.update({
                'name': arm_name,
                'cnName': f'{weapon_cn}稀有碎片',
                'secType': 'arms',
                'description': f'合成{weapon_cn}所需物品。',
                'itemsLevel': arm_data.get('rareDropLevel', 1),
                'iconUrl': arm_data.get('iconUrl') or f'ThingsIcon/{arm_name}Icon',
                'smeltD': {'type': 'armsChip', 'grade': 1, 'price': 10},
                'btnList': ['compose'],
                '_generated': True,
            })
            things_pool[arm_name] = template
            stats['rare_generated'] += 1
            print(f"  [补丁/生成] 稀有碎片: {arm_name} ({template['cnName']})")

    return stats


# ============================================================
#  补丁：套装碎片
# ============================================================

def _generate_suit_chips(things_pool: dict) -> int:
    """为黑色套装部件生成/修补装备碎片条目（XML + suit JSON 合并处理）"""
    black_equip_files = glob.glob(os.path.join(XML_DIR, '*blackEquipClass*'))
    if not black_equip_files:
        return 0

    with open(black_equip_files[0], 'r', encoding='utf-8') as f:
        clean_xml = XmlCleaner.clean(f.read())

    try:
        root_el = ET.fromstring(clean_xml)
    except Exception:
        return 0

    suit_data = _load_suit_data()

    black_template = {
        'father': 'blackChip', 'fatherCnName': '黑色碎片',
        'secType': 'equip', 'btnList': ['compose', 'composeNum'],
        'hideB': True, 'addDropDefineB': True, '_generated': True,
    }

    generated = 0
    for gather in root_el.findall('.//gather'):
        if gather.get('cnName') != '黑色':
            continue
        for father in gather.findall('father'):
            f_name = father.get('name', '')
            parts = suit_data.get(f_name, [])
            parts_by_type = {p.get('type', ''): p for p in parts}

            for image in father.findall('image'):
                img_type = image.find('type')
                img_cn = image.find('cnName')
                type_val = img_type.text.strip() if img_type is not None and img_type.text else ''
                cn_val = img_cn.text.strip() if img_cn is not None and img_cn.text else ''
                if not type_val or not cn_val:
                    continue

                chip_name = f'{f_name}_{type_val}'
                part_info = parts_by_type.get(type_val, {})
                items_level = part_info.get('itemsLevel', 0)

                if chip_name in things_pool:
                    existing = things_pool[chip_name]
                    existing['secType'] = 'equip'
                    existing['itemsLevel'] = items_level
                    existing['smeltD'] = _get_smelt_config(items_level, 'black')
                    existing['btnList'] = ['compose', 'composeNum']
                    if not existing.get('iconUrl'):
                        existing['iconUrl'] = f'ThingsIcon/{chip_name}'
                    existing['_patched'] = True
                    print(f"  [补丁/套装碎片] {chip_name} (已存在，已更新 smeltD/btnList)")
                    continue

                chip = black_template.copy()
                chip['name'] = chip_name
                chip['cnName'] = f'{cn_val}碎片'
                chip['iconUrl'] = f'ThingsIcon/{chip_name}'
                chip['itemsLevel'] = items_level
                chip['smeltD'] = _get_smelt_config(items_level, 'black')
                chip = ValueConverter.prepare_output(chip, "爆枪突击", "things")
                things_pool[chip_name] = chip
                generated += 1
                print(f"  [补丁/生成] 套装碎片: {chip_name} ({chip['cnName']})")

    return generated


# ============================================================
#  补丁：图标修正
# ============================================================

def _patch_chip_icon(things_pool: dict) -> int:
    """修正碎片 iconUrl：xxx/chip → xxx/xxxChip"""
    count = 0
    for name, data in things_pool.items():
        icon = data.get('iconUrl', '')
        m = re.match(r'^(.+)/chip$', icon)
        if m:
            data['iconUrl'] = f'{m.group(1)}/{m.group(1)}Chip'
            data['_patched'] = True
            count += 1
            print(f"  [补丁/iconUrl] {name}: {icon} -> {data['iconUrl']}")
    return count


# ============================================================
#  手动添加条目（历史 Bug 产物，Wiki 需要体现但已在游戏中移除）
# ============================================================

def _add_manual_entries(things_pool: dict) -> int:
    """
    向物品池中添加无法从 XML 提取的手动条目。

    添加方法：在下方 MANUAL_ENTRIES 列表中按格式添加，脚本自动处理。
    """
    MANUAL_ENTRIES: list = [
        {
            "name": "huntParts_1",
            "cnName": "猎人技能器",
            "father": "other",
            "fatherCnName": "其他",
            "iconUrl": "ThingsIcon/huntParts1"
        },
        {
            "name": "acidicParts_1",
            "cnName": "腐蚀芯片",
            "father": "other",
            "fatherCnName": "其他",
            "iconUrl": "ThingsIcon/acidicParts1"
        },
    ]

    added = 0
    for entry in MANUAL_ENTRIES:
        name = entry.get('name')
        if not name:
            print("  [!] 手动条目缺少 name 字段，已跳过")
            continue
        if name in things_pool:
            print(f"  [!] 手动条目 {name} 与已有物品冲突，已跳过（请检查 MANUAL_ENTRIES）")
            continue
        entry['_manual'] = True
        entry = ValueConverter.prepare_output(entry, "爆枪突击", "things")
        things_pool[name] = entry
        added += 1
        print(f"  [手动条目] {name} ({entry.get('cnName', '')})")

    if added:
        print(f"[手动条目] 已添加 {added} 个手动条目")
    return added


# ============================================================
#  补丁协调
# ============================================================

def _apply_patches(things_pool: dict) -> dict:
    """对 things_pool 执行全套补丁（武器碎片 + 套装碎片 + 图标修正 + 手动条目），返回统计信息"""
    # 武器碎片
    arms_data = _load_arms_data()

    gen_stats = {'black_generated': 0, 'rare_generated': 0}
    stats = {'black_chips': 0, 'rare_chips': 0, 'black_generated': 0,
             'rare_generated': 0, 'suit_generated': 0, 'chip_icon_fixed': 0,
             'manual': 0, 'skipped': 0, 'errors': 0}

    if arms_data:
        gen_stats = _generate_missing_chips(things_pool, arms_data)

        for thing_name, thing_data in things_pool.items():
            try:
                father = thing_data.get('father', '')
                if father not in ['blackChip', 'rareChip']:
                    continue

                if father == 'blackChip':
                    if _patch_black_chip(thing_data, arms_data):
                        stats['black_chips'] += 1
                        print(f"  [补丁/黑武碎片] {thing_name} ({thing_data.get('cnName')})")
                    else:
                        stats['skipped'] += 1
                elif father == 'rareChip':
                    if thing_data.get('_generated'):
                        continue
                    if _patch_rare_chip(thing_data, arms_data):
                        stats['rare_chips'] += 1
                        print(f"  [补丁/稀有碎片] {thing_name} ({thing_data.get('cnName')})")
                    else:
                        stats['skipped'] += 1
            except Exception as e:
                print(f"  [!] 处理 {thing_name} 时出错: {e}")
                stats['errors'] += 1

    # 套装碎片
    stats['suit_generated'] = _generate_suit_chips(things_pool)

    # 图标修正
    stats['chip_icon_fixed'] = _patch_chip_icon(things_pool)

    # 手动条目
    stats['manual'] = _add_manual_entries(things_pool)

    stats['black_generated'] = gen_stats.get('black_generated', 0)
    stats['rare_generated'] = gen_stats.get('rare_generated', 0)

    return stats


# ============================================================
#  统计报告
# ============================================================

def generate_summary(things_pool, patch_stats=None):
    """生成数据统计报告"""
    report = []
    report.append("=" * 50)
    report.append(f" 爆枪突击物品数据处理报告 - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report.append("=" * 50)

    total_count = len(things_pool)
    report.append(f"\n[总体概况] 提取物品总数: {total_count} 个")

    report.append("\n[分类统计 (Father)]")
    father_stats = defaultdict(int)
    for data in things_pool.values():
        f_name = data.get('father', 'unknown')
        father_stats[f_name] += 1
    for f_name, count in sorted(father_stats.items(), key=lambda x: x[1], reverse=True):
        report.append(f" - {f_name:20} : {count} 个")

    report.append("\n[重名异常检测 (同一中文名对应多个英文 ID)]")
    cn_map = defaultdict(list)
    for name, data in things_pool.items():
        cn = data.get('cnName') or "[缺失中文名]"
        cn_map[cn].append(name)
    dup_count = 0
    for cn, names in cn_map.items():
        if len(names) > 1:
            dup_count += 1
            report.append(f" [!] 名称: {cn}")
            report.append(f"     关联ID: {', '.join(names)}")
    if dup_count == 0:
        report.append(" [OK] 未发现重名冲突。")
    else:
        report.append(f"\n 共发现 {dup_count} 组重名物品。")

    report.append("\n[异常数据检测]")
    missing_cn = [n for n, d in things_pool.items() if not d.get('cnName')]
    if missing_cn:
        report.append(f" [X] 缺少中文名的物品 ({len(missing_cn)}个):")
        report.append(f"    {', '.join(missing_cn[:20])}...")
    else:
        report.append(" [OK] 所有物品均包含中文名。")

    missing_icon = [n for n, d in things_pool.items() if not d.get('iconUrl')]
    report.append(f"\n[图标缺失 (iconUrl)]")
    if missing_icon:
        report.append(f" [X] 缺少 iconUrl 的物品 ({len(missing_icon)}个):")
        for n in missing_icon[:30]:
            report.append(f"    {n}")
        if len(missing_icon) > 30:
            report.append(f"    ... 共 {len(missing_icon)} 个")
    else:
        report.append(" [OK] 所有物品均包含 iconUrl。")

    # 补丁统计
    if patch_stats:
        total_patched = (patch_stats['black_chips'] + patch_stats['rare_chips']
                         + patch_stats['black_generated'] + patch_stats['rare_generated'])
        report.append(f"\n[补丁水合]")
        report.append(f" 黑色武器碎片已修补: {patch_stats['black_chips']}")
        report.append(f" 稀有武器碎片已修补: {patch_stats['rare_chips']}")
        if patch_stats['black_generated']:
            report.append(f" 黑色武器碎片已生成: {patch_stats['black_generated']}")
        if patch_stats['rare_generated']:
            report.append(f" 稀有武器碎片已生成: {patch_stats['rare_generated']}")
        report.append(f" 跳过: {patch_stats['skipped']}")
        if patch_stats['errors']:
            report.append(f" 错误: {patch_stats['errors']}")
        if patch_stats.get('suit_generated'):
            report.append(f" 套装部件碎片已生成: {patch_stats['suit_generated']}")
        if patch_stats.get('chip_icon_fixed'):
            report.append(f" 碎片 iconUrl 已修正: {patch_stats['chip_icon_fixed']}")
        if patch_stats.get('manual'):
            report.append(f" 手动条目已添加: {patch_stats['manual']}")
        total_all = (total_patched + patch_stats.get('suit_generated', 0)
                     + patch_stats.get('chip_icon_fixed', 0) + patch_stats.get('manual', 0))
        report.append(f" 合计修补/生成: {total_all}")

    final_report = "\n".join(report)
    print(final_report)
    report_path = os.path.join(OUTPUT_DIR, '处理报告.txt')
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(final_report)
    print(f"\n[报告] 统计报告已保存至: {report_path}")


# ============================================================
#  主入口
# ============================================================

def run_things_processor():
    """全自动物品处理器：XML 提取 → 补丁水合 → JSON/Excel 输出"""

    print(f"开始全量扫描目录: {XML_DIR}")

    # ======== Phase 1: XML 提取 ========
    print("\n--- Phase 1: XML 提取 ---")
    things_pool = {}

    for root, _, files in os.walk(XML_DIR):
        for file in files:
            if not file.endswith('.bin'):
                continue
            try:
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    clean_xml = XmlCleaner.clean(f.read())
                root_el = ET.fromstring(clean_xml)
                for father in root_el.findall('.//father'):
                    father_name = father.attrib.get('name')
                    if not father_name or father_name == "parts":
                        continue
                    father_attrs = {}
                    for k, v in father.attrib.items():
                        if k == 'name':
                            father_attrs['father'] = v
                        elif k == 'cnName':
                            father_attrs['fatherCnName'] = v
                        else:
                            father_attrs[k] = ValueConverter.to_smart_value(v, k)
                    for things_node in father.findall('things'):
                        things_data = parse_things_node(things_node, father_attrs)
                        if not things_data or 'name' not in things_data:
                            continue
                        things_data = ValueConverter.prepare_output(things_data, "爆枪突击", "things")
                        things_pool[things_data['name']] = things_data
            except Exception as e:
                print(f"  [!] 错误文件 {file}: {e}")

    print(f"[提取] 共提取 {len(things_pool)} 个物品")

    # ======== Phase 2: 补丁水合 ========
    print("\n--- Phase 2: 补丁水合 ---")
    patch_stats = _apply_patches(things_pool)

    # ======== Phase 3: 报告与输出 ========
    print(f"\n--- Phase 3: 保存输出 ---")
    generate_summary(things_pool, patch_stats)

    # 保存 JSON（独立 + 汇总）
    OutputWriter.write(things_pool, OUTPUT_DIR, 'Things', cn_label='物品',
                       clean_keys=['_generated', '_patched', '_manual'], skip_excel=True)

    # Excel（全量单表）
    timestamp = OutputWriter.write_excel(things_pool, OUTPUT_DIR, 'Things', '物品')

    # ThingsItemData（精简查询 JSON）
    thing_items = []
    for key, data in things_pool.items():
        entry = {}
        for k in ('name', 'cnName', 'iconUrl'):
            val = data.get(k)
            if val is not None and val != '':
                entry[k] = val
        thing_items.append(entry)

    things_item_json = {
        "data": {
            "father": {
                "@name": "ThingsItem",
                "@cnName": "物品标签",
                "item": thing_items
            }
        }
    }

    item_json_path = os.path.join(OUTPUT_DIR, 'ThingsItemData.json')
    with open(item_json_path, 'w', encoding='utf-8') as f:
        json.dump(things_item_json, f, ensure_ascii=False, indent=2)
    print(f"ThingsItemData JSON: {item_json_path} ({len(thing_items)} 条)")

    # 追加到 Excel
    import pandas as pd
    excel_path = os.path.join(OUTPUT_DIR, f'物品数据更新_{timestamp}.xlsx')
    existing_df = pd.read_excel(excel_path, header=None)
    new_row = pd.DataFrame([{
        0: "Data:ThingsItemData.json",
        1: json.dumps(things_item_json, ensure_ascii=False)
    }])
    pd.concat([existing_df, new_row], ignore_index=True).to_excel(excel_path, index=False, header=False)

    # 最终统计
    total_patched = (patch_stats.get('black_chips', 0) + patch_stats.get('rare_chips', 0) +
                     patch_stats.get('black_generated', 0) + patch_stats.get('rare_generated', 0) +
                     patch_stats.get('suit_generated', 0) + patch_stats.get('chip_icon_fixed', 0) +
                     patch_stats.get('manual', 0))
    print(f"\n处理完成！物品总数: {len(things_pool)}，本次修补/生成: {total_patched}")


if __name__ == '__main__':
    run_things_processor()
