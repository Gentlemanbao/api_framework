# -*- coding: utf-8 -*-
"""
@Time ： 2026/2/5 13:50
@Auth ： 章豹
@File ：test_report.py
@IDE ：PyCharm
"""
import pytest
from libs.get_api_data import load_test_data
from datetime import datetime


@pytest.mark.skip("调试")
@pytest.mark.parametrize("case", load_test_data("test_export.yml"))
def test_export_excel(api_client, case):
    resp = api_client.post(case["url"], json=case["request"],headers=case["headers"])
    assert resp.status_code == 200
    with open(f"销售开票报表导出{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.xlsx", "wb") as f:
        f.write(resp.content)