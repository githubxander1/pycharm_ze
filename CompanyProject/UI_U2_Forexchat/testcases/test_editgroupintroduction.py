import unittest
import time

import logging

import yaml

from CompanyProject.UI_U2_Forexchat.data.load_testdata import load_data
from CompanyProject.UI_U2_Forexchat.operation.ChatWindows.GroupWindow import GroupWindow
from CompanyProject.UI_U2_Forexchat.base.basePage import Base1, d
from CompanyProject.UI_U2_Forexchat.operation.GroupSet.GroupSet import GroupSet
from CompanyProject.UI_U2_Forexchat.operation.op_Home import Home

# 设置日志格式
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


class Test_groupNickName(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 在测试类中，setUpClass() 方法会在所有测试用例执行前自动调用一次
        Base1().startApp()
        time.sleep(3)
        Home().click_conversation()
        GroupWindow().click_groupSet()
        time.sleep(2)
        GroupSet().slide_down()

    @classmethod
    def tearDownClass(cls):
        Base1().closeApp()

    def setUp(self):
        # 等待3秒
        time.sleep(3)

    def tearDown(self):
        pass

    def test_nickname_set_all(self):
        for groupNickName in load_data()['groupNickName']:# 加载测试用例数据并迭代每个测试用例
            with self.subTest():
                GroupSet().nickname_set(groupNickName['text'])# 执行每个测试用例并传递相应的文本数据作为参数
                time.sleep(2)
                d.screenshot('test_groupNickName.png')  # 保存截图并关闭驱动器

    # def test_nickname_set(self, text):
    #     GroupSet().nickname_set(text)
    #     print(f"Group nickname set to: {text}")
    #     logging.info("正常用例")

    # group_nickname=d('contains(@content-desc,"我的群昵称")')

    # @unittest.skip('跳过')  # 你可以在这里添加其他跳过标记，例如 @unittest.skip('system_test') 等。
        # text = '群昵称-第一次'
        # GroupSet().nickname_set(text)
        # print(self.group_nickname.get_text())
        # assert d.toast.get_message()=='编辑成功'
        # print(d.toast.get_message())

        # logging.info("正常用例")

    # @unittest.skip('跳过')
    # def test_nickname_set_null(self):
    #     text = ''
    #     GroupSet().nickname_set(text)
    #     logging.info("为空")
    #
    # @unittest.skip('跳过')
    # def test_nickname_set_900(self):
    #     text = '九'
    #     GroupSet().nickname_set(text*900)
    #     logging.info("900字符")
    #
    # @unittest.skip('跳过')
    # def test_nickname_set_abnormal(self):
    #     text = '群昵称-(3)异常值、特殊字符：输入空白(NULL)、空格或"~!@#$%^&*()_+{}|[]:"<>?;’,./?;:’-=等可能导致系统错误的字符、禁止直接输入特殊字符时，' \
    #            '尝试使用粘贴拷贝查看是否能正常提交、word中的特殊功能，通过剪贴板拷贝到输入框，分页符，分节符类似公式的上下' \
    #            '等、数值的特殊符号如∑，㏒，㏑，∏，+，-等、正则表达式： n位的数字：^\d{n}$ ，\n,\r梵蒂冈'
    #     GroupSet().nickname_set(text)
    #     logging.info("异常值")
    #
    # @unittest.skip('跳过')
    # def test_nickname_set_newline(self):
    #     text = '群昵称-' \
    #            '' \
    #            '换行'
    #     GroupSet().nickname_set(text)
    #     logging.info("换行")



if __name__ == "__main__":
    unittest.main()