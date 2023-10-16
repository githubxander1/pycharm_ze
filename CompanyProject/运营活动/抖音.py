
self.state = StateMachine.Login
        self.driver.switch_to.new_window('douyin')
        self.driver.get(self.douyinAccount.homeUrl)
        print('请扫码登录账号，否则后面无法进行')
        common = Common()
        if common.viewPresented(self.driver, "lqiPv8cB"):
            # 关掉悬浮窗口
            closeButtonCss = "dy-account-close"
            common.clickView(self.driver,closeButtonCss)
            # 关掉上下滚动提示，找谁响应这个DOWN时间真的费了好多时间
            if common.viewPresented(self.driver,"I6ivXmaS"):
                ele = self.driver.find_element(By.CLASS_NAME,"I6ivXmaS")
                ele.click()
                action = ActionChains(self.driver)
                action.send_keys(Keys.DOWN).perform()
            # 点击登录
            common.clickView(self.driver,"lqiPv8cB")
            common.clickView(self.driver,'//li[text()="密码登录"]', By.XPATH)
            common.sendKeys(self.driver,'//input[@name="normal-input"]', self.douyinAccount.account, By.XPATH)
            common.sendKeys(self.driver,'//input[@name="button-input"]', self.douyinAccount.password, By.XPATH)
            time.sleep(2)
            common.clickView(self.driver, '//button[@type="submit"]', By.XPATH)
            sliderVerification = SliderVerification(self.driver, LoginType.Douyin, (By.CLASS_NAME, ''), (By.CLASS_NAME, 'captcha_verify_img_slide react-draggable sc-VigVT ggNWOG'), (By.ID, 'captcha-verify-image'), (By.ID, 'captcha-verify-image'))
            checkResult = sliderVerification.verify_2()
            return checkResult