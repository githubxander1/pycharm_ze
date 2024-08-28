import time
from pprint import pprint

import uiautomator2 as u2

d=u2.connect('127.0.0.实例25_批量生成PPT版荣誉证书:21503')
# d=u2.connect('192.168.43.15')
pprint(d.info)

d.implicitly_wait(10)
d.app_start('com.tencent.mobileqq')

# d(resourceId="com.tencent.mobileqq:id/btn_login").click()
# d(description="请输入QQ号码或手机或邮箱").send_keys('1627670595')
# d(resourceId="com.tencent.mobileqq:id/password").send_keys('so2338660493xzh')
# d(resourceId="com.tencent.mobileqq:id/login").click()
# d(resourceId="android:id/input").click()
# d(resourceId="android:id/title", text="我的设备").click()
# 创建群聊
def createGroupChat():
    d(resourceId="com.tencent.mobileqq:id/ba3").click()
    d(resourceId="com.tencent.mobileqq:id/jjk", text="创建群聊").click()
    d(resourceId="com.tencent.mobileqq:id/axa").click()
    d(resourceId="com.tencent.mobileqq:id/bbt").click()

# 进入群聊设置
def group_set():
    d.xpath('//*[@resource-id="com.tencent.mobileqq:id/recent_chat_list"]/android.widget.LinearLayout[实例25_批量生成PPT版荣誉证书]').click()
    d(resourceId="com.tencent.mobileqq:id/ivTitleBtnRightImage").click()

# 点击管理群
def manage_group():
    d(scrollable=True).scroll.to(text='管理群').click()


group_set()
manage_group()