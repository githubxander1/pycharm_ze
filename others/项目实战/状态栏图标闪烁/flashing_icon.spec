# -*- mode: python ; coding: utf-8 -*-

# 分析阶段
a = Analysis(
    ['flashing_icon.py'],  # 主脚本文件
    pathex=[],  # 可执行文件搜索路径
    binaries=[],  # 二进制文件列表
    datas=[('D:/1test/PycharmProject/flashing_icon_0.1/tray_icons', 'tray_icons')],  # 数据文件及其目标路径
    hiddenimports=[],  # 隐藏导入的模块
    hookspath=[],  # 自定义钩子路径
    hooksconfig={},  # 自定义钩子配置
    runtime_hooks=[],  # 运行时钩子
    excludes=[],  # 排除的模块
    noarchive=False,  # 是否不创建归档文件
    optimize=0,  # 优化级别（0 表示不优化）
)

# 创建 PYZ 文件（Python 压缩文件）
pyz = PYZ(a.pure)

# 创建 EXE 文件
exe = EXE(
    pyz,  # Python 压缩文件
    a.scripts,  # 脚本文件
    a.binaries,  # 二进制文件
    a.datas,  # 数据文件
    [],  # 附加文件
    name='flashing_icon',  # 可执行文件名称
    debug=False,  # 是否启用调试模式
    bootloader_ignore_signals=False,  # 是否忽略信号
    strip=False,  # 是否移除符号表和调试信息
    upx=True,  # 是否使用 UPX 压缩
    upx_exclude=[],  # UPX 压缩排除列表
    runtime_tmpdir=None,  # 运行时临时目录
    console=False,  # 是否显示控制台窗口
    disable_windowed_traceback=False,  # 是否禁用窗口化 traceback
    argv_emulation=False,  # 是否启用命令行参数仿真
    target_arch=None,  # 目标架构
    codesign_identity=None,  # 代码签名身份
    entitlements_file=None,  # 权限文件
)
