#
import time

from CompanyProject.UI_U2_Forexchat.base.basePage import Base1,d
from CompanyProject.UI_U2_Forexchat.base.basePage1 import BasePage

class Home(BasePage):
    edittext=d.xpath('//android.widget.EditText')
    search=d.xpath('//android.widget.ScrollView/android.widget.ImageView[1]')
    conversation1=d.xpath('//android.widget.ScrollView/android.view.View[3]')
    # conversation2=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]')
    cancel=d(description="取消")

#     # 点击进入会话聊天窗口
    def click_conversation(self):
        self.conversation1.click()
#     def click_conversation(self):
#         try:
#             self.click(self.conversation1)
#         except:
#             self.click(self.conversation2)

    def click_search(self):
        self.click(self.search)

    def click_cancel(self):
        self.click(self.cancel)

    def send_text(self,text):
        self.input_text(self.edittext,text)

    def swipe_left_conversation(self):
        self.swipe_left(self.conversation1)
#
#     # def click_conversation(self):
#     #     self.click(self.conversation1)
#
#     # def input_message(self, msg):
#     #     self.input(self.conversation1, msg)
#
if __name__ == '__main__':
    Home().click_conversation()
