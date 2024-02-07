import json
import os

import allure
import pytest
from ApiTest_mindmaster.common.logger_handler import LoggerHandler
from CompanyProject.Fastbull.Api_fastbull.logic.ask import addAsk, deleteAsk, get_expert_ask_reply_page, get_ask_ids

from ApiTest_mindmaster.common.yaml_handler import YamlHandler

yamlhandler=YamlHandler('../data/ask.yaml')
filename=os.path.basename(__file__).split('.')[0]
logger=LoggerHandler(name='root',level='WARNING',file=f'../log/{filename}_log.log',format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class TestAddAsk:
    # def __init__(self):
    added_ask_id = None
    def setup(self):
        pass
    def teardown(self):
        print(f'要删除的id: {self.added_ask_id}')
        # pass
        # if self.added_ask_id is not None:
        # delete_response = deleteAsk(self.added_ask_id)
        # print(delete_response)
        # logger.warning(f"删除ask_id={self.added_ask_id}响应内容：{delete_response}")
        # allure.attach(json.dumps(delete_response), name='删除ask_id={self.added_ask_id}响应内容')
        #
        # assert delete_response['message'] == '操作成功'

    @allure.feature('问答-接口测试')
    @allure.story('添加问答')
    @pytest.mark.parametrize('add_data',yamlhandler.read_yaml()['addAsk'],ids=lambda add_data: add_data['name'])
    def test_add_ask(self,add_data):
        # 获取请求参数
        body = add_data['data']

        # 发送请求
        response = addAsk(body)
        print(response)

        # 打印响应内容
        logger.warning(f"响应内容：{response}")

        # 添加Allure附件
        allure.attach(json.dumps(response), name='添加问答响应内容')

        # 断言响应结果
        assert response[0]['message'] == '操作成功'
        self.added_ask_id = response[1]
        assert self.added_ask_id in get_ask_ids()

        # 打印测试结束信息
        logger.info(f"测试结束")

if __name__ == '__main__':
    # pytest.main(['-s', '--alluredir=../allure-results', 'test_addComment.py'])
    # pytest.main(['-s', '--alluredir=../allure-results', __file__])
    # os.system('allure generate ../allure-results -o open ../allure-results/report/html --clean ')

    # pytest.main(['test_addAsk','-vs', '--alluredir', './result', '--clean-alluredir'])
    pytest.main([__file__,'-vs', '--alluredir', './result', '--clean-alluredir'])
    os.system('allure generate ./result/ -o ./report_allure/ --clean')
    os.system('allure serve result')
    os.system('allure open ./report_allure/index.html')
