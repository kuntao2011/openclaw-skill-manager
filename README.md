# OpenClaw 技能分类与统计

> 增强版 OpenClaw 技能列表生成工具，采用模块化架构，支持多种输出格式和高级功能。

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-1.1.0-orange.svg)](CHANGELOG.md)

## ✨ 功能特性

### 核心功能
- ✅ **多格式输出**：Markdown / JSON / HTML
- ✅ **分类统计**：10 大类 48 子类自动归类
- ✅ **状态图标**：✅ Ready / ⚠️ NeedSetup / ❌ Disabled
- ✅ **元数据**：版本号、作者
- ✅ **Web 界面**：交互式 HTML，支持搜索、筛选

### 高级功能
- 🔄 **增量更新**：对比上次运行快照，只输出变化的技能
- 🤖 **自动分类**：基于规则的技能自动归类
- 🔍 **重复检测**：发现功能重复的技能
- 🎯 **灵活过滤**：按状态、关键词、分类过滤
- 📦 **状态检测**：基于 OpenClaw CLI 输出识别缺失依赖（NeedSetup）
- 🌍 **描述汉化**：内置词表替换常见英文描述短语（未命中保持原文）

## 🏗️ 架构设计

```
openclaw-skill-manager/
├── data/                      # 数据层
│   ├── openclaw.py            # OpenClaw CLI 封装
│   ├── filesystem.py          # 文件系统扫描
│   └── meta_reader.py         # 元数据读取
├── classifier/                # 分类层
│   ├── category_map.py        # 分类映射表
│   └── auto_classify.py       # 重复技能检测
├── exporter/                  # 导出层
│   ├── markdown.py            # Markdown 导出
│   ├── json_exporter.py       # JSON 导出
│   └── html_exporter.py       # HTML 交互式导出
├── utils/                     # 工具层
│   ├── config.py              # 配置管理（可自定义输出目录）
│   ├── translator.py          # 描述汉化词表
│   └── diff.py                # 差异对比
├── generate_skill_list.py     # 主入口
└── __init__.py                # 包定义
```

## 🚀 快速开始

### 环境要求
- Python 3.8+
- OpenClaw 已安装并配置

### 安装

1. 通过 OpenClaw 技能安装功能安装（推荐）：
```bash
openclaw skills install git:https://github.com/kuntao2011/openclaw-skill-manager
```

2. 或手动克隆本仓库到 OpenClaw 技能目录：
```bash
git clone https://github.com/kuntao2011/openclaw-skill-manager
cp -r openclaw-skill-manager ~/.openclaw/workspace/skills/
```

### 使用方式

#### 基本用法
```bash
cd ~/.openclaw/workspace/skills/openclaw-skill-manager
python3 generate_skill_list.py
```

#### 指定输出格式
```bash
# Markdown（默认）
python3 generate_skill_list.py -f markdown

# JSON
python3 generate_skill_list.py -f json

# HTML（交互式界面）
python3 generate_skill_list.py -f html

# 全部格式
python3 generate_skill_list.py -f all
```

#### 过滤选项
```bash
# 只导出已激活技能
python3 generate_skill_list.py -F activated

# 只导出未激活技能
python3 generate_skill_list.py -F not_activated

# 按关键词搜索
python3 generate_skill_list.py -s "同花顺"

# 按分类过滤
python3 generate_skill_list.py -c "金融分析工具"
```

#### 高级选项
```bash
# 增量更新（只输出变化）
python3 generate_skill_list.py -i

# 检测重复技能
python3 generate_skill_list.py --check-duplicates

# 自定义输出目录（不存在时自动创建）
python3 generate_skill_list.py -o /path/to/output

# 简洁模式
python3 generate_skill_list.py -q
```

## ⚙️ 配置说明

### 输出目录配置

编辑 `utils/config.py` 自定义输出目录：

```python
# 默认输出目录
OUTPUT_DIR = os.path.join(USER_PROFILE, 'openclaw_out')

# 修改为其他目录
# OUTPUT_DIR = '/your/custom/path'
```

或通过命令行参数临时指定：
```bash
python3 generate_skill_list.py -o ~/my_skills
```

## 📊 输出示例

### Markdown 表格
```
| 序号 | 状态 | 技能名称 | 版本 | 描述 |
|------|------|----------|------|------|
| 1 | ✅ | 问财选A股 | 1.0.0 | A股智能选股 |
| 2 | ⚠️ | futuapi | 2.1.0 | 富途行情API |
```

### HTML 界面特性
- 🔍 实时搜索技能名称和描述
- 📂 按分类过滤
- 📊 按状态筛选
- 📈 实时统计面板
- 🎨 现代化 UI 设计

## 📁 输出文件

运行后生成以下文件：
- `已激活技能列表.md` - Markdown 格式的已激活技能列表
- `未激活技能列表.md` - Markdown 格式的未激活技能列表
- `技能列表.json` - 完整结构化 JSON 数据
- `已激活技能列表.html` - 交互式 HTML 网页
- `未激活技能列表.html` - 交互式 HTML 网页

## 📝 注意事项

1. 首次运行会自动创建输出目录与缓存目录 `~/.openclaw/cache/skill_list/`
2. 增量更新（`-i`）依赖上次运行保存的快照；`--no-snapshot` 可跳过快照保存
3. 分类规则（`classifier/category_map.py` 与 `utils/config.py` 的 `CATEGORY_RULES`）基于作者个人技能库定制，第三方技能大概率落入「其他」，可自行增补映射或用 `-c` 过滤
4. HTML 界面支持响应式布局，手机和电脑都可正常使用

## 🔮 后续规划

- [ ] 支持导出到飞书文档
- [ ] 支持导出到 Notion
- [ ] 技能使用频率统计
- [ ] 技能依赖关系图
- [ ] 批量启用/禁用技能
- [ ] 自动更新检查

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 👤 作者

**kuntao2011**（[GitHub @kuntao2011](https://github.com/kuntao2011)）

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

## 📋 更新日志

详见 [CHANGELOG.md](CHANGELOG.md) 了解各版本的变更历史。
