from selenium import webdriver
from selenium.webdriver import ActionChains


def login():
    d=webdriver.Chrome()
    d.get('https://testfbtw.tostar.top/')
    d.implicitly_wait(10)

    d.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[7]/div[5]').click()
    d.find_element_by_id('inputMailText').send_keys('101@qq.com')
    d.find_element_by_id('inputMailPwd').send_keys('a1234567')
    d.find_element_by_id('mailBtn').click()

    remote_executor=d.command_executor._url
    session_id=d.session_id
    return remote_executor,session_id

