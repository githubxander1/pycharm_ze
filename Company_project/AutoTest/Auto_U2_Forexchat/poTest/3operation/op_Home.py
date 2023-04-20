import time
import uiautomator2 as u2


from basePage import d
# from basePage import d,app
from basePage import Base1

class Home(Base1):
    conversation=d.xpath('//android.widget.ScrollView/android.view.View[2]')

    def openHome(self):
        d.app_start('com.bv.forexchat')

    # 点击进入会话聊天窗口
    def click_conversation(self):
        # d.app_start()
        try:
            d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]').click()
        except:
            d.xpath('//android.widget.ScrollView/android.view.View[2]').click()