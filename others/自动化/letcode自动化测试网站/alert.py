from time import sleep

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

d=webdriver.Edge()
# d=webdriver.Chrome()
d.get('https://letcode.in/alert')
d.implicitly_wait(10)

# Alert弹窗：只有信息及确认按钮
d.find_element_by_id('accept').click()
alert1= d.switch_to.alert
print(alert1.text)
alert1.accept()

sleep(2)
# Confirm弹窗：在Alert弹窗基础上增加了取消按钮
d.find_element_by_id('confirm').click()
alert2=d.switch_to.alert
alert2.accept()

sleep(3)
d.find_element_by_id('confirm').click()
alert2.dismiss()

# Prompt类型弹框：在Confirm的基础上增加了可输入文本内容的功能
sleep(3)
d.find_element_by_id('prompt').click()
alert3=d.switch_to.alert
alert3.send_keys('123')
# alert3.clear_text()
# alert3.send_keys('456')
alert3.accept()

sleep(3)
# Sweet alert弹窗
d.find_element_by_id('modern').click()
# alert4=d.switch_to.alert
# print(alert1.text)
# 切换到弹窗
# alert = Alert(d)
#
# # 获取弹窗的内容
# alert_text = alert.text
# print(alert_text)

message  = WebDriverWait(d, 20).until(EC.visibility_of_element_located((By.ID, 'modern'))).text
print(message)
sleep(3)
d.find_element_by_css_selector('body > app-root > app-alert > section.section.has-background-white-ter > div > div > div.column.is-7-desktop.is-8-tablet > div > div > div.modal.is-active > button').click()