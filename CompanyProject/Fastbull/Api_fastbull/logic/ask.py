import json
import os

import allure
import requests

from ApiTest_mindmaster.common.requests_handler import RequestsHandler
from CompanyProject.Fastbull.Api_fastbull.common.logger_handler import LoggerHandler
from CompanyProject.Fastbull.Api_fastbull.logic.conftest import common_data, generate_nonce, timestamp, generate_btoken, \
    generate_sign_login, generate_token, get_identity
from CompanyProject.Fastbull.Api_fastbull.common.yaml_handler import YamlHandler

nonce = generate_nonce()
req=RequestsHandler()
yamlhandler=YamlHandler('../data/Api.yaml')
filename=os.path.basename(__file__).split('.')[0]
logger=LoggerHandler(name='ask',level='DEBUG',file=f'../log/{filename}_log.log',format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def addAsk(askContent):
    function_name = addAsk.__qualname__
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
    }
    data = yamlhandler.read_yaml()['addAsk']
    url = data['url']
    method = data['method']

    response = req.visit(method, url, headers=headers, json=askContent)

    bodyMessage = response['bodyMessage']
    bodyMessage1 = json.loads(bodyMessage)
    id = bodyMessage1['id']
    # print(id)
    allure.step(f'{function_name}请求头：{headers}')
    allure.step(f'{function_name}请求体：{data}')
    allure.attach(body=response, name='响应体', attachment_type=allure.attachment_type.JSON)
    logger.warning(f'{function_name}请求头：{headers}')
    logger.warning(f'{function_name}请求体：{data}')
    logger.warning(f'{function_name}响应体：{response}')

    return response,id


data = {
        "askContent": "日元趋势如何",
        "askImage": "https://img.fastbull.com/test/image/2024/02/C0F94A3E97D149449A0BA67A93F4050E?w=3840&h=2400"
        }
# print(addAsk(data))
# print(get_addAsk_id(data))
def deleteAsk(body):
    headers = {
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6",
        "beta": "true",
        "btoken": "cf0cabf8f9cefab23b3c4ef6c4f9a395",
        "cache-control": "no-cache",
        "client-type": "4",
        "clientversion": "latest",
        "content-type": "application/json",
        "deviceid": "51cee82782f69741d228946af2d2cda3",
        "deviceno": "51cee82782f69741d228946af2d2cda3",
        "langid": "实例25_批量生成PPT版荣誉证书",
        "nonce": "vbo6E8OG",
        "pragma": "no-cache",
        "sec-ch-ua": "\"Not A(Brand\";v=\"99\", \"Microsoft Edge\";v=\"121\", \"Chromium\";v=\"121\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "sign": "4A26AA7095B803FF9205D1E413478562",
        "timestamp": "1706750312",
        "uid": common_data['uid']
    }
    function_name = addAsk.__qualname__
    logger.warning(f'{function_name}请求头：{headers}')
    allure.step(f'{function_name}请求头：{headers}')
    data = yamlhandler.read_yaml()['deleteAsk']
    logger.warning(f'{function_name}请求体：{data}')
    allure.step(f'{function_name}请求体：{data}')
    url = data['url']
    method = data['method']

    response = req.visit(method, url, headers=headers, json=body)
    response_str = json.dumps(response, ensure_ascii=False)
    logger.warning(f'{function_name}响应体：{response}')

    header_str = json.dumps(headers, indent=4)
    allure.attach(header_str, name='请求头', attachment_type=allure.attachment_type.JSON)

    # 将请求体转换为字符串并附加到Allure报告
    body_str = json.dumps(body, indent=4)
    allure.attach(body_str, name='请求体', attachment_type=allure.attachment_type.JSON)

    allure.attach(body=response_str, name='响应体', attachment_type=allure.attachment_type.JSON)

    # assert response.status_code == 200, f"登录请求失败，状态码为：{response.status_code}"
    #
    # response = response.json()
    # print(response)
    return response
body= {
        "id": 1649,
            }
# print(deleteAsk(body))

def get_expert_ask_reply_page(pagesize):
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
    }
    data = yamlhandler.read_yaml()['get_expert_ask_reply_page']
    # url = data['url']+f'?r=0.2840183065749913&pageSize={pagesize}&timestamp={timestamp}'
    url = data['url']+f'?r=0.2840183065749914&pageSize={pagesize}&startTime={timestamp}'
    # ?r=0.2840183065749913&pageSize={pagesize}&timestamp=1706780569357
    method = data['method']
    response = req.visit(method, url, headers=headers)
    return response

    # response = response.json()
    # print(response)
def get_ask_ids():
    res=get_expert_ask_reply_page(100)
    bodyMessage=json.loads(res['bodyMessage'])
    # print(bodyMessage)
    ids=[]
    for item in bodyMessage['pageDatas']:
        ids.append(item['ask']['id'])
        # for reply in item['replyList']:
        #     ids.append(reply['id'])

    # ids=res1['pageDatas']['ask']['id']
    print(ids)
    return ids

get_ask_ids()

# print(get_expert_ask_reply_page(100))