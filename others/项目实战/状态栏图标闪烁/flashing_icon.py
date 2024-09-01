import os
import time
import threading
from PIL import Image
import pystray
import sys

# 获取当前脚本所在目录
script_dir = os.path.dirname(os.path.abspath(__file__))
icon_dir = os.path.join(script_dir, 'tray_icons')
icon_files = ['1.ico', '2.ico', '3.ico', '4.ico']

# 加载图标并检查是否存在
icons = []
for file in icon_files:
    try:
        icon_path = os.path.join(icon_dir, file)
        if not os.path.exists(icon_path):
            print(f"警告：文件 {icon_path} 不存在")
            continue
        icons.append(Image.open(icon_path))
    except Exception as e:
        print(f"错误：无法加载文件 {icon_path}，原因：{e}")

# 检查是否有图标被成功加载
if not icons:
    print("没有找到任何图标文件，请检查路径和文件名")
    sys.exit()  # 使用 sys.exit() 替换 exit()

# 当前图标索引
current_index = 0

# 定义一个函数来切换图标
def toggle_icon(icon):
    global current_index
    current_index = (current_index + 1) % len(icons)
    icon.icon = icons[current_index]
    icon.update_menu()

# 创建系统托盘图标
def create_icon():
    menu = pystray.Menu(
        pystray.MenuItem('退出', lambda icon, item: icon.stop())
    )
    icon = pystray.Icon("name", icons[0], menu=menu)
    return icon

# 启动系统托盘图标
def run_icon(icon):
    icon.run()

# 启动定时器切换图标
def run_timer(icon):
    while True:
        toggle_icon(icon)
        time.sleep(0.01)

# 主程序入口
if __name__ == '__main__':
    icon = create_icon()
    threading.Thread(target=run_icon, args=(icon,)).start()
    threading.Thread(target=run_timer, args=(icon,)).start()
