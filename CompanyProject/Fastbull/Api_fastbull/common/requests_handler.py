import requests

# from CompanyProject.Fastbull.Api_fastbull.common.yaml_handler import read_yaml


class RequestsHandler:
    def __init__(self):
        self.session = requests.session()
    def visit(self, method, url, params = None, data= None, json= None, headers= None):
        # if headers is None:
        #     headers = {}
        # headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.
        return self.session.request(method, url, params=params, data=data, json=json, headers=headers)
# url=read_yaml('Api.yaml')[0]['url']
# url=read_yaml('Api.yaml')['login']['url']
# method=read_yaml('Api.yaml')[0]['method']
# print(url)
# print(method)
# request=RequestsHandler()
# request.visit(url,method)