import re

from CompanyProject.Fastbull.Api_fastbull.common.requests_handler import RequestsHandler
from CompanyProject.Fastbull.Api_fastbull.common.yaml_handler import YamlHandler
from CompanyProject.Fastbull.Api_fastbull.logic.conftest import headers1, generate_nonce

req=RequestsHandler()
yamlhandler=YamlHandler('../common/Api.yaml')
nonce = generate_nonce()
def login():
    data=yamlhandler.read_yaml()['login']
    url = data['url']
    method = data['method']
    body = data['body']

    response = req.visit(method, url, json=body)

    assert response.status_code == 200, f"登录请求失败，状态码为：{response.status_code}"

    response_json = response.json()
    return response_json
    # body_message_str = response_json['bodyMessage'][1:-1]  # 去除首尾单引号
# login()

def get_identity():
    response_json=login()
    body_message_str = response_json['bodyMessage']
    # 使用正则表达式提取 identity 字段的值
    match_result = re.search(r'"identity":"([^"]+)"', body_message_str)
    extracted_identity = match_result.group(1)
    print(extracted_identity)
    return extracted_identity
# get_identity()
def logout():
    headers = headers1(nonce)
    data=yamlhandler.read_yaml()['logout']
    url = data['url']
    method = data['method']
    body = data['body']

    response = req.visit(method, url, headers=headers,json=body)
    # print(response)
    assert response.status_code == 200, f"登录请求失败，状态码为：{response.status_code}"
    #
    response_json = response.json()
    assert response_json['message'] == '操作成功'
    print(response_json)
# logout()