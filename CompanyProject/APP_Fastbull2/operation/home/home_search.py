import allure

from CompanyProject.APP_Fastbull2.base.basePage import d


class home_search:
    searchBox_out=d.xpath('//android.widget.ScrollView/android.widget.ImageView[实例25_批量生成PPT版荣誉证书]')
    search_input=d.xpath('//android.widget.EditText')
    cancel = d(description="取消")
    find_friend=d(description="找好友")
    find_group=d(description="找群聊")
    find_chat_record=d(description="聊天记录")

    unfold=d(description="展开")
    @allure.step("点击展开")
    def click_unfold(self):
        self.unfold.click()

    @allure.step("首页点击搜索框")
    def click_searchBox_out(self):
        self.searchBox_out.click()

    @allure.step("输入搜索内容")
    def send_search_input(self,text):
        self.click_search_input()
        self.search_input.set_text(text)

    @allure.step("点击搜索框_内")
    def click_search_input(self):
        self.search_input.click()

    @allure.step("点击取消")
    def click_cancel(self):
        self.cancel.click()

    @allure.step("点击找好友")
    def click_find_friend(self):
        self.find_friend.click()

    @allure.step("点击找群聊")
    def click_find_group(self):
        self.find_group.click()

    @allure.step("点击聊天记录")
    def click_find_chat_record(self):
        self.find_chat_record.click()



    @allure.step("搜索_全部")
    def search_all(self,text):
        self.click_searchBox_out()
        self.send_search_input(text)
    @allure.step("搜索好友")
    def search_friend(self,text):
        self.click_find_friend()
        self.click_search_input()
        self.send_search_input(text)

    @allure.step("搜索群聊")
    def search_group(self,text):
        self.click_find_group()
        self.click_search_input()
        self.send_search_input(text)

    @allure.step("搜索聊天记录")
    def search_chat_record(self,text):
        self.click_find_chat_record()
        self.click_search_input()
        self.send_search_input(text)

    # def click_search_button(self):
    #     self.search_button.click()
    #
    # def click_search_result(self,text):
    #     self.search_result.click()
    #
    # def click_search_result_button(self,text):
    #     self.search_result_button.click()
