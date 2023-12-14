import inspect
import os
import time
from datetime import datetime

from CompanyProject.UI_U2_Forexchat.base.basePage import d, Base1
from CompanyProject.UI_U2_Forexchat.operation.ChatWindows.GroupWindow import GroupWindow
from CompanyProject.UI_U2_Forexchat.operation.GroupSet.GroupSet import GroupSet
from CompanyProject.UI_U2_Forexchat.operation.op_Home import Home

class common:
    def take_screenshot(self,file_basename,sc_name):
        basename_without_extension = os.path.splitext(file_basename)[0]
        file_without_prefixAndextension = basename_without_extension[5:]  # 去掉前面的text_
        print(file_without_prefixAndextension)
        if os.path.exists(f'./result_screenshots/{file_without_prefixAndextension}'):
            pass
        else:
            os.makedirs(f'./result_screenshots/{file_without_prefixAndextension}')
            os.path.join(f'./result_screenshots/{file_without_prefixAndextension}', '__init__.py')  # 创建__init__.py文件
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'./result_screenshots/{file_without_prefixAndextension}/{sc_name}_{timestamp}.png'
        time.sleep(4)
        d.screenshot(filename)
        return filename

    def login(self):
        Base1().startApp()
        time.sleep(8)
        Home().click_conversation()
        GroupWindow().click_groupSet()
        time.sleep(2)
        GroupSet().slide_down()