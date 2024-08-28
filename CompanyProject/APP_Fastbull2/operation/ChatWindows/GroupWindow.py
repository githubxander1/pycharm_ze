import time

from CompanyProject.APP_Fastbull2.base.basePage import Base1,d
from CompanyProject.APP_Fastbull2.operation.op_Home import Home


class GroupWindow(Base1):
    # 返回首页
    back=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.widget.ImageView[实例25_批量生成PPT版荣誉证书]')
    # 输入框
    input_msg=d.xpath('//android.widget.EditText')
    # 表情
    # emoji=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.widget.ImageView[3]')
    emoji=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.widget.ImageView[3]')
    emoji1=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[5]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.widget.ImageView[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[2]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.widget.ImageView[11]')
    # 发送
    send=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.widget.ImageView[5]')
    send_text=d.xpath('//android.widget.FrameLayout[2]/android.widget.LinearLayout[实例25_批量生成PPT版荣誉证书]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.widget.ImageView[4]')
    # 扩展
    expand=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.widget.ImageView[4]')
    # 群设置
    groupSet=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[3]/android.widget.ImageView[3]')
    # 相册
    amble=d(description="相册")
    # 名片
    namecard=d(description="名片")
    # 文件
    file=d(description="文件")

    # 转发
    selectfriend=d(description="选择好友")
    select_friend1=d.xpath('//*[contains(@content-desc,"A1311-马保国")]/android.widget.ImageView[实例25_批量生成PPT版荣誉证书]')
    # select_friend1=d(description="A1311-马保国~的VBB回发废话话费发发广告病好爸爸gvv加")
    slelct_group1=d(description="1313群主")
    selectgroup=d(description="选择群聊")
    select_multiple=d(description="多选")
    cancel=d(description="取消")
    select_send=d.xpath('//*[contains(@content-desc,"发送")]')

    send_cancel=d(description="取消")
    send_comfirm=d(description="发送")

    def click_select_multiple(self):
        self.select_multiple.click()

    def click_send_cancel(self):
        self.send_cancel.click()

    def click_send_comfirm(self):
        self.send_comfirm.click()

    def click_back(self):
        self.back.click()
    def click_send_text(self):
        # self.send_text.click()
        self.d.click(0.92, 0.941)

    def click_input_msg(self):
        self.input_msg.click()

    def input_input_msg(self,text):
        self.input_msg.set_text(text)

    def click_selectfriend(self):
        self.selectfriend.click()

    def click_select_friend1(self):
        self.select_friend1.click()

    def click_selectgroup(self):
        self.selectgroup.click()

    def click_slelct_group1(self):
        self.slelct_group1.click()

    def click_cancel(self):
        self.cancel.click()

    def click_select_send(self):
        self.select_send.click()

    def forward_tofriendandgroup(self):
        self.click_select_multiple()
        self.click_selectfriend()
        # self.click_select_friend1()
        time.sleep(2)
        self.d.click(0.396, 0.281)
        self.click_back()
        self.click_selectgroup()
        self.click_slelct_group1()
        self.click_select_send()
        self.click_send_comfirm()


    # def send_text(self,msg):
    #     # 点击输入框
    #     GroupWindow().input_msg.send_keys(msg)
    #     # 点击发送按钮
    #     d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.widget.ImageView[6]').click()
        # send.click()
    #
    # # 发送emoji表情
    # def send_emoji(self):
    #     GroupWindow().click_conversation()
    #     # 点击表情按钮
    #     GroupWindow().emoji.click()
    #     d(scrollable=True).scroll.toEnd()
    #     d.xpath(
    #         '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[3]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.widget.ImageView[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.widget.ImageView[27]').click()
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

    def sendText(self,text):
        self.click_input_msg()
        time.sleep(2)
        self.input_input_msg(text)
        time.sleep(4)
        self.click_send_text()

    def sendEmoji(self):
        self.click_emoji()
        time.sleep(3)
        self.chooseEmoji()
        time.sleep(2)
        self.click_send()

if __name__ == '__main__':
    msg='xinxi'
    Base1().startApp()
    time.sleep(3)
    Home().click_conversation()
    GroupWindow().sendText('发送文字')
    # GroupWindow().click_groupSet()
    time.sleep(5)
    # Home().closeApp()