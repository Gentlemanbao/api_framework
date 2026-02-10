# -*- coding: utf-8 -*-
"""
@Time ： 2026/2/5 13:48
@Auth ： 章豹
@File ：settings.py.py
@IDE ：PyCharm
"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent


BASE_URLS = {
    "test": "http://192.168.10.137",
    "uat": "http://192.168.10.134",
}

TIMEOUT = 10

LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

REPORT_DIR = BASE_DIR / "reports"
REPORT_DIR.mkdir(exist_ok=True)

DATA_DIR = BASE_DIR / "data"
print(f"读取api接口文件路径：{DATA_DIR}")

RUN_ENV = BASE_DIR / "config" # 执行环境文件