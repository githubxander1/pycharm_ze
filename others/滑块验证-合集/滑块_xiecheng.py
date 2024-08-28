# coding = utf-8
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# 打开chrome浏览器
d = webdriver.Chrome()
# d.maximize_window()
d.implicitly_wait(10)
# 打开携程网注册页面
d.get('https://passport.ctrip.com/user/reg/home')
# 点击同意并继续
d.find_element(By.XPATH, '//div[@class="pop_footer"]/a[@class="reg_btn reg_agree"]').click()
# 定位到滑块按钮元素
ele_button = d.find_element(By.XPATH, '//*[@id="slideCode"]/div[实例25_批量生成PPT版荣誉证书]/div[2]')
ele_button_width=ele_button.size['width']
# 打印滑块按钮的宽和高
print('滑块按钮的宽：', ele_button_width)
# print('滑块按钮的高：', ele_button.size['height'])
# 定位到滑块区域元素
ele_background = d.find_element(By.XPATH, '//div[@class="cpt-bg-bar"]')
ele_background_width=ele_background.size['width']
# 打印滑块区域的宽和高
print('滑块区域的宽：', ele_background_width)
# print('滑块区域的高：', ele_background.size['height'])
distance=ele_background_width-ele_button_width
print(distance)
# 拖动滑块
# ActionChains(d).drag_and_drop_by_offset(ele_button, ele_background.size['width'], ele_background.size['height']).perform()
ActionChains(d).click_and_hold(ele_button).perform()
ActionChains(d).move_by_offset(distance,0).perform()
ActionChains(d).release()
sleep(5)