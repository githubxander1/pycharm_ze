import time
import uiautomator2 as u2
# from pg_home import homePage
# from pg_groupWindow import groupPage
# from basePage import BasePage
# try:
#     d=u2.connect('127.0.0.1:21513')
# except:
# d=u2.connect('127.0.0.1:21503')
from basePage import d
from op_Home import openHome, conversation

# from pg_home import conversation
# from pg_groupWindow import input_msg,group_set,send,emoji,expand

d.implicitly_wait(10)

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
def click_conversation():
    openHome()
    conversation.click()

def send_text(msg):
    click_conversation()
    # 点击输入框
    # input_msg.send_keys(msg)
    d(className='android.widget.EditText').send_keys(msg)
    # 点击发送按钮
    d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[6]').click()
    # send.click()

# 发送emoji表情
def send_emoji():
    click_conversation()
    # 点击表情按钮
    emoji.click()
    d(scrollable=True).scroll.toEnd()
    d.xpath(
        '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[3]/android.view.View[1]/android.widget.ImageView[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[27]').click()
    # 点击发送
    send()

    # 进入群设置
def groupSet():
    group_set.click()

if __name__ == '__main__':
    send_text('文本')