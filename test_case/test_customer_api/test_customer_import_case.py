# -*- coding: utf-8 -*-
"""
@Time ： 2026/2/10 10:41
@Auth ： 章豹
@File ：test_customer_import_case.py
@IDE ：PyCharm
"""
import allure

from api.customer_api.customer_business_api import BaseCustomerImportApi
from libs.get_api_data import load_test_data
from paths_manger import customer_import_xlsx


class TestCustomerImportCase:

    @allure.title("导入重点非交易客户测试用例")
    def test_customer_import(self,login_fixture):
        res = BaseCustomerImportApi(login_fixture,"重点非交易客户导入模板下载20260210101253.xlsx",customer_import_xlsx)
        resp = res.send()
        assert resp.status_code == load_test_data("customer_import.yml")[0]["expected"]["status_code"]
        assert resp.json()["retMsg"] == load_test_data("customer_import.yml")[0]["expected"]["retMsg"]