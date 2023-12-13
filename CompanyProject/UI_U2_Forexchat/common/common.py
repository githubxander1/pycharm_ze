import inspect
import os
import time
from datetime import datetime

from CompanyProject.UI_U2_Forexchat.base.basePage import d, Base1
from CompanyProject.UI_U2_Forexchat.operation.ChatWindows.GroupWindow import GroupWindow
from CompanyProject.UI_U2_Forexchat.operation.GroupSet.GroupSet import GroupSet
from CompanyProject.UI_U2_Forexchat.operation.op_Home import Home


def take_screenshot(filename):
    # print(os.path.dirname(__file__))#当前文件所在目录
    # directory = os.getcwd()#获取当前工作目录
    # print(directory)
    # if not os.path.exists(directory):
    #     os.makedirs(directory)
    # name = inspect.stack()[1][3]  # 当前方法名字
    # timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    d.screenshot(filename)

def login():
    Base1().startApp()
    time.sleep(8)
    Home().click_conversation()
    GroupWindow().click_groupSet()
    time.sleep(2)
    GroupSet().slide_down()