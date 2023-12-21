
from selenium import webdriver
from selenium.webdriver import ActionChains

d=webdriver.Chrome()


d.get('https://tradinglive-testwebpc.tostar.top/cn')
# d.maximize_window()
d.implicitly_wait(5)
# # 跳过引导蒙层
d.find_element(By.XPATH,'/html/body/div[2]/div/div/div[1]/div/a[1]/span').click()
#
# # # 手机号登录
# d.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/header/div/div[2]/div/div[3]/div/p/a').click()
# # d.find_element(By.XPATH,'//div[contains(@class,"region-select")]//input').send_keys("+852")
# # d.find_element_by_css_selector('[placeholder="请输入手机号"]').send_keys('91111111')
# # 悬停在活动icon上
# icon=d.find_element(By.XPATH,'//*[@id="app"]/div[6]/ul/li[1]/div/span/span/div/img')
# ActionChains(d).move_to_element(icon).perform()
# time.sleep(2)
# # # F12--resource--ctrl+\
# # 用完整的xpath定位
# d.find_element(By.XPATH,'/html/body/div[2]/div[1]/div').click()

# 进入邀请弹窗，点击登录
# iframe=d.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/iframe')
# d.switch_to.frame(iframe)
# d.find_element(By.XPATH,'//*[@id="invitation"]/div[2]/div[1]/div').click()
# time.sleep(3)
# # 手机号登录
# d.find_element(By.XPATH,'//div[contains(@class,"region-select")]//input').send_keys("+852")
# d.find_element_by_css_selector('[placeholder="请输入手机号"]').send_keys('91111111')