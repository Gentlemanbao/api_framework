# -*- coding: utf-8 -*-
"""
@Time ： 2026/2/5 13:50
@Auth ： 章豹
@File ：test_auth.py
@IDE ：PyCharm
"""
from datetime import datetime
import pytest
from libs.get_api_data import load_test_data
from loguru import logger

class TestOne:

    # @pytest.mark.parametrize("case", load_test_data("test_login.yml"))
    # def test_login(self, api_client, case):
    #     print(case,type(case))
    #     resp = api_client.post(case["url"], json=case["request"])
    #
    #     assert resp.status_code == case["expected"]["status_code"]
    #     assert resp.json()["retMsg"] == case["expected"]["retMsg"]


    @pytest.mark.parametrize("case",load_test_data("test_export.yml"))
    def test_export_excel(self, test_login, api_client, case):
        headers = {"Authorization": f"Bearer {test_login}"}
        logger.info(case)
        resp = api_client.post(case["url"], json=case["request"],headers=headers)
        assert resp.status_code == 200
        with open(f"销售开票报表导出{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.xlsx", "wb") as f:
            f.write(resp.content)