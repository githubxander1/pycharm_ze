import os
import sys

# 获取当前脚本所在的绝对路径
script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

# 获取 DLL 文件的相对路径
dll_path = os.path.join(script_dir, 'python310.dll')

# 将 DLL 文件添加到 binaries 中
binaries = [(dll_path, '.')] if os.path.exists(dll_path) else []

from PyInstaller.utils.hooks import collect_data_files

a = Analysis(
    ['status_bar_notification.py'],  # 主脚本路径
    pathex=['.'],  # 当前工作目录
    binaries=binaries,
    datas=collect_data_files('status_bar_notification'),  # 收集所有数据文件
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='status_bar_notification',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
