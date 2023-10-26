import time

from selenium import webdriver

# 打开网页
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("https://testfben.tostar.top/")
driver.maximize_window()
# 输入用户名和密码，点击登录
email = "40@qq.com"
password = "a1234567"

# 鼠标悬浮
loginbtnmain=driver.find_element(By.XPATH,'login_btn-main')
ActionChains(driver).move_to_element(loginbtnmain).perform()


driver.find_element(By.XPATH,"login_btn").click()

time.sleep(2)
driver.find_element(By.CSS_SELECTOR,'#inputMailText').send_keys(email)
driver.find_element(By.CSS_SELECTOR,'#inputMailPwd').send_keys(password)
driver.find_element(By.ID,"mailBtn").click()

# 确认登录成功
# assert "Welcome" in driver.page_source

# 关闭浏览器
driver.close()