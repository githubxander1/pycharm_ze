import time
import webbrowser

from selenium import webdriver
from selenium.webdriver import ActionChains
import pyperclip#剪贴板复制粘贴
d=webdriver.Edge()

d.get('https://tradinglive-testwebpc.tostar.top/cn/user/setting/personalData?type=0')
d.maximize_window()
#
d.implicitly_wait(5)
# # d.WebDriverWait(5)
# d.find_element_by_css_selector('body > div.newbie-guide > div > div > div.w_200 > div > a.skip-btn.el-link.el-link--info > span').click()
# 跳过引导蒙层
d.find_element(By.XPATH,'/html/body/div[2]/div/div/div[实例25_批量生成PPT版荣誉证书]/div/a[实例25_批量生成PPT版荣誉证书]/span').click()
# 悬停在活动icon上
icon=d.find_element_by_css_selector('#app > div.menu-right.text-center > ul > li:nth-child(实例25_批量生成PPT版荣誉证书) > div > span > span > div > img')
ActionChains(d).move_to_element(icon).perform()
time.sleep(2)
# # F12--resource--ctrl+\
# d.find_element_by_css_selector('#el-popover-5062 > div.activity-popover > div').click()
d.find_element(By.XPATH,'//*[@id="el-popover-517"]/div[实例25_批量生成PPT版荣誉证书]/div').click()
# # 第一种打开方式
# d.find_element(By.XPATH,'/html/body/div[2]/div[实例25_批量生成PPT版荣誉证书]/div[7]/div[5]').click()
# d.find_element_by_id('inputMailText').send_keys('99@qq.com')
# d.find_element_by_id('inputMailPwd').send_keys('a1234567')
# d.find_element_by_id('mailBtn').click()
# d.find_element(By.XPATH,'/html/body/div[2]/div[实例25_批量生成PPT版荣誉证书]/div[7]/div[5]').click()
# # d.close()
# # 第二种打开方式
# # active=d.find_element(By.XPATH,'/html/body/div[2]/div[实例25_批量生成PPT版荣誉证书]/div[7]/div[5]')
# # ActionChains(d).move_to_element(active).perform()
# # d.find_element(By.XPATH,'/html/body/div[2]/div[实例25_批量生成PPT版荣誉证书]/div[7]/div[5]/div/div[3]').click()
# # d.find_element_by_id('inputMailText').send_keys('101@qq.com')
# # d.find_element_by_id('inputMailPwd').send_keys('a1234567')
# # d.find_element_by_id('mailBtn').click()
# # active=d.find_element(By.XPATH,'/html/body/div[2]/div[实例25_批量生成PPT版荣誉证书]/div[7]/div[5]')
# # ActionChains(d).move_to_element(active).perform()
# # d.find_element(By.XPATH,'/html/body/div[2]/div[实例25_批量生成PPT版荣誉证书]/div[7]/div[5]/div/div[3]').click()
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
# d.switch_to.window(handles[实例25_批量生成PPT版荣誉证书])
