import inspect
import os
from datetime import datetime

from CompanyProject.UI_U2_Forexchat.base.basePage import d


def take_screenshot():
    # print(os.path.dirname(__file__))#当前文件所在目录
    directory = os.getcwd()#获取当前工作目录
    if not os.path.exists(directory):
        os.makedirs(directory)
    name = inspect.stack()[1][3]  # 当前方法名字
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f'./result_screenshots/{name}_{timestamp}.png'
    d.screenshot(filename)