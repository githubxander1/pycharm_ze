import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

d=webdriver.Edge()
url = "https://testfb.tostar.top/login?next=/"
d.get(url)
# 填写用户名密码
user = '*****'
password = '*******'
d.find_element(By.XPATH,'//*[@id="phoneLogin"]/div[1]/div[1]/p/input').clear()
d.find_element(By.XPATH,'//*[@id="phoneLogin"]/div[1]/div[1]/p/input').send_keys('+86')
d.find_element(By.XPATH,'//*[@id="inputPhoneText"]').send_keys(13111111111)
d.find_element(By.XPATH,'//*[@id="codeBtn"]').click()
time.sleep(3)
iframe = d.find_element(By.XPATH,'/html/body/iframe')
d.switch_to.frame(iframe)
# 获取背景滑块的大小
span_background = d.find_element(By.XPATH,'//*[@id="app"]/main/div/div/div[2]')
span_background_size = span_background.size
print('背景滑块大小：',span_background_size)
# 获取滑块的位置
button = d.find_element(By.XPATH,'//*[@id="app"]/main/div/div/div[2]/i')
button_location = button.location
print('滑块位置：',button_location)
# 拖动操作：drag_and_drop_by_offset
# 将滑块的位置由初始位置，右移一个滑动条长度（即为x坐标在滑块位置基础上，加上滑动条的长度，y坐标保持滑块的坐标位置）
x_location = span_background_size["width"]
y_location = button_location["y"]
print(x_location, y_location)
action = ActionChains(d)
action.click_and_hold(button).perform()
action.move_by_offset(300, 0)
action.release().perform()
time.sleep(1)
# 登录
# d.find_element(By.XPATH,'//*[@id="phoneBtn"]').click()
# print('登录成功\n')