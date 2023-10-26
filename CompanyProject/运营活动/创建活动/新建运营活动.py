from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from wenan import CN,EN,TW,ID,TH,AR,VN

driver=webdriver.Edge()
# driver=webdriver.Chrome()
driver.get('https://cc-test.tostar.top/login')
driver.implicitly_wait(10)

project='bv'

def login():
    driver.find_element(By.NAME,'username').send_keys('xiaozehua')
    driver.find_element(By.NAME,'password').send_keys('a1234567')
    driver.find_element(By.CSS_SELECTOR,'#app > div > form > button').click()

    driver.find_element(By.CSS_SELECTOR,'#app > div > div.main-container > section > div > div.project-list.el-row > div:nth-child(6) > img').click()
login()
def new(project):
     # 点击新建活动
    driver.find_element(By.CSS_SELECTOR,'#app > div > div.right > div.inner > div > div.status-container > div > div.create-plan.search-btn > button > span').click()
    # 选择项目
    if project=='HuiChaCha':
        driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[6]/div/div[2]/div/div[1]/span').click()
    elif project == 'Fazzaco':
        driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div[6]/div/div[2]/div/div[2]/span').click()
    elif project == 'BrokersShow':
        driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div[6]/div/div[2]/div/div[3]/span').click()
    elif project=='fb':
        driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[6]/div/div[2]/div/div[4]/span').click()
    elif project=='bv':
        driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[6]/div/div[2]/div/div[5]/span').click()
    elif project=='FX110':
        driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[6]/div/div[2]/div/div[6]/span').click()
    elif project=='tl':
        driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[6]/div/div[2]/div/div[7]/span').click()
    elif project == 'FX110_OVERSEAS':
        driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div[6]/div/div[2]/div/div[8]/span').click()
    elif project == '法布':
        driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div[6]/div/div[2]/div/div[9]/span').click()
    else:
        print('项目名称错误')
    # 点击下一步
    driver.find_element(By.CSS_SELECTOR,'#app > div > div.right > div.inner > div > div.el-dialog__wrapper > div > div.el-dialog__footer > span > span > button.el-button.el-button--primary.el-button--mini > span').click()
    # # # 选择新用户注册
    driver.find_element(By.CSS_SELECTOR,'#app > div > div.right > div.inner > div > div.el-dialog__wrapper > div > div.el-dialog__body > div > div.template-wrap > div:nth-child(1) > div > img').click()
    # 点击确定
    sleep(2)
    driver.find_element(By.CSS_SELECTOR,'#app > div > div.right > div.inner > div > div.el-dialog__wrapper > div > div.el-dialog__footer > span > span > button.el-button.el-button--primary.el-button--mini > span').click()
    # driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[6]/div/div[3]/span/span/button[2]/span').click()
    sleep(2)
new()

# 点击编辑活动
driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[4]/div[1]/div[3]/table/tbody/tr[1]/td[10]/div/button[1]/span').click()
#活动地址
driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[1]/div[2]/div/div[2]/div/label[1]/span[1]/span').click()
driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[1]/div[3]/div/div/div/input').send_keys('https://bvwebtestevent.tostar.top')
driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[1]/div[4]/div/div[1]/div/input').send_keys('https://bvh5testevent.tostar.top')
# 奖品类型
driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[2]/div[3]/div/div/div/input').click()
driver.find_element(By.XPATH,'/html/body/div[6]/div[1]/div[1]/ul/li').click()

