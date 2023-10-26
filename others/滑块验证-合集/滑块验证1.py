from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 创建一个新的Chrome浏览器实例
driver = webdriver.Chrome()
# 访问需要滑块验证的网站
driver.get(“http://your-website-url.com”)
# 找到滑块元素
slider = driver.find_element_by_id(“slider”)
# 找到验证按钮
verify_button = driver.find_element_by_id(“verify-button”)
# 将滑块移动到中间位置
slider.send_keys(Keys.END + Keys.PAGE_DOWN)
# 等待验证按钮变为可点击状态
wait = WebDriverWait(driver, 10)
verify_button = wait.until(EC.element_to_be_clickable((By.ID, “verify-button”)))
# 点击验证按钮
verify_button.click()
# 关闭浏览器
# driver.quit()