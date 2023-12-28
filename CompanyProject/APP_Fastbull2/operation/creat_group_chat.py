import allure

from CompanyProject.APP_Fastbull2.base.basePage import Base1, d


class Create_group_chat(Base1):
    confirm = d.xpath('//*[contains(@content-desc,"完成")]')
    @allure.step("完成")
    def click_confirm(self):
        # self.confirm.click()
        self.d.click(0.894, 0.067)

    cancel = d(description="取消")
    @allure.step("取消")
    def click_cancel(self):
        self.cancel.click()

    @allure.step("创建群聊")
    def Create_group_chat(self):
        self.d.click(0.083, 0.268)
        self.d.click(0.077, 0.43)
        self.click_confirm()