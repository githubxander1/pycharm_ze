from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

# driver=webdriver.Edge()
driver=webdriver.Chrome()
driver.get('https://cc-test.tostar.top/login')
driver.implicitly_wait(10)

driver.find_element(By.NAME,'username').send_keys('xiaozehua')
driver.find_element(By.NAME,'password').send_keys('a1234567')
driver.find_element(By.CSS_SELECTOR,'#app > div > form > button').click()

driver.find_element(By.CSS_SELECTOR,'#app > div > div.main-container > section > div > div.project-list.el-row > div:nth-child(6) > img').click()
# 点击新建活动
driver.find_element(By.CSS_SELECTOR,'#app > div > div.right > div.inner > div > div.status-container > div > div.create-plan.search-btn > button > span').click()
# 选择bv
driver.find_element(By.CSS_SELECTOR,'#app > div > div.right > div.inner > div > div.el-dialog__wrapper > div > div.el-dialog__body > div > div:nth-child(4) > div > img').click()
# 点击下一步
driver.find_element(By.CSS_SELECTOR,'#app > div > div.right > div.inner > div > div.el-dialog__wrapper > div > div.el-dialog__footer > span > span > button.el-button.el-button--primary.el-button--mini > span').click()
# 选择新用户注册
driver.find_element(By.CSS_SELECTOR,'#app > div > div.right > div.inner > div > div.el-dialog__wrapper > div > div.el-dialog__body > div > div.template-wrap > div:nth-child(1) > div > img').click()
# 点击确定
sleep(2)
# driver.find_element(By.CSS_SELECTOR,'#app > div > div.right > div.inner > div > div.el-dialog__wrapper > div > div.el-dialog__footer > span > span > button.el-button.el-button--primary.el-button--mini > span').click()
driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[6]/div/div[3]/span/span/button[2]/span').click()
sleep(2)
driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[4]/div[1]/div[3]/table/tbody/tr[1]/td[10]/div/button[1]/span').click()
sleep(2)

driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[1]/div[2]/div/div[2]/div/label[1]/span[1]/span').click()
driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[1]/div[3]/div/div/div/input').send_keys('https://bvwebtestevent.tostar.top')
driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[1]/div[3]/div/div/div/input').send_keys('https://bvh5testevent.tostar.top')
# 日期
driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[1]/div[6]/div/div/input[1]').click()
driver.find_element(By.XPATH,'/html/body/div[8]/div[1]/div/div[2]/table/tbody/tr[6]/td[4]/div/span').click()

