import uiautomator2 as u2

from Company_project.AutoTest.Auto_U2_Forexchat.poTest.data.datas import editGropDescription_textInput

d=u2.connect('127.0.0.1:21513')


EditGroupProfile=d(description="编辑群资料")

# 群头像
Avatar=d.xpath('//*[contains(@content-desc,"群头像")]')
# 群名称
Name=d.xpath('//*[contains(@content-desc,"群名称")]')
InputGroupName=d(className="android.widget.EditText")
# 群介绍
Description=d.xpath('//*[contains(@content-desc,"群介绍")]')
InputGroupDescription=d(className="android.widget.EditText")

Cancel=d.xpath('//*[contains(@content-desc,"编辑群介绍")]/android.widget.ImageView[1]')
complete=d(description="完成")
Sure=d.xpath('//*[@content-desc="确定"]')























