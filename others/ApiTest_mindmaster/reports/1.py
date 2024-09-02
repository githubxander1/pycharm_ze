import unittest
from HTMLTestRunner import HTMLTestRunner

# 导入测试模块

# 创建测试套件

suite = unittest.TestSuite()

# 将测试用例添加到测试套件中
# suite.addTest(TestLogin('test_login_success'))
unittest.TestLoader().discover("../", "flashing_icon*.py")
# suite.addTest(TestLogin('test_login_fail'))

# 定义报告存放路径和文件名
report_path = '/'
report_name = '1login_report.html'

# 创建 HTMLTestRunner 实例对象
with open('{}/{}'.format(report_path, report_name), 'wb') as fp:
    runner = HTMLTestRunner(title='测试标题', description='描述本次测试的大概内容', stream=fp)
    # 运行测试用例
    runner.run(suite)
