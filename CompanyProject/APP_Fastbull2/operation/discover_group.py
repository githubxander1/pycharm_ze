from CompanyProject.APP_Fastbull2.base.basePage import Base1, d


class DiscoverGroup(Base1):
    search_box = d.xpath(
        '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[1]')

    def click_search_box(self):
        self.search_box.click()

    search=d.xpath('//android.widget.EditText')
    def input_search(self,text):
        self.search.set_text(text)
        self.d.press("enter")

    cancel=d(description="取消")
    def click_cancel(self):
        self.cancel.click()

    # enter=d.xpath('//*[contains(@content-desc="加入")]')
    join = d.xpath('//*[contains(@content-desc,"加入")]')
    def click_join(self):
        self.join.click()

    back=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[1]')
    def click_back(self):
        self.back.click()

    send=d(description="发送")
    def click_send(self):
        self.send.click()