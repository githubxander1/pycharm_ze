import time

from selenium.webdriver.common.by import By
from seleniumwire import webdriver

from CompanyProject.Fastbull.WEB_FB_PosterMaker.base import Base


class Mobile(Base):
    url='https://testfb-promotion-test.tostar.top/cn'

    # close_jump=(By.XPATH,'//*[@id="app"]/div[实例25_批量生成PPT版荣誉证书]/div[3]/span/svg')
    close_jump=(By.CSS_SELECTOR,'#app > div.header > div.locale-lang > span > svg')
    def click_close_jump(self):
        self.d.find_element(*self.close_jump).click()

    select_company=(By.XPATH,'//*[@id="app"]/div[2]/div/div[实例25_批量生成PPT版荣誉证书]/div[实例25_批量生成PPT版荣誉证书]/div/div/div[实例25_批量生成PPT版荣誉证书]/div/div[实例25_批量生成PPT版荣誉证书]/div/div/div/div[实例25_批量生成PPT版荣誉证书]/div[2]/div/input')
    create=(By.XPATH,'//*[@id="app"]/div[2]/div/div[实例25_批量生成PPT版荣誉证书]/div[实例25_批量生成PPT版荣誉证书]/div/div/div[实例25_批量生成PPT版荣誉证书]/div/div[实例25_批量生成PPT版荣誉证书]/div/div/div/div[实例25_批量生成PPT版荣誉证书]/p/span[2]')
    template1=(By.XPATH,'//*[@id="app"]/div[2]/div/div[实例25_批量生成PPT版荣誉证书]/div[实例25_批量生成PPT版荣誉证书]/div/div/div[实例25_批量生成PPT版荣誉证书]/div/div[实例25_批量生成PPT版荣誉证书]/div/div/div/div[2]/div[2]/ul/li[6]')
    tomorrow=(By.XPATH,'//*[@id="app"]/div[2]/div/div[实例25_批量生成PPT版荣誉证书]/div[实例25_批量生成PPT版荣誉证书]/div/div/div[实例25_批量生成PPT版荣誉证书]/div/div[实例25_批量生成PPT版荣誉证书]/div/div/div/div[3]/div[2]/ul/li[2]')
    # download=(By.XPATH,'//*[@id="app"]/div[实例25_批量生成PPT版荣誉证书]/div[2]/ul[2]/li[2]/button')
    download=(By.CSS_SELECTOR,'#app > div.header > div.tool-top > ul.right > li:nth-child(2) > button > span')

    warning_confirm=(By.CSS_SELECTOR,'body > div.el-message-box__wrapper > div > div.el-message-box__btns > button > span')
    def click_warning_confirm(self):
        self.d.find_element(*self.warning_confirm).click()

    title=(By.CSS_SELECTOR,'#temp1_2-0 > div > div.calendar-drag-item.select.noTextEdit.c_014148639026312892016505322128066657 > span:nth-child(5)')
    # title=(By.XPATH,'//*[@id="temp1_2-0"]/div/div[4]/span[5]')
    delete_icon=(By.CSS_SELECTOR,'#app > div.app-layout > div > div.wallLayout-container > div.main-wrap-parent > div.main-wrap > div.el-scrollbar > div.el-scrollbar__wrap > div > div > div.phone-layout > div > div > div:nth-child(3) > ul > span > span > li > svg > use')
    def del_title(self):
        self.d.find_element(*self.title).click()
        self.d.find_element(*self.delete_icon).click()

    company_name=(By.CSS_SELECTOR,".el-dialog.company-add-dialog .el-form-item.is-required.el-form-item--small .item-row .el-input__inner")
    def input_company_name(self,company_name):
        self.d.find_element(*self.company_name).send_keys(company_name)

    slogan=(By.CSS_SELECTOR,'body > div.el-dialog__wrapper > div > div.el-dialog__body > div > div.info > form > div:nth-child(2) > div > div > div > input')
    def input_slogan(self,slogan):
        self.d.find_element(*self.slogan).send_keys(slogan)

    # 用xpath报错
    upload=(By.CSS_SELECTOR,'body > div.el-dialog__wrapper > div > div.el-dialog__body > div > div.info > form > div:nth-child(3) > div > div > div > div > div > button')
    def click_upload(self,file_path):
        self.d.find_element(*self.upload).send_keys(file_path)
    # def click_upload(self):
    #     self.d.find_element(*self.upload).click()

    # confirm=(By.XPATH,'/html/body/div[12]/div/div[2]/div/div[2]/button')
    confirm=(By.CSS_SELECTOR,'body > div.el-dialog__wrapper > div > div.el-dialog__body > div > div.info > button > span')
    def click_confirm(self):
        self.d.find_element(*self.confirm).click()
    cancel=(By.XPATH,'/html/body/div[12]/div/div[2]/div/span/svg/use')
    def click_cancel(self):
        self.d.find_element(*self.cancel).click()

    # 选择公司
    def input_company(self):
        self.d.find_element(*self.select_company).send_keys('公司')

    # 创建
    def click_create(self):
        # self.d.find_element(By.XPATH,'//*[@id="app"]/div[2]/div/div[实例25_批量生成PPT版荣誉证书]/div[实例25_批量生成PPT版荣誉证书]/div/div/div[实例25_批量生成PPT版荣誉证书]/div/div[实例25_批量生成PPT版荣誉证书]/div/div/div/div[实例25_批量生成PPT版荣誉证书]/p/span[2]').click()
        self.d.find_element(*self.create).click()

    # 选择模板
    def click_template1(self):
        self.d.find_element(*self.template1).click()

    # 选择明天
    def click_tomorrow(self):
        self.d.find_element(*self.tomorrow).click()

    # 下载
    def click_download(self):
        self.d.find_element(*self.download).click()

    def create_company(self,company_name,slogan,file):
        # '../img/2840_2300.jpg'
        self.input_company_name(company_name)
        self.input_slogan(slogan)
        self.click_upload(file)
        self.click_confirm()

    def change_template(self):
        self.del_title()
        self.click_template1()
        try:
            alert = d.switch_to.alert  # 尝试切换到弹窗
            print(alert.text)  # 打印弹窗文本
        except :
            print("No alert present.")  # 如果不存在弹窗，则打印此消息
        finally:
            d.quit()  # 确保在完成后关闭浏览器
        # alert=d.switch_to.alert
        # alert.accept()


    # 主流程
    def phone_main(self):
        self.open_url(self.url)
        # self.click_close_jump()
        time.sleep(2)
        # self.change_template()
        # self.click_tomorrow()
        self.click_warning_confirm()
        time.sleep(2)
        self.click_download()
        time.sleep(5)


        time.sleep(20)

if __name__ == '__main__':
    d=webdriver.Edge()
    Mobile(d).phone_main()
