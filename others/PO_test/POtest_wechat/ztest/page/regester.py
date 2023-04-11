from selenium import webdriver
from selenium.webdriver.support.select import Select

from others.PO_test.POtest_wechat.ztest.base import BasePage

d=webdriver.Edge()

class Regester(BasePage):
    def regester(self):
        d.find_element_by_id('corp_name').send_keys('企业微信名称')
        d.find_element_by_css_selector('#corp_industry > a').click()
        # 定位到下拉框
        sel1=d.find_element_by_css_selector('#corp_industry > div > table > tbody > tr > td.register_industry_wrap.register_industry_maintype_wrap > div:nth-child(7) > a').click()
        # 点击下拉框内容
        Select(sel1).select_by_value('教育').click()

        d.find_element_by_css_selector('#corp_industry > div > table > tbody > tr > td:nth-child(2) > div:nth-child(7) > div:nth-child(5) > a').click()
        Select(sel1).select_by_value('培训机构')


Regester().regester()
