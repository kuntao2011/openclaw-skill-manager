---
name: openclaw-skill-manager
description: "OpenClaw 技能分类与统计工具。自动扫描所有技能，多格式导出（Markdown/JSON/HTML）与飞书/Notion 推送，自动分类（10 大类 48 子类），使用统计，缺失依赖关系图，批量启停，更新检查，交互式 Web 界面。"
license: MIT
metadata:
  version: "1.2.0"
  author: kuntao2011
---

# OpenClaw 技能统计与分类管理

增强版 OpenClaw 技能列表生成工具，采用模块化架构，支持多种输出格式和高级功能。

## ✨ 功能特性

### 核心功能
- ✅ **多格式输出**：Markdown / JSON / HTML
- ✅ **分类统计**：10 大类 48 子类自动归类，支持用户自定义覆盖层
- ✅ **状态图标**：✅ Ready / ⚠️ NeedSetup / ❌ Disabled
- ✅ **元数据**：版本号、作者、emoji、来源、主页链接
- ✅ **Web 界面**：交互式 HTML，支持搜索、筛选、表头排序

### 高级功能
- 🔄 **增量更新**：对比上次运行快照，只输出变化的技能
- 🤖 **自动分类**：基于规则的技能自动归类
- 🔍 **重复检测**：名称模式 + 描述相似度（SequenceMatcher）
- 🎯 **灵活过滤**：按状态、关键词、分类过滤
- 📦 **状态检测**：基于 OpenClaw CLI 输出识别缺失依赖（含 anyBins 组）
- 🌍 **描述汉化**：内置词表替换常见英文描述短语，附未汉化词报告
- 📊 **使用统计**：state 库 skill_usage 表 / curator 双数据源，`--usage`
- 🔗 **依赖关系图**：缺失依赖边可视化，md 为 mermaid、html 为 SVG，`--deps`
- 🔁 **批量启停**：写 `skills.entries.<名>.enabled`，自动备份 + 写后验证
- ⬆️ **更新检查**：git 轨对比远端 HEAD，ClawHub 轨提示官方命令，只报告不升级
- 📤 **远端推送**：Markdown 一键推送为飞书云文档 / Notion 页面

## 🏗️ 架构设计

```
openclaw-skill-manager/
├── data/                      # 数据层
│   ├── openclaw.py            # OpenClaw CLI 封装与状态判定
│   ├── filesystem.py          # 文件系统扫描
│   ├── meta_reader.py         # 元数据读取
│   ├── usage.py               # 使用统计（skill_usage 表 / curator）
│   ├── deps.py                # 缺失依赖边收集与 mermaid 渲染
│   ├── updates.py             # 更新检查（git 轨 / ClawHub 轨）
│   └── toggle.py              # 批量启停（备份 + 校验 + 验证）
├── classifier/                # 分类层
│   ├── category_map.py        # 分类映射表 + 用户覆盖层
│   └── auto_classify.py       # 重复技能检测
├── exporter/                  # 导出层
│   ├── markdown.py            # Markdown 导出（含 mermaid 依赖图）
│   ├── json_exporter.py       # JSON 导出
│   ├── html_exporter.py       # HTML 交互式导出（含 SVG 依赖图）
│   ├── feishu.py              # 飞书云文档推送
│   └── notion.py              # Notion 页面推送
├── utils/                     # 工具层
│   ├── config.py              # 配置管理（可自定义输出目录）
│   ├── translator.py          # 描述汉化词表
│   ├── diff.py                # 差异对比
│   └── webclient.py           # 标准库 HTTP 客户端（白名单主机）
├── tests/                     # pytest 单测
├── generate_skill_list.py     # 主入口
└── __init__.py                # 包定义
```

## 🚀 使用方式

### 基本用法
```bash
python3 generate_skill_list.py
```

### 指定输出格式
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

### 过滤选项
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

