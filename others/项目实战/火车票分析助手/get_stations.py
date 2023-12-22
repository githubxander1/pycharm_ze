import json
import os
import re
import sys

import requests
from PyQt5.QtWidgets import QApplication

from others.项目实战.火车票分析助手.window import MainWindow


def write(stations,filename):
    with open(filename,'w',encoding='utf-8') as f:
        f.write(stations)

def read(filename):
    with open(filename,'r',encoding='utf-8') as f:
        data=f.readlines()
        return data

def is_stations(filename):
    is_stations=os.path.exists(filename)
    return is_stations
import requests
import re

def get_stations():
    url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9050'
    response = requests.get(url)
    # 检查请求是否成功
    if response.status_code == 200:
        # 获取需要的车站名称
        stations = re.findall('([\u4e00-\u9fa5]+)\|([A-Z]+)', response.text)
        # 创建字典
        stations_dict = dict(stations)
        stations_dict = str(stations)
        print(stations_dict)
        # 使用字典写入文件
        with open('stations.text', 'w', encoding='utf-8') as file:
            file.write(stations_dict)

def get_selling_time():
    url='https://www.12306.cn/index/script/core/common/qss_v10001.js'
    response=requests.get(url, verify=True)
    # print(response.text)
    if response.status_code == 200:
        json_str=re.findall('{[^}]+}', response.text)
        time_js=json.loads(json_str[0])
        with open('time.text','w',encoding='utf8') as  file:
            file.write(str(time_js))



if __name__ == '__main__':
    if not os.path.exists('stations.text') and os.path.exists('time.text'):
        get_stations()
        get_selling_time()
    else:
        print('文件已存在')
    # if os.path.exists('stations.text') and os.path.exists('time.text'):
    #     app = QApplication(sys.argv)
    #     window = MainWindow()
    #     window.ui.show()
    #     sys.exit(app.exec_())
    # else:
    #     MainWindow().messageDialog('提示','请先获取车站和售票时间')
