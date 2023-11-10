from selenium import webdriver
import pyautogui

# 创建Chrome浏览器的WebDriver对象
driver = webdriver.Chrome()
# driver = webdriver.Edge()

# 打开开发者工具
pyautogui.hotkey('f12')

# 等待开发者工具打开
pyautogui.sleep(2)

# 切换到手机模式
pyautogui.hotkey('ctrl', 'shift', 'm')

# 打开网页
driver.get('https://bvwebtest.tostar.top/')

# 获取当前页面的URL
url = driver.current_url
print(url)

# 关闭浏览器
# driver.quit()