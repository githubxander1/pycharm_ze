import base64
import json

import requests
import time

from numpy.ma import count

from CompanyProject.Fastbull.Api_fastbull.logic.common import generate_btoken, generate_sign_login, generate_token, \
    get_identity, generate_nonce, timestamp, common_data

# uid = "205050" #8@qq.com
# btoken = "881c64f16359dc75180efa784ad047db"
# client_type = "4"
# client_version="latest"
# device_no = "51cee82782f69741d228946af2d2cda3"
# uuid="2a3cd0189ea31b1d5f177b66df8705f8"
# vip = "0"  # 根据实际情况填写会员状态
# timestamp = str(int(time.time()))[:10]  # 获取当前时间戳
nonce = generate_nonce()

def add_comment(content):
    headers = {
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6",
        "beta": "true",
        "btoken": generate_btoken(common_data["client_type"], common_data["client_version"], common_data['uuid'],common_data['device_no']),
        "cache-control": "no-cache",
        "client-type": common_data["client_type"],
        "clientversion": common_data["client_version"],
        "content-type": "application/json",
        "deviceid": "2a3cd0189ea31b1d5f177b66df8705f8",  # 根据实际情况填写设备ID
        "deviceno": "2a3cd0189ea31b1d5f177b66df8705f8",  # 根据实际情况填写设备号
        "langid": "1",
        "nonce": nonce,
        "pragma": "no-cache",
        # 下面是浏览器相关头信息，如果在非浏览器环境下可以不设置
        "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "sign": generate_sign_login(common_data['uid'], generate_token(get_identity()), timestamp, nonce),
        "timestamp": timestamp,
        "uid": common_data['uid']
    }

    # body = {
        # "comment": commentContent,
        # "imageInfoModel": [],
        # "postId": "3707814_1",#新闻id：对当今世界的资产泡沫要敬而远之
        # "type": commentType
    # }

    response = requests.post("https://testfbapi.tostar.top/fastbull-news-service/api/postComment", headers=headers, json=content)
    # print(type(response))
    assert response.status_code == 200  # 接口状态
    response=response.json()
    assert json.loads(response['subCode']) == 1000000 #业务状态
    comment_id = json.loads(response['bodyMessage'])['id']
    # print(comment_id)
    return response,comment_id
# comment_id=response.json()['bodyMessage']['Id']
# print(comment_id)

def delete_comment(post_id):
    url = f"https://testfbapi.tostar.top/fastbull-news-service/api/deleteComment?postId={post_id}"
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
        "timestamp":timestamp,
        "uid": common_data['uid']
    }
    response = requests.post(url, headers=headers)
    # print(response.json())
    assert response.status_code == 200  # 或您期望的其他状态码
    return response.json()

def get_comment_list(postId):
    url = f"https://testfbapi.tostar.top/fastbull-news-service/api/getCommentPage?r=0.27805524689164374&pageIndex=1&pageSize=100&sortType=1&postId={postId}"
    headers = {
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6",
        "beta": "true",
        "btoken": generate_btoken(common_data["client_type"], common_data["client_version"], common_data['uuid'],common_data['device_no']),
        "cache-control": "no-cache",
        "client-type": "4",
        "clientversion": "latest",
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
        "timestamp":timestamp,
        "uid": common_data['uid']
    }
    response = requests.get(url, headers=headers)
    response_json = response.json()
    # print(response_json)
    body_message = json.loads(response_json['bodyMessage'])
    # print(body_message)
    # message=json.loads(response_json['message'])
    # print(message)
    comments_data = body_message['pageDatas']
    # print(comments_data)
    #
    comment_ids = [comment['id'] for comment in comments_data]
    print(comment_ids)
    print(count(comment_ids))
    assert response.status_code == 200  # 或您期望的其他状态码
    # return comment_ids


# get_comment_list('3707814_1')
# for id in get_comment_list(common_data["uid"], '3707814_1'):
#     delete_comment(common_data["uid"], id)
# print(add_comment(common_data["uid"],'美国真坏'))
# print(delete_comment('65bb49e835df7d0007cf6302'))
