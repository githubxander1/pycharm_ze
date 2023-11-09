import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 创建Chrome浏览器实例
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("--headless")  # 无头模式，不显示浏览器界面
options.add_argument("--disable-gpu")  # 禁用GPU加速
# driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome()
# driver = webdriver.Edge(options=options)

# 打开页面
driver.get("https://bvwebtest.tostar.top/")
time.sleep(4)
# 切换到手机模式
driver.set_window_size(375, 812)  # 设置窗口大小，模拟手机屏幕尺寸

# 在H5页面执行操作
# 例如，点击页面上的元素
element = driver.find_element(By.XPATH,"//button[contains(text(), 'Click Me')]")
element.click()

# 获取页面内容
page_source = driver.page_source
print(page_source)
#
# # 关闭浏览器
# driver.quit()