import allure

from CompanyProject.APP_Fastbull2.base.basePage import Base1, d



class Add_friend(Base1):

    directory=d.xpath('//androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.widget.ImageView[2]')
    add_friend=d(description="添加好友")
    add_home=d.xpath('//androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.widget.ImageView[3]')

    add_friend_top=d(description="添加好友")
    nickname_tab=d.xpath('//*[contains(@content-desc,"用户昵称")]')
    fxid_tab=d.xpath('//*[contains(@content-desc,"ID")]')
    phone=d.xpath('//*[contains(@content-desc,"电话号码")]')
    email_tab=d.xpath('//*[contains(@content-desc,"邮箱")]')

    search=d.xpath('//android.widget.EditText')
    @allure.step("输入内容")
    def seatch_friend(self,text):
        self.search.set_text(text)

    @allure.step("点击用户昵称")
    def click_nickname_tab(self):
        self.nickname_tab.click()

    @allure.step("点击FXID")
    def click_fxid_tab(self):
        self.fxid_tab.click()

    @allure.step("点击电话号码")
    def click_phone(self):
        self.phone.click()

    @allure.step("点击邮箱")
    def click_email_tab(self):
        self.email_tab.click()



    edit_text=d.xpath('//android.widget.EditText')

    @allure.step("输入内容")
    def send_edit_text(self,text):
        self.edit_text.set_text(text)
        self.d.press("enter")

    @allure.step("点击添加好友")
    def click_add_friend(self):
        self.add_friend.click()

    add_btn=d(description="添加")
    def click_add_btn(self):
        self.add_btn.click()

    create_group_chat=d(description="创建群聊")
    @allure.step("点击创建群聊")
    def click_creat_group_chat(self):
        self.create_group_chat.click()

    discovery_group_chat=d(description="发现群聊")
    @allure.step("点击发现群聊")
    def click_discovery_group_chat(self):
        self.discovery_group_chat.click()

    disturbe_group_chat=d(description="免打扰群聊")
    @allure.step("点击免打扰群聊")
    def click_disturbe_group_chat(self):
        self.disturbe_group_chat.click()

    @allure.step("点击首页的+")
    def click_add_home(self):
        self.add_home.click()







if __name__ == '__main__':
    add_friend=Add_friend()
    add_friend.startApp()
    add_friend.click_add_home()
    add_friend.click_add_friend()
    add_friend.click_nickname_tab()
    add_friend.send_edit_text("实例25_批量生成PPT版荣誉证书")

