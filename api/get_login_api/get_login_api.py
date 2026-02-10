# -*- coding: utf-8 -*-
"""
@Time ： 2026/2/9 09:32
@Auth ： 章豹
@File ：get_login_api.py
@IDE ：PyCharm
"""
from libs.client import RequestsClient
from libs.get_api_data import load_test_data
from libs.run_edit import get_env_data
from libs.logger import logger

class BaseLoginApi(RequestsClient):

    def __init__(self,username,password):
        super().__init__()
        self.method = load_test_data("test_login.yml")[0]["method"]
        self.url = get_env_data() + load_test_data("test_login.yml")[0]["url"]
        self.json = {
            "username": username,
            "password": password,
            "source": 1
        }


