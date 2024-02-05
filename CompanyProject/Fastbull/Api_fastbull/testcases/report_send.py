import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests

report_url = 'http://127.0.0.1:63342/pycharmProject0/CompanyProject/Fastbull/Api_fastbull/testcases/report_allure/index.html?_ijt=6ulaqrl15v9s761mk7bk5f7alk&_ij_reload=RELOAD_ON_SAVE'  # 你的报告网页URL
def Dingtalk():
    webhook_url = 'https://oapi.dingtalk.com/robot/send?access_token=ad751f38f241c5088b291765818cfe294c2887198b93655e0e20b1605a8cd6a2'
    # report_url = 'http://your_server/allure_report_html/index.html'  # 你的报告网页URL

    message = {
        "msgtype": "link",
        "link": {
            "text": "自动化测试报告",
            "title": "最新测试报告",
            "picUrl": "",
            "messageUrl": report_url,
        }
    }

    response = requests.post(webhook_url, json=message)
    response.raise_for_status()  # 检查请求是否成功
    print(response.text)

def Email():

    sender_email = '2695418206@qq.com'
    password = 'txj0103@xl'  # 或者是授权码
    receiver_email = '12i_ynhx5b51i2@dingtalk.com'

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = '自动化测试报告'

    body = f"请点击以下链接查看最新测试报告：{report_url}"
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.example.com', 587)  # 替换为你的SMTP服务器和端口
    server.starttls()  # 启用TLS加密
    server.login(sender_email, password)

    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)
    server.quit()
Email()