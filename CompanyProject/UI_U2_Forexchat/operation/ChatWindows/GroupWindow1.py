from CompanyProject.UI_U2_Forexchat.base.basePage1 import BasePage
from CompanyProject.UI_U2_Forexchat.operation.op_Home import Home


class GroupWindow(BasePage):
    back = ('xpath', '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[1]')
    input_msg = ('text', '输入消息...')
    emoji = ('xpath', '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[3]')
    send = ('xpath', '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[5]')
    expand = ('xpath', '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[4]')
    group_set = ('xpath', '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.widget.ImageView[3]')

    # def click_conversation(self):
    #     Home().conversation.click()

    def send_text(self, msg):
        Home().click_conversation()
        self.input(self.input_msg, msg)
        self.click(self.send)

    # def send_emoji(self):
    #     self.click_conversation()
    #     self.click(self.emoji)
    #     self.d(scrollable=True).scroll.toEnd()
    #     self.d.xpath(
    #         '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[3]/android.view.View[1]/android.widget.ImageView[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[27]').click()
    #     self.send()
    #
    # def group_set(self):
    #     self.click(self.group_set)


if __name__ == '__main__':
    msg = 'xinxi'
    Home().click_conversation()
    GroupWindow().send_text(msg)
