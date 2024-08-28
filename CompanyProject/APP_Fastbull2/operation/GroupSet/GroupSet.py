import logging
import time

import allure

from CompanyProject.APP_Fastbull2.operation.ChatWindows.GroupWindow import GroupWindow
from CompanyProject.APP_Fastbull2.base.basePage import Base1, d
from CompanyProject.APP_Fastbull2.operation.common import Common
from CompanyProject.APP_Fastbull2.operation.op_Home import Home

class GroupSet(Base1):
    groupNotice = d(description="公告")
    groupFile = d(description="文件")
    groupAlbum = d(description="相册")

    def click_groupNotice(self):
        self.groupNotice.click()

    def click_groupFile(self):
        self.groupFile.click()

    def click_groupAlbum(self):
        self.groupAlbum.click()


    shownickname = d.xpath('//*[contains(@content-desc,"显示群成员的昵称")]')
    # 群成员
    groupmembers = d.xpath('//*[contains(@content-desc,"群成员")]')
    groupmemberMore=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.widget.ImageView[2]')
    groupmemberAdd=d(description="添加群成员")
    groupmemberDel=d(description="删除群成员")
    member1=(0.083, 0.348)
    memberdel=d.xpath('//*[contains(@content-desc,"删除(")]')

    # 修改群昵称
    nickname = d.xpath('//*[contains(@content-desc,"我的群昵称")]')
    nameinput = d(className='android.widget.EditText')
    complete = d(description="完成")

    # 群二维码
    QRcodesave=d(description="保存")
    QRcodeshare=d(description="分享")
    groupManage=d(description="管理群")


    # 修改群介绍
    groupintroduction = d.xpath('//*[contains(@content-desc,"群介绍")]')
    groupDescription=d(description="群介绍")
    # nameinput = d(className='android.widget.EditText')
    # complete = d(description="完成")

    chatHistoryroaming = d.xpath('//*[contains(@content-desc,"聊天记录漫游")]')
    clearlocalchathistory = d.xpath('//*[contains(@content-desc,"清空本地聊天记录")]')
    clearchathistory = d.xpath('//*[contains(@content-desc,"清空聊天记录")]')

    def click_clearlocalchathistory(self):
        self.clearlocalchathistory.click()

    def click_clearchathistory(self):
        self.clearchathistory.click()

    def clearHistory(self):
        self.slide_down()
        self.click_clearlocalchathistory()
        self.click_clearchathistory()
        time.sleep(1)
        self.click_back()

    # 解散群
    disbandgroup = d.xpath('//*[contains(@content-desc,"解散该群")]')
    cancel = d.xpath('//*[contains(@content-desc,"取消")]')
    # confirm = d.xpath('//*[contains(@content-desc,"确定")]')
    confirm=d(description="确定")
    # 举报
    report = d.xpath('//*[contains(@content-desc,"举报")]')
    sexual=d(description="发布色情/违法等低俗")
    fraud=d(description="存在欺诈骗钱行为")
    ads=d(description="发布广告骚扰信息")
    politics=d(description="发布政治敏感信息")
    rumor=d(description="散播谣言信息")
    others=d(description="存在其他违规行为")
    submit=d(description="提交")
    # 输入群昵称

    back=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.widget.ImageView[实例25_批量生成PPT版荣誉证书]')

    @allure.step('点击我的群昵称')
    def click_mygroupnickname(self):
        self.nickname.click()

    # 群成员
    @allure.step('点击群成员')
    def click_groupmembers(self):
        self.groupmembers.click()

    @allure.step('点击群成员更多')
    def click_groupmemberMore(self):
        self.groupmemberMore.click()

    @allure.step('点击群成员添加')
    def click_groupmemberAdd(self):
        self.groupmemberAdd.click()

    @allure.step('点击群成员删除')
    def click_groupmemberDel(self):
        self.groupmemberDel.click()

    # def click_member1(self):
    #     self.member1.click()

    @allure.step('点击群成员删除')
    def click_memberdel(self):
        self.memberdel.click()

    @allure.step('点击群成员添加')
    def groupmembersadd(self):
        # 进入会话
        # Home().click_conversation()
        # # 点击群设置
        # GroupWindow().click_groupSet()
        # 点击群二维码
        # time.sleep(2)
        self.click_groupmembers()
        self.click_groupmemberMore()
        self.click_groupmemberAdd()

    @allure.step('点击群成员删除')
    def groupmembersdel(self):
        self.click_groupmembers()
        self.click_groupmemberMore()
        self.click_groupmemberDel()
        time.sleep(1)
        self.d.click(0.092, 0.306)
        time.sleep(2)
        self.click_memberdel()
        self.click_cancel()
        time.sleep(1)
        self.click_memberdel()
        time.sleep(1)
        self.click_confirm()

    @allure.step('点击我的群介绍')
    def click_mygroupintroduction(self):
        self.groupintroduction.click()

    @allure.step('点击保存')
    def click_save(self):
        self.QRcodesave.click()

    @allure.step('点击分享')
    def click_share(self):
        self.QRcodeshare.click()

    @allure.step('点击解散群')
    def click_disbandgroup(self):
        self.disbandgroup.click()

    @allure.step('点击取消')
    def click_cancel(self):
        self.cancel.click()

    @allure.step('点击确定')
    def click_confirm(self):
        self.confirm.click()

    @allure.step('点击举报')
    def click_report(self):
        self.report.click()

    @allure.step('点击色情')
    def click_sexual(self):
        self.sexual.click()

    @allure.step('点击欺诈')
    def click_fraud(self):
        self.fraud.click()

    @allure.step('点击广告')
    def click_ads(self):
        self.ads.click()

    @allure.step('点击政治敏感')
    def click_politics(self):
        self.politics.click()

    @allure.step('点击散播谣言')
    def click_rumor(self):
        self.rumor.click()

    @allure.step('点击其他')
    def click_others(self):
        self.others.click()

    @allure.step('点击提交')
    def click_submit(self):
        self.submit.click()

    @allure.step('点击返回')
    def click_back(self):
        self.back.click()

    @allure.step('点击聊天记录漫游')
    def click_chathistoryroaming(self):
        self.chatHistoryroaming.click()

    @allure.step('输入群昵称')
    def edit_mygroupnickname(self,text):
        self.nameinput.set_text(text)

    @allure.step('点击完成')
    def click_complete(self):
        self.complete.click()

    # 下滑到管理群
    @allure.step('下滑到管理群')
    def slide_down(self):
        while not d(description="管理群").exists():
            d(scrollable=True).scroll.forward()
            time.sleep(1)
        # d(description="管理群").click()

    @allure.step('上滑到管理群')
    def slide_up(self):
        # 获取设备屏幕尺寸
        width, height = d.window_size()

        # 计算起始坐标和终点坐标
        start_x = width // 2
        start_y = height // 4
        end_x = width // 2
        end_y = height // 2
        print(start_x, start_y, end_x, end_y)

        # 模拟鼠标下拉操作
        d.swipe(start_x, start_y, end_x, end_y, duration=0.5)

    @allure.step('进入群设置')
    def enter_groupSet(self):
        Base1().startApp()
        time.sleep(7)
        Home().click_conversation()
        GroupWindow().click_groupSet()
        time.sleep(2)

    # 保存群二维码
    @allure.step('保存群二维码')
    def GroupQRcodesave(self):
        # 进入会话
        # Home().click_conversation()
        # # 点击群设置
        # GroupWindow().click_groupSet()
        # 点击群二维码
        time.sleep(2)
        # 点击保存
        self.d.click(0.918, 0.664)
        self.click_save()
        # self.click_share()

    # 分享群二维码
    @allure.step('分享群二维码')
    def GroupQRcodeshare(self):
        # 进入会话
        # Home().click_conversation()
        # # 点击群设置
        # GroupWindow().click_groupSet()
        # 点击群二维码
        time.sleep(2)
        # 点击保存
        self.d.click(0.918, 0.664)
        self.click_share()
        Common().forward_tofriendandgroup()


    # 编辑群介绍
    @allure.step('编辑群介绍')
    def editgroupDescription(self,text):
        # 点击群介绍
        time.sleep(2)
        # self.click_mygroupintroduction()
        self.d.click(0.148, 0.749)
        # self.groupDescription.click()
        # self.groupDescription.click()
        # 输入群名称
        self.edit_mygroupnickname(text)
        # 点击完成
        self.click_complete()

    # 编辑群昵称
    @allure.step('编辑群昵称')
    def nickname_set(self, text):
        # 进入会话
        # Home().click_conversation()
        # # 点击群设置
        # GroupWindow().click_groupSet()
        # 下滑
        self.slide_down()
        # d(scrollable=True).scroll.forward.to('contains(@content-desc,"我的群昵称")')
        # 点击我的群名称
        time.sleep(2)
        self.click_mygroupnickname()
        # 输入群名称
        self.edit_mygroupnickname(text)
        # 点击完成
        self.click_complete()


    # 聊天记录漫游
    @allure.step('聊天记录漫游')
    def chathistoryroaming(self):
        # 进入会话
        # Home().click_conversation()
        # # 点击群设置
        # GroupWindow().click_groupSet()
        # 下滑
        self.slide_down()
        # d(scrollable=True).scroll.forward.to('contains(@content-desc,"我的群昵称")')
        # 点击我的群名称
        # time.sleep(2)
        self.click_chathistoryroaming()
        time.sleep(1)
        self.click_back()
        # 开始下滑
        # self.slide_up()
        # self.d.swipe(0.505, 0.177,0.483, 0.85)

    # 举报
    @allure.step('举报')
    def Report(self):
        # 进入会话
        # Home().click_conversation()
        # # 点击群设置
        # GroupWindow().click_groupSet()
        # 下滑
        self.slide_down()
        # d(scrollable=True).scroll.forward.to('contains(@content-desc,"我的群昵称")')
        # 点击举报
        self.click_report()
        self.click_sexual()
        self.click_submit()

    # 解散群
    @allure.step('解散群')
    def disbandGroup(self):
        Base1().startApp()
        # 进入会话
        Home().click_conversation()
        # 点击群设置
        GroupWindow().click_groupSet()
        # 下滑
        self.slide_down()
        # d(scrollable=True).scroll.forward.to('contains(@content-desc,"我的群昵称")')
        # 点击解散群
        self.click_disbandgroup()
        self.click_cancel()

    # 显示群昵称
    @allure.step('显示群昵称')
    def shownicknames(self):
        # 进入会话
        Home().click_conversation()
        # 点击群设置
        GroupWindow().click_groupSet()
        # 下滑
        self.slide_down()
        self.d.click(0.875, 0.456)

    # 设置置顶
    @allure.step('设置置顶')
    def settop(self):
        # 下滑
        self.slide_down()
        self.d.click(0.873, 0.189)
        self.click_back()
        time.sleep(1)
        self.click_back()
        time.sleep(3)
        # 进入会话
        # Home().click_conversation()
        # # 点击群设置
        # GroupWindow().click_groupSet()

    # 设置消息免打扰
    @allure.step('设置消息免打扰')
    def notdisturb(self):
        # 下滑
        self.slide_down()
        self.d.click(0.88, 0.274)
        time.sleep(1)
        self.click_back()
        time.sleep(1)
        self.click_back()
        time.sleep(3)

    @allure.step('点击管理群')
    def click_managegroup(self):
        # time.sleep(5)
        # # 进入会话
        # Home().click_conversation()
        # # 点击群设置
        # GroupWindow().click_groupSet()
        # 点击管理群
        # 垂直向前滚动到指定位置（横向同理）
        while not d(description="管理群").exists():
            d(scrollable=True).scroll.forward()
            time.sleep(1)
        d(description="管理群").click()

if __name__ == '__main__':
    Base1().startApp()
    # Home().click_conversation()
    # GroupWindow().click_groupSet()
    # time.sleep(2)
    # 群二维码
    # GroupSet().GroupQRcodesave()
    # GroupSet().GroupQRcodeshare()
    # 群介绍
    # GroupSet().editgroupDescription('群介绍1')
    screenshot_path = "./screenshot1.png"  # 截图保存的路径
    d.screenshot(screenshot_path)  # 截取当前屏幕并保存为图片
    # 设置置顶
    # GroupSet().settop()
    # 消息免打扰
    # GroupSet().notdisturb()
    # 群昵称
    # GroupSet().nickname_set('1314群昵称123')
    # 显示群昵称
    # GroupSet().shownicknames()
    # 消息漫游
    # GroupSet().chathistoryroaming()
    # 清空本地聊天记录
    # GroupSet().clearHistory()
    # 群成员
    # GroupSet().groupmembersadd()
    # GroupSet().groupmembersdel()

    # 举报
    # GroupSet().Report()
    # 解散群
    # GroupSet().disbandGroup()

    # time.sleep(3)
    # Base1().closeApp()
