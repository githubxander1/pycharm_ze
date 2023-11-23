import csv
import os

def base_dir():
    return os.path.dirname(os.path.dirname(__file__))

def readCsvlist():
    '''列表的形式读取数据'''
    lists=[]
    with open(os.path.join(base_dir(),'data','sina.csv'),encoding='utf-8-sig')as f:
        reader=csv.reader(f)
        #忽略第一行的内容
        next(reader)
        for item in reader:
            lists.append(item)
        return lists