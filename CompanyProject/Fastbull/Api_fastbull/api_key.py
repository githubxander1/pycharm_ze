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
    def get_text(self, data):
        try:
            # 使用f-string格式化key，更加简洁
            json_data = json.loads(data)
            # 使用format()方法进行字符串格式化
            value = json_data['bodyMessage']
            return value
        except json.JSONDecodeError:
            # 如果数据格式不正确，捕获JSONDecodeError异常
            raise ValueError(f"Provided data is not in a correct JSON format: {data}")
