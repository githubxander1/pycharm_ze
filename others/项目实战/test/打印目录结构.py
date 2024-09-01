import os

def print_directory_structure(path, indent=0):
    """
    打印目录结构
    :param path: 要打印的目录路径
    :param indent: 当前层级的缩进数量
    """
    items = os.listdir(path)
    for item in items:
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            print("  " * indent + f"{item}/")
            print_directory_structure(item_path, indent + 1)
        else:
            print("  " * indent + item)

if __name__ == '__main__':
    current_directory = os.getcwd()
    print(f"当前目录结构：")
    print_directory_structure(current_directory)
