import json
import os
from pprint import pprint

import allure
import pytest
import requests
from requests.auth import HTTPBasicAuth
import logging
# from allure_commons._allure import Allure
from CompanyProject.Fastbull.Api_fastbull.logic.ask import addAsk, deleteAsk
from ApiTest_mindmaster.common.yaml_handler import YamlHandler

yamlhandler=YamlHandler('../data/ask.yaml')
class TestDeleteAsk:
    def setup(self):
        # pass
        print('开始执行测试')
    def teardown(self):
        # pass
        print('测试结束')

    @allure.feature("提问-接口")
    @allure.story("删除提问")
    @pytest.mark.parametrize('delete_data',yamlhandler.read_yaml()['deleteAsk'],ids=lambda delete_data: delete_data['name'])
    def test_delete_ask(self,delete_data):
        body=delete_data['body']

        # 将请求体转换为字符串并附加到Allure报告
        # body_str = json.dumps(body, indent=4)
        # allure.attach(body_str, name='请求体', attachment_type=allure.attachment_type.JSON)

        name=delete_data['name']
        with allure.step('用例标题：' + name):
            response=deleteAsk(body)
        # print(response)
        assert response['message']=='操作成功'
        # 检查响应状态码是否为200（正常）或400（错误）等预期的码，这里可以根据实际需求修改检查条件。这里仅作示例。
        # 将响应内容记录到日志中，方便后续分析。这里可以根据实际需求修改日志格式和输出位置。
        # logger.info(f"响应内容：{response}")
        # 结束测试，将测试结果和报告写入Allure测试报告中。这里可以根据实际需求修改测试结果和报告的输出位置。
        # allure.attach(response)  # 可以根据需要添加其他Allure附件，例如截图、日志等。
        # allure.test_step("添加问询接口测试")  # 为测试步骤添加描述，方便跟踪和识别。可以根据实际需求修改描述内容。
        # logger.info(f"测试结束")

if __name__ == '__main__':
    # pytest.main(['-s', '--alluredir=../allure-results', 'test_addComment.py'])
    pytest.main(['-s', '--alluredir=../allure-results', __file__])
    os.system('allure generate ../allure-results -o open ../allure-results/report/  ')
    os.system('allure open ../allure-results/report/html/index.html')