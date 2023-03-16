from selenium import webdriver

d = webdriver.Chrome()

d.get('http://the-internet.herokuapp.com/basic_auth')
d.switch_to_alert()
