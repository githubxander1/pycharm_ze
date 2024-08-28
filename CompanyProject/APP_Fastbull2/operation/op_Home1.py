#
import time
from CompanyProject.APP_Fastbull2.others.basePage1 import BasePage

class Home(BasePage):
    edittext={'xpath':'//android.widget.EditText'}
    search={'xpath':'//android.widget.ScrollView/android.widget.ImageView[实例25_批量生成PPT版荣誉证书]'}
    conversation1={'xpath':'//android.widget.ScrollView/android.view.View[3]'}
    # conversation2={'xpath':'//*[@resource-id="android:id/content"]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[2]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[2]'}
    cancel={'description':"取消"}

#     # 点击进入会话聊天窗口
    def click_conversation(self):
        self.click(self.conversation1)
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
    Home().launch_app()
    # 搜索
    # Home().click_search()
    # Home().send_text(实例25_批量生成PPT版荣誉证书)
    # 点击会话
    time.sleep(10)
    Home().click_conversation()
    # 左滑会话列表
    # Home().swipe_left_conversation()
    # time.sleep(5)
    # 关闭app
    time.sleep(3)
    Home().close_app()
