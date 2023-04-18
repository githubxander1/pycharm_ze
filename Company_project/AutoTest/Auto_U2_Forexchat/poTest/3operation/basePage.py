import uiautomator2 as u2


# d=u2.connect('127.0.0.1:21503')
# 模拟器
d=u2.connect('127.0.0.1:21513')
# 真机
# d=u2.connect('5ENDU18C21003487')
app ='com.bv.forexchat'
d.implicitly_wait(10)
# def findelement(self,*loc):
#     self.ele=ele1(loc)
# def scroll(self,%s):
#     self.d(scrollable=True).scroll.to(description="%管理群")

def input(self,value):
    self.ele.send_keys(value)

def click(self,ele):
    self.click(ele)

    # def quit(self,app):
    #     self.d.app_stop(app)

# BasePage=BasePage()