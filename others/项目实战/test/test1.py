from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMessageBox


class stats():
    def __init__(self):
        # 从文件中加载ui文件
        self.window = uic.loadUi('薪资统计.ui')

        # self.window = QMainWindow()
        # self.window.resize(800, 600)
        # self.window.move(500, 500)
        # self.window.setWindowTitle('薪资统计')

        # self.textEdit = QTextEdit('请输入', self.window)
        # self.textEdit.setPlaceholderText('薪资表：')
        # self.textEdit.move(100, 100)
        # self.textEdit.resize(300, 200)
        #
        # self.button = QPushButton('统计', self.window)
        # self.button.move(300, 400)
        # self.button.clicked.connect(self.handleCalc)

    def handleCalc(self):
        print('按钮被点击了')
        # info = self.textEdit.toPlainText()

        # 薪资20000 以上 和 以下 的人员名单
        salary_above_20k = ''
        salary_below_20k = ''
        for line in info.splitlines():
            if not line.strip():
                continue
            parts = line.split(' ')
            # 去掉列表中的空字符串内容
            parts = [p for p in parts if p]
            name, salary, age = parts
            if int(salary) >= 20000:
                salary_above_20k += name + '\n'
            else:
                salary_below_20k += name + '\n'

        QMessageBox.about(self.window,
                          '统计结果',
                          f'''薪资20000 以上的有：\n{salary_above_20k}
                        \n薪资20000 以下的有：\n{salary_below_20k}'''
                          )


app = QApplication([])
stats = stats()
stats.window.show()
app.exec_()
