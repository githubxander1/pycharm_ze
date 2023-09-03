from importlib import reload

import test

while True:
    c= input('请输入1：')
    if c != '1':
        break
    print(f'Number:{test.Number}')