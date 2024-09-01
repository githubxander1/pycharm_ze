# status_bar_notification.spec
# 用于 PyInstaller 打包配置

from PyInstaller.__main__ import run

# 设置打包参数
opts = [
    '--name=status_bar_notification',
    '--onefile',
    '--noconsole',
    '--add-data=tray_icons/*;tray_icons',
    '--icon=tray_icons/1.ico',
    '--legal-trademarks=Developed by Your Company Name',
    '--product-name=Status Bar Notification',
    '--version-file=version_info.txt',
    'status_bar_notification.py'  # 确保这里正确指定了脚本文件
]

# 运行 PyInstaller
run(opts)
