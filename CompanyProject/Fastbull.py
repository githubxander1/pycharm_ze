import time
from selenium import webdriver
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.options import Options

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# # Path to the Edge WebDriver
# # path = "msedgedriver.exe"
#
# class headless_edge():
#     edge_driver = r'C:\Users\Admin\AppData\Local\Programs\Python\Python38\msedgedriver.exe'
#
#     EDGE = {
#         "browserName": "MicrosoftEdge",
#         "version": "",
#         "platform": "WINDOWS",
#
#         # 关键是下面这个
#         "ms:edgeOptions": {
#             'extensions': [],
#             'args': [
#                 '--headless',
#                 '--disable-gpu',
#                 # '--remote-debugging-port=9222',
#             ]}
#     }
#     driver = webdriver.Edge(executable_path=edge_driver, capabilities=EDGE)
#
#     driver.get('http://www.baidu.com')
#     driver.find_element(By.ID, 'kw').send_keys('selenium')
#     driver.find_element(By.ID, 'su').click()
#
#     assert driver.find_element(By.ID, 'kw').get_attribute('value') == 'selenium'
#     print('完成')
#
# class headless_chrome():
#     from selenium.webdriver import Chrome
#
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")
#     # chrome_options.add_argument(
#     #     'user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36')
#
#     # driver = Chrome('./chromedriver', options=chrome_options)
#     driver = Chrome(options=chrome_options)
#     driver.get('http://www.baidu.com')
#     driver.find_element(By.ID, 'kw').send_keys('selenium')
#     driver.find_element(By.ID, 'su').click()
#
#     assert driver.find_element(By.ID, 'kw').get_attribute('value') == 'selenium'
#     print('完成')
#
# # headless_chrome()
# headless_edge()
# 启动浏览器
# driver = webdriver.Edge()
# Create a new Edge session
# driver = webdriver.Edge(executable_path=edge_driver)
# Open a page in Edge
# 使用 EdgeChromiumDriverManager 自动下载和管理 Edge 浏览器驱动
# driver = webdriver.Edge(EdgeChromiumDriverManager().install())
driver = webdriver.Chrome()
driver.maximize_window()

# 打开网站
driver.get("https://testfb.tostar.top/cn")

# 悬浮到元素上
avatar=driver.find_element(By.ID,'login_btn-main')
ActionChains(driver).move_to_element(avatar).perform()

# login=driver.find_element(By.ID,'login_btn').click()
driver.find_element(By.ID,'login_btn').click()
driver.find_element(By.ID,'loginMethodMail').click()
driver.find_element(By.ID,'inputMailText').send_keys('7@qq.com')
driver.find_element(By.ID,'inputMailPwd').send_keys('a1234567')
driver.find_element(By.ID,'mailBtn').click()
#
# # 等待toast提示出现
# toast = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "body > div.toast-main > div > span")))
#
# # 获取toast提示的文本内容
# toast_text = toast.text
#
# # 断言toast提示的内容
# assert "登录成功1" in toast_text
#
#
