# -*- coding: utf-8 -*-
"""
@Time ： 2026/2/10 10:28
@Auth ： 章豹
@File ：customer_business_api.py
@IDE ：PyCharm
"""
from libs.client import RequestsClient
from libs.get_api_data import load_test_data
from libs.run_edit import get_env_data
from libs.logger import logger
from paths_manger import customer_import_xlsx


class BaseCustomerImportApi(RequestsClient):

    def __init__(self,id_token,file_name,filepath):
        super().__init__()
        self.headers = {
            "Authorization": f"Bearer {id_token}"
        }
        self.method = load_test_data("customer_import.yml")[0]["method"]
        self.url = get_env_data() + load_test_data("customer_import.yml")[0]["url"]
        self.files = {"file": (file_name,open(filepath, "rb").read(), "multipart/form-data")}
        logger.info(f"文件流：{self.files}")