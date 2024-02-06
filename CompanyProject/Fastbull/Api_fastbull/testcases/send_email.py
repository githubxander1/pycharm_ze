import os
import zipfile

test_script = 'test_deleteAsk.py'
allure_results_dir = './result'
allure_report_dir = './report_allure/'
sender_email = '2695418206@qq.com'
password = 'jatpgmthopgedhcb'  # 这里应替换为真实的授权码
receiver_email = '12i_ynhx5b51i2@dingtalk.com'
def pack_to_zip(source_path, target_zip):
    """
    将源路径(source_path)下的文件和/或目录打包成zip文件(target_zip)。

    参数：
    source_path (str): 需要打包的源文件或目录路径。
    target_zip (str): 目标zip文件的完整路径及名称。

    示例：
    pack_to_zip('E:\\PythonTest\\BackupTest\\code', 'E:\\PythonTest\\BackupTest\\backup\\current_backup.zip')
    """

    # 检查目标路径是否存在，如果不存在则创建
    # if not os.path.exists(os.path.dirname(target_zip)):
    #     os.makedirs(os.path.dirname(target_zip), exist_ok=True)

    # 创建ZipFile对象，'w'表示写模式（会覆盖已存在的同名文件）
    with zipfile.ZipFile(target_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # 如果source_path是个目录，则递归打包其下所有文件
        if os.path.isdir(source_path):
            for root, dirs, files in os.walk(source_path):
                for file in files:
                    # 计算相对路径，并添加到zip文件中
                    rel_path = os.path.relpath(os.path.join(root, file), os.path.dirname(source_path))
                    zipf.write(os.path.join(root, file), arcname=rel_path)
        else:
            # 如果source_path是个文件，则直接添加到zip文件中
            zipf.write(source_path)

    print(f"Successfully packed '{source_path}' into '{target_zip}'.")
    return target_zip


# 使用方法
pack_to_zip(f'{allure_report_dir}', 'report.zip')