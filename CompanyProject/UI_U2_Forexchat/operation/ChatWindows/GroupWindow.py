import time

from CompanyProject.UI_U2_Forexchat.base.basePage import Base1,d
from CompanyProject.UI_U2_Forexchat.operation.op_Home import Home


class GroupWindow(Base1):
    # 返回首页
    back=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[1]')
    # 输入框
    input_msg=d(text="输入消息...")
    # 表情
    # emoji=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[3]')
    emoji=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[4]')
    emoji1=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[5]/android.view.View[1]/android.widget.ImageView[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[11]')
    # 发送
    send=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[5]')
    # 扩展
    expand=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[4]')
    # 群设置
    groupSet=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[3]')
    # 相册
    amble=d(description="相册")
    # 名片
    namecard=d(description="名片")
    # 文件
    file=d(description="文件")
    # d_text(msg):
    #     GroupWindow().conversation.
    #     # 点击输入框
    #     GroupWindow().input_msg.send_keys(msg)
    #     # 点击发送按钮
    #     d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[6]').click()
    #     # send.click()
    #
    # # 发送emoji表情
    # def send_emoji(self):
    #     GroupWindow().click_conversation()
    #     # 点击表情按钮
    #     GroupWindow().emoji.click()
    #     d(scrollable=True).scroll.toEnd()
    #     d.xpath(
    #         '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[3]/android.view.View[1]/android.widget.ImageView[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[27]').click()
    #     # 点击发送
    #     GroupWindow().send()
    def click_send(self):
        self.send.click()
    # 点击拓展
    def click_expand(self):
        self.expand.click()

    # 点击相册
    def click_amble(self):
        self.amble.click()

    # 点击名片
    def click_namecard(self):
        self.namecard.click()

    # 点击文件
    def click_file(self):
        self.file.click()

    # 点击表情
    def click_emoji(self):
        self.emoji.click()

    # 选中表情
    def chooseEmoji(self):
        self.emoji1.click()

    # 群设置
    def click_groupSet(self):
        # Home().click_conversation()
        self.groupSet.click()

    def sendEmoji(self):
        Home().click_conversation()
        self.click_emoji()
        time.sleep(3)
        self.chooseEmoji()
        time.sleep(2)
        self.click_send()

if __name__ == '__main__':
    msg='xinxi'
    GroupWindow().sendEmoji()
    time.sleep(5)
    Home().closeApp()