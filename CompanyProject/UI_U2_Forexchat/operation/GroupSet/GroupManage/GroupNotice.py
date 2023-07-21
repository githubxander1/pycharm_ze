import time

from CompanyProject.UI_U2_Forexchat.operation.ChatWindows.GroupWindow import GroupWindow
from CompanyProject.UI_U2_Forexchat.operation.GroupSet.GroupManage.ManageGroup import ManageGroup
from CompanyProject.UI_U2_Forexchat.base.basePage import Base1, d
from CompanyProject.UI_U2_Forexchat.operation.op_Home import Home


class GroupNotice(Base1):
    groupNotice=d(description="公告")
    groupFile=d(description="文件")
    groupAlbum=d(description="相册")
    createNoticeImmediately=d(description="立即创建")
    createNotice=d(description="创建")
    editNotice=d.xpath('//android.widget.EditText')
    addPicture=d.xpath('//android.widget.ScrollView/android.view.View[1]')
    picture1=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]')
    publish=d(description="发布")

    usePop=d.xpath('//android.widget.ScrollView/android.widget.Switch[1]')
    setTop=d.xpath('//android.widget.ScrollView/android.widget.Switch[2]')


    forNewComers=d.xpath('//android.widget.ScrollView/android.widget.Switch[3]')
    cancel=d(description="取消")
    confirm=d(description="确定")

    # 更多
    noticeMore=d.xpath('//*[contains(@content-desc,"更新于")]/android.widget.ImageView[2]')
    modifynotice=d(description="修改群公告")
    more_setTop=d(description="设为置顶")
    more_cancelTop=d(description="取消置顶")
    delNotice=d(description="删除群公告")

    # def click_forNewComers(self):
    #     NewComers = d.xpath('//*[@content-desc[contains(., "新人必看")]]')
    #     while not NewComers.exists():
    #         d(scrollable=True).scroll.forward()
    #         time.sleep(1)
    #     self.forNewComers.click()
    # def click_forNewComers(self):
    #     while not d.xpath('//android.widget.ScrollView/android.widget.Switch[3]').exists:
    #         d(scrollable=True).scroll.forward()
    #         time.sleep(1)
    #     d.xpath('//android.widget.ScrollView/android.widget.Switch[3]').click()

    def click_forNewComers(self):
        while not self.forNewComers.exists:
            d(scrollable=True).scroll.forward()
            time.sleep(1)
        self.forNewComers.click()
    #     d(scrollable=True).scroll.to(d.xpath('//*[contains(@content-desc,"新人进群必看")]'))

    def click_confirm(self):
        self.confirm.click()

    def click_more_setTop(self):
        self.more_setTop.click()

    def click_more_cancelTop(self):
        self.more_cancelTop.click()

    def click_modifyNotice(self):
        self.modifynotice.click()

    def click_setTop(self):
        self.setTop.click()

    def click_delNotice(self):
        self.delNotice.click()

    def click_noticeMore(self):
        self.noticeMore.click()

    def click_usePop(self):
        self.usePop.click()

    def click_groupNotice(self):
        self.groupNotice.click()

    def click_groupFile(self):
        self.groupFile.click()

    def click_groupAlbum(self):
        self.groupAlbum.click()

    def click_createNoticeImmediately(self):
        self.createNoticeImmediately.click()

    def click_editNotice(self,text):
        self.editNotice.set_text(text)

    def click_addPicture(self):
        self.addPicture.click()

    def click_createNotice(self):
        self.createNotice.click()

    def click_publish(self):
        self.publish.click()
        # 确定替换
        if self.confirm.exists:
            self.confirm.click()
        # 取消替换
        # if self.cancel.exists:
        #     self.cancel.click()

    def choosePicture(self):
        self.picture1.click()

    # 创建纯文本群公告
    def create_gropNotice_text(self,text):
        Home().click_conversation()
        GroupWindow().click_groupSet()
        self.click_groupNotice()
        # 检查是否存在"立即创建"按钮
        time.sleep(2)
        if self.createNoticeImmediately().exists():
            self.click_createNoticeImmediately()
        else:
            self.click_createNotice()
        self.click_editNotice(str(text))
        self.click_publish()

    # 创建群公告_文本+图片
    def create_gropNotice_textandpicture(self,text):
        Home().click_conversation()
        GroupWindow().click_groupSet()
        # # 输出一些调试信息
        # print("当前界面:", d.info)
        # print("是否存在公告按钮:", d(description="公告").exists())
        self.click_groupNotice()
        # 检查是否存在"立即创建"按钮
        time.sleep(2)
        if self.createNoticeImmediately.exists():
            self.click_createNoticeImmediately()
        else:
            self.click_createNotice()
        self.click_editNotice(str(text))
        self.click_addPicture()
        self.choosePicture()
        self.click_forNewComers()
        self.click_publish()

    # 删除群公告
    def deleteNotice(self):
        Home().click_conversation()
        GroupWindow().click_groupSet()
        self.click_groupNotice()
        self.click_noticeMore()
        self.click_delNotice()
        self.click_confirm()

    # 修改群公告
    def modifyNotice(self):
        Home().click_conversation()
        GroupWindow().click_groupSet()
        self.click_groupNotice()
        self.click_noticeMore()
        self.click_modifyNotice()
        # self.click_confirm()

    # 设置置顶
    def setNoticeTop(self):
        Home().click_conversation()
        GroupWindow().click_groupSet()
        self.click_groupNotice()
        self.click_noticeMore()
        self.click_more_setTop()







if __name__ == '__main__':
    # GroupNotice().create_gropNotice_textandpicture('Hello,Notice:图+文-替12112122换')
    GroupNotice().deleteNotice()