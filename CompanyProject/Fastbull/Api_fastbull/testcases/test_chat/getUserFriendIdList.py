import requests
import pytest


def test_get_user_friend_id_list():
    url = "http://192.168.7.45:32019/api/userFriend/getUserFriendIdList"
    params = {
        "userId": 1009154
    }
    headers = {
        "accept": "application/json",
        "Accept-Language": "zh-CN",
        "swagger": "实例25_批量生成PPT版荣誉证书"
    }

    response = requests.get(url, headers=headers, params=params)

    message = response.json()['message']
    print(response.text)

    assert message == '操作成功'



if __name__ == "__main__":
    pytest.main(['-v', __file__])