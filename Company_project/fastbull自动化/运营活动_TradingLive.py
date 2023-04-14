import time
import webbrowser
# from telnetlib import EC

from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver import ActionChains
import pyperclip#剪贴板复制粘贴
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

d=webdriver.Edge()
d.get('https://tradinglive-testwebpc.tostar.top/cn/login')
# d.maximize_window()

# d.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div/div/div[1]/span[2]').click()
WebDriverWait(driver=d, timeout=30, ignored_exceptions=None).until(EC.presence_of_all_elements_located(
    (By.XPATH, '//div[contains(@class,"region-select")]//input')))
number = "+852"
# 输入区号
d.find_element_by_xpath('//div[contains(@class,"region-select")]//input').send_keys(number)
time.sleep(1)
# 选择区号
d.find_element_by_xpath('//li[contains(string(),"{}")]'.format(number)).click()
time.sleep(1)
d.find_element_by_css_selector('[placeholder="请输入手机号"]').send_keys('91111111')
# 点击获取验证码
d.find_element_by_css_selector(
'#app > div.container-layer.app-view.bg > div.container_content > div > div > form > div.phone-verification-component > form > div > div.el-col.el-col-10 > button > span').click()

time.sleep(2)
#切换到弹窗
iframe = d.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div/div/form/div[1]/div[2]/iframe')
d.switch_to.frame(iframe)
# 定位滑块元素
# 获取滑块背景的大小
span_background = d.find_element_by_xpath('//*[@id="app"]/main/div/div/div[2]')
span_background_size = span_background.size
print('滑块背景大小：',span_background_size)
# 获取滑块的位置
button = d.find_element_by_xpath('//*[@id="app"]/main/div/div/div[2]/i')
button_location = button.location
print('滑块位置：',button_location)
# 拖动操作：drag_and_drop_by_offset
# 将滑块的位置由初始位置，右移一个滑动条长度（即为x坐标在滑块位置基础上，加上滑动条的长度，y坐标保持滑块的坐标位置）
x_location = span_background_size["width"]
y_location = button_location["y"]
button_end_location = button_location['x']+x_location
print(button_end_location)
print('滑块移动的位置：',button_end_location, y_location)

source = WebDriverWait(d, 30).until(EC.presence_of_element_located(
    (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/i')))
ActionChains(d).click_and_hold(on_element=source).perform()
ActionChains(d).move_to_element_with_offset(source, xoffset=x_location, yoffset=y_location).perform()
time.sleep(0.3)
ActionChains(d).pause(1).release().perform()






# 点击登录
# d.find_element_by_css_selector('#app > div.container-layer.app-view.bg > div.container_content > div > div > form > p:nth-child(3) > button > span').click()
# d.find_element_by_xpath('//div[contains(@class,"region-select")]//input').send_keys("+852")
# d.find_element_by_css_selector('[placeholder="请输入手机号"]').send_keys('91111111')
#
# d.find_element_by_css_selector('input').click()
# d.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li[3]/span[1]').click()
# d.find_element_by_css_selector('[placeholder="请输入手机号"]').send_keys('91111111')
# select1=d.find_element_by_css_selector('#app > div.container-layer.app-view.bg > div.container_content > div > div > form > div.phone-verification-component > form > div > div.region-layer.isolate.text-left.el-col.el-col-8 > div > div.el-input.el-input--suffix')
# Select(select1).select_by_visible_text('香港')
# d.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div/div/div[1]/span[2]').click()
# d.find_element_by_css_selector('#app > div.container-layer.app-view.bg > div.container_content > div > div > div.type_list.isolate > span.login_type.email').click()

# 邮箱登录
# d.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div/div/div[2]/form/div[1]/div/div/div/div/input').send_keys('1@qq.com')
# d.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div/div/div[2]/form/div[2]/div/div/div/div/input').send_keys('a1234567')
# d.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div/div/div[2]/form/div[4]/button/span').click()




# # 第一种打开方式
# d.find_element_by_xpath('/html/body/div[2]/div[1]/div[7]/div[5]').click()
# d.find_element_by_id('inputMailText').send_keys('99@qq.com')
# d.find_element_by_id('inputMailPwd').send_keys('a1234567')
# d.find_element_by_id('mailBtn').click()
# d.find_element_by_xpath('/html/body/div[2]/div[1]/div[7]/div[5]').click()
# # d.close()
# # 第二种打开方式
# # active=d.find_element_by_xpath('/html/body/div[2]/div[1]/div[7]/div[5]')
# # ActionChains(d).move_to_element(active).perform()
# # d.find_element_by_xpath('/html/body/div[2]/div[1]/div[7]/div[5]/div/div[3]').click()
# # d.find_element_by_id('inputMailText').send_keys('101@qq.com')
# # d.find_element_by_id('inputMailPwd').send_keys('a1234567')
# # d.find_element_by_id('mailBtn').click()
# # active=d.find_element_by_xpath('/html/body/div[2]/div[1]/div[7]/div[5]')
# # ActionChains(d).move_to_element(active).perform()
# # d.find_element_by_xpath('/html/body/div[2]/div[1]/div[7]/div[5]/div/div[3]').click()
#
# d.switch_to.frame(d.find_element_by_id('popup-active-iframe'))
# # 点击复制按钮
# d.find_element_by_css_selector('#invitation > div > div.invitation-content > div.input-wrap > span').click()
# copy_url=pyperclip.paste()#剪贴板粘贴
# print("copy_url:",copy_url)
# # js="window.open('{}'.format(copy_url))"
# # js='window.open("%s %(copy_url))'
# # js='window.open("f{copy_url}")'
# js=f'window.open("{copy_url}")'
# print("js:",js)
# d.execute_script(js)
# # 获取当前窗口句柄集合(列表类型)
# handles = d.window_handles
# print(handles)
# d.switch_to.window(handles[1])
