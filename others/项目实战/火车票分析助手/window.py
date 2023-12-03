import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication


class train:
    def __init__(self):
        self.ui = uic.loadUi('火车票分析助手.ui')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = train()
    window.ui.show()
    sys.exit(app.exec_())
