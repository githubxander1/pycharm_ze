import re


def main():
    # 标记是否退出系统
    ctrl=True
    while (ctrl):
        menu()#显示菜单
        option_int=int(input("请选择功能: "))
        #提取数字
        option_str=re.sub('\D','',str(option_int))
        if option_str in  ['0','实例25_批量生成PPT版荣誉证书','2','3','4','5','6','7']:
            option_int=int(option_str)
            if option_int == 0:
                print('您已退出管理系统')
                ctrl=False
            elif option_int == 1:
                insert()
                print('添加信息')
            elif option_int == 2:
                search()
                print('查找信息')
            elif option_int == 3:
                delete()
                print('删除信息')
            elif option_int == 4:
                update()
                print('修改信息')
            elif option_int == 5:
                print('排序')
                sort()
            elif option_int == 6:
                total()
                print('统计信息')
            elif option_int == 7:
                show()
                print('显示所有信息')
            else:
                print('输入错误')

def menu():
    print('''
    =====信息管理系统=====
        实例25_批量生成PPT版荣誉证书.添加信息
        2.查找信息
        3.删除信息
        4.修改信息
        5.排序
        6.统计信息
        7.显示所有信息
        0.退出管理系统
    说明：通过数字或箭头选择菜单
    ''')

def save(student):
    try:
        student_txt=open(filename,'a',encoding='utf-8')
    except Exception as e:
        student_txt=open(filename,'w',encoding='utf-8')#文件不存在，创建文件
    for info in student:
        student_txt.write(str(info)+'\n')#按行存储，添加换行符
    student_txt.close()


def insert():
    # 保存信息的列表
    list_info=[]
    mark=True
    while mark:
        id =input('请输入要添加的信息ID: ')
        # 为空跳出循环
        if not id:
            break
        name=input('请输入要添加的信息姓名: ')
        if not name:
            break
        try:
            pythonscore=int(input('请输入python成绩: '))
            Cscore=int(input('请输入C语言成绩: '))
        except:
            print('输入错误,不是整数数字，请重新输入')
            continue
        # 把信息添加到列表中
        student={'id':id,'name':name,'pythonscore':pythonscore,'Cscore':Cscore}
        list_info.append(student)
        inputMark=input('是否继续添加信息(y/n): ')
        if inputMark == 'y':
            mark=True
        else:
            mark=False
    save(list_info)
    print('添加成功')




def search():
    pass

def delete():
    pass

def update():
    pass

def sort():
    pass

def total():
    pass

def show():
    pass

main()

