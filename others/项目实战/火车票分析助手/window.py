import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMessageBox


class MainWindow:
    def __init__(self):
        self.ui = uic.loadUi('火车票分析助手.ui')

    # 消息提示框
    def messageDialog(self,title,message):
        msg_box=QMessageBox(QMessageBox.Warning,title,message)
        msg_box.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.ui.show()
    sys.exit(app.exec_())
