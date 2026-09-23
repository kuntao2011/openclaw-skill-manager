# -*- coding: utf-8 -*-
"""
描述汉化模块
基于内置词表将常见英文短语替换为中文（命中一条规则即停，未命中的保持原文）
"""
from typing import Dict
from utils.config import TRANSLATION_RULES


def translate_description(desc: str) -> str:
    """
    汉化技能描述

    Args:
        desc: 技能描述

    Returns:
        替换后的描述（未命中词表时保持原文）
    """
    if not desc:
        return desc

    result = desc

    # 优先匹配长规则
    for eng, chn in sorted(TRANSLATION_RULES.items(), key=lambda x: len(x[0]), reverse=True):
        if eng in result:
            result = result.replace(eng, chn)
            break

    return result
