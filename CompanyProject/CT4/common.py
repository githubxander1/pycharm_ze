from time import sleep

import uiautomator2 as u2

d=u2.connect('127.0.0.1:21503')
print(d.info)
d.app_start('com.app.ct4')
d.implicitly_wait(10)

btn_login=d(resourceId="com.app.ct4:id/btn_action")

def login_email():
    if btn_login.exists:
        d(resourceId="com.app.ct4:id/btn_action").click()#点击登录
        d(resourceId="com.app.ct4:id/tv_email").click()
        d(resourceId="com.app.ct4:id/edit_input", text="请完整输入该账户绑定的邮箱地址：").send_keys('ct2@linshiyou.com')
        d(resourceId="com.app.ct4:id/edit_input", text="请输入登录密码").send_keys('a1234567')
        d(resourceId="com.app.ct4:id/iv_policy").click()
        d(resourceId="com.app.ct4:id/tv_login").click()
        # login_email('ct2@linshiyou.com','a1234567')
    else:
        # TODO: Add implementation
        d.xpath('//*[@resource-id="com.app.ct4:id/navigation_mine"]/android.widget.FrameLayout[1]').click()
        # pass
# login_email('ct2@linshiyou.com','a1234567')

def close_app():
    sleep(3)
    d.app_stop('com.app.ct4')