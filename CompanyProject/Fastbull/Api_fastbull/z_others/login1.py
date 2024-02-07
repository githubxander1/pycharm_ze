import json

from CompanyProject.Fastbull.Api_fastbull.z_others.api_key import ApiKey
# from CompanyProject.Fastbull.Api_fastbull.config import url


def login():
    ak=ApiKey()
    url = 'https://testfbapi.tostar.top/fastbull-user-service/api/postLoginByAccount'
    headers = {
        "appType": '1',
        "langId" : '1',
        "accept": "application/json;charset=UTF-8",
        "Content-Type": "application/json"
    }

    request_data = "OqRZEG9mm9B/y92h7+muv9Wo/hqLayfEHblOiW/1ePColbT1ffuMo1ApsQPHr4G02+zbOMm2tnftFXUAhKjlxV6rosUNFayqQABV7DhESBjMTNzgCI3tF5P5afpnQFK0Ux09uC6F4gHEE+MN4Ydt32pu25IbXW0GVRzoSjAaDxB+cQVsBQ2JKGlXPVEI+FfU"

    response = ak.post(url, headers=headers, data=json.dumps({"requestData": request_data}))
    print(response.json())

    # msg=ak.get_text(response.text,'message')
    # print(msg)
    # assert msg == "操作成功"
    # 检查响应状态码和内容
#     if response.status_code == 200:
#         print("登录成功")
#         print("返回内容:", response.json())
#     else:
#         print("Request failed with status code:", response.status_code)
#
login()
