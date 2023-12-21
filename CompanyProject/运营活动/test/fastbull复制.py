import webbrowser

from selenium import webdriver
from selenium.webdriver import ActionChains
import pyperclip#剪贴板复制粘贴
d=webdriver.Chrome()

d.get('https://testfbtw.tostar.top/')
# d.maximize_window()

d.implicitly_wait(5)
# d.WebDriverWait(5)
# 第一种打开方式
d.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[7]/div[5]').click()
d.find_element_by_id('inputMailText').send_keys('101@qq.com')
d.find_element_by_id('inputMailPwd').send_keys('a1234567')
d.find_element_by_id('mailBtn').click()
d.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[7]/div[5]').click()
# d.close()
# 第二种打开方式
# active=d.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[7]/div[5]')
# ActionChains(d).move_to_element(active).perform()
# d.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[7]/div[5]/div/div[3]').click()
# d.find_element_by_id('inputMailText').send_keys('101@qq.com')
# d.find_element_by_id('inputMailPwd').send_keys('a1234567')
# d.find_element_by_id('mailBtn').click()
# active=d.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[7]/div[5]')
# ActionChains(d).move_to_element(active).perform()
# d.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[7]/div[5]/div/div[3]').click()

d.switch_to.frame(d.find_element_by_id('popup-active-iframe'))
d.find_element_by_css_selector('#invitation > div > div.invitation-content > div.input-wrap > span').click()
copy_url=pyperclip.paste()#剪贴板粘贴
print(copy_url)
# js="window.open('{}'.format(copy_url))"
# js='window.open("%s %(copy_url))'
# js='window.open("f{copy_url}")'
js='window.open("https://operational-h5-test.tostar.top/share?activityId=56&clientType=5&deviceId=1e583e9d4563723661782e0fa9567466&langId=2&productId=26&userId=204288")'
d.execute_script(js)
handles = d.window_handles
print(handles)
# 获取当前窗口句柄集合(列表类型)
d.switch_to.window(handles[1])
