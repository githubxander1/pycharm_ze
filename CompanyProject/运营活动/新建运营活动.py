from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# driver=webdriver.Edge()
driver=webdriver.Chrome()
driver.get('https://cc-test.tostar.top/login')
driver.implicitly_wait(10)

driver.find_element(By.NAME,'username').send_keys('xiaozehua')
driver.find_element(By.NAME,'password').send_keys('a1234567')
driver.find_element(By.CSS_SELECTOR,'#app > div > form > button').click()

driver.find_element(By.CSS_SELECTOR,'#app > div > div.main-container > section > div > div.project-list.el-row > div:nth-child(6) > img').click()
# # # # 点击新建活动
# driver.find_element(By.CSS_SELECTOR,'#app > div > div.right > div.inner > div > div.status-container > div > div.create-plan.search-btn > button > span').click()
# # # 选择bv
# driver.find_element(By.CSS_SELECTOR,'#app > div > div.right > div.inner > div > div.el-dialog__wrapper > div > div.el-dialog__body > div > div:nth-child(4) > div > img').click()
# # # 点击下一步
# driver.find_element(By.CSS_SELECTOR,'#app > div > div.right > div.inner > div > div.el-dialog__wrapper > div > div.el-dialog__footer > span > span > button.el-button.el-button--primary.el-button--mini > span').click()
# # # 选择新用户注册
# driver.find_element(By.CSS_SELECTOR,'#app > div > div.right > div.inner > div > div.el-dialog__wrapper > div > div.el-dialog__body > div > div.template-wrap > div:nth-child(1) > div > img').click()
# # # 点击确定
# sleep(2)
# driver.find_element(By.CSS_SELECTOR,'#app > div > div.right > div.inner > div > div.el-dialog__wrapper > div > div.el-dialog__footer > span > span > button.el-button.el-button--primary.el-button--mini > span').click()
# # driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[6]/div/div[3]/span/span/button[2]/span').click()
# sleep(2)
# 点击编辑活动
driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[4]/div[1]/div[3]/table/tbody/tr[1]/td[10]/div/button[1]/span').click()
# sleep(2)
#
driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[1]/div[2]/div/div[2]/div/label[1]/span[1]/span').click()
driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[1]/div[3]/div/div/div/input').send_keys('https://bvwebtestevent.tostar.top')
driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[1]/div[4]/div/div[1]/div/input').send_keys('https://bvh5testevent.tostar.top')
# 奖品类型
# driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[2]/div[3]/div/div/div/input').click()
# driver.find_element(By.XPATH,'/html/body/div[7]/div[1]/div[1]/ul/li/span').click()

elm = driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[2]/div[3]/div/div/div/input')
js = 'arguments[0].removeAttribute("readonly");'
driver.execute_script(js, elm)
sleep(0.5)
elm.clear()
elm.send_keys('USD')
# 日期
sleep(1)
# driver.find_element(By.XPATH,'/html/body/div[7]/div[1]/div/div[2]/table/tbody/tr[4]/td[3]/div/span').click()
driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[1]/div[6]/div/div/input[1]').send_keys('2023-10-04 00:00:00')
sleep(1)
# driver.find_element(By.XPATH,'/html/body/div[8]/div[1]/div/div[2]/table/tbody/tr[6]/td[4]/div/span').click()
driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[1]/div[6]/div/div/input[2]').send_keys('2023-11-16 23:59:59')
# driver.find_element(By.XPATH,'/html/body/div[7]/div[2]/button[2]/span').click()
# 提现网络
driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[2]/div[4]/div/div/input').send_keys("TRC20")
# 奖金参数
driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[2]/div[5]/div/div/div[1]/label/span[1]/span').click()
driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[2]/div[5]/div/div/div[1]/label/span[2]/span/div/input').send_keys(300)
# 特殊国家
# driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[2]/div[6]/div/div/div[3]/table/tbody/tr[1]/td[2]/div/div/input').send_keys(40)
# driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[2]/div[6]/div/div/div[3]/table/tbody/tr[1]/td[3]/div/div/input').send_keys(1000)
# driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[2]/div[6]/div/div/div[3]/table/tbody/tr[2]/td[2]/div/div/input').send_keys(5)
# driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[2]/div[6]/div/div/div[3]/table/tbody/tr[2]/td[3]/div/div/input').send_keys(100)
#
# driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[2]/div[6]/div/div/div[3]/table/tbody/tr[2]/td[2]/div/div/input').send_keys(8)
# driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[2]/div[6]/div/div/div[3]/table/tbody/tr[2]/td[3]/div/div/input').send_keys(100)
#
# driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[2]/div[6]/div/div/div[3]/table/tbody/tr[2]/td[2]/div/div/input').send_keys(50)
# driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[2]/div[6]/div/div/div[3]/table/tbody/tr[2]/td[3]/div/div/input').send_keys(1000)
#
# driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[2]/div[6]/div/div/div[3]/table/tbody/tr[2]/td[2]/div/div/input').send_keys(10)
# driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[2]/div[6]/div/div/div[3]/table/tbody/tr[2]/td[3]/div/div/input').send_keys(200)
#
# driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[2]/div[6]/div/div/div[3]/table/tbody/tr[2]/td[2]/div/div/input').send_keys(2)
# driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[2]/div[6]/div/div/div[3]/table/tbody/tr[2]/td[3]/div/div/input').send_keys(50)
#
# driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[2]/div[6]/div/div/div[3]/table/tbody/tr[2]/td[2]/div/div/input').send_keys(2)
# driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[2]/div[6]/div/div/div[3]/table/tbody/tr[2]/td[3]/div/div/input').send_keys(50)
# 关联奖金配置
sleep(2)
fixed_button = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/div[3]/form/div/div/div/div[1]/label/span[1]')

