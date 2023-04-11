from selenium import webdriver

d=webdriver.Edge()

class Login:
    def scanlogin(self):
        pass

    def goto_regester(self):
        d.find_element_by_css_selector('#wework_admin\.loginpage_wx2_\$ > main > div.login_registerBar > a').click()