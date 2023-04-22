from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
d=webdriver.Edge()
d.implicitly_wait(5)
d.get('https://testfastbullliveevent.tostar.top/tw/share/170?clientType=5&version=2.0.0&userId=24283&deviceId=51511f47f44e7b5e38c80de2aad4814d')

d.find_element_by_xpath('//*[@id="share"]/div[1]/div[2]/button').click()

# locator=d.find_element_by_xpath('/html/body/div[3]/div')
# WebDriverWait(d,5,0.5).until(EC.presence_of_element_located(locator))
# 获取toast
t = d.find_element_by_css_selector('/html/body/div[3]/div').text
print(t)

