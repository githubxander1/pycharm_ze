import logging

from CompanyProject.UI_U2_Forexchat.base.basePage import d
from CompanyProject.UI_U2_Forexchat.operation.ChatWindows.GroupWindow1 import GroupWindow
from CompanyProject.UI_U2_Forexchat.operation.GroupSet.GroupManage.ManageGroup import ManageGroup
from CompanyProject.UI_U2_Forexchat.base.basePage1 import BasePage
from CompanyProject.UI_U2_Forexchat.operation.op_Home import Home


# class Mynickname(Base1):
#     # adminset = ('xpath':'//*[contains(@content-desc,"设置管理员")]')
#     nickname = ('xpath':'//*[contains(@content-desc,"我的群昵称")]')
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
class Mynickname(BasePage):
    # adminset = {'xpath':'//*[contains(@content-desc,"设置管理员"}
    nickname = {'xpath':'//*[contains(@content-desc,"我的群昵称")'}
    # 输入群昵称
    nameinput = {'className':'android.widget.EditText'}
    complete = {'description':"完成"}

    def click_mygroupnickname(self):
        self.click(self.nickname)

    def edit_mygroupnickname(self,text):
        self.input_text(self.nameinput,text)

    def click_complete(self):
        self.click(self.complete)

    # 编辑群昵称
    def nickname_set(self,text):
        # 进入会话
        Home().click_conversation()
        # 点击群设置
        GroupWindow().click_group_set()
        # 下滑
        d(scrollable=True).scroll.forward.to(description="管理群")
        # d(scrollable=True).scroll.forward.to('contains(@content-desc,"我的群昵称")')
        Mynickname().click_mygroupnickname()
        Mynickname().edit_mygroupnickname(text)
        Mynickname().click_complete()

if __name__ == '__main__':
    Home.launch_app()
    Mynickname().nickname_set('fdgfsd')
