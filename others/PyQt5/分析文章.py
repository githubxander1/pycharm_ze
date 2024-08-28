
"""
示例：文章分析工具（可视化）
"""
from PyQt5.QtWidgets import *
# 引入自定义模块
import aa
# 引入库
import sys
import os
import pdfplumber
from snownlp import SnowNLP
from docx import Document


class parentWindow(QWidget, aa.Ui_Form):
    # 初始化方法
    def __init__(self):
        # 找到父类 首页面
        super(parentWindow, self).__init__()
        # 初始化页面方法
        self.setupUi(self)
        self.download_path = ''  # 选择文件的信息
        # 点击选择文件
        self.selectButton.clicked.connect(self.select_file)
        # 点击分析文章
        self.analysisButton.clicked.connect(self.analysis_article)

    # 选择文件
    def select_file(self):
        # 设置文件过滤器
        filter_types = "文本文件 (*.txt);;Word 文件 (*.docx *.doc);;PDF 文件 (*.pdf)"
        # 启动选择文件对话框
        self.download_path = QFileDialog.getOpenFileName(self, "选择要分析的文章", os.getcwd() + '/files',
                                                         filter_types)
        # 判断是否选择图片
        if not self.download_path[0].strip():
            QMessageBox.information(self, '提示信息', '没有选择文件')
            self.download_path = ''
            pass
        else:
            self.fileEdit.setText(self.download_path[0])

    # 点击分析文章
    def analysis_article(self):
        # 判断是否选择文件
        if not self.download_path:
            QMessageBox.information(self, '提示信息', '请先选择文件')
            return

        # 获取后缀名并去掉.
        file_extension = os.path.splitext(self.download_path[0])[1][1:]

        # 判断不同类型调用不同方法
        if file_extension == 'txt':
            content = self.get_txt(self.download_path[0])
        elif file_extension == 'docx' or file_extension == 'doc':
            content = self.get_word(self.download_path[0])
        elif file_extension == 'pdf':
            content = self.get_pdf(self.download_path[0])
        s = SnowNLP(content)
        keywords = s.keywords(5, True)  # 提取5个关键词，第二个参数指示是否使用TF-IDF算法
        self.keywordEdit.setText(self.conversion_data(keywords, ','))
        summary = s.summary(3)  # 生成3句摘要
        self.abstractEdit.setText(self.conversion_data(summary, '\n'))

    # 获取txt的内容
    def get_txt(self, file_path):
        # 获取文本
        with open(file_path, 'r', encoding='utf-8') as file:
            # 读取文件内容
            full_text = file.read()
        return full_text

    # 获取word的内容
    def get_word(self, file_path):
        # 打开Word文档
        doc = Document(file_path)
        # 初始化一个空字符串以存储所有段落的文本
        full_text = ""

        # 遍历文档中的每个段落
        for para in doc.paragraphs:
            # 将当前段落的文本添加到全文字符串中
            full_text += f"{para.text}\n"
        # 返回合并后的文本
        return full_text

    # 获取pdf的内容
    def get_pdf(self, file_path):
        with pdfplumber.open(file_path) as pdf:
            # 初始化一个空字符串以存储所有页面的文本
            full_text = ""

            # 遍历PDF中的所有页面
            for i, page in enumerate(pdf.pages, start=1):
                # 提取当前页面的文本
                page_text = page.extract_text()

                # 将当前页面的文本添加到全文字符串中
                full_text += f"{page_text}\n"

            # 返回合并后的文本
            return full_text

    # 列表转字符串
    def conversion_data(self, lists, symbol):
        str_text = f"{symbol.join(lists)}"
        return str_text


if __name__ == '__main__':
    # 每一个PyQt5应用都必须创建一个应用对象
    app = QApplication(sys.argv)
    # 初始化页面
    window = parentWindow()
    # 显示首页
    window.show()
    sys.exit(app.exec_())