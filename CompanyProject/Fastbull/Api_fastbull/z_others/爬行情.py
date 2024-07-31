import os
from multiprocessing import freeze_support

import requests
import concurrent.futures
from urllib.parse import urlencode
import json
from ApiTest_mindmaster.common.logger_handler import LoggerHandler
from ApiTest_mindmaster.common.requests_handler import RequestsHandler
# from CompanyProject.Fastbull.Api_fastbull.logic.comment import nonce
from CompanyProject.Fastbull.Api_fastbull.logic.conftest import generate_sign_login, get_identity, generate_btoken, \
    generate_nonce, generate_token, timestamp, common_data, headers1
from CompanyProject.Fastbull.Api_fastbull.common.yaml_handler import YamlHandler
nonce = generate_nonce()
req=RequestsHandler()
yamlhandler=YamlHandler('../data/Api.yaml')
filename=os.path.basename(__file__).split('.')[0]
logger=LoggerHandler(name='ask',level='DEBUG',file=f'../log/{filename}_log.log',format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 定义请求头
# headers = {
#     # 这里列出你提供的所有头部信息...
#     "accept": "*/*",
#     "accept-language": "zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6",
#     # ... 其他header信息
# }
# headers = {
#     "accept": "*/*",
#     "accept-language": "zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6",
#     "beta": "true",
#     "btoken": generate_btoken(common_data["client_type"], common_data["client_version"], common_data['uuid'],
#                               common_data['device_no']),
#     "cache-control": "no-cache",
#     "client-type": "4",
#     "clientversion": "latest",
#     "content-type": "application/json",
#     "deviceid": "51cee82782f69741d228946af2d2cda3",
#     "deviceno": "51cee82782f69741d228946af2d2cda3",
#     "langid": "1",
#     "nonce": nonce,
#     "pragma": "no-cache",
#     "sec-ch-ua": "\"Not A(Brand\";v=\"99\", \"Microsoft Edge\";v=\"121\", \"Chromium\";v=\"121\"",
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-ua-platform": "\"Windows\"",
#     "sec-fetch-dest": "empty",
#     "sec-fetch-mode": "cors",
#     "sec-fetch-site": "same-site",
#     "sign": generate_sign_login(common_data['uid'], generate_token(get_identity()), timestamp, nonce),
#     "timestamp": timestamp,
#     "uid": common_data['uid']
# }
params = {
    "r": "0.7605017467273048",
    "pageIndex": "",
    "pageSize": "20",
    "category": "all_106",
    # 注意 nonce 和 sign 等可能需要每次请求动态生成的参数
}
headers=headers1(nonce)

# 动态生成页码
# pages = [i for i in range(1, 452)]
pages = [i for i in range(1, 10)]


def fetch_data(page_index):
    params["pageIndex"] = str(page_index)
    # 如果有签名算法，请确保这里的nonce和sign等参数正确生成
    # nonce和sign通常需要根据timestamp或其他动态参数计算得到
    # 这里假设已经处理好这些动态参数

    url = f"https://api.fastbull.com/fastbull-quotes-service/api/getStocksByCategory?" + urlencode(params)
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print(json.loads(response.text))
        return json.loads(response.text)
    else:
        print(f"请求失败，状态码：{response.status_code}")
        return None


def multi_process_fetch(max_workers=None):
    with concurrent.futures.ProcessPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(fetch_data, page): page for page in pages}

        all_results = []
        for future in concurrent.futures.as_completed(futures):
            page = futures[future]
            try:
                data = future.result()
                if data is not None:
                    all_results.extend(data)
            except Exception as exc:
                print(f"页面 {page} 请求出现错误: {exc}")

        return all_results


if __name__ == '__main__':
    freeze_support()
    results = multi_process_fetch(max_workers=10)
    print(results)
# 将所有结果整合到一起，并进一步处理（如写入文件或数据库）
# ...