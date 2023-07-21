#
import time

from CompanyProject.UI_U2_Forexchat.base.basePage import Base1,d
from CompanyProject.UI_U2_Forexchat.base.basePage1 import BasePage

class Home(Base1):
    edittext=d.xpath('//android.widget.EditText')
    gloableSearch=d.xpath('//android.widget.ScrollView/android.widget.ImageView[1]')
    conversation1=d.xpath('//android.widget.ScrollView/android.view.View[2]')
    # conversation2=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]')
    cancel=d(description="取消")

#     # 点击进入会话聊天窗口
    def click_conversation(self):
        time.sleep(6)
        self.conversation1.click()

    def click_golableSearch(self):
        self.gloableSearch.click()
        # self.click(self.gloableSearch)

    def click_cancel(self):
        self.cancel.click()

    def send_text(self,text):
        self.edittext.set_text(str(text))

    # 搜索
    def search(self,text):
        self.click_golableSearch()
        self.send_text(text)

    # def swipe_left_conversation(self):
    #     self.swipe_left(self.conversation1)

if __name__ == '__main__':
    # Home().launch_app()
    # time.sleep(6)
    # Home().click_conversation()
    Home().search(1)

    time.sleep(3)
    Home().closeApp()

