import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# # 设置webdriver路径和选项
# driver_path = 'path/to/your/webdriver'  # 比如： driver_path = '/usr/bin/chromedriver'
# # browser = webdriver.Chrome()
# browser = webdriver.Chrome()
#
# # 访问页面
# browser.get('https://www.shanghairanking.cn/rankings/bcur/2023')
#
# # 等待元素加载
# wait = WebDriverWait(browser, 10)
#
# # 初始化时找到并等待下一页按钮可点击
# next_page_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content-box"]/ul/li[9]/a')))
# next_page_button.click()
#
# time.sleep(15)
for xpath_expression in [
    '//*[@id="content-box"]/ul/li[9]/a/i',
    '//*[@id="content-box"]/ul/li[10]/a/i',
    '//*[@id="content-box"]/ul/li[11]/a/i'
]:
    try:
        print(xpath_expression)
        break  # 找到并点击后，跳出循环
    except Exception as e:
        print(e)