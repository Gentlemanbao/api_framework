# -*- coding: utf-8 -*-
"""
@Time ： 2026/2/24 15:35
@Auth ： 章豹
@File ：response_assertions.py
@IDE ：PyCharm
"""

class ApiResponseAssertions:
    @staticmethod
    def assert_success_response(response, expected_fields=None):
        assert response.status_code == 200
        data = response.json()
        assert data['errMsg'] == 'ok'

    @staticmethod
    def assert_error_response(response, expected_error_code):
        assert response.status_code in [400, 401, 403, 404, 500]
        data = response.json()
        assert data['error_code'] == expected_error_code
