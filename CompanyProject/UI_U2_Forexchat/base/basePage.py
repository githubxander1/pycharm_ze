import uiautomator2 as u2


d=u2.connect('127.0.0.1:21503')

class Base1:
    def __init__(self):
        self.d = u2.connect('127.0.0.1:21503')
        print(self.d.info['currentPackageName'])
        # '''
        # 在 try 子句中添加需要运行的代码，在 except 子句中添加处理运行1错误后要运行的代码。
        # 当运行1出错时，Python会执行 except 代码块，并通过 as 关键字将错误信息存储在变量 e 中，
        # 然后通过 print 函数打印错误信息，最后执行运行2的代码。
        # '''
        # try:
        #     d = u2.connect('190.0.0.1:21513')
        # except Exception as e:
        #     print("Erro:",e)
        #     d=u2.connect('127.0.0.1:21503')
        d.app_start('com.bv.forexchat')
        d.implicitly_wait(10)
        # try:
        #     d.app_start('com.bv.forexchat')
        # except Exception as e:
        #     print("Erro:",e)
        #     d.app_start('com.sy.fxchat')

        d.implicitly_wait(10)

    def closeApp(self):
        self.d.app_stop('com.bv.forexchat')

    # def findelement(self,*loc):
    #     self.ele=ele1(loc)

    # def scroll(self,%s):
    #     self.d(scrollable=True).scroll.to(description="%管理群")
    #
    # def input(self,value):
    #     self.ele.send_keys(value)
    #
    # def click(self,ele):
    #     self.click(ele)

    # def quit(self,app):
    #     self.d.app_stop(app)

# BasePage=BasePage()