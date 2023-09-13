from time import sleep

from selenium import webdriver
from selenium.webdriver.support.select import Select

d=webdriver.Edge()
d.implicitly_wait(10)
d.get('https://letcode.in/dropdowns')

# Select the apple using visible text
# select=Select(d.find_element_by_id('fruits'))
# # select.select_by_value('Apple')
# select.select_by_index(1)
# sleep(2)
# select.select_by_visible_text('Banana')
# select.select_by_value('Orange')

sleep(2)
# 滚动条
slide = d.find_element_by_css_selector('#superheros > option:nth-child(21)')
d.execute_script("arguments[0].scrollIntoView();", slide)