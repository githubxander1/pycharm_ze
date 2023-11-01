import os
import sys

import time

from PyQt5 import uic
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QApplication, QFileDialog


class  RCQ:
    def  __init__(self):
        self.ui=uic.loadUi('读者书库.ui')

        # # 获取当前日期并设置到QLineEdit中
        # current_date = QDate.currentDate()
        # year = current_date.year()
        # month = current_date.month()
        # self.ui.edt_qishu.setText(f"{year}-{month}")

        # 获取当前年份和月份
        strDate = (str)(time.localtime().tm_year) + "-"+(str)(time.localtime().tm_mon)
        self.ui.edt_qishu.setText(strDate)  # 设置默认期数

        self.ui.edt_savePath.setText(os.getcwd())#设置当前程序路径

        self.ui.btn_select.clicked.connect(self.msg)#为选择按钮绑定事件
        # self.ui.btn_select.clicked.connect(self.ui.edt_savePath.setText)
    def msg(self):
        try:
            self.dir_path=QFileDialog.getExistingDirectory(self.ui,"选择保存路径",os.getcwd())
            self.ui.edt_savePath.setText(self.dir_path)
        except Exception as e:
            print(e)





if __name__ == '__main__':
    app=QApplication(sys.argv)
    w=RCQ()
    w.ui.show()
    sys.exit(app.exec_())    #)



