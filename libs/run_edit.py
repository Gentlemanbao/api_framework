# -*- coding: utf-8 -*-
"""
@Time ： 2026/2/6 15:46
@Auth ： 章豹
@File ：run_edit.py
@IDE ：PyCharm
"""
import os
from config.settings import BASE_URLS
from libs.get_api_data import load_test_run_env
from libs.read_yaml import ReadConfig
from loguru import logger

def run_edit(env):
    """
    修改执行环境配置文件内容
    :param env: 执行环境
    :return:
    """
    file_path = os.path.dirname(__file__).split(sep="libs")
    obj = ReadConfig(file_path[0]+"/config/run_env.yml")
    obj.clear_relydata()
    obj.write_config({"run": env})

def get_env_data():
    red_env = load_test_run_env("run_env.yml")
    logger.info(f"目前执行环境：{red_env}")
    if red_env["run"] == "test":
        return BASE_URLS["test"]
    elif red_env["run"] == "uat":
        return BASE_URLS["uat"]
    else:
        logger.error(f"请求环境异常: {red_env}")
        raise