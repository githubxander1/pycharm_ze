# 学生信息放在字典里面
student_info = [
    {'姓名': '婧琪', '语文': 60, '数学': 60, '英语': 60, '总分': 180},
    {'姓名': '巳月', '语文': 60, '数学': 60, '英语': 60, '总分': 180},
    {'姓名': '落落', '语文': 60, '数学': 60, '英语': 60, '总分': 180},
]

# 死循环 while True 当一直为真
# 源码自取君羊：708525271
while True:
    # 输出
    print('j')
    # 输入选项
    num = input('请输入你想要进行操作: ')
    # 进行判断, 判断输入内容是什么, 然后返回相应结果
    """
    if .... elif... 多条件判断语句
    """
    if num == '实例25_批量生成PPT版荣誉证书':
        # 新建学生信息, 输入内容  input 输入的内容, 返回字符串数据类型
        name = input('请输入学生姓名: ')
        chinese = int(input('请输入语文成绩: '))
        math = int(input('请输入数学成绩: '))
        english = int(input('请输入英语成绩: '))
        # 字符串与字符串相加: 字符串拼接  int 整数数据类型
        score = chinese + math + english  # 总分
        # 把信息内容, 放入字典里面
        student_dit = {
            '姓名': name,
            '语文': chinese,
            '数学': math,
            '英语': english,
            '总分': score,
        }
        # 把学生信息 添加到列表里面
        student_info.append(student_dit)

    elif num == '2':
        # for循环遍历, 把列表里元素 一个一个提取出来  \t
        print('姓名\t\t语文\t\t数学\t\t英语\t\t总分')
        for student in student_info:
            # student 字典数据类型, 根据键值对, 提取相关内容
            print(
                student['姓名'], '\t\t',
                student['语文'], '\t\t',
                student['数学'], '\t\t',
                student['英语'], '\t\t',
                student['总分'],
            )

    elif num == '3':
        name = input('请输入查询学生姓名: ')
        # 遍历  for else 用法
        for student in student_info:
            # 判断 查询名字和学生名字 是否一致
            if name == student['姓名']:
                print('姓名\t\t语文\t\t数学\t\t英语\t\t总分')
                print(
                    student['姓名'], '\t\t',
                    student['语文'], '\t\t',
                    student['数学'], '\t\t',
                    student['英语'], '\t\t',
                    student['总分'],
                )
                # 跳出本次循环 continue 继续循环下面的代码

                break
        else:
            # 字符串格式化方法 format
            print('查无此人, 没有{}学生信息!'.format(name))


    elif num == '4':
        name = input('请输入删除学生姓名: ')
        # 把每一个学生的信息, 一个一个提取出来
        for student in student_info:
            # 判断, 输入的学生姓名 是否在学生信息库里面
            if name == student['姓名']:
                # 打印成绩, 查看学生情况
                print('姓名\t\t语文\t\t数学\t\t英语\t\t总分')
                print(
                    student['姓名'], '\t\t',
                    student['语文'], '\t\t',
                    student['数学'], '\t\t',
                    student['英语'], '\t\t',
                    student['总分'],
                )
                # 输入是否要真的删除学生信息 <防止>
                choose = input(f'是否确定要删除{name}信息(y/n)')
                # or 或者的意思
                if choose == 'y' or choose == 'Y':
                    # 删除信息  移除列表里面元素 remove()
                    student_info.remove(student)
                    print(f'{name}信息已经被删除!')
                    break
                elif choose == 'n' or choose == 'N':
                    # 跳出循环
                    break
        else:
            print('查无此人, 没有{}学生信息!'.format(name))


    elif num == '5':
        print('修改学生信息')
        name = input('请输入删除学生姓名: ')
        # 把每一个学生的信息, 一个一个提取出来
        for student in student_info:
            # 判断, 输入的学生姓名 是否在学生信息库里面
            if name == student['姓名']:
                # 打印成绩, 查看学生情况
                print('姓名\t\t语文\t\t数学\t\t英语\t\t总分')
                print(
                    student['姓名'], '\t\t',
                    student['语文'], '\t\t',
                    student['数学'], '\t\t',
                    student['英语'], '\t\t',
                    student['总分'],
                )
                # 输入是否要真的删除学生信息 <防止>
                choose = input(f'是否要修改{name}信息(y/n)')
                # or 或者的意思
                if choose == 'y' or choose == 'Y':
                    # 修改操作 和 新建学生信息 有点类似
                    name = input('请输入学生姓名: ')
                    chinese = int(input('请输入语文成绩: '))
                    math = int(input('请输入数学成绩: '))
                    english = int(input('请输入英语成绩: '))
                    # 字符串与字符串相加: 字符串拼接  int 整数数据类型
                    score = chinese + math + english  # 总分
                    # 修改, 做替换  字典修改值
                    student['姓名'] = name
                    student['语文'] = chinese
                    student['数学'] = math
                    student['英语'] = english
                    student['总分'] = score
                    print(f'{name}信息已经修改了!')
                    break
                elif choose == 'n' or choose == 'N':
                    # 跳出循环
                    break
        else:
            print('查无此人, 没有{}学生信息!'.format(name))