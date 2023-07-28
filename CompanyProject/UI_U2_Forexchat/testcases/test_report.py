import os
import unittest
import webbrowser

import uiautomator2 as u2
import HTMLTestRunner

class TestUIAutomation(unittest.TestCase):
    # 测试方法省略，保持不变
    def test_1(self):
        pass

if __name__ == '__main__':
    # 创建测试套件
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestUIAutomation))

    # 指定测试报告生成路径
    # report_path = 'test_report.html'

    # 使用os.path模块来获取当前脚本文件的绝对路径，并将测试报告文件保存在与当前脚本文件相同的目录下
    report_dir = os.path.dirname(os.path.abspath(__file__))
    print(report_dir)
    report_path = os.path.join(report_dir, 'test_report.html')
    print(report_path)

    # 运行测试套件并生成测试报告
    with open(report_path, 'wb') as report_file:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=report_file,
            title='UI Automation Test Report',
            description='Test results:'
        )
        runner.run(suite)

        # 在浏览器中打开测试报告
        webbrowser.open(report_path)