### 高级选项
```bash
# 增量更新（只输出变化）
python3 generate_skill_list.py -i

# 检测重复技能
python3 generate_skill_list.py --check-duplicates

# 自定义输出目录（不存在时自动创建）
python3 generate_skill_list.py -o /path/to/output

# 简洁模式
python3 generate_skill_list.py -q

# 使用次数列（数据源：state 库 skill_usage 表 / curator）
python3 generate_skill_list.py --usage

# 缺失依赖关系图（md=mermaid，html=SVG）
python3 generate_skill_list.py --deps

# 未汉化英文词报告（辅助扩充词表）
python3 generate_skill_list.py --i18n-report

# 更新检查（git 轨对比远端 HEAD；只报告，不自动升级）
python3 generate_skill_list.py --check-updates

# 批量启停（自动备份 openclaw.json，写后跑 CLI 验证）
python3 generate_skill_list.py --disable skill-a,skill-b
python3 generate_skill_list.py --enable skill-a

# 推送本次导出的 Markdown 到飞书 / Notion
python3 generate_skill_list.py -f all --push feishu,notion
```

## 🔐 远端推送凭据（只走环境变量）

| 目标 | 必填 | 可选 |
|------|------|------|
| 飞书 | `FEISHU_APP_ID`、`FEISHU_APP_SECRET` | `FEISHU_FOLDER_TOKEN`（缺省写入云空间根目录） |
| Notion | `NOTION_TOKEN`、`NOTION_PAGE_ID` | — |

凭据一律从环境变量读取，任何凭据字面量不得写入本仓库。

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

### 自定义分类覆盖层

新建 `~/.openclaw/skill_categories.json`（优先级高于内置映射表）：

```json
{
  "my-skill": ["开发工具", "编码与开发"]
}
```

## 📊 输出示例

### Markdown 表格
```
| 序号 | 状态 | 技能名称 | 版本 | 来源 | 调用量 | 描述 |
|------|------|----------|------|------|------|------|
| 1 | ✅ | [🔮 问财选A股](https://...) | 1.0.0 | workspace | 12 | A股智能选股 |
| 2 | ⚠️ | futuapi | 2.1.0 | bundled | - | 富途行情API |
```

### HTML 界面特性
- 🔍 实时搜索技能名称和描述
- 📂 按分类过滤、按状态筛选
- 🔃 表头点击排序（名称/版本/来源/调用量/分类）
- 🔗 缺失依赖关系 SVG 二部图
- 📈 实时统计面板
- 🎨 响应式布局，手机和电脑都可正常使用

## 📝 注意事项

1. 首次运行会自动创建输出目录与缓存目录 `~/.openclaw/cache/skill_list/`
2. 增量更新（`-i`）依赖上次运行保存的快照；`--no-snapshot` 可跳过快照保存
3. 分类规则基于作者个人技能库定制，第三方技能大概率落入「其他」——用 `~/.openclaw/skill_categories.json` 覆盖层或修改 `classifier/category_map.py` 增补
4. 批量启停会修改 `~/.openclaw/openclaw.json`，每次改动前自动生成带时间戳的备份
5. 使用统计依赖 OpenClaw 的 `skill_usage` 记录，暂无数据时输出占位符 `-`

## 🔮 后续规划

- [x] 支持导出到飞书文档（v1.2.0 `--push feishu`）
- [x] 支持导出到 Notion（v1.2.0 `--push notion`）
- [x] 技能使用频率统计（v1.2.0 `--usage`）
- [x] 技能依赖关系图（v1.2.0 `--deps`）
- [x] 批量启用/禁用技能（v1.2.0 `--enable` / `--disable`）
- [x] 自动更新检查（v1.2.0 `--check-updates`）

- [ ] 技能使用趋势图（按周聚合）
- [ ] 更多远端文档目标（Obsidian / 语雀）

## 👤 作者

**kuntao2011**（[GitHub @kuntao2011](https://github.com/kuntao2011)）

## 📄 许可证

MIT License
