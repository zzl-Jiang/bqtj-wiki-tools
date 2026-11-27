"""
爆枪突击活跃度（Active）数据处理器

从 XML 提取活跃度任务定义和奖励档位数据，输出单个 active.json。
数据结构：<data> → <task>/<gift> → <one>（两层，无 father 包裹）
  - task/one：每日活跃任务，自闭合属性型
  - gift/one：活跃奖励档位，含嵌套 <gift> 子标签（分号分隔字符串）
"""
import json
import os
import datetime
import xml.etree.ElementTree as ET
from core import XmlCleaner, ValueConverter, clean_str
from config import is_skipped_xml

# --- 配置 ---
XML_DIR = './xml'
OUTPUT_DIR = './data/others/active'

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
            if not file.endswith('.bin') or is_skipped_xml(file):
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

    # 清理内部标记字段
    for pool in (task_pool, gift_pool):
        for data in pool.values():
            data.pop('subType', None)
            if data.get('name'):
                data['name'] = clean_str(data['name'])

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # --- 输出单个 active.json ---
    active_json = {
        "data": {
            "father": [
                {
                    "@name": "task",
                    "@cnName": "活跃任务",
                    "item": list(task_pool.values()),
                },
                {
                    "@name": "gift",
                    "@cnName": "奖励档位",
                    "item": list(gift_pool.values()),
                },
            ]
        }
    }

    active_path = os.path.join(OUTPUT_DIR, 'active.json')
    with open(active_path, 'w', encoding='utf-8') as f:
        json.dump(active_json, f, ensure_ascii=False, indent=2)
    print(f"active JSON: {active_path} "
          f"({len(task_pool)} 个任务 + {len(gift_pool)} 个奖励档位)")

    # ======== 报告 ========
    report = []
    report.append("=" * 50)
    report.append(f" 爆枪突击活跃度数据处理报告 - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report.append("=" * 50)
    report.append(f"\n[总体概况]")
    report.append(f" 活跃任务: {len(task_pool)} 个")
    report.append(f" 奖励档位: {len(gift_pool)} 个")

    report.append("\n[异常数据检测]")
    missing_name = [k for k in list(task_pool) + list(gift_pool) if not k]
    if missing_name:
        report.append(f" [X] 缺少 name 的条目 ({len(missing_name)}个)")
    else:
        report.append(" [OK] 所有条目均包含 name。")

    final_report = "\n".join(report)
    print(final_report)
    report_path = os.path.join(OUTPUT_DIR, '处理报告.txt')
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(final_report)
    print(f"\n[报告] 统计报告已保存至: {report_path}")

    print(f"\n处理完成！活跃任务 {len(task_pool)} 个 + 奖励档位 {len(gift_pool)} 个")


if __name__ == '__main__':
    run_active_processor()
