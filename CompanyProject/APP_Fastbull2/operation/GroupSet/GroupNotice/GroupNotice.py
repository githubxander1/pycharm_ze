import time

from CompanyProject.APP_Fastbull2.operation.ChatWindows.GroupWindow import GroupWindow
from CompanyProject.APP_Fastbull2.operation.GroupSet.GroupManage.ManageGroup import ManageGroup
from CompanyProject.APP_Fastbull2.base.basePage import Base1, d
from CompanyProject.APP_Fastbull2.operation.GroupSet.GroupSet import GroupSet
from CompanyProject.APP_Fastbull2.operation.op_Home import Home


class GroupNotice(Base1):
    groupNotice=d(description="公告")
    groupFile=d(description="文件")
    groupAlbum=d(description="相册")

    # 创建群公告
    createNoticeImmediately=d(description="立即创建")
    createNotice=d(description="创建")
    editNotice=d.xpath('//android.widget.EditText')
    addPicture=d.xpath('//android.widget.ScrollView/android.view.View[实例25_批量生成PPT版荣誉证书]')
    # picture1=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[2]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]')
    picture1=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[2]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]')
    picture_gif=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[2]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]')

    publish=d(description="发布")
    confirm=d(description="确定")

    usePop=d.xpath('//android.widget.ScrollView/android.widget.Switch[实例25_批量生成PPT版荣誉证书]')
    setTop=d.xpath('//android.widget.ScrollView/android.widget.Switch[2]')
    forNewComers=d.xpath('//android.widget.ScrollView/android.widget.Switch[3]')

    viewdetails=d(description="查看详情")
    close=d.xpath('//*[contains(@content-desc,"群公告")]/android.widget.ImageView[2]')

    def click_viewdetails(self):
        self.viewdetails.click()

    def click_close(self):
        self.close.click()

    def closenoticepop(self):
        if self.viewdetails.exists:
            self.click_close()



    def click_usePop(self):
        self.usePop.click()

    def click_setTop(self):
        self.setTop.click()

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
    #         time.sleep(实例25_批量生成PPT版荣誉证书)
    #     self.forNewComers.click()
    # def click_forNewComers(self):
    #     while not d.xpath('//android.widget.ScrollView/android.widget.Switch[3]').exists:
    #         d(scrollable=True).scroll.forward()
    #         time.sleep(实例25_批量生成PPT版荣誉证书)
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

    def click_delNotice(self):
        self.delNotice.click()

    def click_noticeMore(self):
        self.noticeMore.click()

    def click_groupNotice(self):
        self.groupNotice.click()

    def click_groupFile(self):
        self.groupFile.click()

    def click_groupAlbum(self):
        self.groupAlbum.click()

    def click_createNoticeImmediately(self):
        self.createNoticeImmediately.click()

    def input_editNotice(self,text):
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

    def click_create(self):
        time.sleep(2)
        if self.createNoticeImmediately.exists:
            self.click_createNoticeImmediately()
        else:
            self.click_createNotice()

    # 创建纯文本群公告并使用弹窗
    def create_gropNotice_text_popup(self,text):
        self.closenoticepop()
        # self.click_groupNotice()
        time.sleep(2)
        self.click_create()
        self.input_editNotice(str(text))
        self.click_usePop()
        self.click_publish()

    # 创建纯文本群公告并设置置顶
    def create_gropNotice_text_top(self,text):
        self.closenoticepop()
        # self.click_groupNotice()
        time.sleep(2)
        self.click_create()
        self.input_editNotice(str(text))
        self.click_setTop()
        self.click_publish()

    # 新人必看
    def create_gropNotice_text_fornewcommer(self,text):
        self.closenoticepop()
        # self.click_groupNotice()
        time.sleep(2)
        self.click_create()
        self.input_editNotice(str(text))
        self.click_forNewComers()
        self.click_publish()

    # 创建群公告_文本+图片
    def create_gropNotice_textandpicture(self,text):
        self.closenoticepop()
        # self.click_groupNotice()
        self.click_create()
        self.input_editNotice(str(text))
        self.click_addPicture()
        self.choosePicture()
        # # 设置新人必看
        # self.click_forNewComers()
        self.click_publish()

    # 删除群公告
    def deleteNotice(self):
        # Home().click_conversation()
        # GroupWindow().click_groupSet()
        # self.click_groupNotice()
        self.click_noticeMore()
        self.click_delNotice()
        self.click_confirm()

    # 修改群公告
    def modifyNotice(self,text):
        self.click_noticeMore()
        self.click_modifyNotice()
        self.input_editNotice(text)
        self.click_publish()

    # 置顶群公告
    def topNotice(self):
        self.click_noticeMore()
        self.click_more_setTop()







if __name__ == '__main__':
    # GroupNotice().create_gropNotice_textandpicture('Hello,Notice:图+文-替12112122换')
    Base1().startApp()
    time.sleep(3)
    Home().click_conversation()
    GroupWindow().click_groupSet()
    time.sleep(2)
    GroupSet().click_groupNotice()
    GroupNotice().create_gropNotice_text_top('dfsgfdsg ')
    # GroupNotice().deleteNotice()
    # 等待Toast消息的出现
    # timeout = 10  # 设置超时时间（秒）
    # start_time = time.time()
    # while time.time() - start_time < timeout:
    #     toast_message = d.toast.get_message()
    #     if toast_message is not None:
    #         break
    #     time.sleep(实例25_批量生成PPT版荣誉证书)
    #     print(toast_message)
    # 断言Toast消息是否包含'删除成功'
    # assert '删除成功' in toast_message, "Toast消息不包含'删除成功'"
    # time.sleep(2)
    # GroupNotice().topNotice()
    # time.sleep(2)
    # GroupNotice().modifyNotice('修改')
    #
    # GroupNotice().create_gropNotice_text_popup('弹窗')
    # GroupNotice().create_gropNotice_text_top('置顶')
    # GroupNotice().create_gropNotice_text_fornewcommer('新人必看')
    # time.sleep(3)
    # Base1().closeApp()