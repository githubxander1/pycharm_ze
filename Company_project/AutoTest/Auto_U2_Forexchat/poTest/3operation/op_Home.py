import time
import uiautomator2 as u2


from basePage import d
from basePage import d,app

conversation=d.xpath('//android.widget.ScrollView/android.view.View[2]')

def openHome():
    d.app_start(app)

# 点击进入会话聊天窗口
def click_conversation():
    d.app_start(app)
    try:
        d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]').click()
    except:
        d.xpath('//android.widget.ScrollView/android.view.View[2]').click()