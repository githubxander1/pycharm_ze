import os

def print_directory_tree(root_dir):
    for root, dirs, files in os.walk(root_dir):
        level = root.replace(root_dir, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))  # 打印目录名
        sub_indent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(sub_indent, f))  # 打印文件名

root_dir = r'D:\1test\PycharmProject\CompanyProject\Fastbull\Api_fastbull'
print_directory_tree(root_dir)
