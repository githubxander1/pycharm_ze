from appium import webdriver
# from selenium import webdriver

desire_cap={
    'devicesName':'127.0.0.1:21503 device',
    'platformName':'Android',
    'platformVersion':'7',
    'appPackage':'com.android.settings',
    'appActivity':'com.android.settings.Settings'
}
driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desire_cap)
