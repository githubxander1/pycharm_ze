import os
import smtplib
import zipfile
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests

# 从命令行参数获取配置信息
test_script = 'test_deleteAsk.py'
allure_results_dir = './result'
allure_report_dir = './report_allure/'
dingtalk_webhook = 'https://oapi.dingtalk.com/robot/send?access_token=ad751f38f241c5088b291765818cfe294c2887198b93655e0e20b1605a8cd6a2'
sender_email = '2695418206@qq.com'
password = 'jatpgmthopgedhcb'  # 是授权码
receiver_email = '12i_ynhx5b51i2@dingtalk.com'

report_url = 'http://127.0.0.1:63342/pycharmProject0/CompanyProject/Fastbull/Api_fastbull/testcases/report_allure/index.html?_ijt=6ulaqrl15v9s761mk7bk5f7alk&_ij_reload=RELOAD_ON_SAVE'  # 你的报告网页URL
def Dingtalk(report_url,keyword):
    webhook_url = 'https://oapi.dingtalk.com/robot/send?access_token=ad751f38f241c5088b291765818cfe294c2887198b93655e0e20b1605a8cd6a2'

    # 确保"link.text"或者"link.title"中包含关键词
    message = {
        "msgtype": "link",
        "link": {
            "text": f"{keyword}自动化测试报告",  # 在文本部分添加关键词
            "title": f"{keyword}: 最新测试报告",  # 或者在标题部分添加关键词
            "picUrl": "",
            "messageUrl": report_url,
        }
    }

    response = requests.post(webhook_url, json=message)
    response.raise_for_status()  # 检查请求是否成功
    print(response.text)

def send_email_with_report_attachment(sender_email, password, receiver_email, report_url, allure_report_dir):
    server = smtplib.SMTP('smtp.qq.com', 25)  # 替换为你的SMTP服务器和端口
    server.login(sender_email, password)

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = '自动化测试报告'

    body = f"请点击以下链接查看最新测试报告：{report_url}"
    msg.attach(MIMEText(body, 'plain'))

    msg.attach(pack_report(allure_report_dir))
    text = msg.as_string()
    try:
        server.sendmail(sender_email, receiver_email, text)
    except Exception as e:
        print(f"发送邮件时发生错误: {e}")
        server.quit()
        return False
    finally:
        server.quit()

def pack_report(allure_report_dir):
    # 添加测试报告ZIP文件作为附件
    allure_report_dir = f'{allure_report_dir}.zip'
    with zipfile.ZipFile(allure_report_dir, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(allure_report_dir):
            for file in files:
                zipf.write(os.path.join(root, file))

    with open(allure_report_dir, 'rb') as file:
        part = MIMEApplication(file.read(), Name=os.path.basename(allure_report_dir))
        part['Content-Disposition'] = f'attachment; filename="{os.path.basename(allure_report_dir)}"'
        return part

# print(pack_report(allure_report_dir))

    # try:
    #     server.sendmail(sender_email, receiver_email, text)
    # except Exception as e:
    #     print(f"发送邮件时发生错误: {e}")
    #     server.quit()
    #     return False
    # finally:
    #     server.quit()
    #     os.remove(attachment_path)  # 删除临时ZIP文件

def pack_and_send_test_report(sender_email, password, receiver_email, report_url, allure_report_dir):
    if not send_email_with_report_attachment(sender_email, password, receiver_email, report_url, allure_report_dir):
        print("报告打包和发送失败。")

pack_and_send_test_report(sender_email, password, receiver_email, report_url, allure_report_dir)
# Dingtalk(report_url,'fastbull')