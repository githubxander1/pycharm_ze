
# # print('---欢迎来到ATM系统--- \n---请选择操作---\n--1.注册 2.登录 3.查询 4.存款 5.取款 6.转账 7.退出--'.center(40))
def shouye():
    print('---欢迎来到ATM系统---'.center(40))
    print('---请选择操作---'.center(40))
    print('--1.注册 2.登录 3.查询 4.存款 5.取款 6.转账 7.退出--'.center(40))
shouye()

print(input('请输入操作：'))

def register():
    print(input('请输入用户名：'))
