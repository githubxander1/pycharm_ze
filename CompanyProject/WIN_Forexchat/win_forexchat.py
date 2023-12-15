import unittest
# from appium import webdriver
from selenium import webdriver

class WindowsCalculatorTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        # set up appium
        desired_caps = {
            "app": "D:\\progam files\\XMind\\XMind.exe",
            'platformName': 'Windows',
            'automationName': 'Windows'
        }
        self.driver = webdriver.Remote('http://localhost:4723', **desired_caps)
        # self.driver.
        # print(self.driver)

    # @classmethod
    # def tearDownClass(self):
    #     self.driver.quit()

    def test_addition(self):
        pass


if __name__ == '__main__':
    unittest.main()