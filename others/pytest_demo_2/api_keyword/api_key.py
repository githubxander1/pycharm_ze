import allure
import json
import jsonpath
import requests

# 定义一个关键字类
class ApiKey:
    # 将get请求行为进行封装
    @allure.step("发送get请求")
    def get(self, url, params=None, **kwargs):
        return requests.get(url=url, params=params, **kwargs)

    # 将post请求行为进行封装
    @allure.step("发送post请求")
    def post(self, url, data=None, **kwargs):
        return requests.post(url=url, data=data, **kwargs)

    # 由于接口之间可能相互关联，因此下一个接口需要上一个接口的某个返回值，此处采用jsonpath对上一个接口返回的值进行定位并取值
    @allure.step("获取返回结果字典值")
    def get_text(self, data, key):
        # json数据转换为字典
        json_data = json.loads(data)
        # jsonpath取值
        value = jsonpath.jsonpath(json_data, '$..{0}'.format(key))
        return value[0]