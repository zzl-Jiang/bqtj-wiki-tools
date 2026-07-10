"""
爆枪突击活跃度（Active）数据处理器

从 XML 提取活跃度任务定义和奖励档位数据，输出 JSON + Excel。
数据结构：<data> → <task>/<gift> → <one>（两层，无 father 包裹）
  - task/one：每日活跃任务，自闭合属性型
  - gift/one：活跃奖励档位，含嵌套 <gift> 子标签（分号分隔字符串）
"""
import json
import os
import datetime
import xml.etree.ElementTree as ET
from core import XmlCleaner, ValueConverter, OutputWriter, ReportGenerator

# --- 配置 ---
XML_DIR = './xml'
OUTPUT_DIR = './data/active'

# 活跃度奖励的 gift 子标签字段顺序（type;name;num，3 字段）
ACTIVE_GIFT_KEYS = ['type', 'name', 'num']


def parse_active_gift_string(gift_str):
    """
    解析活跃度奖励的 <gift> 子标签内容。

    格式: type;name;num（如 "things;skillFleshCard;1"）
    返回: {"type": "things", "name": "skillFleshCard", "num": 1}
    解析失败时返回原始字符串作为备用。
    """
    if not gift_str or not gift_str.strip():
        return None

    parts = gift_str.strip().split(';')
    if len(parts) >= 3:
        try:
            return {
                'type': parts[0].strip(),
                'name': parts[1].strip(),
                'num': int(parts[2].strip())
            }
        except (ValueError, IndexError):
            return gift_str.strip()
    return gift_str.strip()


def parse_task_one(one_node):
    """解析 <task> 下的 <one> 节点（活跃任务），返回数据字典"""
    task = {}
    for k, v in one_node.attrib.items():
        if k == 'name':
            task['name'] = v
        elif k == 'num':
            task[k] = int(v)
        elif k == 'active':
            task[k] = int(v)
        elif k == 'noGotoB':
            task[k] = v == '1'
        else:
            task[k] = ValueConverter.to_smart_value(v, k)
    task['subType'] = 'task'
    return task


def parse_gift_one(one_node):
    """解析 <gift> 下的 <one> 节点（活跃奖励档位），返回数据字典"""
    gift_entry = {}
    for k, v in one_node.attrib.items():
        if k == 'name':
            gift_entry['name'] = v
        elif k == 'must':
            gift_entry[k] = int(v)
        else:
            gift_entry[k] = ValueConverter.to_smart_value(v, k)
    gift_entry['subType'] = 'gift'

    # 解析嵌套的 <gift> 子标签
    nested_gifts = []
    for gift_child in one_node.findall('gift'):
        parsed = parse_active_gift_string(gift_child.text)
        if parsed:
            nested_gifts.append(parsed)
    if nested_gifts:
        gift_entry['gifts'] = nested_gifts

    return gift_entry


def run_active_processor():
    """全自动活跃度处理器：扫描 XML → 提取 task/gift 的 one 节点 → JSON/Excel 输出"""
    print(f"开始全量扫描目录: {XML_DIR}")

    task_pool = {}
    gift_pool = {}

    for root_dir, _, files in os.walk(XML_DIR):
        for file in files:
            if not file.endswith('.bin'):
                continue
            try:
                with open(os.path.join(root_dir, file), 'r', encoding='utf-8') as f:
                    clean_xml = XmlCleaner.clean(f.read())
                root_el = ET.fromstring(clean_xml)

                # 解析 <task> → <one>（活跃任务）
                task_root = root_el.find('task')
                if task_root is not None:
                    for one_node in task_root.findall('one'):
                        task_data = parse_task_one(one_node)
                        if not task_data or 'name' not in task_data:
                            continue
                        task_data = ValueConverter.prepare_output(task_data, "爆枪突击", "active")
                        task_pool[task_data['name']] = task_data

                # 解析 <gift> → <one>（活跃奖励档位）
                gift_root = root_el.find('gift')
                if gift_root is not None:
                    for one_node in gift_root.findall('one'):
                        gift_data = parse_gift_one(one_node)
                        if not gift_data or 'name' not in gift_data:
                            continue
                        gift_data = ValueConverter.prepare_output(gift_data, "爆枪突击", "active")
                        gift_pool[gift_data['name']] = gift_data

            except Exception as e:
                print(f"  [!] 错误文件 {file}: {e}")

    print(f"\n[提取] 共提取 {len(task_pool)} 个任务 + {len(gift_pool)} 个奖励档位，"
          f"合计 {len(task_pool) + len(gift_pool)} 个条目")

    # 合并池（用于独立 JSON / Excel），同时清理内部标记字段
    all_pool = {}
    all_pool.update(task_pool)
    all_pool.update(gift_pool)
    for data in all_pool.values():
        data.pop('subType', None)

    # 生成报告
    report_pool = {
        **{k: {**v, '_group': 'task'} for k, v in task_pool.items()},
        **{k: {**v, '_group': 'gift'} for k, v in gift_pool.items()},
    }
    ReportGenerator.generate(report_pool, OUTPUT_DIR,
                             report_prefix='活跃度',
                             group_field='_group')

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    # --- 保存独立 JSON ---
    json_dir = os.path.join(OUTPUT_DIR, 'json')
    os.makedirs(json_dir, exist_ok=True)
    for name, data in all_pool.items():
        file_path = os.path.join(json_dir, f"{name}.json")
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"独立 JSON: {json_dir}/ ({len(all_pool)} 个文件)")

    # --- 保存拆分结构的汇总 JSON ---
    summary_path = os.path.join(OUTPUT_DIR, f'活跃度数据汇总_{timestamp}.json')
    with open(summary_path, 'w', encoding='utf-8') as f:
        json.dump({
            'taskArr': list(task_pool.values()),
            'giftArr': list(gift_pool.values())
        }, f, ensure_ascii=False, indent=2)
    print(f"汇总 JSON（拆分结构）: {summary_path}")

    print(f"\n处理完成！活跃任务 {len(task_pool)} 个 + 奖励档位 {len(gift_pool)} 个")


if __name__ == '__main__':
    run_active_processor()
