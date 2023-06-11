#
#pytest -help
# 可以输出用例更加详细的执行信息
# pytest -v
# 输出用例中的调式信息，比如print的打印信息等。
# pytest -s
# pytest -m
# 说明：用于标记测试并分组，执行特定的测试用例。
# pytest -k
# 说明：可以通过表达式运行指定的测试用例。
# 比如使用命令：pytest -k "test_demo01 or test_demo02"，就会指定运行test_demo01和test_demo02两条用例。
# pytest -x
# 说明：遇到错误或者用例不通过，则退出执行。
# 运行指定用例
# 模块、类、函数及方法之间用::进行分割。
# 比如想运行TestLogin类下的测试用例。
# 使用命令：pytest -v login/test_login_unittest.py::TestLogin