import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 创建浏览器实例并打开网页
browser = webdriver.Chrome()
url = "https://tradinglive-testwebpc.tostar.top/cn/login"
browser.get(url)

# 点击下拉框并选择"852香港"
WebDriverWait(driver=browser, timeout=30, ignored_exceptions=None).until(EC.presence_of_all_elements_located(
    (By.XPATH, '//div[contains(@class,"region-select")]//input')))
number = "+852"
# 输入区号
browser.find_element_by_xpath('//div[contains(@class,"region-select")]//input').send_keys(number)
time.sleep(1)
# 选择区号
browser.find_element_by_xpath('//li[contains(string(),"{}")]'.format(number)).click()
time.sleep(1)

# area_code_btn = browser.find_element_by_css_selector("#app > div > div.login-container > div > div.form-container > div.form-content > form > div.form-items > div:nth-child(1) > div.el-select > div")
# area_code_btn.click()
# hk_option = browser.find_element_by_xpath('//li/span[text()="香港"]')
# hk_option.click()

# 输入手机号和密码
phone_input = browser.find_element_by_css_selector("input[placeholder='请输入手机号']")
phone_input.send_keys("91111110")
# password_input = browser.find_element_by_css_selector("input[placeholder='请输入密码']")
# password_input.send_keys("a1234567")

# 滑块验证码识别及滑动
browser.find_element_by_css_selector(
'#app > div.container-layer.app-view.bg > div.container_content > div > div > form > div.phone-verification-component > form > div > div.el-col.el-col-10 > button > span').click()
# 定位滑块元素
iframe = browser.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div/div/form/div[1]/div[2]/iframe')

browser.switch_to.frame(iframe)

# 获取滑块背景的大小
# slider = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#verifyCode")))
# span_background = browser.find_element_by_xpath('//*[@id="app"]/main/div/div/div[2]')
slider_bg = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='app']/main/div/div/div[2]")))
slider_handle = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='app']/main/div/div/div[2]/i")))
slide_distance = slider_bg.size['width'] - slider_handle.size['width']
actions = ActionChains(browser)
actions.click_and_hold(slider_handle).perform()
actions.move_by_offset(slide_distance, 0).perform()
actions.release().perform()

# 输入验证码并点击登录
verify_code_input = browser.find_element_by_css_selector("input[placeholder='请输入验证码']")
verify_code_input.send_keys("1234")
login_btn = browser.find_element_by_css_selector("#app > div > div.login-container > div > div.form-container > div.form-content > form > div.form-items > div:nth-child(5) > div > button")
login_btn.click()
