#! /usr/bin/env python
# -*- coding:utf-8 -*-
# author:张红

import time as t
import json
# from utils.operationJson import readJson
# from test.test_login import LoginTest
# from page.baofeng import *
import unittest

from api_暴风影音.page.baofeng import addProduct, delProduct, modifyProduct, queryProduct
from api_暴风影音.test.test_login import LoginTest
from api_暴风影音.utils.operationJson import readJson


class Fengbao(LoginTest):


    # 测试添加产品
    def test_addProduct(self):
        r = addProduct(name=readJson()['name'], product_type=readJson()['product_type'], version=readJson()['version'], master=readJson()['master'], description=readJson()['description'])
        delProduct()
        self.assertEqual(r.status_code, 201)

    # 测试删除产品
    def test_delProduct(self):
        addProduct(name=readJson()['name'], product_type=readJson()['product_type'], version=readJson()['version'], master=readJson()['master'], description=readJson()['description'])
        r=delProduct()
        self.assertEqual(r.status_code, 204)


    # 测试修改产品名称
    def test_modifyProduct_name(self):
        addProduct(name=readJson()['name'], product_type=readJson()['product_type'], version=readJson()['version'], master=readJson()['master'], description=readJson()['description'])
        r=modifyProduct(name=readJson()['modifyname'], product_type=readJson()['product_type'], version=readJson()['version'], master=readJson()['master'], description=readJson()['description'])
        delProduct()
        self.assertEqual(r.json()['name'],'小明')
        self.assertEqual(r.status_code,200)


    # 修改产品类型
    def test_modifyProduct_product_type(self):
        addProduct(name=readJson()['name'], product_type=readJson()['product_type'], version=readJson()['version'], master=readJson()['master'], description=readJson()['description'])
        r=modifyProduct(name=readJson()['name'], product_type=readJson()['modifyproduct_type'], version=readJson()['version'], master=readJson()['master'], description=readJson()['description'])
        delProduct()
        self.assertEqual(r.json()['product_type'],'APP')
        self.assertEqual(r.status_code,200)


    # 修改产品版本
    def test_modifyProduct_version(self):
        addProduct(name=readJson()['name'], product_type=readJson()['product_type'], version=readJson()['version'], master=readJson()['master'], description=readJson()['description'])
        r = modifyProduct(name=readJson()['name'], product_type=readJson()['product_type'], version=readJson()['modifyversion'], master=readJson()['master'], description=readJson()['description'])
        delProduct()
        self.assertEqual(r.json()['version'], '1.0.1')
        self.assertEqual(r.status_code, 200)


    #修改产品作者
    def test_modifyProduct_master(self):
        addProduct(name=readJson()['name'], product_type=readJson()['product_type'], version=readJson()['version'], master=readJson()['master'], description=readJson()['description'])
        r = modifyProduct(name=readJson()['name'], product_type=readJson()['product_type'], version=readJson()['version'], master=readJson()['modifymaster'], description=readJson()['description'])
        delProduct()
        self.assertEqual(r.json()['master'], '化')
        self.assertEqual(r.status_code, 200)


    # 修改产品描述
    def test_modifyProduct_description(self):
        addProduct(name=readJson()['name'], product_type=readJson()['product_type'], version=readJson()['version'], master=readJson()['master'], description=readJson()['description'])
        r = modifyProduct(name=readJson()['name'], product_type=readJson()['product_type'], version=readJson()['version'], master=readJson()['master'], description=readJson()['modifydescription'])
        delProduct()
        self.assertEqual(r.json()['description'], '这个是测试')
        self.assertEqual(r.status_code, 200)


    # 模糊查询
    def test_queryProduct_vague(self):
        addProduct(name=readJson()['name'], product_type=readJson()['product_type'], version=readJson()['version'], master=readJson()['master'], description=readJson()['description'])
        r=queryProduct(queryname='无')
        delProduct()
        self.assertEqual(r.status_code,200)


    # 搜索查询
    def test_queryProduct_query(self):
        addProduct(name=readJson()['name'], product_type=readJson()['product_type'], version=readJson()['version'], master=readJson()['master'], description=readJson()['description'])
        r = queryProduct(queryname='')
        delProduct()
        self.assertEqual(r.status_code,200)

    # 精确查询
    def test_queryProduct_accurate(self):
        addProduct(name=readJson()['name'], product_type=readJson()['product_type'], version=readJson()['version'], master=readJson()['master'], description=readJson()['description'])
        r = queryProduct(queryname='无涯')
        delProduct()
        self.assertEqual(r.status_code,200)



if __name__ == '__main__':
    unittest.main(verbosity=2)