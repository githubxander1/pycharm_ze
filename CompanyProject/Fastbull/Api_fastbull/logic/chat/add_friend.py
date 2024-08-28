import requests
import json


def test_add_friend():
    url = "http://192.168.7.45:32019/api/userFriend/addFriend"

    headers = {
        "accept": "application/json",
        "Accept-Language": "zh-CN",
        "swagger": "实例25_批量生成PPT版荣誉证书",
        "Content-Type": "application/json"
    }

    data = {
        "userId": 1009154,
        "friendId": 1009117,
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    print(response.json()['message'])
    message=response.json()['message']
    print(response.text)

    assert message == '该用户已经是您的好友了'

