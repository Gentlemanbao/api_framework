# -*- coding: utf-8 -*-
"""
@Time ： 2026/2/5 13:50
@Auth ： 章豹
@File ：token_manger.py
@IDE ：PyCharm
"""
from libs.api_client import APIClient
from libs.run_edit import get_env_data


class TokenManager:
    def __init__(self):
        self._token = None
        self.client = APIClient()

    def login(self):
        resp = self.client.post("/api/user/login", json={"username": "ceshizb", "password": "af5fb18512832d334578b162669621d08926a3ddc00bf841657743930375fd47"})
        self._token = resp.json().get("data", {}).get("id_token")
        return self._token

    def get_token(self):
        if not self._token:
            self.login()
        return self._token

    def is_token_required(self, endpoint: str) -> bool:
        """

        :param endpoint: 请求接口路径，如果这个路径在public_apis里面，说明就是在白名单里面，不需要token就可以访问，
        :return: 只要 endpoint 以 public_apis 中任意一个路径开头，就返回 True
        如果 any(...) == True → 是公开接口 → 不需要 Token → 返回 False
        如果 any(...) == False → 不是公开接口 → 需要 Token → 返回 True
        """
        public_apis = []
        return not any(endpoint.startswith(api) for api in public_apis)