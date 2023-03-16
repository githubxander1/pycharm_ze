import time

import uiautomator2 as u2

# 连接模拟器或手机
d=u2.connect('127.0.0.1:21513')
# 获取设备基本信息
# print(d.info)
d.implicitly_wait(5)
d.app_start('com.sy.fxchat')
# 启动app
# def appStart():
#     # 判断是否需要登录
#     if d(text="登录汇聊").exists:
#         d.implicitly_wait(5)
#         d(description="​邮​箱​/​F​X​I​D​/​手​机​号​").click()
#         d(text="邮箱/FXID").send_keys('12i_ynhx5b51i2@dingtalk.com')
#         d.implicitly_wait(3)
#         time.sleep(3)
#         d(text="密码").set_text('a1234567')
#         next1=d.xpath('//*[@content-desc="登录"]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[4]')
#         next1.click()
#     else:
#         pass
# 点击聊天室
# d.xpath('//android.widget.ScrollView/android.view.View[1]').click()
# 发送文本
def send_text():
    # 点击输入框
    time.sleep(2)
    d(text="输入消息...").send_keys('dsfds')
    time.sleep(3)
    # 点击发送按钮
    d.xpath(
        '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[3]').click()

# 发送emoji表情
# def send_emoji():
#     # 点击表情按钮
#     time.sleep(2)
#     d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[3]').click()
#     scrollTo=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[3]/android.view.View[1]/android.widget.ImageView[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[27]')
#     # d(scrollable=True).scroll.to(scrollTo)
#     d(scrollable=True).scroll.toEnd()
#     d.xpath(
#         '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[3]/android.view.View[1]/android.widget.ImageView[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[27]').click()
#     # 点击发送
#     d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[5]').click()

# d.app_stop('com.sy.fxchat')
def mark_read():
    # 先定位元素，再滑动
    hh=d.xpath('//android.widget.ScrollView/android.view.View[2]')
    # hh.swipe('left')
    hh.swipe('left')
    time.sleep(2)
    d.xpath('//android.widget.ScrollView/android.view.View[2]/android.widget.ImageView[1]').click()
    # d.xpath('//android.widget.ScrollView/android.view.View[3]/android.widget.ImageView[1]')

# 点击进入会话聊天窗口
def session():
    d.xpath('//android.widget.ScrollView/android.view.View[2]').click()

    # 进入群设置
def groupSet():
    d.xpath(
        '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.widget.ImageView[3]').click()

def Manage_groups():
    d.xpath('//android.widget.ScrollView/android.view.View[2]').click()
    time.sleep(5)
    set=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[3]')
    set.click()
    time.sleep(3)
    d(scrollable=True).scroll.to(description="管理群")
    d(description="管理群").click()

if __name__ == '__main__':
    # appStart()
    Manage_groups()
    # mark_read()
    # send_text()
    # time.sleep(3)
    # send_emoji()
    # time.sleep(4)
    # d.app_stop('com.sy.fxchat')


