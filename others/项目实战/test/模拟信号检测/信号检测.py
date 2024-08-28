from os.path import join

import sys
import time
from PyQt5 import uic, QtCore
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget


class myWin(QWidget):
    my_single = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi('模拟信号检测.ui')
        self.ui.msg_history = list()
        self.ui.btn_jc.clicked.connect(self.check)
        self.my_single.connect(self.my_slot)
        self.ui.setAttribute(QtCore.Qt.WA_DeleteOnClose)

    def my_slot(self, msg):
        print(msg)
        self.ui.msg_history.append(msg)
        self.ui.msg.setText('<br/>' + join(self.ui.msg_history))
        self.ui.msg.setFixedSize(400, self.ui.msg.size().height() + 15)
        self.ui.msg.repaint()  # 刷新

    def check(self):
        for i, ip in enumerate(['192.168.实例25_批量生成PPT版荣誉证书.%d' % x for x in range(1, 50)]):
            msg = '模拟，正在检测 %s 的漏洞' % ip
            if i % 5 == 0:
                self.my_single.emit(msg + ' 发现漏洞')
            else:
                self.my_single.emit(msg)
            time.sleep(0.01)
            QApplication.processEvents()
        time.sleep(2)
        self.ui.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = myWin()
    win.ui.show()
    sys.exit(app.exec_())
