# [爆枪突击] Wiki 数据自动化处理工具库

本项目用于处理 [爆枪突击] 的原始 XML 游戏数据，并将其转化为适用于 [灰机 Wiki](https://bqtj.huijiwiki.com) 的 JSON 格式。

## 项目功能

- **全量扫描**：自动遍历目录下的所有 XML 资源文件
- **智能解析**：针对游戏特有的 XML 格式（如 `<obj>` 标签、分号分隔数据）进行特殊处理
- **类型转换**：根据字段命名约定自动转换数据类型（`B` 结尾→布尔，`Arr` 结尾→数组）
- **双路输出**：
  - 生成单个文件的 `.json`（用于留档与核对）
  - 生成符合 HuijiBot 格式的 `.xlsx` 批量更新表
- **数据水合**：通过补充数据补全缺失字段

## 目录结构

```
.
├── scripts/                # Python 处理脚本
├── core/                   # 核心解析模块
│   ├── cleaner.py          # XML 清洗器
│   ├── parser.py           # XML 解析器
│   └── converter.py        # 类型转换器
├── config/                 # 配置数据
├── xml/                    # 游戏原始 XML 数据（纳入版本控制）
├── data/                   # 输出目录（gitignored）
├── requirements.txt        # Python 依赖
├── pyproject.toml          # 项目配置
├── CLAUDE.md               # Claude Code 工作指南
└── README.md               # 本文件
```

## 环境准备

1. **克隆仓库**:
   ```bash
   git clone https://github.com/zzl-Jiang/bqtj-wiki-tools
   cd bqtj-wiki-tools
   ```

2. **安装 Python**: 建议使用 Python 3.9 或更高版本

3. **创建虚拟环境** (推荐):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   .venv\Scripts\activate     # Windows
   ```

4. **安装依赖**：
   ```bash
   pip install -e .
   ```

## 使用指南

### 1. 准备原始数据

将从游戏客户端提取的 XML 文件（`.bin` 格式）放入 `xml/` 目录下。

### 2. 运行处理器

```bash
# 处理武器数据（输出至 data/arms/）
python -m scripts.parse_arms
```

以及其他 scripts 文件夹中的处理脚本。

### 3. 上传数据到 Wiki

- 脚本运行完成后，进入 `data/` 目录查看生成的 `.json` 和 `.xlsx` 文件
- 可通过生成的 `.xlsx` 文件使用官方 灰机Wiki 数据更新器 进行自动更新
- 详情可移步至编辑群讨论咨询

## 注意事项

- `data/` 目录已加入 `.gitignore`，生成的数据文件不会提交
- XML 文件常存在格式问题（属性间缺少空格），由 `XmlCleaner` 自动处理
- 本项目仅供 wiki 编辑者学习交流使用，请勿用于商业或非法用途

## 技术说明

### XML 数据清洗

游戏 XML 存在格式不规范问题（如属性间缺少空格），`core/cleaner.py` 会自动修复：
- 修复 XML 头部格式
- 修复属性间缺失空格
- 移除注释和 CDATA

### 智能类型转换

根据字段命名约定自动推断类型：
- 以 `B` 结尾 → 布尔值
- 以 `Arr` 结尾 → 列表
- 以 `0x` 开头 → 保留为十六进制字符串（颜色值）
- 纯数字 → int/float

## 贡献与反馈

如果你在处理数据过程中发现字段缺失或解析错误，请：
1. 提交 Issue 描述问题
2. 或修改对应脚本中的解析逻辑并提交 Pull Request

---
*由 爆枪突击wiki编辑团队 / Nai He 维护*
