from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 创建浏览器对象并打开网页
driver = webdriver.Chrome()
driver.get("https://tradinglive-testwebpc.tostar.top/cn/login")

# 找到区号输入框并点击
country_code_input = driver.find_element_by_name("code")
country_code_input.click()

# 找到香港并选择
hongkong_option = driver.find_element_by_xpath("//li[@data-value='852']")
hongkong_option.click()

# 找到手机号输入框并输入手机号
phone_number_input = driver.find_element_by_name("username")
phone_number_input.send_keys("91111110")

# 找到获取验证码按钮并点击
get_code_button = driver.find_element_by_class_name("mobile-code-button")
get_code_button.click()

# 等待弹窗出现并切换到弹窗的iframe中
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//div[@class="tcaptcha-content"]/iframe')))

# 找到滑块元素
slider_button = driver.find_element_by_id("tcaptcha_drag_button")

# 使用ActionChains库模拟鼠标按下并拖动滑块
action = ActionChains(driver)
action.click_and_hold(slider_button).perform()
action.move_by_offset(258, 0).perform()
action.release().perform()

# 切回默认的iframe中
driver.switch_to.default_content()

# 找到验证码输入框并输入验证码
code_input = driver.find_element_by_name("captchaCode")
code_input.send_keys("1234")

# 找到登录按钮并点击
login_button = driver.find_element_by_class_name("submit-button")
login_button.click()

# 关闭浏览器
driver.quit()
