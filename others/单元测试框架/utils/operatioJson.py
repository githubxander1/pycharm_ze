import json
import os

def base_dir():
    return os.path.dirname(os.path.dirname(__file__))

def readJson():    #load()对文件进行反序列化，本质上是读取文件里面的内容
    return json.load(open(os.path.join(base_dir(),'data','sina.json')))