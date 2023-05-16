import time

from selenium import webdriver

# 打开网页
from selenium.webdriver import ActionChains

driver = webdriver.Edge()
driver.get("https://testfben.tostar.top/")
driver.maximize_window()
# 输入用户名和密码，点击登录
email = "40@qq.com"
password = "a1234567"

# 鼠标悬浮
loginbtnmain=driver.find_element_by_id('login_btn-main')
ActionChains(driver).move_to_element(loginbtnmain).perform()


driver.find_element_by_id("login_btn").click()

time.sleep(2)
driver.find_element_by_css_selector('#inputMailText').send_keys(email)
driver.find_element_by_css_selector('#inputMailPwd').send_keys(password)
driver.find_element_by_id("mailBtn").click()

# 确认登录成功
# assert "Welcome" in driver.page_source

# 关闭浏览器
driver.close()