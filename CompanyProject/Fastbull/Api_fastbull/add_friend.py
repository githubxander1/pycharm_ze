import requests
import json


def test_add_friend():
    url = "http://192.168.7.45:32019/api/userFriend/addFriend"

    headers = {
        "accept": "application/json",
        "Accept-Language": "zh-CN",
        "swagger": "1",
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

    # try:
    #     response_data = response.json()
    #     # 根据实际返回数据结构进行断言和验证
    #     assert 'key' in response_data and isinstance(response_data['key'], str), "返回数据中未找到预期的键或类型不正确"
    # except json.JSONDecodeError:
    #     assert False, "返回的数据不是有效的JSON格式"
    #
    # print(f"请求成功，返回数据：{response.json()}")