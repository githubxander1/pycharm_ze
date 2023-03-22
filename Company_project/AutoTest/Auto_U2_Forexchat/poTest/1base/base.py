'''1base.py'''
# Base（基类）：封装page 页面一些公共的方法，如初始化方法、查找元素方法、点击元素方法、输入方法、获取文本方法、截图方法等

# 发送文本
import time
import uiautomator2 as u2

# 连接模拟器或手机
d=u2.connect('127.0.0.1:21513')

class Base:
    # 初始化方法
    def __init__(self,d):
        d=u2.connect('127.0.0.1:21513')


class ChatWindow:

    GroupSet=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[3]')
    Add=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[1]')
    Input=d(text="输入消息...")
    emoji=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[2]')
    send=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[3]')
    back=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[1]')

class ManageGroupsPage:
    # 初始化
    def __init__(self,d):
        self.d=u2.connect('127.0.0.1:21513')

    EditGroupProfile=d(description="编辑群资料")
    AddAdmins=d.xpath('//*[contains(@content-desc,"管理员"]')
    RestrictSendingMessage=d.xpath('//*[contains(@content-desc,"设置群内禁言"]')
    RestrictSendingFriendsRequest=d(description="禁止群内成员互加好友")
    AddGroupMethod=d(description="加群方式")
    GroupBlacklist=d(description="群黑名单")
    TransferOwenership=d(description="转让群")

class EditProfile:
    Avatar=d(description="群头像")
    Name=d.xpath('//*[contains(@content-desc,"群名称")]')
    InputGroupName = d(text='请输入群名称')

    Description = d.xpath('//*[contains(@content-desc,"群介绍")]')
    InputGroupDescription = d(text='请输入群介绍')

    Cancel = d.xpath('//*[contains(@content-desc,"编辑群介绍")]/android.widget.ImageView[1]')
    Sure = d.xpath('//*[@content-desc="确定"]')

    # 截图
    # def base_get_image(self, ):
    #     self.d.screenshot("./{}.png".format(time.strftime("%Y_%m_%d_%H_%M_%S")))


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


