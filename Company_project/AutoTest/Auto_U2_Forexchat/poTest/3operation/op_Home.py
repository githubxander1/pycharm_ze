import time
import uiautomator2 as u2

d=u2.connect('127.0.0.1:21513')

# 点击进入会话聊天窗口
def session1():
    try:
        d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]').click()
    except:
        d.xpath('//android.widget.ScrollView/android.view.View[2]').click()