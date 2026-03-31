# [爆枪突击] Wiki 数据自动化处理工具库

本项目用于处理 [爆枪突击] 的原始 XML 游戏数据，并将其转化为适用于 [灰机 Wiki](https://bqtj.huijiwiki.com) 的 JSON 格式。

## 🚀 项目功能
- **全量扫描**：自动遍历目录下的所有 XML 资源文件。
- **双路输出**：
    - 生成单个文件的 `.json` 文件（用于留档与核对）。
    - 生成符合 HuijiBot 格式的 `.xlsx` 批量更新表。

## 📂 目录结构说明
```text
.
├── scripts/                # Python 处理脚本
├── xml/                    # 当前版本的游戏 xml 数据
├── data/                   # 数据输出文件夹 (暂存，不会保留)
├── requirements.txt        # 第三方依赖库清单
└── README.md               # 本说明文件
```

## 🛠️ 环境准备与安装

1. **安装 Python**: 建议使用 Python 3.9 或更高版本。
2. **创建虚拟环境** (推荐):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   .venv\Scripts\activate     # Windows
   ```
3. **安装依赖**:
   ```bash
   pip install -r requirements.txt
   ```

## 📖 使用指南

### 1. 放置原始数据
将从游戏客户端提取的 XML 文件放入 `xml/` 目录下 (通常保持最新数据)。

### 2. 运行脚本
在项目根目录下执行：
```bash
python scripts/xxx/xxx.py (具体脚本名称)
```

### 3. 上传数据到 Wiki
- 脚本运行完成后，进入 `data/` 目录，可选择通过生成的 .json 手动上传更新，或使用官方 灰机Wiki 数据更新器 进行自动更新。
- 详情可移步至编辑群讨论咨询。

## ⚠️ 注意事项
- 注意，所有非必要文件 (包括生成的数据文件、旧版本 xml 文件等) 均不会在该仓库提交 / 保留，若有相关需求请私下联系维护者获取。
- 本项目仅供 wiki 编辑者学习交流使用，请勿用于商业或非法用途。

## 🤝 贡献与反馈
如果你在处理数据过程中发现字段缺失或解析错误，请：
1. 提交 Issue 描述问题。
2. 或修改 `scripts/xml_to_json_arms.py` 中的解析逻辑并提交 Pull Request。

---
*由 爆枪突击wiki编辑团队 / Nai He 维护*