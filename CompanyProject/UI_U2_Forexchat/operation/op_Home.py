#
from CompanyProject.UI_U2_Forexchat.base.basePage1 import BasePage
#
class Home(BasePage):
    conversation1=('xpath',('//android.widget.ScrollView/android.view.View[2]'))
    conversation2=('xpath',('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]'))
#
#     # def openHome(self):
#     #     d.app_start('com.bv.forexchat')
#
#     # 点击进入会话聊天窗口
    def click_conversation(self):
        try:
            self.click(self.conversation1)
        except:
            self.click(self.conversation2)
#
#     # def swipe_left(self):
#     #     self.swipe_left(self.conversation)
#
#     # def click_conversation(self):
#     #     self.click(self.conversation1)
#
#     # def input_message(self, msg):
#     #     self.input(self.conversation1, msg)
#
Home().click_conversation()
# from CompanyProject.UI_U2_Forexchat.base.basePage1 import BaseTestClass
#
#
# class MyTestClass(BaseTestClass):
#     def test_example(self):
#         self.launch_app()
#
#         # 点击会话1
#         self.click_element(conversation1)
#
#         # 点击输入框输入字符
#         # self.input_text('com.bv.forexchat:id/input_box', 'Hello, World!')
#         #
#         # # 左滑会话2
#         # self.swipe_left('com.bv.forexchat:id/conversation_2')
#
#         self.close_app()
#
#
# test = MyTestClass()
# test.test_example()
