import os

import allure
import pytest
import requests
from requests.auth import HTTPBasicAuth
import logging
# from allure_commons._allure import Allure
from ApiTest_mindmaster.common.logger_handler import LoggerHandler
from CompanyProject.Fastbull.Api_fastbull.logic.ask import addAsk, deleteAsk

from ApiTest_mindmaster.common.yaml_handler import YamlHandler

yamlhandler=YamlHandler('../data/ask.yaml')
filename=os.path.basename(__file__).split('.')[0]
logger=LoggerHandler(name='root',level='WARNING',file=f'../log/{filename}_log.log',format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
class TestAddAsk:
# 定义测试用例
    def setup(self):
        pass
    def teardown(self):
        pass

    # @pytest.mark.skip("跳过")
    @pytest.mark.parametrize('add_data',yamlhandler.read_yaml()['addAsk'])
    def test_add_ask(self,add_data):
        body = add_data['data']
        response=addAsk(body)
        print(response)
        logger.warning(f"响应内容：{response}")
        allure.attach(response)  # 可以根据需要添加其他Allure附件，例如截图、日志等。
        assert response['message']=='操作成功'
        # 将响应内容记录到日志中，方便后续分析。这里可以根据实际需求修改日志格式和输出位置。
        # 结束测试，将测试结果和报告写入Allure测试报告中。这里可以根据实际需求修改测试结果和报告的输出位置。
        logger.info(f"测试结束")

    def test_add_ask_error(self):
        # 创建Allure测试报告对象
        # allure = Allure()
        # 设置日志记录器
        logger = logging.getLogger(__name__)
        logger.info(f"开始测试添加问询")
        deleteAsk(1224)

if __name__ == '__main__':
    # pytest.main(['-s', '--alluredir=../allure-results', 'test_addComment.py'])
    # pytest.main(['-s', '--alluredir=../allure-results', __file__])
    # os.system('allure generate ../allure-results -o open ../allure-results/report/html --clean ')

    pytest.main(['test_addAsk','-vs', '--alluredir', './result', '--clean-alluredir'])
    # pytest.main([__file__,'-vs', '--alluredir', './result', '--clean-alluredir'])
    os.system('allure generate ./result/ -o ./report_allure/ --clean')
    os.system('allure serve result')
