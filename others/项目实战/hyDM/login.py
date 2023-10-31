# from PySide2.QtWidgets import QApplication, QMessageBox
# from PySide2.QtUiTools import QUiLoader
import requests
from PyQt5 import uic
from PyQt5.QtWidgets import QMessageBox, QApplication

from lib.share import SI


class Win_Login:

    def __init__(self):
        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        # self.ui = QUiLoader().load('main.ui')
        # 从文件中加载UI定义
        self.ui = uic.loadUi("login.ui")
        self.ui.btn_login.clicked.connect(self.onSigIn)

    def onSigIn(self):
        username = self.ui.edt_username.text().strip()
        password = self.ui.edt_password.text().strip()

        s = requests.Session()
        url = 'https://192.168.1.105/api/sign'
        res = s.post(url, json={
            "action": "signin",
            "username": "xxxx",
            "password": "yyyy"
        })
        resObj = res.json()
        if resObj['ret'] != 0:
            QMessageBox.warning(self.ui,
                                '登录失败',
                                resObj['msg'])
            return
        SI.mainwin = Win_Main()
        SI.mainwin.ui.show()

        self.ui.edt_password.setText('')
        self.ui.hide()
        # self.ui.close()


class Win_Main:
    def __init__(self):
        self.ui = uic.loadUi('main.ui')

        self.ui.act_exit.traggered.connect(self.onSigOut)

    def onSigOut(self):
        SI.mainwin.ui.hide()
        SI.loginwin.ui.show()
        
        s = requests.Session()
        url = 'https://192.168.1.105/api/sign'
        res = s.post(url, json={
            "action": "signin",
            "username": "xxxx",
            "password": "yyyy"
        })
        resObj = res.json()
        if resObj['ret'] != 0:
            QMessageBox.warning(self.ui,
                                '登录失败',
                                resObj['msg'])
            return


app = QApplication([])
SI.loginwin = Win_Login()
SI.loginwin.ui.show()
app.exec_()
