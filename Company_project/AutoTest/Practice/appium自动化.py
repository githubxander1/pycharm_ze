from select import select

from selenium import webdriver
import time
from selenium.webdriver.common.by import By

d=webdriver.Chrome()
d.get('https://www.saucedemo.com/inventory.html')

# 登录
#通过ID查找
d.find_element(By.ID,'user-name').send_keys('standard_user')
#通过NAME查找
d.find_element(By.NAME,'password').send_keys('secret_sauce')
#通过CSS_SELECTOR查找
d.find_element(By.CSS_SELECTOR,'#login-button').click()

#首页
d.find_element(By.CSS_SELECTOR,'#header_container > div.header_secondary_container > div.right_component > span > select').click()
# 添加1个商品
d.find_element(By.CSS_SELECTOR,'#add-to-cart-sauce-labs-backpack').click()
time.sleep(2)
#进入购物车
d.find_element(By.CSS_SELECTOR,'#shopping_cart_container > a').click()
#继续添加商品
d.find_element(By.ID,'continue-shopping').click()
#再次添加1个商品
d.find_element(By.ID,'add-to-cart-sauce-labs-bike-light').click()
#再次进入购物车
d.find_element(By.CSS_SELECTOR,'#shopping_cart_container > a').click()
time.sleep(2)
#checkout
d.find_element(By.ID,'checkout').click()
d.find_element(By.ID,'first-name').send_keys('No.1')
d.find_element(By.ID,'last-name').send_keys('No.2')
d.find_element(By.ID,'postal-code').send_keys('postal-code')
d.find_element(By.ID,'continue').click()
#完成
d.find_element(By.ID,'finish').click()
d.find_element(By.ID,'back-to-products').click()
#侧边栏
# d.find_element(By.CSS_SELECTOR,'#react-burger-menu-btn').click()
# d.find_element(By.XPATH,'//*[@id="about_sidebar_link"]').click()
#首页
# drop=d.find_element(By.CSS_SELECTOR,'#header_container > div.header_secondary_container > div.right_component > span > select')
d.find_element(By.CSS_SELECTOR,'#header_container > div.header_secondary_container > div.right_component > span > select > option:nth-child(4)').click()
# select1=select(drop)
# select1.select_by_index(1)
# select1.click()



time.sleep(3)
# d.close()