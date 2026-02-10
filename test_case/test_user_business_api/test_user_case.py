# -*- coding: utf-8 -*-
"""
@Time ： 2026/2/9 13:53
@Auth ： 章豹
@File ：test_user_case.py
@IDE ：PyCharm
"""
import allure
import pytest

from api.user_api.user_business_api import BaseAddUserApi, BaseDeleteUserApi
from libs.get_api_data import load_test_data
import jsonpath
from loguru import logger


class TestUserCase:
    user_uid = ""

    @allure.title("新增用户测试用例")
    @pytest.mark.run(order=1)
    def test_add_user(self,login_fixture):
        res = BaseAddUserApi(id_token=login_fixture)
        resp = res.send()
        TestUserCase.user_uid = resp.json()['data']
        assert resp.status_code == load_test_data('user_create.yml')[0]['expected']['status_code']
        assert resp.json()['errMsg'] == load_test_data('user_create.yml')[0]['expected']['errMsg']

    @allure.title("删除用户测试用例")
    @pytest.mark.run(order=2)
    def test_delete_user(self,login_fixture):
        res = BaseDeleteUserApi(id_token=login_fixture,user_uid=TestUserCase.user_uid)
        logger.info(f"用户id:{TestUserCase.user_uid}")
        resp = res.send()
        assert resp.status_code == load_test_data('user_delete.yml')[0]['expected']['status_code']
        assert resp.json()['errMsg'] == load_test_data('user_delete.yml')[0]['expected']['errMsg']
