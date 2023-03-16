# class animal:
#     age=0
#     def __init__(self,name):
#         self.name=name
#
#     def run(self):
#         print(f'{self.name}跑起来了')
#
# # if __name__ =='main':
# #     animal.run('gou')
#
# # dog=animal(name='gou')
# # dog.run()
#
# dog=animal(name='gou')
# animal.run(dog)

# class animal:
#     age=0
#     def __init__(self,name):
#         self.name=name
#
#     def run(self):
#         print(f'{self.name}跑了')
#
# dog=animal(name='1')
# # dog.run()
# animal.run(dog)

# coding=utf-8

from selenium import webdriver

browser=webdriver.Chrome()
browser.maximize_window()  # 窗口最大化

browser.get('https://www.baidu.com')  # 在当前浏览器中访问百度

# 新开一个窗口，通过执行js来新开一个窗口
js='window.open("https://www.sogou.com");'
browser.execute_script(js)

# print (browser.current_window_handle)  # 输出当前窗口句柄（百度）
# handles = (browser.window_handles)  # 获取当前窗口句柄集合（列表类型）
# print (handles)  # 输出句柄集合
#
# for handle in handles:# 切换窗口（切换到搜狗）
#     if handle!=browser.current_window_handle:
#         print ('switch to ',handle)
#         browser.switch_to.window(handle)
#         print (browser.current_window_handle)  # 输出当前窗口句柄（搜狗）
#         break
#
# browser.close()  # 关闭当前窗口（搜狗）
# browser.switch_to.window(handles[0])  # 切换回百度窗口
# import time
# time.sleep(10)
# browser.quit()