import time
import webbrowser
# from telnetlib import EC

from selenium import webdriver
from selenium.webdriver import ActionChains
import pyperclip#剪贴板复制粘贴
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
d=webdriver.Chrome()


d.get('https://tradinglive-testwebpc.tostar.top/cn/user/setting/personalData?type=0')
# # d.maximize_window()
# #
d.implicitly_wait(5)
# # 跳过引导蒙层
d.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/a[1]/span').click()
# 悬停在活动icon上
icon=d.find_element_by_xpath('//*[@id="app"]/div[6]/ul/li[1]/div/span/span/div/img')
ActionChains(d).move_to_element(icon).perform()
time.sleep(2)
# # F12--resource--ctrl+\
# 用完整的xpath定位
d.find_element_by_xpath('/html/body/div[2]/div[1]/div').click()

# 进入邀请弹窗，点击登录
iframe=d.find_element_by_xpath('/html/body/div[3]/div/div[2]/iframe')
d.switch_to.frame(iframe)
d.find_element_by_xpath('//*[@id="invitation"]/div[2]/div[1]/div').click()
time.sleep(3)
# 手机号登录
d.switch_to.window(d.window_handles[0])
WebDriverWait(driver=d,timeout=30, ignored_exceptions=None).until(EC.presence_of_all_elements_located(
  (By.XPATH, '//div[contains(@class,"region-select")]//input')))
number = "+852"
d.find_element_by_xpath('//div[contains(@class,"region-select")]//input').send_keys(number)
time.sleep(1)
d.find_element_by_xpath('//li[contains(string(),"{}")]'.format(number)).click()
time.sleep(1)
d.find_element_by_css_selector('[placeholder="请输入手机号"]').send_keys('91111111')
d.find_element_by_css_selector('#app > div.container-layer.app-view.bg > div.container_content > div > div > form > div.phone-verification-component > form > div > div.el-col.el-col-10 > button > span').click()
d.find_element_by_css_selector('[placeholder="请输入验证码"]').send_keys(1234)
d.find_element_by_xpath('//*[@id="app"]/main/div/div/div[2]/i')
d.find_element_by_css_selector('#app > div.container-layer.app-view.bg > div.container_content > div > div > form > p:nth-child(3) > button > span').click()
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
