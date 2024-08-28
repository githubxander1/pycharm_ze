import time

from CompanyProject.APP_Fastbull2.others.basePage1 import BasePage
from CompanyProject.APP_Fastbull2.operation.op_Home import Home


class GroupWindow(BasePage):
    back = {'xpath': '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.widget.ImageView[实例25_批量生成PPT版荣誉证书]'}
    input_msg = {'text': '输入消息...'}
    edittext={'xpath':'//android.widget.EditText'}
    emoji = {'xpath': '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.widget.ImageView[3]'}
    send = {'xpath': '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.widget.ImageView[5]'}
    expand = {'xpath': '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.widget.ImageView[4]'}
    group_set = {'xpath': '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[2]/android.widget.ImageView[3]'}
    # def click_conversation(self):
    #     Home().conversation.click()
    def click_group_set(self):
        self.click(self.group_set)

    def send_text(self,msg):
        Home().click_conversation()
        self.input_text(self.edittext, msg)
        self.click(self.send)

    # def send_emoji(self):
    #     self.click_conversation()
    #     self.click(self.emoji)
    #     self.d(scrollable=True).scroll.toEnd()
    #     self.d.xpath(
    #         '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[3]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.widget.ImageView[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.widget.ImageView[27]').click()
    #     self.send()
    #
    # def group_set(self):
    #     self.click(self.group_set)


if __name__ == '__main__':
    Home().launch_app()
    # msg = 'xinxi'
    time.sleep(10)
    # 点击会话
    Home().click_conversation()
    time.sleep(3)
    # 发送文本
    # GroupWindow().send_text('fdsf')
    # 点击群设置
    GroupWindow().click_group_set()
    # 关闭app
    time.sleep(3)
    Home().close_app()

