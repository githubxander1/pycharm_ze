import os
import xlrd

def base_dir():
    return os.path.dirname(os.path.dirname(__file__))

def readExcel():
    lists=[]
    sheet=xlrd.open_workbook(os.path.join(base_dir(),'data','sina.xls'))
    book=sheet.sheet_by_index(0) #excel文件中的第一个表 索引为0
    for item in range(1,book.nrows): #从第一行开始读取它的所有行
        lists.append(book.row_values(item)) #读取行内的所有值 将这些值添加到列表里
    return lists