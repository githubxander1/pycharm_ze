import json

import requests
import pytest


def test_update_friend_note_name():
    url = "http://192.168.7.45:32019/api/userFriend/updateFriendNoteName"
    params = {
        "friendId": 1009154,
        "friendNoteName": "好友备注名",
        "userId": 1009117
    }
    headers = {
        "accept": "application/json",
        "Accept-Language": "zh-CN",
        "swagger": "1"
    }

    response = requests.put(url, headers=headers, params=params)
    print(response.text)

    message = response.json()['message']
    print(response.text)

    assert message == '操作成功'




if __name__ == "__main__":
    pytest.main(['-v', __file__])