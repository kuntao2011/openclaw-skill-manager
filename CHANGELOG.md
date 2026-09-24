# 更新日志 (CHANGELOG)

## [1.2.1] - 2026-09-24

### 📝 说明双语化
- frontmatter `description`、README 简介与 GitHub 仓库描述统一为「英文在前、中文在后」的双语格式

---

## [1.2.0] - 2026-09-23

### 🚀 待提升项目全部落地（roadmap 六项 + 六项增强）

#### 新功能
- **使用频率统计**（`--usage`）：主路读 state 库 `skill_usage` 表，回退 `skills curator status --json`；md/html/json 增加调用量列
- **缺失依赖关系图**（`--deps`）：md 输出 mermaid 图，HTML 输出 SVG 二部图；数据源为 skills list 的 `missing` 字段（43 条边实测）
- **批量启用/禁用**（`--enable` / `--disable`）：写官方机制 `skills.entries.<名>.enabled`，改前自动备份 openclaw.json、写回前 JSON 校验、写后跑 CLI 验证
- **更新检查**（`--check-updates`）：git 安装轨对比本地/安装记录 commit 与远端 HEAD；ClawHub 轨提示官方 `openclaw skills update --all`；只报告不自动升级
- **飞书云文档导出**（`--push feishu`）：上传 md → docx 导入任务 → 返回文档链接
- **Notion 页面导出**（`--push notion`）：md 转 blocks 分批追加；两者凭据一律走环境变量，零第三方依赖

#### 增强
- **修复状态误判**：`get_skill_status` 补检 `anyBins` 组（此前仅缺 anyBins 的技能如 spotify-player 被误标 Ready）
- **输出利用元数据**：emoji、来源（bundled/workspace/…）、主页链接进入所有输出格式
- **分类自定义覆盖层**：`~/.openclaw/skill_categories.json` 优先于内置映射表，第三方技能不再必须改源码
- **汉化词表辅助**（`--i18n-report`）：输出未命中词表的英文词清单
- **判重算法升级**：描述相似度从「前 20 字符相等」改为 `difflib.SequenceMatcher`（阈值 0.9）
- **HTML 表头排序**：名称/版本/来源/调用量/分类点击排序

#### 工程化
- 新增 `tests/`：47 个 pytest 用例（状态判定/分类/覆盖层/导出器/差异/用量/更新/启停/HTTP 客户端/Notion blocks）
- 新增 GitHub Actions CI：compileall + pytest（Python 3.9 / 3.12 矩阵）
- 新增 `utils/webclient.py`：标准库 HTTP 客户端，强制 HTTPS + 主机白名单 + 拒绝内网/环回/保留地址

---

## [1.1.0] - 2026-09-23

### 🛠 对抗审查整改

#### 修复
- **`-o` 自定义输出目录**：目标目录不存在时自动创建（此前三个导出器直接 `FileNotFoundError` 崩溃）；同时规范化路径并拒绝包含 `..` 的路径段
- **frontmatter 规范化**：`name` 改为 `openclaw-skill-manager`（与目录同名，符合 AgentSkills 规范的小写连字符要求），`version`/`author` 迁入 `metadata`
- **移除 `scripts/` 旧版脚本**：其中硬编码了作者本机私人路径，且为 Windows-only 死代码

#### 对齐
- 文档功能清单与代码对齐：移除「HTML 排序」「目录大小/安装时间」「快照 24 小时过期」「分类学习自动保存」等无实现声明
- 「自动翻译」改述为「描述汉化：内置词表替换」（实际行为）；「依赖检查」改述为「状态检测：识别缺失依赖（NeedSetup）」
- 分类数字修正为实测口径：10 大类 48 子类
- 注意事项声明分类规则适用范围（基于作者个人技能库定制）

#### 清理
- 移除死代码：分类学习、未注册技能扫描、依赖检查、目录大小等未接线函数及空循环桩
- `openclaw` CLI 调用改为参数列表形式，并预检命令是否存在
- 输出/缓存目录改为运行时惰性创建，消除 import 副作用
- 消除重复 import 与重复汉化调用
- 全部示例命令 `python` → `python3`；旧目录名 `kt_skill_list_skill` 统一为 `openclaw-skill-manager`
- 作者署名统一为 handle `kuntao2011`

---

## [1.0.1] - 2026-05-10

### 🔄 名称调整
- 技能名称由 "OpenClaw技能统计与分类管理" 改为 **"OpenClaw技能分类与统计"**
- 优化名称表述，减少歧义

---

## [1.0.0] - 2026-05-10

### ✨ 首次公开发布

**技能正式名称**：**OpenClaw技能统计与分类管理**

### 🎯 核心功能

- ✅ **多格式输出**：Markdown / JSON / HTML
- ✅ **自动分类**：9 大类 30+ 子类自动归类
- ✅ **状态图标**：✅ Ready / ⚠️ NeedSetup / ❌ Disabled
- ✅ **元数据提取**：版本号、作者、目录大小
- ✅ **交互式 HTML**：实时搜索、分类筛选、状态过滤、统计面板
- ✅ **增量更新**：对比历史快照，仅输出变化的技能
- ✅ **重复检测**：自动识别功能重复的技能
- ✅ **灵活过滤**：按状态、关键词、分类筛选
- ✅ **自动翻译**：英文描述自动翻译为中文

### 🏗️ 模块化架构

```
openclaw-skill-manager/
├── data/          # 数据层（OpenClaw CLI、文件系统、元数据）
├── classifier/    # 分类层（映射表、重复检测）
├── exporter/      # 导出层（Markdown、JSON、HTML）
└── utils/         # 工具层（配置、描述汉化、差异对比）
```

### 📄 GitHub 发布配套文件

- `README.md` - 完整的项目说明和使用文档
- `LICENSE` - MIT 开源许可证
- `.gitignore` - Python 项目标准忽略规则
- `requirements.txt` - 依赖说明文件
- `CHANGELOG.md` - 本更新日志

### 👤 作者信息

- **作者**：kuntao2011
- **发布日期**：2026-05-10
