import inspect
import os
import unittest
import time

import logging
from datetime import datetime

import allure
import pytest
import yaml
from xmlrunner import XMLTestRunner

# from CompanyProject.APP_Fastbull2.common import C
# from CompanyProject.APP_Fastbull2.data.load_testdata import load_data
from CompanyProject.APP_Fastbull2.common.common import Common
from CompanyProject.APP_Fastbull2.operation.ChatWindows.GroupWindow import GroupWindow
from CompanyProject.APP_Fastbull2.base.basePage import Base1, d
from CompanyProject.APP_Fastbull2.operation.GroupSet.GroupSet import GroupSet
from CompanyProject.APP_Fastbull2.operation.op_Home import Home

# 设置日志格式
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


class Test_groupNickName(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 在测试类中，setUpClass() 方法会在所有测试用例执行前自动调用一次
        GroupSet().enter_groupSet()
        GroupSet().slide_down()

    @classmethod
    def tearDownClass(cls):
        Base1().closeApp()

    def setUp(self):
        # 等待3秒
        time.sleep(3)

    def tearDown(self):
        pass

    # def test_nickname_set_all(self):
    #     for groupNickName in load_data()['groupNickName']:# 加载测试用例数据并迭代每个测试用例
    #         with self.subTest():
    #             if groupNickName.get('skip', 'n') == 'y':  # 如果跳过标志为'y'，则跳过该用例
    #                 # continue
    #                 pytest.skip("Skipping test case")
    #             GroupSet().nickname_set(groupNickName['text'])# 执行每个测试用例并传递相应的文本数据作为参数
    #             time.sleep(2)
    #             d.screenshot('test_groupNickName.png')  # 保存截图并关闭驱动器
    #
    #         assert GroupSet().nickname.get_text() in groupNickName['text']
    # def test_nickname_set(self, text):
    #     GroupSet().nickname_set(text)
    #     print(f"Group nickname set to: {text}")
    #     logging.info("正常用例")

    # group_nickname=d('contains(@content-desc,"我的群昵称")')
    # def take_screenshot(self):
    #     # print(os.path.dirname(__file__))#当前文件所在目录
    #     directory=os.getcwd()
    #     name=inspect.stack()[实例25_批量生成PPT版荣誉证书][3]#当前方法名字
    #     timestamp=datetime.now().strftime('%Y%m%d_%H%M%S')
    #     filename=f'./result_screenshots/{directory}/{name}_{timestamp}.png'
    #     d.screenshot(filename)
            # @unittest.skip('跳过')  # 你可以在这里添加其他跳过标记，例如 @unittest.skip('system_test') 等。
    def test_nickname_sus(self):
        filebasename=os.path.basename(__file__)
        text = '群昵称-第一次'
        with allure.step('设置群昵称'):
            GroupSet().nickname_set(text)
            time.sleep(2)
            if GroupSet().disbandgroup.exists:
                Common().take_screenshot(filebasename,text)
                print('截图成功')
            else:
                print('未截图')

        # print(self.group_nickname.get_text())
        # assert d.toast.get_message()=='编辑成功'
        # print(d.toast.get_message())

        logging.info("正常用例")

    # @unittest.skip('跳过')
    def test_nickname_set_null(self):
        text = ''
        with allure.step('设置群昵称:空'):
            GroupSet().nickname_set(text)
            logging.info("为空")
            time.sleep(2)
            if GroupSet().disbandgroup.exists:
                filebasename = os.path.basename(__file__)
                Common().take_screenshot(filebasename,text)
                print('截图成功')
            else:
                print('未截图')

    # @unittest.skip('跳过')
    def test_nickname_set_900(self):
        text = '九'
        with allure.step('设置群昵称:900字符'):
            GroupSet().nickname_set(text*900)
            time.sleep(2)
            if GroupSet().disbandgroup.exists:
                filebasename = os.path.basename(__file__)
                Common().take_screenshot(filebasename, text)
                print('截图成功')
            else:
                print('未截图')
            logging.info("900字符")

    @unittest.skip('跳过')
    def test_nickname_set_abnormal(self):
        text = '群昵称-(3)异常值、特殊字符：输入空白(NULL)'
        # text = '群昵称-(3)异常值、特殊字符：输入空白(NULL)、空格或"~!@#$%^&*()_+{}|[]:"<>?;’,./?;:’-=等可能导致系统错误的字符、禁止直接输入特殊字符时，尝试使用粘贴拷贝查看是否能正常提交、word中的特殊功能，通过剪贴板拷贝到输入框，分页符，分节符类似公式的上下等、数值的特殊符号如∑，㏒，㏑，∏，+，-等、正则表达式： n位的数字：^\d{n}$ ，\n,\r梵蒂冈'
        with allure.step('设置群昵称:异常值'):
            GroupSet().nickname_set(text)
            time.sleep(2)
            if GroupSet().disbandgroup.exists:
                filebasename = os.path.basename(__file__)
                Common().take_screenshot(filebasename, text)
                print('截图成功')
            else:
                print('未截图')
            logging.info("异常值")

    # @unittest.skip('跳过')
    def test_nickname_set_newline(self):
        text = '群昵称-' \
               '' \
               '换行'
        with allure.step('设置群昵称:换行'):
            GroupSet().nickname_set(text)
            time.sleep(2)
            if GroupSet().disbandgroup.exists:
                filebasename = os.path.basename(__file__)
                Common().take_screenshot(filebasename, text)
                print('截图成功')
            else:
                print('未截图')
            logging.info("换行")



if __name__ == "__main__":
    # unittest.main()
    # 创建测试套件
    # test_suite = unittest.TestSuite()
    # test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_groupNickName))
    #
    # # 运行测试套件
    # runner = unittest.TextTestRunner()
    # result = runner.run(test_suite)
    #
    # # 将结果写入文件
    # with open('test_report.txt', 'w') as f:
    #     f.write(str(result))
    # with open('test-results.xml', 'wb') as output:
    #     runner = XMLTestRunner(output)
    #     unittest.main(testRunner=runner)

    # pytest.main(["-vs", "--junitxml=test_report.xml"])
    # pytest.main(["-vs", '--return 实例25_批量生成PPT版荣誉证书','--html=report.html'])
    # pytest.main(["-vs", '--return 实例25_批量生成PPT版荣誉证书','—alluredir report'])
    pytest.main(['-s', '--alluredir=../allure-results', 'test_editgroup_nickname.py'])
    os.system('allure generate ../allure-results -o open ../allure-results/report/html --clean ')

