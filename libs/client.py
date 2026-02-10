# -*- coding: utf-8 -*-
"""
@Time ： 2026/2/9 10:15
@Auth ： 章豹
@File ：client.py
@IDE ：PyCharm
"""
import requests

from libs.abnormal_test import CustomizeError
from libs.logger import logger

class RequestsClient:

    session = requests.session()

    def __init__(self):
        self.url = None
        self.method = None
        self.headers = None
        self.params = None
        self.data = None
        self.json = None
        self.files = None
        self.resp = None

    def send(self):
        logger.info(f"请求url:{self.url}")
        logger.info(f"请求method:{self.method}")
        logger.info(f"请求headers:{self.headers}")
        logger.info(f"请求params:{self.params}")
        logger.info(f"请求data:{self.data}")
        logger.info(f"请求json:{self.json}")
        logger.info(f"请求files:{self.files}")
        try:
            self.resp = RequestsClient.session.request(method=self.method,
                                                       url=self.url,
                                                       headers=self.headers,
                                                       params=self.params,
                                                       data=self.data,
                                                       json=self.json,
                                                       files=self.files,
                                                       verify=False)
            logger.info(f"响应状态码：{self.resp.status_code}")
            logger.info(f"响应内容：{self.resp.text}")
        except CustomizeError as e:
            logger.exception("接口发起失败！")
            raise CustomizeError(f"接口发起失败{e}")
        return self.resp