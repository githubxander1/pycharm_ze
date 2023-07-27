import unittest
import time

import logging
from CompanyProject.UI_U2_Forexchat.operation.ChatWindows.GroupWindow import GroupWindow
from CompanyProject.UI_U2_Forexchat.base.basePage import Base1
from CompanyProject.UI_U2_Forexchat.operation.GroupSet.GroupSet import GroupSet
from CompanyProject.UI_U2_Forexchat.operation.op_Home import Home

# 设置日志格式
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')



class Test_groupDescription(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 在测试类中，setUpClass() 方法会在所有测试用例执行前自动调用一次
        Base1().startApp()
        Home().click_conversation()
        GroupWindow().click_groupSet()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        Base1().closeApp()

    def setUp(self):
        # 等待3秒
        time.sleep(3)

    def tearDown(self):
        pass

    def test_editgrouintroduction1_sus(self):
        text = '群介绍-第一次'
        GroupSet().editgroupintroduction(text)
        logging.info("1正常用例")

    def test_editgrouintroduction2_null(self):
        text = ''
        GroupSet().editgroupintroduction(text)
        logging.info("2为空")

    def test_editgrouintroduction3_900(self):
        text = '第三次的撒发达飒飒的范德萨范德萨发打发的撒丰东股份地方撒打发问题糊涂范德萨发撒反倒是给对方和在v发放热污染费官方的手工费第三个放大是官方第三位而确认为托管人和官方依然头疼了公开课MV把对方VB小城镇VS大范围而我委屈日期为提高范德萨发的帮助下把在v在沙发上风格割发代首嘎范德萨范德萨粉我亲爱额未发生场个梵蒂冈反倒是广东省干啥放大梵蒂冈讽德诵功放大士大夫根深蒂固森岛帆高离开家票发的时刻割发代首刮痧师傅挖人转发第三个防火规范从VG发送给社团热工时费浦东平顶山牌佛是可怕的风格第三方的撒发达飒飒的范德萨范德萨发打发的撒丰东股份地方撒打发问题糊涂范德萨发撒反倒是给对方和在v发放热污染费官方的手工费第三个放大是官方第三位而确认为托管人和官方依然头疼了公开课MV把对方VB小城镇VS大范围而我委屈日期为提高范德萨发的帮助下把在v在沙发上风格割发代首嘎范德萨范德萨粉我亲爱额未发生场个梵蒂冈反倒是广东省干啥放大梵蒂冈讽德诵功放大士大夫根深蒂固森岛帆高离开家票发的时刻割发代首刮痧师傅挖人转发第三个防火规范从VG发送给社团热工时费浦东平顶山牌佛是可怕的风格第三方的撒发达飒飒的范德萨范德萨发打发的撒丰东股份地方撒打发问题糊涂范德萨发撒反倒是给对方和在v发放热污染费官方的手工费第三个放大是官方第三位而确认为托管人和官方依然头疼了公开课MV把对方VB小城镇VS大范围而我委屈日期为提高范德萨发的帮助下把在v在沙发上风格割发代首嘎范德萨范德萨粉我亲爱额未发生场个梵蒂冈反倒是广东省干啥放大梵蒂冈讽德诵功放大士大夫根深蒂固森岛帆高离开家票发的时刻割发代首刮痧师傅挖人转发第三个防火规范从VG发送给社团热工时费浦东平顶山牌佛是可怕的风格第三方的撒发达飒飒的范德萨范德萨发打发的撒丰东股份地方撒打发问题糊涂范德萨发撒反倒是给对方和在v发放热污染费官方的手工费第三个放大是官方第三位而确认为托管人和官方依然头疼了公开课MV把对方VB小城镇VS大范围而我委屈日期为提高范德萨发的帮助下把在v在沙发上风格割发代首嘎范德萨范德萨粉我亲爱额未发生场个梵蒂冈反倒是广东省干啥放大梵蒂冈讽德诵功放大士大夫根深蒂固森岛帆高离开家票发的时刻割发代首刮痧师傅挖人转发第九百'
        GroupSet().editgroupintroduction(text)
        logging.info("3-900字符")

    def test_editgrouintroduction4_abnormal(self):
        text = '异常值-(3)异常值、特殊字符：输入空白(NULL)、空格或"~!@#$%^&*()_+{}|[]:"<>?;’,./?;:’-=等可能导致系统错误的字符、禁止直接输入特殊字符时，' \
               '尝试使用粘贴拷贝查看是否能正常提交、word中的特殊功能，通过剪贴板拷贝到输入框，分页符，分节符类似公式的上下' \
               '等、数值的特殊符号如∑，㏒，㏑，∏，+，-等、正则表达式： n位的数字：^\d{n}$ ，\n,\r梵蒂冈'
        GroupSet().editgroupintroduction(text)
        logging.info("4异常值")

    def test_editgrouintroduction5_newline(self):
        text = '群介绍-第五次' \
               '' \
               '' \
               '' \
               '' \
               '' \
               '' \
               '换行'
        GroupSet().editgroupintroduction(text)
        logging.info("5换行")



if __name__ == "__main__":
    unittest.main()