from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://bvwebtest.tostar.top/cn")

driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div[1]/div[1]/div[2]/div[3]').click()
driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div[1]/div[2]/div/div/div[2]/div[1]/form/div[1]/div/div/input').send_keys('3@qq.com')
driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div[1]/div[2]/div/div/div[2]/div[1]/form/div[2]/div/div/input').send_keys('a1234567')
driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div[1]/div[2]/div/div/div[2]/div[1]/form/div[4]/div/button/span').click()
sleep(2)


# 悬浮到icon上
icon=driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div[3]/div/img')
ActionChains(driver).move_to_element(icon).perform()
driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div[3]/div/div/div[2]').click()

sleep(2)
iframe=driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div[3]/div[2]/div/iframe')
driver.switch_to.frame(iframe)
# driver.find_element(By.XPATH,'//*[@id="invitation"]/div[2]/div[1]/div').click()
# 点击复制
driver.find_element(By.XPATH,'//*[@id="invitation"]/div[2]/div[2]/div[2]').click()

# 执行JavaScript脚本，在当前标签页外打开新标签页
driver.execute_script('window.open("");')

# 切换到新打开的标签页
driver.switch_to.window(driver.window_handles[-1])

# 在新标签页中打开链接
driver.get("https://bvwebtestevent.tostar.top/cn/share/217?ump=3694_Hazel Tao")

driver.find_element(By.XPATH,'//*[@id="share"]/div[1]/div[2]/div[1]/input').send_keys('88@qq.com')
driver.find_element(By.XPATH,'//*[@id="share"]/div[1]/div[2]/div[2]/input').send_keys('a1234567')
driver.find_element(By.XPATH,'//*[@id="share"]/div[1]/div[2]/div[3]/button/span').click()
driver.find_element(By.XPATH,'//*[@id="share"]/div[1]/div[2]/div[3]/input').send_keys(1234)

# # 安全验证弹窗
wait = WebDriverWait(driver, 10)
anquan=driver.find_element(By.XPATH,'//*[@id="share"]/div[2]/div/iframe')
driver.switch_to.frame(anquan)

# 等待滑块弹窗出现
# wait = WebDriverWait(driver, 10)
# slider_iframe = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="share"]/div[2]/div/iframe')))
# driver.switch_to.frame(slider_iframe.find_element(By.XPATH,'//*[@id="share"]/div[2]/div/iframe')

# 定位滑块
slider = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='app']/main/div/div/div[2]/i")))
slider_width = slider.size['width']

# 模拟拖动滑块
action = ActionChains(driver)
action.click_and_hold(slider).perform()
sleep(0.5)
# action.move_by_offset(slider_width, 0).perform()
action.move_by_offset(slider_width * 2, 0).perform()
action.release().perform()

driver.find_element(By.XPATH,'//*[@id="share"]/div[1]/div[2]/button').click()

# 切换回默认的frame
driver.switch_to.default_content()


# # 获取当前窗
# 口句柄
# current_window_handle = driver.current_window_handle
# # 切换到新打开的窗口
# for window_handle in driver.window_handles:
#     if window_handle != current_window_handle:
#         driver.switch_to.window(window_handle)
#         break
# driver.get('https://bvwebtestevent.tostar.top/cn/share/217?ump=3694_Hazel Tao')

sleep(3)
