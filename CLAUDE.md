# CLAUDE.md

本文档为 Claude Code (claude.ai/code) 提供在本仓库中工作时的指导。

## 重要限制

**所有输出必须使用中文。**

## 项目概述

爆枪突击 Wiki 数据处理工具库 - 用于处理游戏 XML 数据并转换为 灰机 Wiki (Huiji Wiki) 所需的 JSON 格式的 Python 工具。

## 架构设计

本项目采用三层架构：

```
core/        - XML 解析与转换工具类
config/      - 映射配置（如武器类别映射）
scripts/     - 数据处理器入口
xml/         - 源 XML 游戏数据文件（纳入 git 管理）
data/        - 生成的输出文件（JSON + Excel，已加入 gitignore）
```

### 核心模块 (`core/`)

- `XmlCleaner` ([cleaner.py](core/cleaner.py)) - 预处理原始 XML，修复格式问题（属性间缺少空格、头部格式错误）后再进行解析
- `XmlParser` ([parser.py](core/parser.py)) - 递归将 XML 转换为 Python 字典；处理包含嵌入式 JSON 的特殊 `<obj>` 标签
- `ValueConverter` ([converter.py](core/converter.py)) - 基于字段命名约定的智能类型转换：
  - 以 `B` 结尾的字段 → 布尔值
  - 以 `Arr` 结尾的字段 → 列表
  - 以 `0x` 开头的值 → 保留为十六进制字符串（颜色值）
  - 数字字符串 → 整数/浮点数

### 脚本 (`scripts/`)

每个脚本都是针对特定数据类型的独立处理器：

- `parse_arms.py` - 从 XML 处理武器数据，输出独立的 JSON 文件 + Excel 更新表
- `parse_skills.py` - 处理具有 father/skill 层级结构的技能数据，包含重名检测和报告功能

## 常用命令

### 运行处理器

```bash
# 处理武器数据（输出至 data/arms/）
python scripts/parse_arms.py

# 处理技能数据（输出至 data/skills/）
python scripts/parse_skills.py

# 处理其他物品类型（chipClass.xml 等）
python materials/things/convert_things_xml.py
```

### 环境配置

```bash
# 创建虚拟环境（.venv/ 已存在）
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows

# 以可编辑模式安装
pip install -e .
```

## 关键约定

### XML 文件格式

源文件使用 `.bin` 扩展名（而非 `.xml`），但内容实际为 XML 格式。它们存放在 `xml/` 目录中并纳入 git 管理。

### 数据结构模式

- **武器**：存储在 `<father type="...">` → `<bullet>` 节点下；通过存在 `bodyImgRange` 或 `allImgRange` 子元素来识别武器
- **技能**：存储在 `<father name="...">` → `<skill>` 节点下
- **物品**：存储在 `<father>` → `<things>` 节点下

### 输出格式

- 独立 JSON 文件：以实体的 `name` 字段命名，存放在 `data/<type>/json/`
- Excel 批量文件：生成时附带时间戳，用于 HuijiBot 批量上传，存放在 `data/<type>/`

### 类别映射

武器类别在 [config/arm_map.py](config/arm_map.py) 中通过 `CATEGORY_MAP` 字典手动映射，因为游戏数据缺乏可靠的类别元数据。

## 注意事项

- `data/` 目录已加入 gitignore - 生成的文件不应提交
- XML 文件常存在格式问题（属性间缺少空格），由 `XmlCleaner` 处理
- 本项目使用 `pandas` 生成 Excel，使用 `xml.etree.ElementTree` 解析 XML
