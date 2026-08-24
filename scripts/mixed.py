"""
爆枪突击 Wiki 数据处理工具 - 全量运行入口

自动发现 scripts/ 下所有 parse_*.py 并运行。
依赖关系：parse_arms、parse_suit 需要提前运行（parse_things 依赖它们补全数据）。
"""
import glob
import subprocess
import sys
import os

# 需要提前运行的脚本（被其它脚本依赖）
PRIORITY_SCRIPTS = ['parse_arms', 'parse_suit']


def main():
    scripts_dir = os.path.dirname(os.path.abspath(__file__))

    # 自动发现所有 parse_*.py
    all_scripts = sorted(glob.glob(os.path.join(scripts_dir, 'parse_*.py')))
    script_names = [os.path.splitext(os.path.basename(p))[0] for p in all_scripts]

    # 前置脚本 + 其余脚本（按字母序）
    priority = [n for n in PRIORITY_SCRIPTS if n in script_names]
    rest = [n for n in script_names if n not in PRIORITY_SCRIPTS]
    ordered = priority + rest

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

    print(f'\n{"=" * 60}')
    print(f"全部运行结束。成功 {len(ordered) - len(failed)} 个，失败 {len(failed)} 个。")
    if failed:
        print(f"失败脚本: {', '.join(failed)}")
        sys.exit(1)
    else:
        print("所有数据处理器运行成功！")


if __name__ == '__main__':
    main()
