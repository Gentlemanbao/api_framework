# -*- coding: utf-8 -*-
"""
@Time ： 2026/2/5 13:50
@Auth ： 章豹
@File ：conftest.py
@IDE ：PyCharm
"""
import os
import pytest
from api.get_login_api.get_login_api import BaseLoginApi
from libs.get_api_data import load_test_data
from libs.logger import logger


def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


@pytest.fixture(scope="session")
def login_fixture():
    logger.info("测试开始，仅登录一次！")
    resp = BaseLoginApi(load_test_data("test_login.yml")[0]["request"]["username"],
                        load_test_data("test_login.yml")[0]["request"]["password"]).send()
    logger.info(f"{resp.text}")
    yield resp.json()['data']['id_token']
