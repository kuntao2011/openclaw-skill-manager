# -*- coding: utf-8 -*-
"""
openclaw-skill-manager - OpenClaw 技能分类与统计工具

功能特性：
- ✅ 多格式输出：Markdown / JSON / HTML
- ✅ 分类统计：10 大类 48 子类自动归类
- ✅ 状态图标：Ready / NeedSetup / Disabled
- ✅ 元数据：版本号、作者
- ✅ 增量更新：检测新增/删除/变化的技能
- ✅ 自动分类：基于规则的技能自动归类
- ✅ 重复检测：发现功能重复的技能
- ✅ Web 界面：交互式 HTML，支持搜索、筛选
- ✅ 灵活过滤：按状态、关键词、分类过滤

架构：
- data/ - 数据层（OpenClaw CLI、文件系统、元数据）
- classifier/ - 分类层（映射表、重复检测）
- exporter/ - 导出层（Markdown、JSON、HTML）
- utils/ - 工具层（描述汉化、差异对比、配置）
"""

__version__ = "1.1.0"
__author__ = "kuntao2011"
