# 2022/7/15 22:16
from selenium.webdriver import Chrome

from selenium.webdriver.common.action_chains import ActionChains
import time

from selenium.webdriver.common.by import By

web = Chrome()
# 打开界面
web.get('https://kyfw.12306.cn/otn/resources/login.html')

web.find_element(By.XPATH,'//*[@id="J-userName"]').send_keys('132')
web.find_element(By.XPATH,'//*[@id="J-password"]').send_keys('Liujiaqing2858')
time.sleep(2)
# 点击登录按钮
web.find_element(By.XPATH,'//*[@id="J-login"]').click()

time.sleep(2)

# 获取滑块的按钮Xpath
btn = web.find_element(By.XPATH,'//*[@id="nc_1_n1z"]')
# 操作滑块向右平移100，上下移动0
ActionChains(web).drag_and_drop_by_offset(btn, 300, 0).perform()