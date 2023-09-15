#! /usr/bin/env python
# -*- coding:utf-8 -*-
# author:张红

# 数据格式是json,如果要用data参数,就需要对请求参数进行序列化处理
import requests

from api_baofyy.common.public import writeID, getID
from api_baofyy.utils.operationJson import readYaml, readJson


def login():
    # dict1 = {"username":readJson()['username'],"password":readJson()['password']}
    r = requests.post(
        # url=readJson()['geturl']+'/login/auth/',
        url=readYaml()['url']['nameport'] + '/login/auth/',
        json=readJson()['login'],
        headers={'Content-Type': 'application/json;charset=UTF-8'}

    )
        # 产品登录成功后,会生成一个token,我们再访问其他页面的时候会带上这个token,为了方便,我们把它写入到一个文件中
        # 文件名是token,参数是从响应对象中获取的token值
    writeID(filename='token',countent=str(r.json()['token']))
    # print(r.json()['token'])
# login()
    # 由于多处都用到这个请求头 ,在这个把这个请求头单独写出来了,之后需要的时候只需要调用即可
def headers():
    return {'Authorization':'JWT {token}'.format(token=getID(filename='token'))}