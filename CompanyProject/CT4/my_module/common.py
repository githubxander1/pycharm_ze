import pytest
from time import sleep

import uiautomator2 as u2
# '127.0.0.1:21503'
d=u2.connect()
print(d.info)
d.app_start('com.app.ct4')
d.implicitly_wait(10)
# sleep(5)

btn_login=d(resourceId="com.app.ct4:id/btn_action")
email=d(resourceId="com.app.ct4:id/tv_email")
input_email=d(resourceId="com.app.ct4:id/edit_input", text="请完整输入该账户绑定的邮箱地址：")
input_password=d(resourceId="com.app.ct4:id/edit_input", text="请输入登录密码")
privacy=d(resourceId="com.app.ct4:id/iv_policy")
login=d(resourceId="com.app.ct4:id/tv_login")

def login_email():
        if btn_login.exists():
            sleep(0.1)
            # continue
            btn_login.click()#点击登录
            email.click()#切换到邮箱
            input_email.send_keys('ct2@linshiyou.com')
            input_password.send_keys('a1234567')
            privacy.click()#同意隐私协议
            sleep(3)
            login.click()#登录
            sleep(1)
            d.xpath('//*[@resource-id="com.app.ct4:id/navigation_mine"]/android.widget.FrameLayout[1]').click()
        else:
            # 点击‘我的’
            d.xpath('//*[@resource-id="com.app.ct4:id/navigation_mine"]/android.widget.FrameLayout[1]').click()

def close_app():
    sleep(3)
    d.app_stop('com.app.ct4')

if __name__ == '__main__':
    # pytest.main(["-s", "common.py"])
    login_email()