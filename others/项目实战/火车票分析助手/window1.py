import sys

from PyQt5.QtWidgets import QApplication, QMainWindow


class Main(QMainWindow):
    def __init__(self):
        super(Main,self).__init__()
        self.setupUi(self)

    def show_MainWindow(self):
        app = QApplication(sys.argv)
        main=Main()
        main.show()
        sys.exit(app.exec_())

if __name__ =='__main__':
    Main.show_MainWindow()