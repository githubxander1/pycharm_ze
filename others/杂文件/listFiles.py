import os
import shutil

# 列出文件名
# lists = os.listdir(r'C:/Users/Administrator/Downloads')
path=r'C:/Users/Administrator/Downloads'
# 提取后缀名
# 新建类型文件夹
for root,ds,fs in os.walk(path):
    for f in fs:
        type = f.split('.')[-1]
        if not os.path.exists(f'C:/Users/Administrator/Downloads/{type}'):
            os.mkdir(f'C:/Users/Administrator/Downloads/{type}')
# 设置每个文件的存储路径和每个文件的位置
file = f'C:/Users/Administrator/Downloads/{list}'
print("要移动的文件:",file)
path = f'C:/Users/Administrator/Downloads/{type}'
print("移动的位置:",path)

shutil.move(file, path)
