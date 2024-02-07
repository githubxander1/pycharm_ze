import http.server
import os
import subprocess
import threading
import zipfile
from email import encoders
from email.mime.base import MIMEBase

import pytest
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

report_url = 'http://localhost:8000/index.html'  # 使用实际运行的服务器地址和端口
def run_server():
    # 从命令行参数获取报告URL和端口号
    port = 8000  # 指定一个端口号，例如8000
    # 本地服务器打开
    os.chdir(allure_report_dir)
    Handler = http.server.SimpleHTTPRequestHandler

    with http.server.HTTPServer(("", port), Handler) as httpd:
        print("Serving at port", port)
        httpd.serve_forever()
def send_dingtalk_notification():
    project_name = test_script.split('.')[0]
    dingtalk_webhook = 'https://oapi.dingtalk.com/robot/send?access_token=ad751f38f241c5088b291765818cfe294c2887198b93655e0e20b1605a8cd6a2'
    keyword = 'fastbull'
    message = {
        "msgtype": "text",
        "text": {
            "content": f"'{project_name}'测试报告\n"
                       f"时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
                       f"执行人：我是你华哥\n"
                       f"{keyword}接口报告链接: {report_url}"
        }
    }
    response = requests.post(dingtalk_webhook, json=message)
    if response.status_code == 200:
        print("钉钉消息发送成功")
    else:
        print(f"钉钉消息发送失败：{response.text}")

# 打包 Allure 报告成 ZIP 文件
def zip_allure_report(source_path,target_zip):
    with zipfile.ZipFile(target_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:# 创建ZipFile对象，'w'表示写模式（会覆盖已存在的同名文件）
        if os.path.isdir(source_path):# 如果source_path是个目录，则递归打包其下所有文件
            for root, dirs, files in os.walk(source_path):
                for file in files:
                    rel_path = os.path.relpath(os.path.join(root, file), os.path.dirname(source_path))# 计算相对路径，并添加到zip文件中
                    zipf.write(os.path.join(root, file), arcname=rel_path)
        else:
            zipf.write(source_path)# 如果source_path是个文件，则直接添加到zip文件中

    print(f"打包测试报告成功：将文件 '{source_path}' 打包到文件 '{target_zip}'.")
    return target_zip
def send_email_with_attachment(zip_file_path):
    send_email = '2695418206@qq.com'
    password = 'jatpgmthopgedhcb'  # 是授权码
    receiver_email = '12i_ynhx5b51i2@dingtalk.com'

    msg = MIMEMultipart()
    msg['From'] = send_email
    msg['To'] = receiver_email
    msg['Subject'] = '自动化测试报告'

    body = f"请点击以下链接查看最新测试报告：{report_url}"
    msg.attach(MIMEText(body, 'plain'))

    # 使用with语句确保文件正确关闭
    with open(zip_file_path, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        filename = os.path.basename(zip_file_path)
        part.add_header('Content-Disposition', f"attachment; filename= {filename}")
        msg.attach(part)

    try:
        server = smtplib.SMTP('smtp.qq.com', 587)
        server.starttls()
        server.login(send_email, password)
        server.sendmail(send_email, receiver_email, msg.as_string())
        server.quit()
    except smtplib.SMTPAuthenticationError:
        print("SMTP身份验证错误：请检查您的电子邮件和密码。.")
    except smtplib.SMTPException as e:
        print(f"发送邮件时发生错误: {e}")
    except Exception as e:
        print(f"发送邮件时发生了意外错误: {e}")

def run_testcases_and_generate_report():
    # 使用pytest.main运行测试
    pytest.main([test_script, '--alluredir', allure_results_dir, '--clean-alluredir'])

    # 生成和清理Allure报告
    generate_command = f'allure generate {allure_results_dir} -o {allure_report_dir} --clean'
    subprocess.run(generate_command, shell=True)
def send_notifications():
    # 打包 Allure 报告成 ZIP 文件
    zip_file_path = zip_allure_report(allure_report_dir, 'reports.zip')
    # 在新线程中发送钉钉消息和电子邮件通知
    dingtalk_thread = threading.Thread(target=send_dingtalk_notification())
    email_thread = threading.Thread(target=send_email_with_attachment(zip_file_path))

    dingtalk_thread.start()
    email_thread.start()

    dingtalk_thread.join()  # 确保钉钉消息发送完成
    email_thread.join()  # 确保邮件发送完成


if __name__ == '__main__':
    # 从命令行参数获取配置信息
    test_script = 'test_deleteAsk.py'

    allure_results_dir = './result'
    allure_report_dir = './report_allure/'

    run_testcases_and_generate_report()
    send_notifications()
    run_server()

