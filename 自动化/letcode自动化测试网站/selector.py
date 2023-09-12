from selenium import webdriver
from selenium.webdriver.support.select import Select

d=webdriver.Edge()
d.implicitly_wait(10)
d.get('https://letcode.in/dropdowns')

# Select the apple using visible text
select=Select(d.find_element_by_id('fruits'))
select.select_by_value('Apple')
select.select_by_index(1)

