import time
import uiautomator2 as u2

d=u2.connect('127.0.0.1:21513')

def manage_groups():
    # 进入会话
    session1()
    # 点击群设置
    groupSet()
    time.sleep(3)
    # 点击管理群
    d(scrollable=True).scroll.to(description="管理群")
    d(description="管理群").click()