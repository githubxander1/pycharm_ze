import xlrd  # 读excel文件的库
import requests  # 做接口自动化测试的库
import ddt  # Python语言数据驱动测试用的库
import xlutils  # 向已存在的excel文件中追加内容的库。
#import pytest


def get_excel_data():
    wb = xlrd.open_workbook("D:\1test\PycharmProject\数据库\file\bv-app.xlsx")
    sheet1 = wb.sheet_by_name("login")
    num = sheet1.nrows
