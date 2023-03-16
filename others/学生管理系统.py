import sqlite3
import easygui
import copy
students = sqlite3.connect("../students.db")
plus = sqlite3.connect("../createdPlus.db")
students.execute("""CREATE TABLE IF NOT EXISTS students(ID INT UNIQUE,NAME TEXT,SCORE INT)""")
plus.execute("""CREATE TABLE IF NOT EXISTS created(NAME TEXT,SCORE INT)""")
def addStudents():
    data = easygui.multenterbox("请输入学生信息：","录入",fields=["学号","姓名"])
    while data:
        data[0] = int(data[0])
        data.append(0)
        students.execute("INSERT INTO students VALUES(?,?,?)",data)
        students.commit()
        data = easygui.multenterbox("请输入学生信息：","录入",fields=["学号","姓名"])
def check():
    data = students.execute("SELECT * FROM students").fetchall()
    names = [i[1] for i in data]
    cache = dict()
    for i in range(len(data)):
        cache[names[i]] = list(data[i])
    data = copy.deepcopy(cache)
    reply = easygui.buttonbox("请选择你要查看的人：","选择",choices=names+['退出'])
    while reply != '退出':
        easygui.msgbox(data[reply][0]+'\n'+data[reply][1]+'\n'+data[reply][2],"信息")
        reply = easygui.buttonbox("请选择你要查看的人：","选择",choices=names+['退出'])
def searchByName(name):
    data = students.execute(f"SELECT * FROM students WHERE NAME = '{name}'").fetchone()
    if data == ():
        return "没有找到这个学生的信息"
    else:
        return data[0]+'\n'+data[1]+'\n'+data[2]
def createNewPlus():
    data = tuple(easygui.multenterbox("请输入此点评的名称和分值：","录入",fields=["名字","分数"]))
    plus.execute("INSERT INTO created VALUES(?,?)",data)
    plus.commit()
    easygui.msgbox("录入成功！","提示")
def send():
    names = students.execute("SELECT NAME FROM students").fetchall()
    names = [i[0] for i in names]
    name = easygui.buttonbox("请选择发送点评的人：","发送点评",choices=names+['退出'])
    if name == '退出':
        return None
    else:
        pluses = plus.execute("SELECT * FROM created").fetchall()
        plusname = [i[0] for i in pluses]
        duiying = {i[0]:i[1] for i in pluses}
        if pluses == []:
            return "没有创建点评呢"
        else:
            selected = easygui.buttonbox("请选择发送的点评：","发送点评",choices=plusname+['退出'])
            if selected == '退出':
                return None
            else:
                score = students.execute(f"SELECT SCORE FROM students WHERE NAME = '{name}'").fetchone()[0]
                students.execute(f"UPDATE students SET SCORE = {score+duiying[selected]} WHERE NAME = '{name}'")
                students.commit()
                return "发送成功！"
def mainloop():
    choices = ["查看学生信息","批量添加学生","通过名称搜索","创建新点评","发送点评"]
    choice = ''
    while choice != '退出':
        choice = easygui.buttonbox("欢迎来到学生管理器：","TIANYI PRODUCT",choices=["查看学生信息","批量添加学生","通过名称搜索","创建新点评","发送点评","退出"])
        if choice == choices[0]:
            try:
                check()
            except:
                easygui.msgbox("还没有录入任何信息！","提示")
        elif choice == choices[1]:
            addStudents()
        elif choice == choices[2]:
            name = easygui.enterbox("输入要查找人的名字：","输入")
            if name == None:
                continue
            easygui.msgbox(searchByName(name),"提示",ok_button='好的')
        elif choice == choices[3]:
            createNewPlus()
        elif choice == choices[4]:
            easygui.msgbox(send(),"提示")
        else:
            continue
mainloop()
students.close()
plus.close()