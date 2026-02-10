# -*- coding: utf-8 -*-
"""
@Time ： 2026/2/9 13:46
@Auth ： 章豹
@File ：user_business_api.py
@IDE ：PyCharm
"""
from libs.client import RequestsClient
from libs.get_api_data import load_test_data
from libs.run_edit import get_env_data
from libs.logger import logger

class BaseAddUserApi(RequestsClient):

    def __init__(self, id_token=None):
        super().__init__()
        self.headers = {
            "Authorization": f"Bearer {id_token}"
        }
        self.method = load_test_data("user_create.yml")[0]["method"]
        self.url = get_env_data() + load_test_data("user_create.yml")[0]["url"]
        self.json = load_test_data("user_create.yml")[0]["request"]

class BaseDeleteUserApi(RequestsClient):

    def __init__(self, id_token=None,user_uid=None):
        super().__init__()
        self.headers = {
            "Authorization": f"Bearer {id_token}"
        }
        self.method = load_test_data("user_delete.yml")[0]["method"]
        self.url = get_env_data() + load_test_data("user_delete.yml")[0]["url"]
        logger.info(f"用户user_uid----:{self.data}")
        self.data = f"{user_uid}"
