import logging

from CompanyProject.UI_U2_Forexchat.operation.ChatWindows.GroupWindow import GroupWindow
from CompanyProject.UI_U2_Forexchat.operation.GroupSet.GroupManage.ManageGroup import ManageGroup
from CompanyProject.UI_U2_Forexchat.base.basePage import Base1, d
from CompanyProject.UI_U2_Forexchat.operation.op_Home import Home


# class Mynickname(Base1):
#     # adminset = d.xpath('//*[contains(@content-desc,"设置管理员")]')
#     nickname = d.xpath('//*[contains(@content-desc,"我的群昵称")]')
#     # 输入群昵称
#     nameinput = d(className='android.widget.EditText')
#     complete = d(description="完成")
#
#     # 编辑群昵称
#     def nickname_set(self):
#         # 进入会话
#         logging.info("点击进入会话")
#         Home().click_conversation()
#         # 点击群设置
#         logging.info("点击群设置")
#         GroupWindow().group_set.click()
#         # 下滑
#         logging.info("下滑")
#         d(scrollable=True).scroll.forward.to(description="管理群")
#         # d(scrollable=True).scroll.forward.to('contains(@content-desc,"我的群昵称")')
#         logging.info("点击我的群昵称")
#         Mynickname().nickname.click()
#         logging.info("输入群昵称")
#         Mynickname().nameinput.send_keys('群昵称')
#         logging.info("点击完成")
#         Mynickname().complete.click()
#
#
# #
# if __name__ == 'main':
#     logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
#     Mynickname().nickname_set()
class Mynickname(Base1):
    # adminset = d.xpath('//*[contains(@content-desc,"设置管理员")]')
    nickname = d.xpath('//*[contains(@content-desc,"我的群昵称")]')
    # 输入群昵称
    nameinput = d(className='android.widget.EditText')
    complete = d(description="完成")

    # 编辑群昵称
    def nickname_set(self):
        # 进入会话
        Home().click_conversation()
        # 点击群设置
        GroupWindow().group_set.click()
        # 下滑
        d(scrollable=True).scroll.forward.to(description="管理群")
        # d(scrollable=True).scroll.forward.to('contains(@content-desc,"我的群昵称")')
        Mynickname().nickname.click()
        Mynickname().nameinput.send_keys('群')
        Mynickname().complete.click()

if __name__ == '__main__':
    Mynickname().nickname_set()
