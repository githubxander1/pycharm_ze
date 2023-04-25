import time
from selenium import webdriver
from selenium.webdriver import ActionChains

d=webdriver.Edge()
url = "https://login.taobao.com/member/login.jhtml"
d.get(url)
d.maximize_window() # 最大化
# 填写用户名密码
user = '*****'
password = '*******'
time.sleep(8)
iframe = d.find_element_by_xpath('//div[@class="bokmXvaDlH"]//iframe')
print(iframe)
d.switch_to.frame(iframe)
d.find_element_by_xpath('//*[@id="fm-login-id"]').send_keys(id)
d.find_element_by_xpath('//*[@id="fm-login-password"]').send_keys(password)
time.sleep(2)
# 获取滑块的大小
span_background = d.find_element_by_xpath('//*[@id="nc_1__scale_text"]/span')
span_background_size = span_background.size
print(span_background_size)
# 获取滑块的位置
button = d.find_element_by_xpath('//*[@id="nc_1_n1z"]')
button_location = button.location
print(button_location)
# 拖动操作：drag_and_drop_by_offset
# 将滑块的位置由初始位置，右移一个滑动条长度（即为x坐标在滑块位置基础上，加上滑动条的长度，y坐标保持滑块的坐标位置）
x_location = span_background_size["width"]
y_location = button_location["y"]
print(x_location, y_location)
action = ActionChains(d)
source = d.find_element_by_xpath('//*[@id="nc_1_n1z"]')
action.click_and_hold(source).perform()
action.move_by_offset(300, 0)
action.release().perform()
time.sleep(1)
# 登录
d.find_element_by_xpath('//*[@id="login-form"]/div[4]/button').click()
print('登录成功\n')