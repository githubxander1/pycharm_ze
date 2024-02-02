import requests

from CompanyProject.Fastbull.Api_fastbull.logic.common import common_data


def addAsk(askContent):
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
        "langid": "1",
        "nonce": "vL7b3bAn",
        "pragma": "no-cache",
        "sec-ch-ua": "\"Not A(Brand\";v=\"99\", \"Microsoft Edge\";v=\"121\", \"Chromium\";v=\"121\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "sign": "8CE95A8D10A710B98C0E4108FA6355CF",
        "timestamp": "1706750154",
        "uid": common_data['uid']
    }

    # data = {
    #       "askContent": "美国",
    #       "askImage": "https://img.fastbull.com/test/image/2024/02/C0F94A3E97D149449A0BA67A93F4050E?w=3840&h=2400"
    #     }

    response = requests.post("https://testfbapi.tostar.top/fastbull-universal-service/api/postAddAsk", headers=headers,
                             json=askContent)
    response_json=response.json()
    # print(response_json)  # 打印响应内容
    return response_json

def deleteAsk(id):
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
        "langid": "1",
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

    data = {
        "id": id,
        "type": 1
    }

    response = requests.post("https://testfbapi.tostar.top/fastbull-universal-service/api/deleteAskReply", headers=headers,
                             json=data)
    response_json=response.json()
    # print(response.json())  # 打印响应内容
    return response_json
# print(deleteAsk(13))

def get_expert_ask_reply_page(pagesize):
    headers = {
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6",
        "beta": "true",
        "btoken": "cf0cabf8f9cefab23b3c4ef6c4f9a395",
        "cache-control": "no-cache",
        "client-type": "4",
        "clientversion": "latest",
        "deviceid": "51cee82782f69741d228946af2d2cda3",
        "deviceno": "51cee82782f69741d228946af2d2cda3",
        "langid": "1",
        "nonce": "62RM0Isf",
        "pragma": "no-cache",
        "sec-ch-ua": "\"Not A(Brand\";v=\"99\", \"Microsoft Edge\";v=\"121\", \"Chromium\";v=\"121\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "sign": "88E5CCAD1F2D5A2CF8566FDA1C999195",
        "timestamp": "1706780569",
        "uid": common_data['uid']
    }
    response = requests.get(f"https://testfbapi.tostar.top/fastbull-universal-service/api/getExpertAskReplyPage?r=0.2840183065749913&pageSize={pagesize}&timestamp=1706780569357", headers=headers)
    response_json=response.json()
    print(response_json)
    # assert response.status_code == expected_status_code, f"Expected status code: {expected_status_code}, but got: {response.status_code}"
    # 在这里，你可以添加更多的断言来验证响应的内容或特定字段。
print(get_expert_ask_reply_page(10))