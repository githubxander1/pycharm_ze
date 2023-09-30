import os

from time import sleep


def main():
    ctrl = True
    while ctrl:
        menu()
        # option=input('请选择菜单：')
        # option_int=input('请选择菜单：')
        option_int = int(input('请选择菜单：'))
        if option_int == 1:
            print('录入学生信息')
            insert1()
        elif option_int == 2:
            search2()
        elif option_int == 3:
            delete3()
        elif option_int == 4:
            modify4()
        elif option_int == 5:
            sort5()
        elif option_int == 6:
            count6()
        elif option_int == 7:
            show7()
        elif option_int == 0:
            print('欢迎下次使用')
            crtl = False
            break
        else:
            print('无该功能，请输入正确数字')
            sleep(2)
            menu()


def menu():
    print('''
    ===============学生信息管理系统===========
        1.录入学生信息
        2.查找学生信息
        3.删除学生信息
        4.修改学生信息
        5.排序
        6.统计学生总人数
        7.显示所有学生信息
        0.退出
    ========================================
    说明：通过数字或↕方向键选择菜单''')


def save(student):
    try:
        student_txt = open('students.txt', 'a')  # 追加模式打开
    except Exception as e:
        student_txt = open('students.txt', 'w')  # 文件不存在，创建文件并打开
    for info in student:
        student_txt.write(str(info) + '\n')  # 按行存储，添加换行符
        student_txt.close()  # 关闭文件


def insert1():
    student_list = []  # 保存信息列表
    mark = True  # 是否继续添加
    while mark:
        id = input('请输入ID(如001):')
        if not id:  # ID为空，跳出循环
            break
        name = input('请输入姓名:')
        if not name:  # ID为空，跳出循环
            break
        try:
            english = int(input('请输入英语成绩:'))
            python = int(input('请输入python成绩:'))
            c = int(input('请输入c语言成绩:'))
        except:
            print('输入无效，不是整数，请重新输入')
            continue
        # 将输入的信息存到字典
        student = {'id': id, 'name': name, 'english': english, 'python': python, 'c': c}
        # 将学生信息添加到列表中
        student_list.append(student)
        inputMark = input('是否继续添加？y/n\n')
        if inputMark == 'y':
            mark = True
        else:
            mark = False
    save(student_list)
    print('学生信息录入完毕')


def delete3():
    mark = True  # 标记是否循环
    while mark:
        studentId = input("请输入要删除的学生ID：")
        if studentId != '':  # 判断是否输入要删除的学生
            if os.path.exists('students.txt'):  # 关 判断文件是否存在
                with open('students.txt', 'r') as rfile:  # 打开文件
                    student_old = rfile.readlines()  # 读取全部内容
            else:
                student_old = []
            ifdel = False  # 标记是否删除
            if student_old:  # 如果存在学生信息
                with open('students.txt', 'w') as wfile:  # 以写方式打开文件
                    d = {}  # 定义空字典
                    for list in student_old:
                        d = dict(eval(list))  # 字符串转字典
                        if d['id'] != studentId:
                            wfile.write(str(d) + '\n')  # 将一条学生信息写入文件
                        else:
                            ifdel = True  # 标记已经删除
                    if ifdel:
                        print("ID为%s的学生信息已经被删除。。" % studentId)
                    else:
                        print("没有找到ID为%s的学生信总，，。" % studentId)
            else:  # 不存在学生信息
                print('无学生信息...')
                break  # 退出循环
            show7()  # 显示全部学生信息
            inputMark = input('是否继续删除？（y / n):')
            if inputMark == "y":
                mark = True  # 继续删除
            else:
                mark = False  # 退出删除学生信息功能


def search2():
    mark = True
    student_query = []
    while mark:
        id = ''
        name = ''
        if os.path.exists('students.txt'):
            mode = input('按ID查询请输入1，按名字查询请输入2：')
            if mode == '1':
                input('请输入学生ID：')
            elif mode == '2':
                input('请输入学生姓名：')
            else:
                print('未查询到，请重新输入')
                search2()
            with open('students.txt', 'r') as f:
                student = f.readlines()
                for list in student:
                    d = dict(eval(list))
                    if id != '':  # 判断是否按ID查询
                        if d['id'] == id:
                            student_query.append(d)  # 将找到的ID保存到列表中
                    elif name != '':
                        if d['name'] == name:
                            student_query.append(d)
                show_student(student_query)  # 显示查询结果
                student_query.clear()
                inputMark = input('是否继续查询：y/n:')
                if inputMark == 'y':
                    mark = True
                else:
                    mark = False
        else:
            print('暂未保存数据信息')
            return


def show_student(studentList):
    if not studentList:  # 如果没有学生数据
        print('无数据信息')
        return
    format_title = '{:^6}{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^10}'  # 定义标题显示格式
    print(format_title.format('ID', '名字', '英语成绩', 'python成绩', 'c语言成绩', '总成绩'))

    format_data = '{:^6}{:^12}\t{:^8}\t{:^10}\t{:^12}\t{:^12}'
    for info in studentList:
        print(format_data.format(info.get('id'),
                                 info.get('name'),
                                 str(info.get('english')),
                                 str(info.get('python')),
                                 str(info.get('C')),
                                 str(info.get('english') + info.get('python') + info.get('c')).center(12)))


def show7():
    """显示所有学生信息"""
    student_new = []
    if os.path.exists('students.txt'):
        with open('students.txt', 'r') as rfile:
            student_old = rfile.readlines()
        for list in student_old:
            student_new.append(eval(list))
        if student_new:
            show_student(student_new)
    else:
        print('暂未保存数据信息')


def sort():
    pass


def modify():
    pass


def count():
    pass


main()
# system= main()
# system.menu()
