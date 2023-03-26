import sys
sys.path.append('basePage.py')
from basePage import BasePage
import uiautomator2 as u2
d=u2.connect('127.0.0.1:21503')

# class groupPage(BasePage):
scroll=d(scrollable=True).scroll.to(description="管理群")
# 返回聊天窗口
back=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[1]')
# 群公告
announcement=d(description="公告")
# 群文件
file=d(description="文件")
# 群相册
album=d(description="相册")
# 群二维码
# QRcode=
# 群介绍
introduction=d(description="群介绍")
# 群成员
# members=
# 我的群昵称
mynickname=d.xpath('//*[contains(@content-desc,"我的群昵称")]')
# 输入群昵称
nameinput=d(className='android.widget.EditText')

# 消息免打扰
# messageImmunity=
# 聊天记录漫游
roaming=d(description="聊天记录漫游")
# 清空聊天记录
clearRecord=d(description="清空本地聊天记录")
# 举报
report=d(description="举报")
# 解散群
disbandGroup=d(description="解散该群")
# 管理群
group_manage=d(description="管理群").click()

# 完成
complete=d(description="完成")