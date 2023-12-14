import os

import allure
import pytest
from selenium import webdriver


class Test:
    @allure.severity('critical')
    @allure.feature('测试1')
    @allure.story('测试1.1')
    def test_open_baidu(self):
        '''
        描述：测试打开百度
        '''
        with allure.step('打开百度'):
            d=webdriver.Edge()
            d.get('http://www.baidu.com')
        d.close()

# if __name__ == '__main__':
#     # pytest.main(['-vs', '--rerun 1', 'test1.py','-q', '--alluredir=./result'])
#     # # os.system('allure generate ./allure_result -o allure_result/html --clean open')
#     # os.system('allure serve ./result/ open')
#
#     # pytest.main(['test1.py', '--alluredir=./result/2'])
#     # os.system('allure generate ./result/2 -o ./report/2/ --clean')
#     # os.system('allure open -h 127.0.0.1 -p 8883 ./report/2')
#
#     pytest.main(['-s', '-q', '--alluredir', './report'])