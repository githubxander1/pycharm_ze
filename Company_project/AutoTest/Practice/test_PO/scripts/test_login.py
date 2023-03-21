"""test_cal.py"""
# -*-coding:utf-8 -*-
# Auothor:yue_luo
import unittest

from PO.base.get_driver import GetDriver
from PO.page.page_cal import PageCal
from parameterized import parameterized

from PO.tool.read_json import read_json


def get_data():
    data = read_json("cal.json")
    # print(data)
    """
    期望数据格式：[(1234, 1234, 2468), (1, 2, 3), (123445, 223265, 32626)]
    """
    list = []
    for n in data.values():
        list.append((n["a"], n["b"], n["expect_result"]))
    return list


class TestCal(unittest.TestCase):
    # driver = None
    @classmethod
    def setUpClass(cls):
        cls.driver = GetDriver().get_driver()
        cls.cal = PageCal(cls.driver)

    @classmethod
    def tearDownClass(cls):
        GetDriver().quit_driver()

    @parameterized.expand(get_data())
    def test_add_cla(self, a, b, expect_result):
        self.cal.page_add_cal(a, b)
        result = self.cal.page_get_value()
        print("result:", result)
        print("ex_result:", expect_result)
        # 136465446
        try:
            self.assertEqual(result, str(expect_result))
        except:
            self.cal.page_get_img()
            raise
        finally:
            self.cal.page_click_clear()