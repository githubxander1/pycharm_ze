import os
import urllib

import requests
import sys

import time

from PyQt5 import uic, QtGui
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QApplication, QFileDialog, QMessageBox, QTableWidgetItem
from PyQt5.uic.properties import QtCore
from bs4 import BeautifulSoup
from pyqt5_plugins.examplebutton import QtWidgets


class  RCQ:
    def  __init__(self):
        self.ui=uic.loadUi('读者书库.ui')
        self.lineEdit=self.ui.edt_savePath
        # self.lineEdit_2=self.ui.edt_qishu

        # 获取当前年份和月份
        # strDate = (str)(time.localtime().tm_year) + "-"+(str)(time.localtime().tm_mon)
        # self.ui.edt_qishu.setText(strDate)  # 设置默认期数

        self.ui.edt_savePath.setText(os.getcwd())#设置当前程序路径

        self.ui.btn_select.clicked.connect(self.msg)#为选择按钮绑定事件
        # self.ui.btn_select.clicked.connect(self.ui.edt_savePath.setText)
        self.ui.btn_confirm.clicked.connect(self.getData)#绑定确定按钮
        self.ui.listWidget.itemClicked.connect(self.on_listWidget_itemClicked)#绑定列表单击方法
        self.ui.tableWidget.itemClicked.connect(self.on_tableWidget_cellClicked)#绑定表格单击方法

    def msg(self):
        try:
            self.dir_path=QFileDialog.getExistingDirectory(self.ui,"选择保存路径",os.getcwd())
            self.ui.edt_savePath.setText(self.dir_path)
        except Exception as e:
            print(e)

    def getData(self,url,path):
        soup = self.urlTosoup(url)
        link=soup.select('.booklist a')
        path=path+'\\'+self.data+'\\'
        if not os.path.isdir(path):
            os.makedirs(path)
        for item in link:
            articleUrl=self.baseurl+item['href']
            articleSoup=self.urlTosoup(articleUrl)

            title=str(articleSoup.find('h1')).lstrip('<h1>').rstrip('</h1>')# 获取文章标题
            author=str(articleSoup.find(id='pub_data')).strip()#获取文章作者
            fileName=path+title+'.txt'#设置保存路径
            newFile=open(fileName,'w',encoding='utf-8')#打开文件
            newFile.write('《'+title+'》\n\n')#写入标题
            newFile.write(author+'\n\n')
            content=articleSoup.select('.blkContainerSblkCon p')
            for c in content:
                text=c.text
                newFile.write(text+'\n')
            newFile.close()
        QMessageBox.information(self.ui,'下载完成',self.data+'下载完成',QMessageBox.ok)

    # 从网页提取数据
    def urlTosoup(self,url):
        # url = "https://weread.qq.com/"
        # 发起GET请求获取页面内容
        response = requests.get(url)
        # 使用BeautifulSoup解析页面内容
        soup = BeautifulSoup(response.text, 'html.parser')
        # 在页面中找到所有书籍的信息
        books = soup.find_all('div', class_='ranking_block_book')
        for book in books:
            title = book.find('div', class_='ranking_block_book_title_text').text.strip()
            author = book.find('a', class_='ranking_block_book_author').text.strip()
            print('书名：', title)
            print('作者：', author)

        # response=urllib.request.urlopen(url)
        # html=response.read()#读取网页内容
        # soup=BeautifulSoup(html,'html.parser')
        return soup
    # 获取所有文件
    def getFiles(self):
        self.list=os.listdir(self.ui.edt_savePath.text()+'\\'+self.ui.edt_qishu.text())

    #将文件显示在table中
    def bindTable(self):
        for i in range(0,len(self.list)):
            self.ui.tableWidget.insertRow(i)
            #设置第一列的值为书名
            self.ui.tableWidget.setItem(i,0,QTableWidgetItem(self.lineEdit_2.text()))
            #设置第二列的值为作者
            self.ui.tableWidget.setItem(i,1,QTableWidgetItem(self.list[i]))

    # 将文件显示在List列表中
    def bindList(self):
        for i in range(0, len(self.list)):  # 遍历文件列表
            # 创建列表项
            self.item = QtWidgets.QListWidgetItem(self.ui.listWidget)
            self.item.setIcon(QtGui.QIcon('note.ico'))    #设置列表项图标
            self.item.setText(str(self.list[i])[0:5] + '...')  #截取字符串，显示5个字符
            self.item.setToolTip(self.list[i])  # 设置提示文字
            # 设置选中与否
            self.item.setFlags(QtCore.Qt.ItemIsSelectableIQtcore.Qt.ItemIsEnabled)

    # 抓取所有数据
    def getDatas(self):
        try:
            while True:  # 无限循环
                self.date = self.lineEdit_2.text()  # 记录用户选择的期数
                # 设置文章初始地址
                self.baseurl = "http://www.52duzhe.com/" + self.date.replace('-','-')+'/'
                urlList = self.baseurl + 'index.html'  # 获取文件列表地址
                self.getData(urlList, self.lineEdit.text())  # 执行主方法
        except Exception as e:
            print(e)
        self.getFiles()  # 获取所有文件
        self.bindList()  # 对列表进行绑定
        self.bindTable()  # 对表格进行绑定

    #列表单击方法，用来打开选中的项
    def on_listWidget_itemClicked(self, item):
        os.startfile(self.lineEdit.text()+'\\'+self.lineEdit_2.text()+'\\'+item.toolTip())

    #表格单击方法
    def on_tableWidget_cellClicked(self, item):
        os.startfile(self.lineEdit.text()+'\\'+self.lineEdit_2.text()+'\\'+item.text())

if __name__ == '__main__':
    app=QApplication(sys.argv)
    w=RCQ()
    w.ui.show()
    sys.exit(app.exec_())    #)



