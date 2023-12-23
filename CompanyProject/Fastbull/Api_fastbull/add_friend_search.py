import requests
import json


def test_search_user_info_list():
    url = "https://forexchat-chat-test.tostar.top/apiBase/api/UserInfo/SearchUserInfoList"

    headers = {
        "authority": "forexchat-chat-test.tostar.top",
        "accept": "application/json, text/plain, */*",
        "accept-language": "cn",
        "access": "1f37b1094a8155cb36f1ae8da0bda1fd",
        "btoken": "5E48948EB81332A9321EDA7A46115E32",
        "cache-control": "no-cache",
        "channel": "1",
        "clienttype": "4",
        "content-type": "application/json",
        "cookie": "deviceId=e6e58b4307703042c108aaa0e928492c; homeDriver=true; FIRSTENTER=1",
        "countrycode": "6541",
        "cuid": "0",
        "deviceid": "1fee8086efe6222e46ab93f89d7d879e",
        "dnt": "1",
        "edition": "1",
        "locale": "zh-CN",
        "pid": "26",
        "pragma": "no-cache",
        "random": "24961370",
        "referer": "https://forexchat-chat-test.tostar.top/main",
        "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "sec-gpc": "1",
        "timestamp": "1703317734313",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
        "userid": "0",
        "userkey": "",
        "verifyuid": "0"
    }

    params = {
        "countryCode": "6541",
        "pageIndex": "1",
        "pageSize": "10",
        "searchKey": "13",
        "searchType": "1"
    }

    response = requests.get(url, headers=headers, params=params)

    message = response.json()['message']
    print(response.text)

    assert message == '操作成功'

