import uiautomator2 as u2


d=u2.connect('127.0.0.1:21503')
app ='com.sy.fxchat'

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