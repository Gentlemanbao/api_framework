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
        try:
            with open(filepath, "rb") as f:
                file_content = f.read()
            self.files = {"file": (file_name, file_content, "multipart/form-data")}
            logger.info(f"文件加载成功：{file_name}")
        except FileNotFoundError:
            logger.error(f"文件未找到：{filepath}")
            raise
        except Exception as e:
            logger.error(f"文件读取失败：{str(e)}")
            raise