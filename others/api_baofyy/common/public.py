#! /usr/bin/env python
# -*- coding:utf-8 -*-
# author:张红

import os

# 基础路径
def base_dir():
    return os.path.dirname(os.path.dirname(__file__))
# print(base_dir())
'''这个主要是对动态参数的处理'''

# 读取文件里面的参数
def getID(filename):
    with open(file=os.path.join(base_dir(),'data',filename),mode='r')as f:
            return f.read()


# 将参数写入文件
def writeID(filename,countent):
    with open(file=os.path.join(base_dir(),'data',filename),mode='w')as f:
            f.write(countent)