# 将鼠标移动到目标元素上方
actions = ActionChains(driver)
actions.move_to_element(fixed_button).perform()

# 等待一段时间，确保目标元素可点击
driver.implicitly_wait(5)

# 点击目标元素
fixed_button.click()
# driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/div[3]/form/div/div/div/div[1]/label/span[1]/span').click()
driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/div[3]/form/div/div/div/div[1]/label/span[2]/span/div/input').send_keys(1)

# 客户端展示信息
# 简中
driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[1]/label[1]/span').click()#点击简中
driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[2]/div/div/input').send_keys('活动入口')
driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[3]/div/div/input').send_keys('名称')
driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[4]/div/div/textarea').send_keys('主态')
driver.find_element(By.XPATH,'/html').send_keys('主态')

gaishu=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[5]/div/div/div/div[1]/div[2]/div[1]/iframe')
driver.switch_to.frame(gaishu)#切换到iframe
driver.find_element(By.TAG_NAME,'body').clear()#清空内容
driver.find_element(By.TAG_NAME,'body').send_keys('活动规则概述')
driver.switch_to.default_content()#切换回默认的上下文

driver.switch_to.frame(driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[6]/div/div/div/div[1]/div[2]/div[1]/iframe'))
driver.find_element(By.TAG_NAME,'body').clear()#清空内容
driver.find_element(By.ID,'tinymce').send_keys('活动规则')
driver.switch_to.default_content()#切换回默认的上下文

driver.switch_to.frame(driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[7]/div/div/div/div[1]/div[2]/div[1]/iframe'))
driver.find_element(By.TAG_NAME,'body').clear()#清空内容
driver.find_element(By.ID,'tinymce').send_keys('提现规则')
driver.switch_to.default_content()#切换回默认的上下文

driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[8]/div/div[1]/textarea').send_keys('客态-奖励')

driver.switch_to.frame(driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[6]/div/div/div/div[1]/div[2]/div[1]/iframe'))
driver.find_element(By.TAG_NAME,'body').clear()#清空内容
driver.find_element(By.ID,'tinymce').send_keys('被邀请页注意事项')
driver.switch_to.default_content()#切换回默认的上下文'))

sleep(2)
# 繁中
driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[1]/label[2]/span').click()#点击繁中
driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[2]/div/div/input').send_keys('活动入口-2')
driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[3]/div/div/input').send_keys('名称')
driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[4]/div/div/textarea').send_keys('主态')
driver.find_element(By.XPATH,'/html').send_keys('主态')

gaishu=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[5]/div/div/div/div[1]/div[2]/div[1]/iframe')
driver.switch_to.frame(gaishu)#切换到iframe
driver.find_element(By.TAG_NAME,'body').clear()#清空内容
driver.find_element(By.TAG_NAME,'body').send_keys('活动规则概述')
driver.switch_to.default_content()#切换回默认的上下文

driver.switch_to.frame(driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[6]/div/div/div/div[1]/div[2]/div[1]/iframe'))
driver.find_element(By.TAG_NAME,'body').clear()#清空内容
driver.find_element(By.ID,'tinymce').send_keys('活动规则')
driver.switch_to.default_content()#切换回默认的上下文

driver.switch_to.frame(driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[7]/div/div/div/div[1]/div[2]/div[1]/iframe'))
driver.find_element(By.TAG_NAME,'body').clear()#清空内容
driver.find_element(By.ID,'tinymce').send_keys('提现规则')
driver.switch_to.default_content()#切换回默认的上下文

driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[8]/div/div[1]/textarea').send_keys('客态-奖励')

driver.switch_to.frame(driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[6]/div/div/div/div[1]/div[2]/div[1]/iframe'))
driver.find_element(By.TAG_NAME,'body').clear()#清空内容
driver.find_element(By.ID,'tinymce').send_keys('被邀请页注意事项-2')
driver.switch_to.default_content()#切换回默认的上下文'))
sleep(2)

# 英语
driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[1]/label[3]/span').click()#点击英语
driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[2]/div/div/input').send_keys('活动入口-2')
driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[3]/div/div/input').send_keys('名称')
driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[4]/div/div/textarea').send_keys('主态')
driver.find_element(By.XPATH,'/html').send_keys('主态')

gaishu=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[5]/div/div/div/div[1]/div[2]/div[1]/iframe')
driver.switch_to.frame(gaishu)#切换到iframe
driver.find_element(By.TAG_NAME,'body').clear()#清空内容
driver.find_element(By.TAG_NAME,'body').send_keys('活动规则概述')
driver.switch_to.default_content()#切换回默认的上下文

driver.switch_to.frame(driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[6]/div/div/div/div[1]/div[2]/div[1]/iframe'))
driver.find_element(By.TAG_NAME,'body').clear()#清空内容
driver.find_element(By.ID,'tinymce').send_keys('活动规则')
driver.switch_to.default_content()#切换回默认的上下文

driver.switch_to.frame(driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[7]/div/div/div/div[1]/div[2]/div[1]/iframe'))
driver.find_element(By.TAG_NAME,'body').clear()#清空内容
driver.find_element(By.ID,'tinymce').send_keys('提现规则')
driver.switch_to.default_content()#切换回默认的上下文

driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[8]/div/div[1]/textarea').send_keys('客态-奖励')

driver.switch_to.frame(driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[6]/div/div/div/div[1]/div[2]/div[1]/iframe'))
driver.find_element(By.TAG_NAME,'body').clear()#清空内容
driver.find_element(By.ID,'tinymce').send_keys('被邀请页注意事项-2')
driver.switch_to.default_content()#切换回默认的上下文'))
sleep(2)

# 阿语
driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[1]/label[4]').click()#点击阿语
driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[2]/div/div/input').send_keys('活动入口-2')
driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[3]/div/div/input').send_keys('名称')
driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[4]/div/div/textarea').send_keys('主态')
driver.find_element(By.XPATH,'/html').send_keys('主态')

gaishu=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[5]/div/div/div/div[1]/div[2]/div[1]/iframe')
driver.switch_to.frame(gaishu)#切换到iframe
driver.find_element(By.TAG_NAME,'body').clear()#清空内容
driver.find_element(By.TAG_NAME,'body').send_keys('活动规则概述')
driver.switch_to.default_content()#切换回默认的上下文

driver.switch_to.frame(driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[6]/div/div/div/div[1]/div[2]/div[1]/iframe'))
driver.find_element(By.TAG_NAME,'body').clear()#清空内容
driver.find_element(By.ID,'tinymce').send_keys('活动规则')
driver.switch_to.default_content()#切换回默认的上下文

driver.switch_to.frame(driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[7]/div/div/div/div[1]/div[2]/div[1]/iframe'))
driver.find_element(By.TAG_NAME,'body').clear()#清空内容
driver.find_element(By.ID,'tinymce').send_keys('提现规则')
driver.switch_to.default_content()#切换回默认的上下文

driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[8]/div/div[1]/textarea').send_keys('客态-奖励')

driver.switch_to.frame(driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[6]/div/div/div/div[1]/div[2]/div[1]/iframe'))
driver.find_element(By.TAG_NAME,'body').clear()#清空内容
driver.find_element(By.ID,'tinymce').send_keys('被邀请页注意事项-2')
driver.switch_to.default_content()#切换回默认的上下文'))
sleep(2)

# 泰语
driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[1]/label[5]/span').click()#点击泰语
driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[2]/div/div/input').send_keys('活动入口-2')
driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[3]/div/div/input').send_keys('名称')
driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[4]/div/div/textarea').send_keys('主态')
driver.find_element(By.XPATH,'/html').send_keys('主态')

gaishu=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[5]/div/div/div/div[1]/div[2]/div[1]/iframe')
driver.switch_to.frame(gaishu)#切换到iframe
driver.find_element(By.TAG_NAME,'body').clear()#清空内容
driver.find_element(By.TAG_NAME,'body').send_keys('活动规则概述')
driver.switch_to.default_content()#切换回默认的上下文

driver.switch_to.frame(driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[6]/div/div/div/div[1]/div[2]/div[1]/iframe'))
driver.find_element(By.TAG_NAME,'body').clear()#清空内容
driver.find_element(By.ID,'tinymce').send_keys('活动规则')
driver.switch_to.default_content()#切换回默认的上下文

driver.switch_to.frame(driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[7]/div/div/div/div[1]/div[2]/div[1]/iframe'))
driver.find_element(By.TAG_NAME,'body').clear()#清空内容
driver.find_element(By.ID,'tinymce').send_keys('提现规则')
driver.switch_to.default_content()#切换回默认的上下文

driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[8]/div/div[1]/textarea').send_keys('客态-奖励')

driver.switch_to.frame(driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[6]/div/div/div/div[1]/div[2]/div[1]/iframe'))
driver.find_element(By.TAG_NAME,'body').clear()#清空内容
driver.find_element(By.ID,'tinymce').send_keys('被邀请页注意事项-2')
driver.switch_to.default_content()#切换回默认的上下文'))
sleep(2)

# 越南语
driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[1]/label[6]/span').click()#点击越南语
driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[2]/div/div/input').send_keys('活动入口-2')
driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[3]/div/div/input').send_keys('名称')
driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[4]/div/div/textarea').send_keys('主态')
driver.find_element(By.XPATH,'/html').send_keys('主态')

gaishu=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[5]/div/div/div/div[1]/div[2]/div[1]/iframe')
driver.switch_to.frame(gaishu)#切换到iframe
driver.find_element(By.TAG_NAME,'body').clear()#清空内容
driver.find_element(By.TAG_NAME,'body').send_keys('活动规则概述')
driver.switch_to.default_content()#切换回默认的上下文

driver.switch_to.frame(driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[6]/div/div/div/div[1]/div[2]/div[1]/iframe'))
driver.find_element(By.TAG_NAME,'body').clear()#清空内容
driver.find_element(By.ID,'tinymce').send_keys('活动规则')
driver.switch_to.default_content()#切换回默认的上下文

driver.switch_to.frame(driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[7]/div/div/div/div[1]/div[2]/div[1]/iframe'))
driver.find_element(By.TAG_NAME,'body').clear()#清空内容
driver.find_element(By.ID,'tinymce').send_keys('提现规则')
driver.switch_to.default_content()#切换回默认的上下文

driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[8]/div/div[1]/textarea').send_keys('客态-奖励')

driver.switch_to.frame(driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[6]/div/div/div/div[1]/div[2]/div[1]/iframe'))
driver.find_element(By.TAG_NAME,'body').clear()#清空内容
driver.find_element(By.ID,'tinymce').send_keys('被邀请页注意事项-2')
driver.switch_to.default_content()#切换回默认的上下文'))
sleep(2)

# 印尼语
driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[1]/label[7]/span').click()#点击印尼语
driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[2]/div/div/input').send_keys('活动入口-2')
driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[3]/div/div/input').send_keys('名称')
driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[4]/div/div/textarea').send_keys('主态')
driver.find_element(By.XPATH,'/html').send_keys('主态')

gaishu=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[5]/div/div/div/div[1]/div[2]/div[1]/iframe')
driver.switch_to.frame(gaishu)#切换到iframe
driver.find_element(By.TAG_NAME,'body').clear()#清空内容
driver.find_element(By.TAG_NAME,'body').send_keys('活动规则概述')
driver.switch_to.default_content()#切换回默认的上下文

driver.switch_to.frame(driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[6]/div/div/div/div[1]/div[2]/div[1]/iframe'))
driver.find_element(By.TAG_NAME,'body').clear()#清空内容
driver.find_element(By.ID,'tinymce').send_keys('活动规则')
driver.switch_to.default_content()#切换回默认的上下文

driver.switch_to.frame(driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[7]/div/div/div/div[1]/div[2]/div[1]/iframe'))
driver.find_element(By.TAG_NAME,'body').clear()#清空内容
driver.find_element(By.ID,'tinymce').send_keys('提现规则')
driver.switch_to.default_content()#切换回默认的上下文

driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[8]/div/div[1]/textarea').send_keys('客态-奖励')

driver.switch_to.frame(driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[6]/div/div/div/div[1]/div[2]/div[1]/iframe'))
driver.find_element(By.TAG_NAME,'body').clear()#清空内容
driver.find_element(By.ID,'tinymce').send_keys('被邀请页注意事项-2')
driver.switch_to.default_content()#切换回默认的上下文'))
sleep(2)

driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/div[6]/div[2]/button/span').click()
sleep(2)