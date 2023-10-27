from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Edge()
driver.implicitly_wait(10)
driver.get("https://dun.163.com/trial/sense")

wait = WebDriverWait(driver, 10)
driver.find_element(By.XPATH,'/html/body/main/div[1]/div/div[2]/div[2]/ul/li[2]').click()
# driver.find_element(By.XPATH,'(By.XPATH,"/html/body/main/div[1]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[3]/div/div/div[1]/div[1]/span")').click()
anquan=wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/main/div[1]/div/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[2]/div[3]/div/div/div[1]/div[1]/span")))
anquan.click()

# 切换到安全验证弹窗的iframe
slider_iframe=driver.find_element(By.XPATH,'/html/body/main/div[1]/div/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[2]/div[3]/div/div/div[2]/iframe')
driver.switch_to.frame(slider_iframe)

# 启用selenium-wire的请求捕获功能
# driver.scopes = [{'path': '/cn/slider'}]  # 指定要捕获的URL
# driver.request_interceptor = lambda request: request  # 捕获所有请求

# 定位滑块
slider = wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/main/div[1]/div/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[2]/div[3]/div/div/div[2]/div/div/div[2]/div[2]')))
slider_width = slider.size['width']

# # 模拟拖动滑块
action = ActionChains(driver)
action.click_and_hold(slider).perform()
action.move_by_offset(slider_width, 0).perform()
action.release().perform()

# 切换回默认的frame
driver.switch_to.default_content()

# 关闭浏览器
# driver.quit()

sleep(3)
