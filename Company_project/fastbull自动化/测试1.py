import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# Chrome浏览器驱动路径
# driver_path = "/Users/xxx/chromedriver"

# 打开网站
driver = webdriver.Edge()
driver.get("https://gitee.com/LongbowEnterprise/SliderCaptcha")

# 最大化窗口
driver.maximize_window()

# 等待页面加载完毕
time.sleep(3)

# 切换到iframe
frame = driver.find_element_by_tag_name("iframe")
driver.switch_to.frame(frame)

# 找到滑块元素
slider = driver.find_element_by_id("tcaptcha_drag_button")

# 执行滑块拖动操作
actions = ActionChains(driver)
actions.click_and_hold(slider).move_by_offset(200, 0).release().perform()

# 等待滑块验证结果
time.sleep(3)

# 关闭浏览器
driver.quit()
