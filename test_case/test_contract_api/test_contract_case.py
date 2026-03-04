# -*- coding: utf-8 -*-
"""
@Time ： 2026/2/9 09:38
@Auth ： 章豹
@File ：test_contract_case.py
@IDE ：PyCharm
"""
import allure
import pytest

from api.contract_api.get_contract_code_api import BaseContractApi, BaseCreateContractApi, BaseContractDetailApi, \
    BaseInstructionAuditApi, BaseAuditDeleteApi
from libs.get_api_data import load_test_data
from libs.response_assertions import ApiResponseAssertions
from libs.run_edit import get_env_data
import jsonpath
from loguru import logger


class TestContractCase:

    contract_id = ''
    logic_contract_code = ''
    contract_code = ''
    instruction_no = ''

    @allure.title("创建合同详情测试用例")
    def test_create_contract(self,login_fixture):
        res = BaseCreateContractApi(id_token=login_fixture)
        resp = res.send()
        TestContractCase.contract_id = resp.json()['data']
        ApiResponseAssertions().assert_success_response(resp)

    # @pytest.mark.skip()
    @allure.title("获取合同详情测试用例")
    def test_contract_detail(self, login_fixture):
        res = BaseContractDetailApi(id_token=login_fixture,contract_id=TestContractCase.contract_id)
        resp = res.send()
        TestContractCase.logic_contract_code = jsonpath.jsonpath(resp.json(), '$..logicContractCode')[0]
        TestContractCase.contract_code = jsonpath.jsonpath(resp.json(), '$..contractCode')[0]
        ApiResponseAssertions().assert_success_response(resp)
        assert jsonpath.jsonpath(resp.json(), '$..contractBasic.contractId')[0] ==  TestContractCase.contract_id


    @allure.title("获取合同创建指令测试用例")
    def test_get_audit(self,login_fixture):
        res = BaseInstructionAuditApi(id_token=login_fixture,
                                      logic_contract_code=TestContractCase.logic_contract_code,
                                      contract_code=TestContractCase.contract_code)
        resp = res.send()
        TestContractCase.instruction_no = jsonpath.jsonpath(resp.json(), '$..instructionNo')[0]
        ApiResponseAssertions().assert_success_response(resp)
        assert jsonpath.jsonpath(resp.json(),'$..logicContractCode')[0] == TestContractCase.logic_contract_code

    @allure.title("删除合同创建指令测试用例")
    def test_audit_delete(self,login_fixture):
        res = BaseAuditDeleteApi(id_token=login_fixture,
                                 no=TestContractCase.instruction_no,
                                 contract_id=TestContractCase.contract_id)
        resp = res.send()
        ApiResponseAssertions().assert_success_response(resp)
        assert resp.json()["success"] == load_test_data('instruction_delete.yml')[0]['expected']['success']

    @pytest.mark.skip("调试")
    @allure.title("获取合同详情测试用例")
    def test_get_contract(self,login_fixture):
        res = BaseContractApi(id_token=login_fixture,logic_contract_code=TestContractCase.logic_contract_code)
        resp = res.send()
        logger.info(f"{resp.json()}")
        ApiResponseAssertions().assert_success_response(resp)
        assert jsonpath.jsonpath(resp.json(),'$..logicContractCode')[0] == TestContractCase.logic_contract_code
