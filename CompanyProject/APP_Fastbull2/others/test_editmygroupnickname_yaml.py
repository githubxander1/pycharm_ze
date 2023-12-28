import os.path
import unittest
import time

import logging
from datetime import datetime

import pytest

from CompanyProject.APP_Fastbull2.common.common import common
from CompanyProject.APP_Fastbull2.data.load_testdata import load_yamldata
from CompanyProject.APP_Fastbull2.operation.ChatWindows.GroupWindow import GroupWindow
from CompanyProject.APP_Fastbull2.base.basePage import Base1, d
from CompanyProject.APP_Fastbull2.operation.GroupSet.GroupSet import GroupSet
from CompanyProject.APP_Fastbull2.operation.op_Home import Home

# 设置日志格式
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class Test_group_nickname():
    def setup_class(cls):
        common().login()

    def teardown_class(cls):
        Base1().closeApp()

    def setUp(self):
        # 等待3秒
        time.sleep(3)

    def tearDown(self):
        pass

    group_nickname = load_yamldata()['groupNickName']
    filter_data=[item for item in group_nickname if not item.get('skip','n')=='y']
    print(filter_data)
    @pytest.mark.parametrize('item', filter_data)
    # @pytest.mark.skipif()
    def test_nickname_set(self,item):
        text=item['text']
        GroupSet().nickname_set(text)
        d.implicitly_wait(10)
        time.sleep(2)
        if GroupSet().disbandgroup.exists:
            file_basename=os.path.basename(__file__)
            # 去掉后缀
            # file_extension=file_basename[1]
            # basename_without_extension=os.path.splitext(file_basename)[0]
            #
            # file_without_prefixAndextension=basename_without_extension[5:]# 去掉前面的text_
            # if os.path.exists(f'./result_screenshots/{file_without_prefixAndextension}'):
            #     pass
            #     print('文件夹存在，跳过')
            # else:
            #     os.makedirs(f'./result_screenshots/{file_without_prefixAndextension}')
            #     os.path.join(f'./result_screenshots/{file_without_prefixAndextension}', '__init__.py')# 创建__init__.py文件
            # timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            # # filename = f'./result_screenshots/{file_without_prefixAndextension}/{text}_{timestamp}.png'
            # filename = f'./result_screenshots/group_nickname/{text}_{timestamp}.png'
            # d.screenshot(filename)
            common().take_screenshot(file_basename,text)
            print('截图成功')
        else:
            print('未截图')

if __name__ == "__main__":
    pytest.main(['-vs'])