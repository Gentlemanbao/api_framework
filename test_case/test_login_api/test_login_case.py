# -*- coding: utf-8 -*-
"""
@Time ： 2026/2/9 16:12
@Auth ： 章豹
@File ：test_login_case.py
@IDE ：PyCharm
"""
import allure
from loguru import logger
from api.get_login_api.get_login_api import BaseLoginApi
import pytest
from libs.file_load import read_excel
from libs.get_api_data import load_test_data
from paths_manger import login_data_xlsx


class TestLoginCase:

    @pytest.mark.skip("调试")
    @allure.title("使用excel文件读取来进行数据驱动")
    @pytest.mark.parametrize("case_name,username,password,expect_status,result_data", read_excel(login_data_xlsx, "Sheet1"))
    def test_login_excel(self,case_name,username,password,expect_status,result_data):
        logger.info(f"{username}")
        logger.info(f"{password}")
        resp = BaseLoginApi(username,password).send()
        logger.info(f"{resp.text}")
        assert resp.status_code == expect_status
        assert resp.text == result_data


    logger.info(f"------------{load_test_data('test_login_fail.yml')}")
    # @pytest.mark.skip("调试")
    @allure.title("使用yml文件读取来进行数据驱动")
    @pytest.mark.parametrize("case_name,username,password,expect_status,result_data",
                             load_test_data("test_login_fail.yml"))
    def test_login_yml(self, case_name, username, password, expect_status, result_data):
        logger.info(f"{case_name}")
        logger.info(f"{username}")
        logger.info(f"{password}")
        resp = BaseLoginApi(username, password).send()
        logger.info(f"{resp.text}")
        assert resp.status_code == expect_status
        assert resp.text == result_data