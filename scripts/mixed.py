"""
爆枪突击 Wiki 数据处理工具 - 全量运行入口

自动发现 scripts/ 下所有 parse_*.py 并运行。
依赖关系：parse_arms、parse_suit 需要提前运行（parse_things 依赖它们补全数据）。

运行结束后会与「上一版本」的 data/ 输出做对比，列出哪些数据集发生了变动，
便于定位需要手动更新哪些 py 脚本负责的内容。首次运行（无上一版本）时跳过对比。
"""
import glob
import hashlib
import json
import os
import re
import subprocess
import sys

# 需要提前运行的脚本（被其它脚本依赖）
PRIORITY_SCRIPTS = ['parse_arms', 'parse_suit']

DATA_DIR = './data'

# 输出文件名中的时间戳（如 _20240101_120000），对比时统一归一化
TS_RE = re.compile(r'_\d{8}_\d{6}')

# 各脚本中的输出目录声明，用于反查数据集对应的脚本
OUTPUT_DIR_RE = re.compile(r"OUTPUT_DIR\s*=\s*['\"]\./data/([^'\"]+)['\"]")


def build_script_map(scripts_dir):
    """解析各脚本的 OUTPUT_DIR，返回 {data 下的相对目录: 脚本名}"""
    mapping = {}
    for path in glob.glob(os.path.join(scripts_dir, 'parse_*.py')):
        name = os.path.splitext(os.path.basename(path))[0]
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
        except OSError:
            continue
        match = OUTPUT_DIR_RE.search(content)
        if match:
            mapping[match.group(1).replace('\\', '/')] = name
    return mapping


def snapshot(data_dir):
    """
    为 data 目录生成内容指纹，返回 {归一化相对路径: 内容哈希}。

    - 文件名中的时间戳被归一化为 _<TS>，避免每次运行都判定为新增
    - 同一归一化路径存在多个文件时，只取修改时间最新的那个
    - 只统计 .json 文件（.xlsx 内容由 json 派生，.txt 报告含时间戳）
    """
    snap = {}
    newest_mtime = {}

    for root, _, files in os.walk(data_dir):
        for fname in files:
            if not fname.endswith('.json'):
                continue
            path = os.path.join(root, fname)
            rel = os.path.relpath(path, data_dir).replace('\\', '/')
            key = TS_RE.sub('_<TS>', rel)

            try:
                mtime = os.path.getmtime(path)
            except OSError:
                continue
            if key in newest_mtime and newest_mtime[key] >= mtime:
                continue

            try:
                with open(path, 'r', encoding='utf-8') as f:
                    payload = json.load(f)
                digest = hashlib.md5(
                    json.dumps(payload, ensure_ascii=False, sort_keys=True).encode('utf-8')
                ).hexdigest()
            except (OSError, ValueError):
                continue

            newest_mtime[key] = mtime
            snap[key] = digest

    return snap


def _dataset_of(key, script_map):
    """
    从相对路径反查所属数据集目录。

    优先取最长的、能在脚本映射中找到的目录前缀，
    以便把 skills/json/uavYing.json 归到 skills 而非 skills/json。
    """
    parts = key.split('/')[:-1]
    for i in range(len(parts), 0, -1):
        candidate = '/'.join(parts[:i])
        if candidate in script_map:
            return candidate
    return '/'.join(parts)


def report_diff(before, after, script_map):
    """对比两次快照，按数据集分组输出变动报告"""
    if not before:
        print('\n[数据变动检测] 未发现上一版本的 data 数据，跳过对比。')
        return

    added = sorted(set(after) - set(before))
    removed = sorted(set(before) - set(after))
    changed = sorted(k for k in set(before) & set(after) if before[k] != after[k])

    total = len(added) + len(removed) + len(changed)

    print(f'\n{"=" * 60}')
    print(f'[数据变动检测] 与上一版本对比')
    print(f'{"=" * 60}')

    if total == 0:
        print(' 本次运行没有数据变动。')
        return

    # 按数据集目录分组
    groups = {}
    for kind, keys in (('新增', added), ('修改', changed), ('移除', removed)):
        for key in keys:
            groups.setdefault(_dataset_of(key, script_map), []).append((kind, key))

    print(f' 共 {len(groups)} 个数据集、{total} 个文件发生变动'
          f'（新增 {len(added)} / 修改 {len(changed)} / 移除 {len(removed)}）')

    max_show = 10
    for dataset in sorted(groups):
        items = groups[dataset]
        script = script_map.get(dataset, '未匹配脚本')
        counts = {}
        for kind, _ in items:
            counts[kind] = counts.get(kind, 0) + 1
        summary = ' / '.join(f'{k} {v}' for k, v in counts.items())

        print(f'\n - {script}  ({dataset or "data 根目录"})  {summary}')
        prefix = dataset + '/' if dataset else ''
        for kind, key in items[:max_show]:
            rel = key[len(prefix):] if prefix and key.startswith(prefix) else key
            print(f'     [{kind}] {rel}')
        if len(items) > max_show:
            print(f'     ... 共 {len(items)} 项')


def main():
    scripts_dir = os.path.dirname(os.path.abspath(__file__))

    # 自动发现所有 parse_*.py
    all_scripts = sorted(glob.glob(os.path.join(scripts_dir, 'parse_*.py')))
    script_names = [os.path.splitext(os.path.basename(p))[0] for p in all_scripts]

    # 前置脚本 + 其余脚本（按字母序）
    priority = [n for n in PRIORITY_SCRIPTS if n in script_names]
    rest = [n for n in script_names if n not in PRIORITY_SCRIPTS]
    ordered = priority + rest

    script_map = build_script_map(scripts_dir)

    # 运行前快照（作为「上一版本」基线）
    before = snapshot(DATA_DIR)

    failed = []
    print(f"自动发现 {len(ordered)} 个数据处理器...")
    print(f"Python 解释器: {sys.executable}\n")

    for i, name in enumerate(ordered, 1):
        script_path = os.path.join(scripts_dir, f'{name}.py')
        print(f'\n{"=" * 60}')
        print(f'[{i}/{len(ordered)}] 运行 {name} ...')
        print(f'{"=" * 60}')

        result = subprocess.run([sys.executable, script_path])
        if result.returncode != 0:
            print(f'  [!] {name} 运行失败 (exit code {result.returncode})')
            failed.append(name)
        else:
            print(f'  [OK] {name} 完成')

    # 运行后快照并与基线对比
    after = snapshot(DATA_DIR)
    report_diff(before, after, script_map)

    print(f'\n{"=" * 60}')
    print(f"全部运行结束。成功 {len(ordered) - len(failed)} 个，失败 {len(failed)} 个。")
    if failed:
        print(f"失败脚本: {', '.join(failed)}")
        sys.exit(1)
    else:
        print("所有数据处理器运行成功！")


if __name__ == '__main__':
    main()
