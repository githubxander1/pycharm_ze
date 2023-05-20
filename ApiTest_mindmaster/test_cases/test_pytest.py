# fixture是 pytest 用于将测试前后进行预备、清理工作的代码处理机制,相当于setup，teardown
# scope="session"可以实现多个.py跨文件使用一个session来完成多个用例。

# fixture里面有个scope参数可以控制fixture的作用范围，scope参数可以是session， module，class，function， 默认为function。
# session 会话级别：是多个文件调用一次，可以跨.py文件调用，每个.py文件就是module；
# module 模块级别：模块里所有的用例执行前执行一次module级别的fixture；
# class 类级别 ：每个类执行前都会执行一次class级别的fixture；@pytest.fixture(scope="class")
# function  函数级别：每个测试用例执行前都会执行一次function级别的fixture。

# @pytest.mark.usefixtures()在class前标记要fix哪个方法
# conftest.py作用域：放到项目的根目录下就可以全局调用了，如果放到某个package下，那就在改package内有效。
# conftest.py的fixture调用方式，无需导入，直接使用。
import pytest

from selenium import webdriver

# @pytest.fixture()
# def open_init():
#     d= webdriver.Edge()
#     d.get('https://userapi.edrawsoft.cn/api/user/login')
#     yield d
#     d.close()
#
#     @pytest.mark.usefixtures()
#     def test_login(open_init):
#         open_init.find_element_by_name()
#
#     @pytest.mark.skip()
#     def test_login(open_init):
#         open_init.find_element_by_name()

data=['小米','小明']
@pytest.mark.paremeter('name',data)
def test_demo(name):
    print('测试数据为{}'.format(name))

# 列表嵌套字典
data_1 = [
    {"username": "admin1", "password": "123456"},
    {"username": "admin2", "password": "12345678"},
]
@pytest.mark.paremeter('dataName',data_1)
def test_login(dataName):
    print('测试数据为用户名{}，密码{}'.format(dataName["username"],dataName['password']))

# 列表嵌套列表
data_2 = [
    ["admin1", "123456"],
    ["admin2", "12345678"],
]
@pytest.mark.paremeter('arg1,arg2',data_2)
def test_login2(arg1, arg2):
    print('测试数据为用户名{}，密码{}'.format(arg1,arg2))

# 列表嵌套元组
data_3 = [
    ("admin1", "123456"),
    ("admin2", "12345678"),
]
@pytest.mark.parameterize('arg1,arg2',data_3)
def test_login3(arg1,arg2):
    print('测试数据为用户名{}，密码{}'.format(arg1,arg2))

if __name__ == '__main__':
    pytest.main()
    test_demo()