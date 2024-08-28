import base64
import json
import os

import allure
import requests
import time

from numpy.ma import count

from ApiTest_mindmaster.common.logger_handler import LoggerHandler
from CompanyProject.Fastbull.Api_fastbull.common.requests_handler import RequestsHandler
from CompanyProject.Fastbull.Api_fastbull.common.yaml_handler import YamlHandler
from CompanyProject.Fastbull.Api_fastbull.logic.conftest import generate_btoken, generate_sign_login, generate_token, \
    get_identity, generate_nonce, timestamp, common_data,headers1

nonce = generate_nonce()
req=RequestsHandler()
yamlhandler=YamlHandler('../data/Api.yaml')
filename=os.path.basename(__file__).split('.')[0]
logger=LoggerHandler(name='ask',level='DEBUG',file=f'../log/{filename}_log.log',format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def add_comment(content):
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
    }
    function_name = add_comment.__qualname__
    logger.warning(f'{function_name}请求头：{headers}')
    allure.step(f'{function_name}请求头：{headers}')

    yaml_data=yamlhandler.read_yaml()['add_comment']
    url = yaml_data['url']
    method = yaml_data['method']
    print(yaml_data)

    response = req.visit(method=method, url=url, headers=headers,data=content)

    assert response.status_code == 200, f"登录请求失败，状态码为：{response.status_code}"

    response=response.json()
    print(response)
    # assert json.loads(response['subCode']) == 1000000 #业务状态
    comment_id = json.loads(response['bodyMessage'])['id']
    print(f'评论id:{comment_id}')
    return response,comment_id



def delete_comment(post_id):
    headers2 = headers1(nonce)
    headers = {
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6",
        "beta": "true",
        "btoken": generate_btoken(common_data["client_type"], common_data["client_version"], common_data['uuid'],common_data['device_no']),
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
        "timestamp":timestamp,
        "uid": common_data['uid']
    }

    data = yamlhandler.read_yaml()['delete_comment']
    url = data['url']+f'?postId={post_id}'
    method = data['method']

    response = req.visit(method, url, headers=headers, json=post_id)
    response_json=response.json()
    return response_json
    # assert response['message'] == "操作成功"
    # print(response)
    # print(response_json)

def get_comment_list(postId):
    headers2 = headers1(nonce)
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
    data = yamlhandler.read_yaml()['get_comment_list']
    url = data['url'] + f'&postId={postId}'
    method = data['method']
    # print(url)
    # print(method)

    response = req.visit(method, url, headers=headers, params=postId)
    response_json = response.json()

    # print(response_json)
    return response_json
    # body_message = json.loads(response_json['bodyMessage'])
    # # print(body_message)
    # # message=json.loads(response_json['message'])
    # # print(message)
    # comments_data = body_message['pageDatas']
    # # print(comments_data)
    # #
    # comment_ids = [comment['id'] for comment in comments_data]
    # print(comment_ids)
    # print(count(comment_ids))
    # assert response.status_code == 200  # 或您期望的其他状态码
    # return comment_ids

# body = {
#             "comment": "国际油价重挫4%！沙特“服软”降价，原油将重启跌势？[憨笑]3",
#             "imageInfoModel": [
#                 {
#                     "high": 226,
#                     "url": "https://img.fastbull.com/test/image/2024/02/3E6104A2BE7844E4923B6886D6F2D6A8",
#                     "width": 448
#                 }
#             ],
#             "postId": "3707814_1",
#             "type": 实例25_批量生成PPT版荣誉证书
#         }

# for id in get_comment_list(common_data["uid"], '3707814_1'):
#     delete_comment(common_data["uid"], id)
# print(add_comment(body))


if __name__ == '__main__':
    get_comment_list('15392710_1')
    comment_body = {
        "comment": "2国际油价重挫4%！沙特“服软”降价，原油将重启跌势？[憨笑]112",
        "imageInfoModel": [
            {
                "high": 226,
                "url": "https://img.fastbull.com/test/image/2024/02/3E6104A2BE7844E4923B6886D6F2D6A8",
                "width": 448
            }
        ],
        # "postId": "4279312_1",#对当今世界的资产泡沫要敬而远之
        # "postId": "3707814_1",#对当今世界的资产泡沫要敬而远之
        "postId": "15392710_1",  # 对当今世界的资产泡沫要敬而远之
        "type": 1
    }
    add_comment(comment_body)
    # print(delete_comment('65e6f1cb6f916c000788f763'))