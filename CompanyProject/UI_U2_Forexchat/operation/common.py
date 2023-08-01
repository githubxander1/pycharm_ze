import time

from CompanyProject.UI_U2_Forexchat.operation.ChatWindows.GroupWindow import GroupWindow
from CompanyProject.UI_U2_Forexchat.operation.GroupSet.GroupManage.ManageGroup import ManageGroup
from CompanyProject.UI_U2_Forexchat.base.basePage import Base1, d
# from CompanyProject.UI_U2_Forexchat.operation.GroupSet.GroupSet import GroupSet
from CompanyProject.UI_U2_Forexchat.operation.op_Home import Home


class Common(Base1):
    back = d.xpath(
        '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[1]')
    # 输入框
    input_msg = d(text="输入消息...")
    # 转发
    selectfriend = d(description="选择好友")
    # select_friend1=d.xpath('//*[contains(@content-desc,"A1311-马保国")]/android.widget.ImageView[1]')
    select_friend1=d(description="A1311-马保国~的VBB回发废话话费发发广告病好爸爸gvv加")
    slelct_group1 = d(description="1313群主")
    selectgroup = d(description="选择群聊")
    select_multiple = d(description="多选")
    
    cancel = d(description="取消")
    confirm = d(description="确定")
    
    select_send = d.xpath('//*[contains(@content-desc,"发送")]')

    send_comfirm = d(description="发送")
    
    def click_confirm(self):
        self.confirm.click()

    def click_select_multiple(self):
        self.select_multiple.click()

    def click_cancel(self):
        self.cancel.click()

    def click_send_comfirm(self):
        self.send_comfirm.click()

    def click_back(self):
        self.back.click()

    def click_input_msg(self):
        self.input_msg.click()

    def click_selectfriend(self):
        self.selectfriend.click()

    def click_select_friend1(self):
        self.select_friend1.click()

    def click_selectgroup(self):
        self.selectgroup.click()

    def click_slelct_group1(self):
        while not d(description="1313群主").exists:
            d(scrollable=True).scroll.forward()
            time.sleep(1)
        self.slelct_group1.click()
        # while not d(description="管理群").exists():
        #     d(scrollable=True).scroll.forward()
        #     time.sleep(1)
        # d(description="管理群").click()

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


