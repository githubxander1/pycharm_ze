# -*- coding:utf-8 -*-
import os, yaml


def write_yaml(token):
    cur = os.path.dirname(os.path.realpath(__file__))  # 获取当前路径
    yaml_path = os.path.join(cur, "token.sina.yaml")  # 获取yaml文件的路径
    print(yaml_path)
    t = {"token": token}  # 写入的内容

    with open(yaml_path, 'w', encoding='utf-8') as f:
       yaml.dump(t, stream=f, allow_unicode=True)


def get_yaml(yaml_file):
    # yaml_file = "D:\\code\\api_test\\commen\\token.sina.yaml"
    f = open(yaml_file, 'r', encoding='utf-8')
    cfg = f.read()
    d = yaml.load(cfg, Loader=yaml.FullLoader)
    """
    用load转字典
    yaml5.1版本后弃用了yaml.load(file)这个用法，因为觉得很不安全，5.1版本之后就修改了需要指定Loader，通过默认加载器（FullLoader）禁止执行任意函数
    Loader=sina.yaml.FullLoader 加上这行代码，告警就没了
    """
    d = d["token"]
    return d


if __name__ == '__main__':
    r = write_yaml("token的值")
