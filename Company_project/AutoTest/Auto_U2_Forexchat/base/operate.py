import time
import uiautomator2 as u2

# 连接模拟器或手机
# from Company_project.AutoTest.Auto_U2_Forexchat.page.u2_Forexchat import manage_groups

d=u2.connect('127.0.0.1:21513')

# 点击进入会话聊天窗口
def session1():
    # d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]').click()
    d.xpath('//android.widget.ScrollView/android.view.View[2]').click()

def send_text(self):
    # 点击输入框
    time.sleep(2)
    d(text="输入消息...").send_keys('dsfds')
    time.sleep(3)
    # 点击发送按钮
    d.xpath(
        '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[3]').click()

    # 发送emoji表情
    # def send_emoji():
    #     # 点击表情按钮
    #     time.sleep(2)
    #     d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[3]').click()
    #     scrollTo=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[3]/android.view.View[1]/android.widget.ImageView[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[27]')
    #     # d(scrollable=True).scroll.to(scrollTo)
    #     d(scrollable=True).scroll.toEnd()
    #     d.xpath(
    #         '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[3]/android.view.View[1]/android.widget.ImageView[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[27]').click()
    #     # 点击发送
    #     d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[5]').click()

    # d.app_stop('com.sy.fxchat')


    # 进入群设置
def groupSet():
    d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[3]').click()

# 进入管理群
def manage_groups():
    # 进入会话
    session1()
    # 点击群设置
    groupSet()
    time.sleep(3)
    # 点击管理群
    d(scrollable=True).scroll.to(description="管理群")
    d(description="管理群").click()

def group_admin_add():
    manage_groups()
    d.xpath('//*[contains(@content-desc,"管理员"]').click()

# 编辑群介绍
def group_editGroupProfiles():
    manage_groups()
    d(description="编辑群资料").click()
    d.xpath('//*[contains(@content-desc,"群介绍")]').click()
    d(text="请输入群介绍").send_keys('群介绍：打扫房间独守空闺季拉开')
    d.xpath('//*[@content-desc="完成"]').click()

# 取消编辑群介绍
def group_editGroupProfiles_cancel():
    manage_groups()
    d(description="编辑群资料").click()
    d.xpath('//*[contains(@content-desc,"群介绍")]').click()
    d(text="请输入群介绍").send_keys('群介绍：打扫房间独守空闺季拉开')
    d.xpath('//*[contains(@content-desc,"编辑群介绍")]/android.widget.ImageView[1]').click()
    d.xpath('//*[@content-desc="确定"]').click()

# 标记已读
def mark_read():
    # 先定位元素，再滑动
    hh = d.xpath('//android.widget.ScrollView/android.view.View[2]')
    # hh.swipe('left')
    hh.swipe('left')
    time.sleep(2)
    d.xpath('//android.widget.ScrollView/android.view.View[2]/android.widget.ImageView[1]').click()
    # d.xpath('//android.widget.ScrollView/android.view.View[3]/android.widget.ImageView[1]')


