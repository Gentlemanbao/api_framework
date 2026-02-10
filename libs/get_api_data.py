# -*- coding: utf-8 -*-
"""
@Time ： 2026/2/6 15:41
@Auth ： 章豹
@File ：get_api_data.py
@IDE ：PyCharm
"""
import yaml
from config.settings import DATA_DIR,RUN_ENV
from libs.logger import logger

def load_test_data(filename):
    with open(DATA_DIR / filename, encoding="utf-8") as f:
        return yaml.load(f, Loader=yaml.FullLoader)

def load_test_run_env(filename):
    with open(RUN_ENV / filename, encoding="utf-8") as f:
        return yaml.load(f, Loader=yaml.FullLoader)