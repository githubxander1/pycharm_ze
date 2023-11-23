import yaml
import os

def base_dir():
    return os.path.dirname(os.path.dirname(__file__))

def readYaml():
    with open(os.path.join(base_dir(),'data','sina.yaml'),encoding='utf-8') as f:
        return yaml.safe_load(f)  #读取yaml文件以字典的数据类型