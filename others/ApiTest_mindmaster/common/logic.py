from ApiTest_mindmaster.common.yaml_handler import YamlHandler
from ApiTest_mindmaster.common.logger_handler import LoggerHandler
from others.ApiTest_mindmaster.common.requests_handler import RequestsHandler

# file='Api1.yaml'
from ApiTest_mindmaster.middleware.helper import  token

yamlreader = YamlHandler('Api1.yaml')
# print(yaml_data['login']['url'])

class Logic(object):
    def __init__(self):
        self.name = 'Logic'
        self.__logger = LoggerHandler('logic')
        # self.__logger.info('Logic 初始化')
        self.request=RequestsHandler()
        self.token=token()

    def newFold_add(self):
        # self.__logger.info('newFold_add')
        url=yamlreader.read_yaml()['addNewFold']['url']
        method=yamlreader.read_yaml()['addNewFold']['method']
        data=yamlreader.read_yaml()['addNewFold']['data']
        headers = {
            'Authorization': self.token
        }
        print(url)
        re=self.request.visit(method, url,data,headers=headers)
        print(re)
        # return True

logic=Logic()
logic.newFold_add()

# url = "https://mindapi.edrawsoft.cn/api/mm_web/folder/v2"



# "https://mindapi.edrawsoft.cn/api/mm_web/recycle/batch_create/v2", {
#   "headers": {
#     "accept": "application/json, text/plain, */*",
#     "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
#     "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDk1NTM1MjAsImlhdCI6MTcwNjk2MTQ2MCwiaXNzIjoiRWRyYXdTb2Z0Iiwic3ViIjoie1wiY29ycFVzZXJJZFwiOlwiXCIsXCJvcGVuSWRcIjpcIlwiLFwiY29ycElkXCI6XCJcIn0iLCJhdWQiOiIyMzkyODUxNiIsInNyYyI6InBhc3N3b3JkIn0.vJ3vGHB-7Tfyvd-O-YTc5aX70ild60pic7g-oizam6M",
#     "cache-control": "no-cache",
#     "content-type": "application/json;charset=UTF-8",
#     "pragma": "no-cache",
#     "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Microsoft Edge\";v=\"120\"",
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-ua-platform": "\"Windows\"",
#     "sec-fetch-dest": "empty",
#     "sec-fetch-mode": "cors",
#     "sec-fetch-site": "same-site"
#   },
#   "referrer": "https://mm.edrawsoft.cn/",
#   "referrerPolicy": "strict-origin-when-cross-origin",
#   "body": "{\"delete_file\":[],\"delete_folder\":[],\"objs\":[{\"obj\":\"2695418206@qq.com/Personal/新建/\",\"platform\":\"web\"}],\"folder_id\":0}",
#   "method": "POST",
#   "mode": "cors",
#   "credentials": "include"
# });