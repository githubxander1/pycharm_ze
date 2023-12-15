from CompanyProject.APP_Forexchat.base.basePage import d


class home_search:
    searchBox_out=d.xpath('//android.widget.ScrollView/android.widget.ImageView[1]')
    search_input=d.xpath('//android.widget.EditText')
    cancel = d(description="取消")
    find_friend=d(description="找好友")
    find_group=d(description="找群聊")
    find_chat_record=d(description="聊天记录")

    def click_searchBox_out(self):
        self.searchBox_out.click()
    def send_search_input(self,text):
        self.click_search_input()
        self.search_input.set_text(text)
    def click_search_input(self):
        self.search_input.click()
    def click_cancel(self):
        self.cancel.click()
    def click_find_friend(self):
        self.find_friend.click()
    def click_find_group(self):
        self.find_group.click()
    def click_find_chat_record(self):
        self.find_chat_record.click()




    def search_all(self,text):
        self.click_searchBox_out()
        self.send_search_input(text)

    def search_friend(self,text):
        self.click_find_friend()
        self.click_search_input()
        self.send_search_input(text)


    def search_group(self,text):
        self.click_find_group()
        self.click_search_input()
        self.send_search_input(text)

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
