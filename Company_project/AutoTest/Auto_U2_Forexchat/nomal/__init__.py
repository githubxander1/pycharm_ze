import uiautomator2 as u2

from Company_project.AutoTest.Auto_U2_Forexchat.poTest.data.datas import editGropDescription_textInput

d=u2.connect('127.0.0.1:21513')


EditGroupProfile=d(description="编辑群资料")
Description=d.xpath('//*[contains(@content-desc,"群介绍")]')
# InputGroupDescription=d(text='请输入群介绍')
# InputGroupDescription=d.xpath('//*[contains(@content-desc="编辑群介绍")]/following-sibling::*[1]')
# 兄弟定位
# InputGroupDescription=d.xpath('//*[contains(@content-desc="编辑群介绍")]/android.widget.ImageView[1]').sibling(className="android.widget.EditText")
# classname定位
InputGroupDescription=d(className="android.widget.EditText")

Cancel=d.xpath('//*[contains(@content-desc,"编辑群介绍")]/android.widget.ImageView[1]')
complete=d(description="完成")
Sure=d.xpath('//*[@content-desc="确定"]')

