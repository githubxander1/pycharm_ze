import unittest
from HTMLTestRunner import HTMLTestRunner
# 生成测试套件：
suite = unittest.TestLoader().discover("../", "test*.py")
# 以只写方式打开测试报告文件
f = open("test01.txt", "w", encoding="utf-8")
# 实例化HTMLTestRunner对象：
runner = unittest.TextTestRunner(stream=f, verbosity=2)
# 执行：
runner.run(suite)