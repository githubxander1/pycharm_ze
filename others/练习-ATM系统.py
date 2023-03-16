

def get_menu():
    while True:
        print(
            '''
            ---欢迎来到ATM系统---
            --请选择操作--
            -1注册  2登录  3查询余额  4存款  5取款  6转账  7退出-
            '''
        )
        op = input('请输入操作：')
        if op == '1':
            reg()
        elif op == '2':
            login()
        elif op == '3':
            balance()
        elif op == '4':
            deposit()
        elif op == '5':
            with
