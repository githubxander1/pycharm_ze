from CompanyProject.UI_U2_Forexchat.base.basePage import Base1, d
from CompanyProject.UI_U2_Forexchat.operation.op_Home import Home


class GroupWindow(Base1):
    # 返回首页
    back=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[1]')
    # 输入框
    input_msg=d(text="输入消息...")
    # 表情
    emoji=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[3]')
    # 发送
    send=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[5]')
    # 扩展
    expand=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[4]')
    # 群设置
    group_set=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.widget.ImageView[3]')
    # 点击进入会话聊天窗口
    def click_conversation(self):
        # Home().openHome()
        Home().conversation.click()

    def send_text(msg):
        GroupWindow().click_conversation()
        # 点击输入框
        GroupWindow().input_msg.send_keys(msg)
        # 点击发送按钮
        d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[6]').click()
        # send.click()

    # 发送emoji表情
    def send_emoji(self):
        GroupWindow().click_conversation()
        # 点击表情按钮
        GroupWindow().emoji.click()
        d(scrollable=True).scroll.toEnd()
        d.xpath(
            '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[3]/android.view.View[1]/android.widget.ImageView[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[27]').click()
        # 点击发送
        GroupWindow().send()

        # 进入群设置
    def groupSet(self):
        GroupWindow().group_set.click()

if __name__ == '__main__':
    msg='xinxi'
    GroupWindow().send_text()