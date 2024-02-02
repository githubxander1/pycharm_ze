import os

import pytest
import requests
from requests.auth import HTTPBasicAuth
import logging
# from allure_commons._allure import Allure

from CompanyProject.Fastbull.Api_fastbull.logic.ask import addAsk, deleteAsk


class TestDeleteAsk:
# 定义测试用例
    def setup(self):
        # pass
        print('开始执行测试')
    def teardown(self):
        # pass
        print('测试结束')

    def test_delete_ask(self):
        # 创建Allure测试报告对象
        # allure = Allure()
        # 设置日志记录器
        logger = logging.getLogger(__name__)
        logger.info(f"开始测试添加问询")

        response=deleteAsk(1013)
        print(response)
        # 检查响应状态码是否为200（正常）或400（错误）等预期的码，这里可以根据实际需求修改检查条件。这里仅作示例。
        assert response['message']=='操作成功'
        # 将响应内容记录到日志中，方便后续分析。这里可以根据实际需求修改日志格式和输出位置。
        logger.info(f"响应内容：{response}")
        # 结束测试，将测试结果和报告写入Allure测试报告中。这里可以根据实际需求修改测试结果和报告的输出位置。
        # allure.attach(response)  # 可以根据需要添加其他Allure附件，例如截图、日志等。
        # allure.test_step("添加问询接口测试")  # 为测试步骤添加描述，方便跟踪和识别。可以根据实际需求修改描述内容。
        logger.info(f"测试结束")

if __name__ == '__main__':
    # pytest.main(['-s', '--alluredir=../allure-results', 'test_addComment.py'])
    pytest.main(['-s', '--alluredir=../allure-results', __file__])
    os.system('allure generate ../allure-results -o open ../allure-results/report/html  ')