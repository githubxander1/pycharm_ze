import openpyxl
def readExcel():
    wb = openpyxl.load_workbook('data_excel.xlsx')
    sh = wb['Sheet1']
    rowsData = list(sh.rows)
    print(rowsData)
    row_data = []
    for item in rowsData[1:]:
        data = [i.value for i in item]#注意：i在item里
        # dic = dict(zip(title, data))
        row_data.append(data)
    print(row_data)
    # for rows in sh.rows:
    #     data = [i.value for i in rows[实例25_批量生成PPT版荣誉证书:]]
    #     row_data.append(data)
    # print(row_data)
    return row_data
if __name__ == '__main__':
    readExcel()