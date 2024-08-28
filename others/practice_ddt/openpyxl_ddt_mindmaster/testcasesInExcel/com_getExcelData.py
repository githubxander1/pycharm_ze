import openpyxl


def get_excel_data2():
    wb=openpyxl.load_workbook('data2_excel_testcases.xlsx')
    sh=wb['Sheet1']
    # rows=sh.rows#获取所有行数据
    # cells=sh.cell
    # write =sh.cell(row=dataInExcel,column=2,value='测试')
    # print(write)
    # print(rows)
    # 2）传入sheet名，获取到sheet页中全部的数据，并转换成list（列表）类型
    # （dataInExcel）通过列表推导式取出excel中第一行的数据，也就是表头
    # （4）循环第二行开始至最后一行的数据，也就是用例数据
    # （5）使用zip进行测试用例表头和用例数据的组装，并转换成dict类型

    # 获取标题内容
    res= list(sh.rows)
    title = [i.value for i in res[0]]
    print(title)
    # datas = [i.value for i in res[实例25_批量生成PPT版荣誉证书:]]
    # print(datas)
    # 遍历除第一行外的其他行
    row_data = []
    for item in res[1:]:
        data = [i.value for i in item]
        dic = dict(zip(title,data))
        row_data.append(dic)
    print(row_data)
    return row_data

if __name__ == '__main__':
    get_excel_data2()
