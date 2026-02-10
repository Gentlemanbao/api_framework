# -*- coding: utf-8 -*-
"""
@Time ： 2026/2/9 09:32
@Auth ： 章豹
@File ：get_login_api.py
@IDE ：PyCharm
"""
import json

from libs.client import RequestsClient
from libs.get_api_data import load_test_data
from libs.run_edit import get_env_data
from libs.logger import logger

class BaseContractApi(RequestsClient):

    def __init__(self, id_token=None,logic_contract_code=None):
        super().__init__()
        self.headers = {
            "Authorization": f"Bearer {id_token}"
        }
        self.method = load_test_data("get_contract.yml")[0]["method"]
        self.url = get_env_data() + load_test_data("get_contract.yml")[0]["url"]
        self.data = f"{logic_contract_code}"

class BaseCreateContractApi(RequestsClient):

    def __init__(self, id_token=None):
        super().__init__()
        self.headers = {
            "Authorization": f"Bearer {id_token}"
        }
        self.method = load_test_data("create_contract.yml")[0]["method"]
        self.url = get_env_data() + load_test_data("create_contract.yml")[0]["url"]
        self.json = load_test_data('create_contract.yml')[0]['request']

class BaseContractDetailApi(RequestsClient):

    def __init__(self, id_token=None,contract_id=None):
        super().__init__()
        self.headers = {
            "Authorization": f"Bearer {id_token}"
        }
        self.method = load_test_data("contract_detail.yml")[0]["method"]
        self.url = get_env_data() + load_test_data("contract_detail.yml")[0]["url"] + f"?id={contract_id}"

class BaseInstructionAuditApi(RequestsClient):

    def __init__(self, id_token=None,logic_contract_code=None,contract_code=None,):
        super().__init__()
        self.headers = {
            "Authorization": f"Bearer {id_token}"
        }
        self.method = load_test_data("instruction_audit.yml")[0]["method"]
        self.url = get_env_data() + load_test_data("instruction_audit.yml")[0]["url"]
        self.json = {"logicContractCode":logic_contract_code,
                     "contractCode":contract_code,
                     "leftBranch":0,
                     "deliveryContract":0,
                     "isRecording":1,
                     "departmentLeaderUserAccount":"zhangjingjing",
                     "simpleAudit":False,
                     "draftState":True,
                     "modifyMarginClauseFlag":0}

class BaseAuditDeleteApi(RequestsClient):

    def __init__(self, id_token=None,no=None,contract_id=None):
        super().__init__()
        self.headers = {
            "Authorization": f"Bearer {id_token}"
        }
        self.method = load_test_data("instruction_delete.yml")[0]["method"]
        self.url = get_env_data() + load_test_data("instruction_delete.yml")[0]["url"] + f"?no={no}" + f"&id={contract_id}"