# 日期
sleep(1)
driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[1]/div[6]/div/div/input[1]').send_keys('2023-10-04 00:00:00')
sleep(1)
driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[1]/div[6]/div/div/input[2]').send_keys('2023-11-16 23:59:59')
# 提现网络
driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[2]/div[4]/div/div/input').clear()
driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[2]/div[4]/div/div/input').send_keys("TRC20")
# 邀请人奖金参数
driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[2]/div[5]/div/div/div[1]/label/span[1]/span').click()
driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[2]/div[5]/div/div/div[1]/label/span[2]/span/div/input').clear()
driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[2]/div[5]/div/div/div[1]/label/span[2]/span/div/input').send_keys(50)
# 特殊国家
def special():
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[2]/div[6]/div/div/div[3]/table/tbody/tr[1]/td[2]/div/div/input').send_keys(40)
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[2]/div[6]/div/div/div[3]/table/tbody/tr[1]/td[3]/div/div/input').send_keys(1000)
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[2]/div[6]/div/div/div[3]/table/tbody/tr[2]/td[2]/div/div/input').send_keys(5)
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[2]/div[6]/div/div/div[3]/table/tbody/tr[2]/td[3]/div/div/input').send_keys(100)

    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[2]/div[6]/div/div/div[3]/table/tbody/tr[2]/td[2]/div/div/input').send_keys(8)
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[2]/div[6]/div/div/div[3]/table/tbody/tr[2]/td[3]/div/div/input').send_keys(100)

    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[2]/div[6]/div/div/div[3]/table/tbody/tr[2]/td[2]/div/div/input').send_keys(50)
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[2]/div[6]/div/div/div[3]/table/tbody/tr[2]/td[3]/div/div/input').send_keys(1000)

    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[2]/div[6]/div/div/div[3]/table/tbody/tr[2]/td[2]/div/div/input').send_keys(10)
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[2]/div[6]/div/div/div[3]/table/tbody/tr[2]/td[3]/div/div/input').send_keys(200)

    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[2]/div[6]/div/div/div[3]/table/tbody/tr[2]/td[2]/div/div/input').send_keys(2)
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[2]/div[6]/div/div/div[3]/table/tbody/tr[2]/td[3]/div/div/input').send_keys(50)

    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[2]/div[6]/div/div/div[3]/table/tbody/tr[2]/td[2]/div/div/input').send_keys(2)
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[2]/div[6]/div/div/div[3]/table/tbody/tr[2]/td[3]/div/div/input').send_keys(50)
# 被邀请人关联奖金配置
sleep(2)
fixed_button = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/div[3]/form/div/div/div/div[1]/label/span[1]')
ActionChains(driver).move_to_element(fixed_button).perform()
fixed_button.click()
driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/div[3]/form/div/div/div/div[1]/label/span[2]/span/div/input').send_keys(20)

