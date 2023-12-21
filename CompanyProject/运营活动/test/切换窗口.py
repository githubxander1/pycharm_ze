from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyperclip
#创建webdriver对象，字符串前面加r,声明后面的字符串是普通字符串
wd=webdriver.Chrome()
# 设置最大等待时长为 10秒
wd.implicitly_wait(10)
# 调用webdriver的get方法打开网址
wd.get('http://www.baidu.com')
# wd.maximize_window() # 窗口最大化
# #根据id选择元素
element=wd.find_element_by_id('kw')
# 清除输入框已有的字符串
# element.clear()
# #向已选择的元素输入文字，\n表示换行
element.send_keys('www.baidu.com')
element.send_keys(Keys.CONTROL, 'a')  # 全选
element.send_keys(Keys.CONTROL, 'c')  # 复制
#等待2秒
time.sleep(2)
# copy_url=pyperclip.paste
# print(copy_url)
# #打开新标签页
# js = f'window.open("f.{copy_url}");'
js = f'window.open("http://www.baidu.com");'
wd.execute_script(js)
handles = wd.window_handles
# 获取当前窗口句柄集合(列表类型)
wd.switch_to.window(handles[1])
# #切换窗口至第2个
# element=wd.find_element_by_id('kw')
# element.send_keys(Keys.CONTROL, 'v')
# 复制
# wd.find_element(By.XPATH,"//input[@id='su']").click()