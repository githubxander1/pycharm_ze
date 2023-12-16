# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 设置浏览器驱动路径，这里以 Chrome 为例
driver_path = '/path/to/chromedriver'

# 创建浏览器驱动对象
# driver = webdriver.Chrome()
driver = webdriver.Edge()

# 打开目标网址
driver.get('https://mm.edrawsoft.cn/files')

# # 找到登录表单所在 iframe，切换到该 iframe
# iframe = driver.find_element_by_id('edr_login_dialog')
# driver.switch_to.frame(iframe)
#
# # 找到用户名和密码输入框，输入相应的值，然后按回车键提交。
# username_input = driver.find_element_by_name('email')
# password_input = driver.find_element_by_name('password')
#
# username_input.send_keys('你的用户名')
# password_input.send_keys('你的密码')
# password_input.send_keys(Keys.RETURN)
#
# # 等待页面加载完成
# driver.implicitly_wait(10)
#
# # 登录成功之后，可以继续进行其他操作，例如：
# # 获取当前页面的标题
# print(driver.title)
#
# # 关闭浏览器
# driver.quit()