# 客户端展示信息
def language():
    # 简中
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[1]/label[1]/span').click()#点击简中
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[2]/div/div/input').send_keys(CN.rukou)
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[3]/div/div/input').send_keys(CN.name)
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[4]/div/div/textarea').send_keys(CN.rewards_mains)
    # driver.find_element(By.XPATH,'/html').send_keys(CN.rules)

    gaishu=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[5]/div/div/div/div[1]/div[2]/div[1]/iframe')
    driver.switch_to.frame(gaishu)#切换到iframe
    driver.find_element(By.TAG_NAME,'body').clear()#清空内容
    driver.find_element(By.TAG_NAME,'body').send_keys(CN.Overviewofrules)
    driver.switch_to.default_content()#切换回默认的上下文

    driver.switch_to.frame(driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[6]/div/div/div/div[1]/div[2]/div[1]/iframe'))
    driver.find_element(By.TAG_NAME,'body').clear()#清空内容
    driver.find_element(By.ID,'tinymce').send_keys(CN.rules)
    driver.switch_to.default_content()#切换回默认的上下文

    driver.switch_to.frame(driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[7]/div/div/div/div[1]/div[2]/div[1]/iframe'))
    driver.find_element(By.TAG_NAME,'body').clear()#清空内容
    driver.find_element(By.ID,'tinymce').send_keys(CN.Withdrawalrules)
    driver.switch_to.default_content()#切换回默认的上下文

    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[8]/div/div[1]/textarea').send_keys(CN.rewards_object)

    driver.switch_to.frame(driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[9]/div/div/div/div[1]/div[2]/div[1]/iframe'))
    driver.find_element(By.TAG_NAME,'body').clear()#清空内容
    driver.find_element(By.ID,'tinymce').send_keys(CN.attention)
    driver.switch_to.default_content()#切换回默认的上下文'))
    sleep(2)
    # 繁中
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[1]/label[2]/span').click()#点击繁中
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[2]/div/div/input').send_keys(TW.rukou)
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[3]/div/div/input').send_keys(TW.name)
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[4]/div/div/textarea').send_keys(TW.rewards_mains)
    driver.find_element(By.XPATH,'/html').send_keys(TW.Overviewofrules)

    gaishu=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[5]/div/div/div/div[1]/div[2]/div[1]/iframe')
    driver.switch_to.frame(gaishu)#切换到iframe
    driver.find_element(By.TAG_NAME,'body').clear()#清空内容
    driver.find_element(By.TAG_NAME,'body').send_keys(TW.Overviewofrules)
    driver.switch_to.default_content()#切换回默认的上下文

    driver.switch_to.frame(driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[6]/div/div/div/div[1]/div[2]/div[1]/iframe'))
    driver.find_element(By.TAG_NAME,'body').clear()#清空内容
    driver.find_element(By.ID,'tinymce').send_keys(TW.rules)
    driver.switch_to.default_content()#切换回默认的上下文

    driver.switch_to.frame(driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[7]/div/div/div/div[1]/div[2]/div[1]/iframe'))
    driver.find_element(By.TAG_NAME,'body').clear()#清空内容
    driver.find_element(By.ID,'tinymce').send_keys(TW.Withdrawalrules)
    driver.switch_to.default_content()#切换回默认的上下文

    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[8]/div/div[1]/textarea').send_keys('客态-奖励')

    driver.switch_to.frame(driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[9]/div/div/div/div[1]/div[2]/div[1]/iframe'))
    driver.find_element(By.TAG_NAME,'body').clear()#清空内容
    driver.find_element(By.ID,'tinymce').send_keys(TW.attention)
    driver.switch_to.default_content()#切换回默认的上下文'))
    sleep(2)

    # 英语
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[1]/label[3]/span').click()#点击英语
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[2]/div/div/input').send_keys(EN.rukou)
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[3]/div/div/input').send_keys(EN.name)
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[4]/div/div/textarea').send_keys(EN.rewards_mains)
    driver.find_element(By.XPATH,'/html').send_keys('主态')

    gaishu=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[5]/div/div/div/div[1]/div[2]/div[1]/iframe')
    driver.switch_to.frame(gaishu)#切换到iframe
    driver.find_element(By.TAG_NAME,'body').clear()#清空内容
    driver.find_element(By.TAG_NAME,'body').send_keys(EN.Overviewofrules)
    driver.switch_to.default_content()#切换回默认的上下文

    driver.switch_to.frame(driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[6]/div/div/div/div[1]/div[2]/div[1]/iframe'))
    driver.find_element(By.TAG_NAME,'body').clear()#清空内容
    driver.find_element(By.ID,'tinymce').send_keys(EN.rules)
    driver.switch_to.default_content()#切换回默认的上下文

    driver.switch_to.frame(driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[7]/div/div/div/div[1]/div[2]/div[1]/iframe'))
    driver.find_element(By.TAG_NAME,'body').clear()#清空内容
    driver.find_element(By.ID,'tinymce').send_keys(EN.Withdrawalrules)
    driver.switch_to.default_content()#切换回默认的上下文

    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[8]/div/div[1]/textarea').send_keys(EN.rewards_object)

    driver.switch_to.frame(driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[9]/div/div/div/div[1]/div[2]/div[1]/iframe'))
    driver.find_element(By.TAG_NAME,'body').clear()#清空内容
    driver.find_element(By.ID,'tinymce').send_keys(EN.attention)
    driver.switch_to.default_content()#切换回默认的上下文'))
    sleep(2)

    # 阿语
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[1]/label[4]/span').click()#点击阿语
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[2]/div/div/input').send_keys(AR.rukou)
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[3]/div/div/input').send_keys(AR.name)
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[4]/div/div/textarea').send_keys(AR.rewards_mains)
    driver.find_element(By.XPATH,'/html').send_keys('主态')

    gaishu=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[5]/div/div/div/div[1]/div[2]/div[1]/iframe')
    driver.switch_to.frame(gaishu)#切换到iframe
    driver.find_element(By.TAG_NAME,'body').clear()#清空内容
    driver.find_element(By.TAG_NAME,'body').send_keys(AR.Overviewofrules)
    driver.switch_to.default_content()#切换回默认的上下文

    driver.switch_to.frame(driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[6]/div/div/div/div[1]/div[2]/div[1]/iframe'))
    driver.find_element(By.TAG_NAME,'body').clear()#清空内容
    driver.find_element(By.ID,'tinymce').send_keys(AR.rules)
    driver.switch_to.default_content()#切换回默认的上下文

    driver.switch_to.frame(driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[7]/div/div/div/div[1]/div[2]/div[1]/iframe'))
    driver.find_element(By.TAG_NAME,'body').clear()#清空内容
    driver.find_element(By.ID,'tinymce').send_keys(AR.Withdrawalrules)
    driver.switch_to.default_content()#切换回默认的上下文

    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[8]/div/div[1]/textarea').send_keys(AR.rewards_object)

    driver.switch_to.frame(driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[9]/div/div/div/div[1]/div[2]/div[1]/iframe'))
    driver.find_element(By.TAG_NAME,'body').clear()#清空内容
    driver.find_element(By.ID,'tinymce').send_keys(AR.attention)
    driver.switch_to.default_content()#切换回默认的上下文'))
    sleep(2)

    # # 马来语
    # driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[1]/label[4]/span').click()#点击马来语
    # driver.find_element(By.XPATH,
    #                     '//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[2]/div/div/input').send_keys(
    #     AR.rukou)
    # driver.find_element(By.XPATH,
    #                     '//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[3]/div/div/input').send_keys(
    #     AR.name)
    # driver.find_element(By.XPATH,
    #                     '//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[4]/div/div/textarea').send_keys(
    #     AR.rewards_mains)
    # driver.find_element(By.XPATH, '/html').send_keys('主态')
    #
    # gaishu = driver.find_element(By.XPATH,
    #                              '/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[5]/div/div/div/div[1]/div[2]/div[1]/iframe')
    # driver.switch_to.frame(gaishu)  # 切换到iframe
    # driver.find_element(By.TAG_NAME, 'body').clear()  # 清空内容
    # driver.find_element(By.TAG_NAME, 'body').send_keys(AR.Overviewofrules)
    # driver.switch_to.default_content()  # 切换回默认的上下文
    #
    # driver.switch_to.frame(driver.find_element(By.XPATH,
    #                                            '/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[6]/div/div/div/div[1]/div[2]/div[1]/iframe'))
    # driver.find_element(By.TAG_NAME, 'body').clear()  # 清空内容
    # driver.find_element(By.ID, 'tinymce').send_keys(AR.rules)
    # driver.switch_to.default_content()  # 切换回默认的上下文
    #
    # driver.switch_to.frame(driver.find_element(By.XPATH,
    #                                            '/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[7]/div/div/div/div[1]/div[2]/div[1]/iframe'))
    # driver.find_element(By.TAG_NAME, 'body').clear()  # 清空内容
    # driver.find_element(By.ID, 'tinymce').send_keys(AR.Withdrawalrules)
    # driver.switch_to.default_content()  # 切换回默认的上下文
    #
    # driver.find_element(By.XPATH,
    #                     '//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[8]/div/div[1]/textarea').send_keys(
    #     AR.rewards_object)
    #
    # driver.switch_to.frame(driver.find_element(By.XPATH,
    #                                            '/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[9]/div/div/div/div[1]/div[2]/div[1]/iframe'))
    # driver.find_element(By.TAG_NAME, 'body').clear()  # 清空内容
    # driver.find_element(By.ID, 'tinymce').send_keys(AR.attention)
    # driver.switch_to.default_content()  # 切换回默认的上下文'))
    # sleep(2)

    # 泰语
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[1]/label[5]/span').click()#点击泰语
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[2]/div/div/input').send_keys(TH.rukou)
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[3]/div/div/input').send_keys(TH.name)
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[4]/div/div/textarea').send_keys(TH.rewards_mains)
    driver.find_element(By.XPATH,'/html').send_keys('主态')

    gaishu=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[5]/div/div/div/div[1]/div[2]/div[1]/iframe')
    driver.switch_to.frame(gaishu)#切换到iframe
    driver.find_element(By.TAG_NAME,'body').clear()#清空内容
    driver.find_element(By.TAG_NAME,'body').send_keys(TH.Overviewofrules)
    driver.switch_to.default_content()#切换回默认的上下文

    driver.switch_to.frame(driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[6]/div/div/div/div[1]/div[2]/div[1]/iframe'))
    driver.find_element(By.TAG_NAME,'body').clear()#清空内容
    driver.find_element(By.ID,'tinymce').send_keys(TH.rules)
    driver.switch_to.default_content()#切换回默认的上下文

    driver.switch_to.frame(driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[7]/div/div/div/div[1]/div[2]/div[1]/iframe'))
    driver.find_element(By.TAG_NAME,'body').clear()#清空内容
    driver.find_element(By.ID,'tinymce').send_keys(TH.Withdrawalrules)
    driver.switch_to.default_content()#切换回默认的上下文

    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[8]/div/div[1]/textarea').send_keys(TH.rewards_object)

    driver.switch_to.frame(driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[9]/div/div/div/div[1]/div[2]/div[1]/iframe'))
    driver.find_element(By.TAG_NAME,'body').clear()#清空内容
    driver.find_element(By.ID,'tinymce').send_keys(TH.attention)
    driver.switch_to.default_content()#切换回默认的上下文'))
    sleep(2)

    # 越南语
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[1]/label[6]/span').click()#点击越南语
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[2]/div/div/input').send_keys(VN.rukou)
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[3]/div/div/input').send_keys(VN.name)
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[4]/div/div/textarea').send_keys(VN.rewards_mains)
    driver.find_element(By.XPATH,'/html').send_keys('主态')

    gaishu=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[5]/div/div/div/div[1]/div[2]/div[1]/iframe')
    driver.switch_to.frame(gaishu)#切换到iframe
    driver.find_element(By.TAG_NAME,'body').clear()#清空内容
    driver.find_element(By.TAG_NAME,'body').send_keys(VN.Overviewofrules)
    driver.switch_to.default_content()#切换回默认的上下文

    driver.switch_to.frame(driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[6]/div/div/div/div[1]/div[2]/div[1]/iframe'))
    driver.find_element(By.TAG_NAME,'body').clear()#清空内容
    driver.find_element(By.ID,'tinymce').send_keys(VN.rules)
    driver.switch_to.default_content()#切换回默认的上下文

    driver.switch_to.frame(driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[7]/div/div/div/div[1]/div[2]/div[1]/iframe'))
    driver.find_element(By.TAG_NAME,'body').clear()#清空内容
    driver.find_element(By.ID,'tinymce').send_keys(VN.Withdrawalrules)
    driver.switch_to.default_content()#切换回默认的上下文

    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[8]/div/div[1]/textarea').send_keys(VN.rewards_object)

    driver.switch_to.frame(driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[9]/div/div/div/div[1]/div[2]/div[1]/iframe'))
    driver.find_element(By.TAG_NAME,'body').clear()#清空内容
    driver.find_element(By.ID,'tinymce').send_keys(VN.attention)
    driver.switch_to.default_content()#切换回默认的上下文'))
    sleep(2)

    # 印尼语
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[1]/label[7]/span').click()#点击印尼语
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[2]/div/div/input').send_keys(ID.rukou)
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[3]/div/div/input').send_keys(ID.name)
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[4]/div/div/textarea').send_keys(ID.rewards_mains)
    driver.find_element(By.XPATH,'/html').send_keys('主态')

    gaishu=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[5]/div/div/div/div[1]/div[2]/div[1]/iframe')
    driver.switch_to.frame(gaishu)#切换到iframe
    driver.find_element(By.TAG_NAME,'body').clear()#清空内容
    driver.find_element(By.TAG_NAME,'body').send_keys(ID.Overviewofrules)
    driver.switch_to.default_content()#切换回默认的上下文

    driver.switch_to.frame(driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[6]/div/div/div/div[1]/div[2]/div[1]/iframe'))
    driver.find_element(By.TAG_NAME,'body').clear()#清空内容
    driver.find_element(By.ID,'tinymce').send_keys(ID.rules)
    driver.switch_to.default_content()#切换回默认的上下文

    driver.switch_to.frame(driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[7]/div/div/div/div[1]/div[2]/div[1]/iframe'))
    driver.find_element(By.TAG_NAME,'body').clear()#清空内容
    driver.find_element(By.ID,'tinymce').send_keys(ID.Withdrawalrules)
    driver.switch_to.default_content()#切换回默认的上下文

    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[8]/div/div[1]/textarea').send_keys(ID.rewards_object)

    driver.switch_to.frame(driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form[3]/div[9]/div/div/div/div[1]/div[2]/div[1]/iframe'))
    driver.find_element(By.TAG_NAME,'body').clear()#清空内容
    driver.find_element(By.ID,'tinymce').send_keys(ID.attention)
    driver.switch_to.default_content()#切换回默认的上下文'))
    sleep(2)

language()

# 点击保存
driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/div[6]/div[2]/button/span').click()
sleep(2)