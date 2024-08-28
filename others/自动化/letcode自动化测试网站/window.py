from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By

driver=webdriver.Edge()
driver.get('https://letcode.in/windows')

# 获取当前句柄
current_window=driver.current_window_handle
print('未开新窗口前，当前窗口句柄'+current_window,'标题'+driver.title)
# 获取所有窗口句柄
handers=driver.window_handles
print(f'未开新窗口前，所有窗口句柄1:{handers}')

driver.find_element(By.ID,'multi').click()
print('开新窗口1')
# 再获取所有窗口句柄
handers=driver.window_handles
print(f'开新窗口后，所有窗口句柄2:{handers}')
for hander in handers:
    driver.switch_to.window(hander)
    print('所有窗口的标题：'+driver.title)

driver.switch_to.window(handers[0])
print('返回到原窗口')
driver.find_element(By.ID,'multi').click()
print('开新窗口2')
# 再获取所有窗口句柄
handers1=driver.window_handles
print(f'开新窗口后，所有窗口句柄3:{handers1}')
print('第二次开新窗口后，当前窗口句柄:'+driver.current_window_handle,'标题'+driver.title)
sleep(3)
