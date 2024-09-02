import os
import unittest
import pytest
from pprint import pprint
import allure

from ApiTest_mindmaster.common.logger_handler import LoggerHandler
from ApiTest_mindmaster.common.read_yaml import readYaml
from others.ApiTest_mindmaster.common.requests_handler import RequestsHandler

# 定义测试类 TestLogin
import logging

# 初始化日志模块
from ApiTest_mindmaster.config.yaml_handler import yaml_data

filename=os.path.basename(__file__).split('.')[0]
logger = LoggerHandler(name=yaml_data['logger']['name'],
                       level=yaml_data['logger']['level'],
                       file=f'../log/{filename}_log.txt',
                       format=yaml_data['logger']['format'])
@allure.feature('登录')
class TestLogin:
    """登录用例"""
    def setup(self):
        pass
    def teardown(self):
        pass

    # 使用pytest的autouse=True参数，确保在每个测试方法执行前自动调用set_init方法初始化环境，并在所有测试方法执行后关闭会话
    # @pytest.fixture(autouse=True)
    # def set_init(self):
    #     # 实例化请求类并记录日志
    #     logger.info("开始初始化TestLogin类")
    #     self.req = RequestsHandler()
    #     yield  # 在yield语句之后的内容会在测试方法执行完后执行
    #     self.req.close_session()  # 关闭网络请求会话
    #     logger.info("成功关闭网络请求会话")

    # 使用pytest.mark.parametrize装饰器从yaml文件中读取参数并进行数据驱动测试
    @pytest.mark.parametrize('items', readYaml('../data/loginDataParameter.yaml'))
    # 设置 allure.story 描述为 '登录用例'
    @allure.story('登录用例')
    def test_login(self, items):
        # 记录开始执行登录用例的日志
        # logger.info(f"开始执行登录用例，参数: {items}")
        res = self.req.visit(url=items['url'],
                             method=items['method'],
                             data=items['data'])

        # 输出请求响应的状态信息并记录到日志
        print(res['status'])
        logger.info(f"登录请求状态码: {res['status']}")

        # 可以根据实际需求添加更多关于登录结果的判断和日志记录



        try:
            # 断言：预期结果与实际结果对比:第一个是预期，第二个是实际
            assert items['expected_result'] == res['status']
            result = 'Pass'
        except AssertionError as e:
            result = 'Fail'
            raise e
        # finally:
            # 将响应的状态码，写到excel的第9列，即写入返回的状态码
            # TestLogin.excel.write_excel('../data/openpyxl_mindmaster2.xlsx', 'login',items['case_id'] + 实例25_批量生成PPT版荣誉证书, 8, res['status'])
            # # 如果断言成功，则在第10行(测试结果)写入Pass,否则，写入Fail
            # TestLogin.excel.write_excel('../data/openpyxl_mindmaster2.xlsx', 'login',items['case_id'] + 实例25_批量生成PPT版荣誉证书, 9, result)


if __name__ == '__main__':
    # pytest.main(['-s', '--alluredir=../allure-results', 'test_addComment.py'])
    pytest.main(['-vs', '--alluredir=./allure-results', __file__])
    os.system('allure generate ./allure-results --clean -o ./allure-results/report/html')
    os.system('allure open ./allure-results/report/html')
# 实例25_批量生成PPT版荣誉证书.excel里面字符串要用双引号
# 2.ddt(*data):* 表示对 case_data1 进行序列解包，将其作为独立的参数进行传递。
        # 也就是说，如果 case_data1 是一个列表或元组，这两种写法的效果一样。但是，如果 case_data1 是一个字典，则不能使用 @data(case_data1,) 这种写法。
        # 如果强制使用，会出现以下错误：TypeError: 'dict' object is not iterable
        # ddt(data,)表示将 case_data1 作为一个单独的元素放入元组中，并将该元组作为参数传递给装饰器,
        # 因此，在传递一个字典对象时，应该使用 @data(case_data1,) 的方式，而不是 @data(*case_data1)
# 3.字符串和json格式转换“
        # res_dict = json.dumps(res)  # 将字典字符串转换成json字符串
        # res_dict = json.loads(res)  # 将 JSON 字符串转换成字典