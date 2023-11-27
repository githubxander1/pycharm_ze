import pytest
from time import sleep

import uiautomator2 as u2
#
# d=u2.connect('127.0.0.1:21503')#模拟器
d=u2.connect()#模拟器
# d = u2.connect_adb_wifi('192.168.5.220:5555')#手机
d.app_start('com.app.ct4')
d.implicitly_wait(10)

optional=d(text="自选")
visitorAvatar=d(resourceId="com.app.ct4:id/visitorAvatar")
btn_login=d(resourceId="com.app.ct4:id/btn_action")
nanigation_mine=d(resourceId="com.app.ct4:id/navigation_mine")
navigation_business=d(resourceId="com.app.ct4:id/navigation_business")
email=d(resourceId="com.app.ct4:id/tv_email")
input_email=d(resourceId="com.app.ct4:id/edit_input", text="请完整输入该账户绑定的邮箱地址：")
input_password=d(resourceId="com.app.ct4:id/edit_input", text="请输入登录密码")
privacy=d(resourceId="com.app.ct4:id/iv_policy")
login=d(resourceId="com.app.ct4:id/tv_login")

dropdown=d(resourceId="com.miui.securityinputmethod:id/dropdown")

def login_email():
        sleep(2)
        nanigation_mine.click()
        if visitorAvatar.exists():
            sleep(2)
            visitorAvatar.click()#点击登录
            email.click()#切换到邮箱
            input_email.send_keys('ct2@linshiyou.com')
            input_password.send_keys('a1234567')
            # dropdown.click()
            if dropdown.exists():
                d.press('back')
            privacy.click()#同意隐私协议
            login.click()#登录
            sleep(2)
            nanigation_mine.click()
        else:
            pass

def close_app():
    sleep(3)
    d.app_stop('com.app.ct4')

if __name__ == '__main__':
    # pytest.main(["-s", "common.py"])
    login_email()