

username=['u1','u2','u3']
password=['111','222','333']

def get_menu():
    while True:
        print('''
                  ---欢迎来到ATM系统---
                    ---请选择操作---
    --1.注册 2.登录 3.查询余额 4.存款 5.取款 6.转账 7.退出 8.查询所有用户--
    
    ''')
        op=input('请输入操作：')
        if op == '1':
            reg()
        elif op == '2':
            login()
        elif op == '3':
            balance()
        elif op == '4':
            deposit()
        elif op == '5':
            withdraw()
        elif op == '6':
            transfer()
        # if op == '7':
        #     login()
        else:
            print('请选择正确的操作！')


def reg():
    while True:
        un = input('请输入用户名：')
        for user in username:
            if user ==  un:
                print(input('用户已存在，请重新输入:'))

            else:
                username.append(un)
                print(username)
                break


    while True:
        pw = input('请输入密码：')
        if len(pw) <= 6:
            print('密码需大于6位，请重新输入')




def login():
    un=input('请输入用户名：')
    for user in username:
        if user == username:
            continue
        else:
            print('用户不存在')
def balance():
    pass
def deposit():
    pass
def withdraw():
    pass
def transfer():
    pass

get_menu()
# print(a)