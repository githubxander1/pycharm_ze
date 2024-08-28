import allure

from CompanyProject.APP_Fastbull2.base.basePage import Base1, d


class DiscoverGroup(Base1):
    search_box = d.xpath(
        '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.widget.ImageView[实例25_批量生成PPT版荣誉证书]')
    @allure.step('点击搜索框')
    def click_search_box(self):
        self.search_box.click()

    search=d.xpath('//android.widget.EditText')
    @allure.step('输入搜索内容')
    def input_search(self,text):
        self.search.set_text(text)
        self.d.press("enter")

    cancel=d(description="取消")
    @allure.step('点击取消')
    def click_cancel(self):
        self.cancel.click()

    # enter=d.xpath('//*[contains(@content-desc="加入")]')
    join = d.xpath('//*[contains(@content-desc,"加入")]')
    @allure.step('点击加入')
    def click_join(self):
        self.join.click()

    back=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.widget.ImageView[实例25_批量生成PPT版荣誉证书]')
    @allure.step('点击返回')
    def click_back(self):
        self.back.click()

    send=d(description="发送")
    @allure.step('点击发送')
    def click_send(self):
        self.send.click()