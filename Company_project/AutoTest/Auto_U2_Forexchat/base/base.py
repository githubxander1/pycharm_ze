'''base.py'''
# Base（基类）：封装page 页面一些公共的方法，如初始化方法、查找元素方法、点击元素方法、输入方法、获取文本方法、截图方法等

# 发送文本
import time
import uiautomator2 as u2

# 连接模拟器或手机
from Company_project.AutoTest.Auto_U2_Forexchat.page.u2_Forexchat import manage_groups

class Base:
    # 初始化
    def __init__(self,d):
        self.d=u2.connect('127.0.0.1:21513')

    def base_find_element(self, loc, timeout=30, poll_frequency=0.5):
        return WebDriverWait(driver=self.d, timeout=timeout, poll_frequency=poll_frequency).until(
            lambda x: x.find_element(*loc))

    # 点击方法
    def base_click(self, loc):
        self.base_find_element(loc).click()

    # 输入方法
    def base_input(self, loc, value):
        element = self.base_find_element(loc)
        element.clear()
        element.send_keys(value)

    # 获取文本方法
    def base_get_text(self, loc):
        msg = self.base_find_element(loc).text
        return msg

    # 截图
    def base_get_image(self, ):
        self.d.screenshot("./{}.png".format(time.strftime("%Y_%m_%d_%H_%M_%S")))


# 启动app
# def appStart():
#     # 判断是否需要登录
#     if d(text="登录汇聊").exists:
#         d.implicitly_wait(5)
#         d(description="​邮​箱​/​F​X​I​D​/​手​机​号​").click()
#         d(text="邮箱/FXID").send_keys('12i_ynhx5b51i2@dingtalk.com')
#         d.implicitly_wait(3)
#         time.sleep(3)
#         d(text="密码").set_text('a1234567')
#         next1=d.xpath('//*[@content-desc="登录"]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[4]')
#         next1.click()
#     else:
#         pass

# 点击聊天室
# d.xpath('//android.widget.ScrollView/android.view.View[1]').click()

def send_text():
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
def mark_read():
    # 先定位元素，再滑动
    hh=d.xpath('//android.widget.ScrollView/android.view.View[2]')
    # hh.swipe('left')
    hh.swipe('left')
    time.sleep(2)
    d.xpath('//android.widget.ScrollView/android.view.View[2]/android.widget.ImageView[1]').click()
    # d.xpath('//android.widget.ScrollView/android.view.View[3]/android.widget.ImageView[1]')

# 点击进入会话聊天窗口
def session1():
    # d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]').click()
    d.xpath('//android.widget.ScrollView/android.view.View[2]').click()

    # 进入群设置
def groupSet():
    d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[3]').click()

def group_editGroupProfiles():
    manage_groups()
    d(description="编辑群资料").click()
    d.xpath('//*[contains(@content-desc,"群介绍")]').click()
    d(text="请输入群介绍").send_keys('群介绍：打扫房间独守空闺季拉开')
    d.xpath('//*[@content-desc="完成"]').click()

def group_editGroupProfiles_cancel():
    manage_groups()
    d(description="编辑群资料").click()
    d.xpath('//*[contains(@content-desc,"群介绍")]').click()
    d(text="请输入群介绍").send_keys('群介绍：打扫房间独守空闺季拉开')
    d.xpath('//*[contains(@content-desc,"编辑群介绍")]/android.widget.ImageView[1]').click()
    d.xpath('//*[@content-desc="确定"]').click()