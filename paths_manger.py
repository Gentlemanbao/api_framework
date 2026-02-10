# -*- coding: utf-8 -*-
"""
@Time ： 2026/2/9 16:06
@Auth ： 章豹
@File ：paths_manger.py
@IDE ：PyCharm
"""
import os
import pytest

project_path = os.path.dirname(__file__)
login_data_xlsx = f"{project_path}/data/case_data/case.xlsx"
customer_import_xlsx = f"{project_path}/data/case_data/重点非交易客户导入模板下载20260210101253.xlsx"