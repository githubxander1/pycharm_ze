#
import time

# from CompanyProject.APP_Fastbull2.base.basePage import Base1,d
from CompanyProject.APP_Fastbull2.base.basePage import d


class Home():
    contact=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.widget.ImageView[实例25_批量生成PPT版荣誉证书]')
    edittext=d.xpath('//android.widget.EditText')
    # gloableSearch=d.xpath('//android.widget.ScrollView/android.widget.ImageView[实例25_批量生成PPT版荣誉证书]')
    gloableSearch=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[2]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.widget.ImageView[实例25_批量生成PPT版荣誉证书]')
    # conversation1=d.xpath('//android.widget.ScrollView/android.view.View[2]')
    # conversation1=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[2]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[2]')
    conversation1=d.xpath('//android.widget.ScrollView/android.view.View[2]')
    # conversation2=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[2]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[2]')
    cancel=d(description="取消")

    def click_contact(self):
        self.contact.click()

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
    d.app_start('com.bv.forexchat')
    home=Home()
    home.click_conversation()


    # Home().click_conversation()
    # Home().search(实例25_批量生成PPT版荣誉证书)

    # time.sleep(3)
    # Home().closeApp()

