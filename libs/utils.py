# -*- coding: utf-8 -*-
"""
@Time ： 2026/2/5 13:50
@Auth ： 章豹
@File ：utils.py
@IDE ：PyCharm
"""
def clean_filename(name: str) -> str:
    """清理文件名中的非法字符（Windows）"""
    import re
    return re.sub(r'[<>:"/\\|?*]', '_', name)