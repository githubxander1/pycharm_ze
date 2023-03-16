import os

import yaml


class YamlHandler:
    def __init__(self, file):
        self.file = file

    # # 1.获取当前文件所在路径
    # basedir = os.path.dirname(__file__)
    # print("basedir:" + basedir)
    # # 2.将路径进行拼接
    # upload_path = os.path.join(basedir, "static/upload", filename)

    def read_yaml(self, encoding='utf-8'):
        """读取yaml数据"""
        with open(self.file, encoding=encoding) as f:
            return yaml.load(f.read(), Loader=yaml.FullLoader)

    def write_yaml(self, data, encoding='utf-8'):
        """向yaml文件写入数据"""
        with open(self.file, encoding=encoding, mode='w') as f:
            return yaml.dump(data, stream=f, allow_unicode=True)


yaml_data = YamlHandler(r'C:\Users\Administrator\PycharmProjects\pythonProject\test_mindmaster\config\config.yaml').read_yaml()
# print(yaml_data)
