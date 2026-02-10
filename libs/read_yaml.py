"""
@Time ： 2023/3/11 16:14
@Auth ： 章豹
@File ：read_yaml.py
@IDE ：PyCharm

"""
import yaml


class ReadConfig:
    def __init__(self, yaml_file):
        self.yaml_file = yaml_file

    def read_config(self):
        """
        读取yaml文件内容
        :return:
        """
        with open(self.yaml_file, "r", encoding="utf-8") as f:
            config_data = yaml.load(stream=f, Loader=yaml.FullLoader)
            return config_data

    def write_config(self, data):
        """
        yaml文件内容写入
        :param data: 传写入的内容，注意是字典格式的
        :return:
        """
        with open(self.yaml_file, "a", encoding="utf-8") as f:
            yaml.dump(data, stream=f, allow_unicode=True)

    def clear_relydata(self):
        """
        清空依赖数据
        :return:
        """
        with open(self.yaml_file, "a") as rfile:
            rfile.truncate(0)

    def read_data(self, key):
        """
        读取yaml文件内容，并且指定key取指定的value
        :return:
        """
        with open(self.yaml_file, "r", encoding="utf-8") as f:
            config_data = yaml.load(stream=f, Loader=yaml.FullLoader)
            return config_data[key]