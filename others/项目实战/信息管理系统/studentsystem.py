
def main():
    ctrl=True
    while (ctrl):
        menu()
        optinon_int=int(input('请选择菜单：'))
        if optinon_int in ['0','1','2','3','4','5','6','7']:
            if optinon_int==1:
                insert()
                print('录入学生信息')
            elif optinon_int==2:
                search()
            elif optinon_int==3:
                delete()
            elif optinon_int==4:
                modify()
            elif optinon_int==5:
                sort()
            elif optinon_int==6:
                count()
            elif optinon_int==7:
                show()
            elif optinon_int==0:
                print('欢迎下次使用')
                crtl=False

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

def save(student,filename):
    try:
        student_txt=open(filename,'a')#追加模式打开
    except Exception as e:
        student_txt=open(filename,'w')#文件不存在，创建文件并打开
    for info in student:
        student_txt.write(str(info)+'\n')#按行存储，添加换行符
    student_txt.close()#关闭文件

def insert():
    student_list=[]                      #保存信息列表
    mark=True                            #是否继续添加
    while mark:
        id=input('请输入ID(如1001):')
        if not id:                        #ID为空，跳出循环
            break
        name=input('请输入姓名:')
        if not name:                    #ID为空，跳出循环
            break
        try:
            english=int(input('请输入英语成绩:'))
            python=int(input('请输入python成绩:'))
        except:
            print('输入无效，不是整数，请重新输入')
            continue
        #将输入的信息存到字典
        student={'id':id,'name':name,'english':english,'python':python}
        #将学生信息添加到列表中
        student_list.append(student)
        inputMark=input('是否继续添加？y/n\n')
        if inputMark == 'y':
            mark=True
        else:
            mark=False
    save(student_list)
    print('学生信息录入完毕')
main()
# system= main()
# system.menu()