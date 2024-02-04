import os

import requests

from ApiTest_mindmaster.common.requests_handler import RequestsHandler
from CompanyProject.Fastbull.Api_fastbull.common.yaml_handler import read_yaml

req=RequestsHandler()
file='../common/Api.yaml'
def login():
    url = read_yaml(file)['login']['url']
    method = read_yaml(file)['login']['method']
    data= read_yaml(file)['login']['body']
    print(url)
    print(method)
    print(data)

    # response = req.visit(method, url,json=data)
    # response = requests.post(url,json=data)
    # print(response)
    # print(response.json())
login()
print(os.getcwd())