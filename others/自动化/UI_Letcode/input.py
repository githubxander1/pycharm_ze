from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

d=webdriver.Edge()
# d=webdriver.Chrome()
d.get('https://letcode.in/edit')
# d.find_element(By.ID,'fullName').send_keys('name')
# sleep(2)
# d.find_element(By.ID,'join').send_keys('Append a text and press keyboard tab')
# d.find_element(By.ID,'join').send_keys(Keys.TAB)
# sleep(2)
#
# print(d.find_element(By.ID,'getMe').get_attribute('value'))
# sleep(2)
#
# d.find_element(By.ID,'clearMe').clear()
sleep(2)

# Confirm edit field is disabled
# edit_field=d.find_element(By.ID,'noEdit').is_enabled()
# if edit_field:
#     print("可编辑")
# else:
#     print("不可编辑")
# sleep(2)
# Confirm text is readonly
readonly=d.find_element(By.ID,'dontwrite').get_attribute("readonly")
if readonly:
    print('文本是只读的')
else:
    print('文本不是只读的')