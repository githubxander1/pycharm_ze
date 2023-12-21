import json

import allure
import jsonpath
import requests


class ApiKey:
    # 将get请求行为进行封装
    @allure.step('发送get请求')
    def get(self,url,params=None,**keywords):
        return requests.get(url,params=params,*keywords)
    # 将post请求行为进行封装
    @allure.step('发送post请求')
    def post(self,url,data=None,**keywords):
        return requests.post(url,data=data,**keywords)

    @allure.step('获取返回结果值')
    def get_text(self,data,key):
        json_data=json.loads(data)
        value=jsonpath.jsonpath(json_data,'$..{0}'.format(key))
        return value