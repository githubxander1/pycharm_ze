import time
# https://mp.weixin.qq.com/s?__biz=MzI5ODU1MzkwMA==&mid=2247484841&idx=1&sn=6384ce1c137dce7882985b60a49d90fe#wechat_redirect
# 自定义测试用例的预置条件，实现数据共享，不需要import就能自动找到一些配置
import pytest
from seleniumwire import webdriver

from CompanyProject.Fastbull.UI_Fastbull.page.login_page import Login

@pytest.fixture(scope='session')
def driver():
    d = webdriver.Chrome()
    # d.get('')
    return d
@pytest.fixture(scope='session')
def login():
    # d = webdriver.Chrome()
    login = Login(driver())
    login.login('7@qq.com', 'a1234567')
    # return d