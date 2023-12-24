from CompanyProject.APP_Fastbull2.base.basePage import Base1, d


class Add_friend(Base1):

    directory=d.xpath('//androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[2]')
    add_friend=d(description="添加好友")
    add_friend_home=d.xpath('//androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[3]')

    add_friend_top=d(description="添加好友")
    nickname_tab=d.xpath('//*[contains(@content-desc,"用户昵称")]')
    fxid_tab=d.xpath('//*[contains(@content-desc,"FXID")]')
    phone=d.xpath('//*[contains(@content-desc,"电话号码")]')
    email_tab=d.xpath('//*[contains(@content-desc,"邮箱")]')
    def click_nickname_tab(self):
        self.nickname_tab.click()

    def click_fxid_tab(self):
        self.fxid_tab.click()

    def click_phone(self):
        self.phone.click()

    def click_email_tab(self):
        self.email_tab.click()



    edit_text=d.xpath('//android.widget.EditText')
    def send_edit_text(self,text):
        self.edit_text.set_text(text)
        self.d.press("enter")

    def click_add_friend(self):
        self.add_friend.click()

    def click_add_friend_home(self):
        self.add_friend_home.click()


if __name__ == '__main__':
    add_friend=Add_friend()
    add_friend.startApp()
    add_friend.click_add_friend_home()
    add_friend.click_add_friend()
    add_friend.click_nickname_tab()
    add_friend.send_edit_text("1")

