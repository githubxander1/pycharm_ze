import http.server
import os
import subprocess
import threading
import zipfile
from email import encoders
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email.utils import formataddr

import pytest
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

# 从命令行参数获取报告URL和端口号
report_url = 'http://localhost:8000/index.html'  # 使用实际运行的服务器地址和端口
port = 8000  # 指定一个端口号，例如8000

# 从命令行参数获取配置信息
test_script = 'test_deleteAsk.py'
allure_results_dir = './result'
allure_report_dir = './report_allure/'
dingtalk_webhook = 'https://oapi.dingtalk.com/robot/send?access_token=ad751f38f241c5088b291765818cfe294c2887198b93655e0e20b1605a8cd6a2'
sender_email = '2695418206@qq.com'
password = 'jatpgmthopgedhcb'  # 是授权码
receiver_email = '12i_ynhx5b51i2@dingtalk.com'

zip_file_path=f'{allure_report_dir}.zip'


def send_dingtalk_notification(message):
    response = requests.post(dingtalk_webhook, json=message)
    if response.status_code == 200:
        print("钉钉消息发送成功")
    else:
        print(f"钉钉消息发送失败：{response.text}")

# 打包 Allure 报告成 ZIP 文件
def zip_allure_report(source_path,target_zip):
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
def send_email_with_attachment(zip_file_path):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = '自动化测试报告'

    body = f"请点击以下链接查看最新测试报告：{report_url}"
    msg.attach(MIMEText(body, 'plain'))

    # attachment = open(f'{allure_report_dir}.zip', 'rb')
    attachment = open(zip_file_path, 'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= " + os.path.basename(zip_file_path))
    msg.attach(part)

    server = smtplib.SMTP('smtp.qq.com', 587)
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()


def send_notification(notification_type, message,zip_file_path):
    if notification_type == 'dingtalk':
        send_dingtalk_notification(message)
    elif notification_type == 'email':
        send_email_with_attachment(zip_file_path)
    else:
        raise ValueError(f"Unsupported notification type: {notification_type}")
def run_and_send_notifications():
    # 使用pytest.main运行测试
    pytest.main([test_script, '--alluredir', allure_results_dir, '--clean-alluredir'])

    # 生成和清理Allure报告
    generate_command = f'allure generate {allure_results_dir} -o {allure_report_dir} --clean'
    subprocess.run(generate_command, shell=True)

    # 构建钉钉消息
    keyword = 'fastbull'
    message = {
        "msgtype": "text",
        "text": {
            "content": f"'删除评论'测试报告\n"
                       f"时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
                       f"执行人：我是你华哥\n"
                       f"{keyword}接口报告链接: {report_url}"
        }
    }

    # 打包 Allure 报告成 ZIP 文件
    zip_file_path = zip_allure_report(allure_report_dir, 'report.zip')

    # 在新线程中发送钉钉消息和电子邮件通知
    dingtalk_thread = threading.Thread(target=send_notification, args=('dingtalk', message))
    email_thread = threading.Thread(target=send_notification, args=('email', message, zip_file_path))

    dingtalk_thread.start()
    email_thread.start()

    dingtalk_thread.join()  # 确保钉钉消息发送完成
    email_thread.join()  # 确保邮件发送完成


    # 本地服务器打开
    os.chdir(allure_report_dir)  # 改变工作目录到报告所在位置
    Handler = http.server.SimpleHTTPRequestHandler

    with http.server.HTTPServer(("", port), Handler) as httpd:
        print("Serving at port", port)
        httpd.serve_forever()


if __name__ == '__main__':
    run_and_send_notifications()

    # 本地服务器打开
    os.chdir(allure_report_dir)
    Handler = http.server.SimpleHTTPRequestHandler

    with http.server.HTTPServer(("", port), Handler) as httpd:
        print("Serving at port", port)
        httpd.serve_forever()