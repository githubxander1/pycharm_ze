import openpyxl
import os


def get_excel_data():
    wb = openpyxl.load_workbook('data_excel.xlsx')
    sh = wb['Sheet1']
    # 循环获取当前表格所有数据
    row_data = []
    for row in sh.rows:  # 获取每一行的数据
        for data in row:  # 获取每一行中单元格的数据
            print(data.value)  # 打印单元格的值
        # 将字符串类型的字典转换成成它本身的字典
        # 不转换的画，会将每一行数据都变成列表转换出来，字典多加了引号
        # data[0]=eval(data[0])
        # 将取到的数据存到列表中
        row_data.append(data)
    return row_data


# 如果代码不想让别人执行，就可以把其放在if __name__=="__main__"下面
if __name__ == '__main__':
    get_excel_data()
