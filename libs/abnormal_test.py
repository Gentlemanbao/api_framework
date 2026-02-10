"""
@Time ： 2023/3/14 15:57
@Auth ： 章豹
@File ：abnormal_test.py
@IDE ：PyCharm

"""


class CustomizeError(Exception):
    """
    自定义测试异常类
    """
    def __init__(self, error_info):
        self.error_info = error_info

    def __str__(self):
        return self.error_info
