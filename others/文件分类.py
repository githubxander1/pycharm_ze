# file: all_file.py

import os
import shutil

base1=r'C:\Users\Administrator\Desktop\1'

def files_select():
    for root, ds, fs in os.walk(base1):
        for f in fs:
            type = f.split('.')[-1]
            file=[]
            if not os.path.exists(f'C:\\Users\\Administrator\\Desktop\\1\\{type}'):
                os.mkdir(f'C:\\Users\\Administrator\\Desktop\\1\\{type}')
                fullname = os.path.join(root, file)
                file.append(fullname)
    return file
# file = yuan
# path = f'C:\\Users\\Administrator\\Desktop\\1\\{type}'
# shutil.copyfile(file, path)

# for list in lists:
#     type = list.split('.')[-1]
# print(list)
# if not os.path.exists(f'C:/Users/Administrator/Downloads/{type}'):
#     os.mkdir(f'C:/Users/Administrator/Downloads/{type}')
# # 设置每个文件的存储路径和每个文件的位置
# print(file)
# print(path)
#
# def main():
#     # 1base = './1base/'
#     for i in findAllFile(base1):
#         print(i)
#
#
# if __name__ == '__main__':
#     main()
