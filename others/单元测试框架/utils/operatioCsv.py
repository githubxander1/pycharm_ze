import csv
import os

def base_dir():
    return os.path.dirname(os.path.dirname(__file__))

def readCsvDict():
    '''以字典的形式读取数据'''
    lists=[]
    with open(os.path.join(base_dir(),'data','sina.csv'),encoding='utf-8-sig')as f:
        reader=csv.DictReader(f)
        for item in reader:
            lists.append(dict(item))
        return lists