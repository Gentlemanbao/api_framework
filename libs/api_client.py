# -*- coding: utf-8 -*-
"""
@Time ： 2026/2/5 13:49
@Auth ： 章豹
@File ：api_client.py
@IDE ：PyCharm
"""
import requests
from loguru import logger
from config.settings import BASE_URLS, TIMEOUT
from libs.get_api_data import load_test_data,load_test_run_env
from libs.run_edit import get_env_data
from libs.token_manager import TokenManager

class APIClient:
    def __init__(self):
        self.session = requests.Session()
        self.base_url = get_env_data()

    def request(self, method, endpoint, **kwargs):
        """

        :param method: HTTP 方法，如 "get", "post"
        :param endpoint: 接口路径，如 "/api/users"。最终拼成完整 URL：BASE_URL + endpoint
        :param kwargs:透传给 requests 的其他参数，比如：
                    • json={...}
                    • params={...}
                    • headers={...}
                    • files={...}（但目前未显式支持）
        :return: 响应内容
        """
        url = f"{self.base_url}{endpoint}"
        logger.info(f"目前执行接口的url：{url}")
        # if self.token_manager.is_token_required(endpoint):
        #     headers = kwargs.get("headers", {})
        #     headers["Authorization"] = f"Bearer {self.token_manager.get_token()}"
        #     kwargs["headers"] = headers

        logger.info(f"→ {method.upper()} {url}")
        if kwargs.get("json"):
            logger.debug(f"  Request JSON: {kwargs['json']}")
        try:
            resp = self.session.request(method, url, timeout=TIMEOUT, **kwargs)
            logger.info(f"← {resp.status_code} {resp.reason}")
            if resp.headers.get("content-type", "").startswith("application/json"):
                logger.debug(f"  Response JSON: {resp.json()}")
            return resp
        except Exception as e:
            logger.error(f"请求异常: {e}")
            raise

    def get(self, endpoint, **kwargs): return self.request("get", endpoint, **kwargs)
    def post(self, endpoint, **kwargs): return self.request("post", endpoint, **kwargs)
    def put(self, endpoint, **kwargs): return self.request("put", endpoint, **kwargs)
    def delete(self, endpoint, **kwargs): return self.request("delete", endpoint, **kwargs)
    def upload_file(self, endpoint, file_path, field_name="file", extra_data=None):
        """
        上传单个文件
        :param endpoint: 接口路径
        :param file_path: 文件路径
        :param field_name: 表单字段名，默认 'file'
        :param extra_data: 额外表单字段，如 {'description': 'xxx'}
        """
        with open(file_path, "rb") as f:
            files = {field_name: f}
            data = extra_data or {}
            return self.post(endpoint, files=files, data=data)