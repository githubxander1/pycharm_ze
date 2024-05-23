from selenium import webdriver
from selenium.webdriver.common.by import By

d=webdriver.Edge()
d.get('https://letcode.in/buttons')

button=d.find_element(By.ID,'collor')
print(button.value_of_css_property('value'))