import unittest

# testsuite
# 套件对象.addTest(unittest.makeSuite(测试类名))
# 实例化套件对象
# from ApiTest_mindmaster.test_cases.login_test_ddt import TestLogin
# from ApiTest_mindmaster.test_cases.test_newfold import TestNewFold
#
# suite=unittest.TestSuite()
#
# # 套件对象添加测试用例
# suite.addTest(unittest.makeSuite(TestLogin))
# suite.addTest(unittest.makeSuite(TestNewFold))
# # suite.addTests(unittest.makeSuite(TestLogin,TestNewFold))
#
# # 实例化执行对象，执行测试套件
# runner=unittest.TextTestRunner()
# # 执行
# runner.run(suite)


# testloader
# 作用和testSuite是一样的，也是用来组装测试用例的。
# 他可以指定目录和文件加载执行，适用于测试用例比较多的场景。
# 代码总结：
# unittest.TestLoader().discover('用例所在目录','用例代码名称*.py')
# 实例化套件对象
suite=unittest.TestLoader().discover("../", 'flashing_icon*.py')
# 实例化执行对象，执行套件
runner=unittest.TextTestRunner()
runner.run(suite)

# TestSuite
# 优点：灵活，方便控制加载要执行的测试用例。
# 缺点：需要手动一个一个添加测试用例，比较繁琐。
# TestLoader
# 优点：可以自动搜索加载满足条件的测试用例
# 缺点：不够灵活，不方便具体控制某个要执行的测试用例。