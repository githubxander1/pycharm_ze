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
            insert1()
            print('录入学生信息')
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
        except:
            print('输入无效，不是整数，请重新输入')
            continue
        # 将输入的信息存到字典
        student = {'id': id, 'name': name, 'english': english, 'python': python}
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
        studentID = input('请输入要删除的学生ID：')
        if not studentID:  # 判断学生id是否存在
            print('无效的输入，请输入有效的学生ID')
            continue

        if os.path.exists('students.txt'):
            with open('students.txt', 'r') as rfile:
                students = {line.strip(): dict(eval(line)) for line in rfile}
        else:
            students = {}

        if studentID in students:
            with open('students.txt', 'w') as wfile:
                for id, info in students.items():
                    if id != studentID:
                        wfile.write(str(info) + '\n')
            print(f'ID {studentID} 的学生已被删除。。。')
        else:
            print(f'没有找到ID为 {studentID} 的学生')

        show()  # 显示所有学生信息
        inputmark = input('是否继续删除？y/n:')
        if inputmark == 'y':
            mark = True
        else:
            mark = False


def search2():
    mark = True
    student_query = []
    while mark:
        id = ''
        name = ''
        if os.path.exists('students.txt'):
            mode = input('按ID查询请输入1，按名字查询请输入2：')
            if mode == 1:
                input('请输入学生ID：')
            elif mode == 2:
                input('请输入学生姓名：')
            else:
                print('未查询到，请重新输入')
                search2()
            with open('students.txt', 'r') as f:
                student = f.readlines()
                for list in student:
                    d = dict(eval(list))


def show7():
    """显示所有学生信息"""
    with open('students.txt', 'r') as file:
        # print(file.readlines())
        students = {line.strip(): dict(eval(line)) for line in file}
        print(students)
    # for id, info in students.items():
    #     print(f'ID: {id}, 信息: {info}')


def sort():
    pass


def modify():
    pass


def count():
    pass


main()
# system= main()
# system.menu()
