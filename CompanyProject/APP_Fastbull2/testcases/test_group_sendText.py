
# coding: utf-8
import time

import allure
import pytest
import uiautomator2 as u2

# from Company_project.UI_U2_Forexchat import send_text

from CompanyProject.APP_Fastbull2.base.basePage import Base1
from CompanyProject.APP_Fastbull2.operation.ChatWindows.GroupWindow import GroupWindow
from CompanyProject.APP_Fastbull2.operation.op_Home import Home


class Test_sendText:
    name='发送文本'

    def setup_class(self):
        with allure.step('step：打开应用'):
            Base1().startApp()
            time.sleep(4)
            Home().click_conversation()

    def teardown_class(self):
        with allure.step('step：关闭应用'):
            Base1().closeApp()

    def setup_method(self):
        pass
        # home_search().click_searchBox_out()

    def teardown_method(self):
        # with allure.step('step：点击取消'):
        #     home_search().click_cancel()
        pass

        # 编辑群头像成功
    def test_sendText_sus(self):
        GroupWindow().sendText('发送文字')

if __name__ == '__main__':
    pytest.main(['-vs','test_group_sendText.py'])





