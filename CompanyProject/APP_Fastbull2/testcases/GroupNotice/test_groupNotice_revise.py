import unittest
import time

import logging

import HTMLTestRunner

from CompanyProject.APP_Fastbull2.operation.ChatWindows.GroupWindow import GroupWindow
from CompanyProject.APP_Fastbull2.base.basePage import Base1
from CompanyProject.APP_Fastbull2.operation.GroupSet.GroupManage.GroupNotice.GroupNotice import GroupNotice
from CompanyProject.APP_Fastbull2.operation.GroupSet.GroupSet import GroupSet
from CompanyProject.APP_Fastbull2.operation.op_Home import Home
# 设置日志格式


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class Test_GroupNotice(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Base1().startApp()
        time.sleep(3)
        Home().click_conversation()
        GroupWindow().click_groupSet()
        GroupNotice().closenoticepop()
        time.sleep(1)
        GroupSet().click_groupNotice()
        # 点击创建
        GroupNotice().click_create()

    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        # Base1().closeApp()

    def setUp(self):
        # 等待3秒
        time.sleep(3)

    def tearDown(self):
        pass

    input_box = GroupNotice().editNotice  # 找到输入框元素
    publish_button = GroupNotice().publish  # 找到发布按钮元素

    def test_editgrouintroduction1_textandpicture(self):
        text = '群公告-第一次'
        GroupNotice().create_gropNotice_textandpicture(text)
        logging.info("1正常用例")

if __name__ == '__main__':
    loader=unittest.TestLoader()
    suite=loader.loadTestsFromTestCase(Test_GroupNotice)

    # runner=unittest.TextTestRunner()
    # runner.run(suite)

    # 创建测试套件
    # suite = unittest.TestSuite()
    # suite.addTest(unittest.makeSuite(TestUIAutomation))

    # 指定测试报告生成路径
    report_path = 'test_report.html'

    # 运行测试套件并生成测试报告
    with open(report_path, 'wb') as report_file:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=report_file,
            title='UI Automation Test Report',
            description='Test results:'
        )
        runner.run(suite)