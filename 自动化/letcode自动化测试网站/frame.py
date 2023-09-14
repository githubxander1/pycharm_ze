from time import sleep

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent

ua=UserAgent()

# options = Options()
# options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36")


d=webdriver.Edge()
d.get('https://letcode.in/frame')
d.implicitly_wait(10)

iframe=d.find_element_by_id('firstFr')
d.switch_to.frame(iframe)

d.find_element_by_id('fname').send_keys('firstname')
d.find_element_by_id('lname').send_keys('lastname')

inner_frame=d.find_element_by_css_selector('body > app-root > app-innerframe')
d.switch_to.frame(inner_frame)

d.find_element_by_name('email').send_keys('firstname@gmail.com')