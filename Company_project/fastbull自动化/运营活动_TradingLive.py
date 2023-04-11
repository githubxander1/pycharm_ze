import time
import webbrowser

from selenium import webdriver
from selenium.webdriver import ActionChains
import pyperclip#剪贴板复制粘贴
from selenium.webdriver.support.select import Select

d=webdriver.Chrome()

d.get('https://tradinglive-testwebpc.tostar.top/cn/user/setting/personalData?type=0')
# d.maximize_window()
#
d.implicitly_wait(5)
# 跳过引导蒙层
d.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/a[1]/span').click()
# 悬停在活动icon上
icon=d.find_element_by_xpath('//*[@id="app"]/div[6]/ul/li[1]/div/span/span/div/img')
ActionChains(d).move_to_element(icon).perform()
time.sleep(2)
# # F12--resource--ctrl+\
# 用完整的xpath定位
d.find_element_by_xpath('/html/body/div[2]/div[1]/div').click()

# 点击登录
iframe=d.find_element_by_xpath('/html/body/div[3]/div/div[2]/iframe')
d.switch_to.frame(iframe)
d.find_element_by_xpath('//*[@id="invitation"]/div[2]/div[1]/div').click()
time.sleep(2)
# 登录
# select1=d.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div/div/form/div[1]/form/div/div[1]/div/div/input')
# select1=d.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/form/div[1]/form/div/div[1]/div/div/input')
d.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div/div/form/div[1]/form/div/div[1]/div/div[1]/input').click()
# select1=d.find_element_by_css_selector('#app > div.container-layer.app-view.bg > div.container_content > div > div > form > div.phone-verification-component > form > div > div.region-layer.isolate.text-left.el-col.el-col-8 > div > div.el-input.el-input--suffix > input')

# select1=d.find_element_by_css_selector('#app > div.container-layer.app-view.bg > div.container_content > div > div > form > div.phone-verification-component > form > div > div.region-layer.isolate.text-left.el-col.el-col-8 > div > div.el-input.el-input--suffix')
# Select(select1).select_by_visible_text('香港')





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
