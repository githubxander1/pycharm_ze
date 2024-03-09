import os

import allure

from ApiTest_mindmaster.common.logger_handler import LoggerHandler
from ApiTest_mindmaster.common.requests_handler import RequestsHandler
# from CompanyProject.Fastbull.Api_fastbull.logic.comment import nonce
from CompanyProject.Fastbull.Api_fastbull.logic.conftest import generate_sign_login, get_identity, generate_btoken, \
    generate_nonce, generate_token, timestamp, common_data
from CompanyProject.Fastbull.Api_fastbull.common.yaml_handler import YamlHandler

nonce = generate_nonce()
req=RequestsHandler()
yamlhandler=YamlHandler('../common/Api.yaml')
filename=os.path.basename(__file__).split('.')[0]
logger=LoggerHandler(name='ask',level='DEBUG',file=f'../log/{filename}_log.log',format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def post_like_operate(postId,like_type):
    """点赞操作
    1.postId:被点赞的帖子id
    2.like_type:1:点赞 2:取消点赞

    """
    function_name = post_like_operate.__qualname__
    allure.step(f'{function_name}请求头')
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
        "langid": "1",
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


    data = yamlhandler.read_yaml()['post_like']
    logger.warning(f'{function_name}请求头：{headers}')
    url = data['url']
    method = data['method']
    body= {
        "postId": postId,
        "operate": like_type  # 点赞
        # "operate": 0 #取消点赞
    }

    response = req.visit(method, url, headers=headers, json=body)
    response_json = response['message']
    # print(response_json)
    assert response_json == '操作成功'

    # print(response_json)
# post_like_operate('65ba072cc1034b00073da295',0)