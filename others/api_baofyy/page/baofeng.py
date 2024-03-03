#! /usr/bin/env python
# -*- coding:utf-8 -*-
# author:张红
import requests
# from common.public import writeID
# from common.public import getID
# from utils.operationJson import readJson
# import json
# from page.login import headers
# from utils.operationJson import readYaml




        # 定义一个增加产品的函数
from others.api_baofyy.common.public import writeID, getID
from others.api_baofyy.page.login import headers
from others.api_baofyy.utils.operationJson import readYaml


def addProduct(name, product_type, version, master, description):
    from others.api_baofyy.page.login import headers
    r = requests.post(
        url=readYaml()['url']['nameport']+'/interface/product/',
        json={"name": name, "product_type": product_type, "version": version, "master": master,
                  "description": description},
        headers=headers()
    )
    writeID(filename='productID', countent=str(r.json()['id']))
    return r


    # 定义一个删除产品的函数
def delProduct():
    from others.api_baofyy.page.login import headers
    r = requests.delete(
        url=readYaml()['url']['nameport']+'/interface/product/{productID}/'.format(
            productID=getID(filename='productID')),
        headers=headers()
    )
    return r


    # 定义一个修改产品的函数
def modifyProduct(name,product_type,version,master,description):
    r=requests.put(
        url=readYaml()['url']['nameport']+'/interface/product/{productID}/'.format(productID=getID(filename='productID')),
        headers=headers(),
        json={"name":name,"product_type":product_type,"version":version,"master":master,"description":description}
    )
    return r


    # 定义一个查询产品的函数
def queryProduct(queryname):
    r=requests.get(
        url=readYaml()['url']['nameport']+'/interface/products?name=',
        headers=headers()
    )
    return r