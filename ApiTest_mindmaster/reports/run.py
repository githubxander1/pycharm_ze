import HTMLTestRunner
import unittest


# suite = unittest.TestSuite()
# 创建一个测试套对象
suite = unittest.TestLoader().discover("../", "flashing_icon*.py")
# 以只写方式打开测试报告文件
f = open("test01.txt", "w", encoding="utf-8")
# 实例化HTMLTestRunner对象：
runner = HTMLTestRunner.HTMLTestRunner(stream=f, verbosity=2)
# 执行：
runner.run(suite)
# # 将登陆的测试用例添加到测试套中
Report_file = u"H:\\pydj\\Lmd_auto_test\\Report\\Result.html"
# # 设置测试报告输出的位置及文件名
Rf = file(Report_file,'wb')
# # 使用 python 标准库 file 打开测试报告文件，wb 是以二进制写的模式
# # 打开。
Case_run=HTMLTestRunner.HTMLTestRunner(stream=Rf,title='flashing_icon')
# # 登陆测试',description=u"测试报告输出")
# # 创建一个 HTMLTestRunner 的对象，并且将上面打开的用于输出测试报
# # 告的对象传入，title 是 html 报告页面的 title，description 对测试
# # 报告的描述
Case_run.run(suite)
# 开始运行测试套