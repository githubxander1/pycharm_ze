# 收藏
import json
import logging
import os
import time

import allure
import jsonpath

from ApiTest_mindmaster.common.logger_handler import LoggerHandler
from others.ApiTest_mindmaster.common.requests_handler import RequestsHandler
# from CompanyProject.Fastbull.Api_fastbull.logic.comment import nonce
from CompanyProject.Fastbull.Api_fastbull.logic.conftest import generate_sign_login, get_identity, generate_btoken, \
    generate_nonce, generate_token, timestamp, common_data
from CompanyProject.Fastbull.Api_fastbull.common.yaml_handler import YamlHandler

nonce = generate_nonce()
req=RequestsHandler()
yamlhandler=YamlHandler('../data/Api.yaml')
filename=os.path.basename(__file__).split('.')[0]
logger=LoggerHandler(name='ask',level='DEBUG',file=f'../log/{filename}_log.log',format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def add_favour(refId,favourType):
    # headers=headers1(nonce)
    headers = {
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6",
        "beta": "true",
        "btoken": generate_btoken(common_data["client_type"], common_data["client_version"], common_data['uuid'],
                                  common_data['device_no']),
        "cache-control": "no-cache",
        "client-type": "4",
        "clientversion": "latest",
        "content-type": "application/json",
        "deviceid": "51cee82782f69741d228946af2d2cda3",
        "deviceno": "51cee82782f69741d228946af2d2cda3",
        "langid": "实例25_批量生成PPT版荣誉证书",
        "nonce": nonce,
        "pragma": "no-cache",
        "sec-ch-ua": "\"Not A(Brand\";v=\"99\", \"Microsoft Edge\";v=\"121\", \"Chromium\";v=\"121\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "sign": generate_sign_login(common_data['uid'], generate_token(get_identity()), timestamp, nonce),
        "timestamp": timestamp,
        "uid": common_data['uid']
        # "uid": '204830'
    }
    api_data = yamlhandler.read_yaml()['add_favour']
    url = api_data['url']
    method = api_data['method']
    # print(api_data)
    # print(url)
    # print(method)
    data={
        "refId": refId,
        "favourType": favourType
    }
    # try:
    #     import http.client as http_client
    # except ImportError:
    #     # Python 2
    #     import httplib as http_client
    # http_client.HTTPConnection.debuglevel = 实例25_批量生成PPT版荣誉证书
    #
    # # You must initialize logging, otherwise you'll not see debug output.
    # logging.basicConfig()
    # logging.getLogger().setLevel(logging.DEBUG)
    # requests_log = logging.getLogger("requests.packages.urllib3")
    # requests_log.setLevel(logging.DEBUG)
    # requests_log.propagate = True
    # response=req.visit(url=yamlhandler.read_yaml()['add_favour']['url'],method=method,headers=headers,data=data)
    response=req.visit(url=url+f'favourType={favourType}&refId={refId}',method=method,headers=headers,data=data)
    print(response)
    return response
    # logger.info(response)
def delete_favour(refId,favourType):
    # headers=headers1(nonce)
    headers = {
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6",
        "beta": "true",
        "btoken": generate_btoken(common_data["client_type"], common_data["client_version"], common_data['uuid'],
                                  common_data['device_no']),
        "cache-control": "no-cache",
        "client-type": "4",
        "clientversion": "latest",
        "content-type": "application/json",
        "deviceid": "51cee82782f69741d228946af2d2cda3",
        "deviceno": "51cee82782f69741d228946af2d2cda3",
        "langid": "实例25_批量生成PPT版荣誉证书",
        "nonce": nonce,
        "pragma": "no-cache",
        "sec-ch-ua": "\"Not A(Brand\";v=\"99\", \"Microsoft Edge\";v=\"121\", \"Chromium\";v=\"121\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "sign": generate_sign_login(common_data['uid'], generate_token(get_identity()), timestamp, nonce),
        "timestamp": timestamp,
        "uid": common_data['uid']
        # "uid": '204830'
    }
    api_data = yamlhandler.read_yaml()['add_favour']
    url = api_data['url']
    method = api_data['method']
    # print(api_data)
    # print(url)
    # print(method)
    data={
        "refId": refId,
        "favourType": favourType
    }
    # try:
    #     import http.client as http_client
    # except ImportError:
    #     # Python 2
    #     import httplib as http_client
    # http_client.HTTPConnection.debuglevel = 实例25_批量生成PPT版荣誉证书
    #
    # # You must initialize logging, otherwise you'll not see debug output.
    # logging.basicConfig()
    # logging.getLogger().setLevel(logging.DEBUG)
    # requests_log = logging.getLogger("requests.packages.urllib3")
    # requests_log.setLevel(logging.DEBUG)
    # requests_log.propagate = True
    # response=req.visit(url=yamlhandler.read_yaml()['add_favour']['url'],method=method,headers=headers,data=data)
    response=req.visit(url=url+f'favourType={favourType}&refId={refId}',method=method,headers=headers,data=data)
    print(response)
    return response
    # logger.info(response)
def get_favour_list():
    # headers=headers1(nonce)
    headers = {
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6",
        "beta": "true",
        "btoken": generate_btoken(common_data["client_type"], common_data["client_version"], common_data['uuid'],
                                  common_data['device_no']),
        "cache-control": "no-cache",
        "client-type": "4",
        "clientversion": "latest",
        "content-type": "application/json",
        "deviceid": "51cee82782f69741d228946af2d2cda3",
        "deviceno": "51cee82782f69741d228946af2d2cda3",
        "langid": "实例25_批量生成PPT版荣誉证书",
        "nonce": nonce,
        "pragma": "no-cache",
        "sec-ch-ua": "\"Not A(Brand\";v=\"99\", \"Microsoft Edge\";v=\"121\", \"Chromium\";v=\"121\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "sign": generate_sign_login(common_data['uid'], generate_token(get_identity()), timestamp, nonce),
        "timestamp": timestamp,
        "uid": common_data['uid']
        # "uid": '204830'
    }
    api_data = yamlhandler.read_yaml()['get_favour_list']
    url = api_data['url']
    method = api_data['method']

    response=req.visit(url=url,method=method,headers=headers)
    # print(response)
    # print(type(response))
    bodyMessage=response['bodyMessage']
    # print(bodyMessage)
    # print(type(bodyMessage))
    json_Data=json.loads(bodyMessage)
    # titles=jsonpath.jsonpath(json_Data, '$..pageDatas[*].refContent.title')
    titles=jsonpath.jsonpath(json_Data, '$..title')
    # print(briefs)
    count=0
    # 输出提取到的所有brief
    for title in titles:
        print(title+'\n')
        count+=1
    print(count)


if __name__ == '__main__':
    # add_favour('16419046_1','实例25_批量生成PPT版荣誉证书')
    # delete_favour('16419046_1','实例25_批量生成PPT版荣誉证书')
    time.sleep(2)
    get_favour_list()