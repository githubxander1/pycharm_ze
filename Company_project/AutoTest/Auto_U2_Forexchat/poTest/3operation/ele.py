import uiautomator2 as u2

from Company_project.AutoTest.Auto_U2_Forexchat.poTest.data.datas import editGropDescription_textInput

d=u2.connect('127.0.0.1:21513')

# 编辑群资料
editgroupprofile=d(description="编辑群资料")

# 群头像
avatar=d.xpath('//*[contains(@content-desc,"群头像")]')
defaultavatar=d(description="默认头像选择")
avatar1=d.xpath('//*[@resource-id="android:id/content"]/android.widget.framelayout[1]/android.view.view[1]/android.view.view[1]/android.view.view[1]/android.view.view[1]/android.view.view[2]/android.view.view[1]/android.widget.imageview[1]')

# 群名称
name=d.xpath('//*[contains(@content-desc,"群名称")]')
inputgroupname=d(className="android.widget.edNittext")
# 群介绍
description=d.xpath('//*[contains(@content-desc,"群介绍")]')
inputgroupdescription=d(className="android.widget.edittext")

cancel=d.xpath('//*[contains(@content-desc,"编辑群介绍")]/android.widget.imageview[1]')
complete=d(description="完成")
sure=d.xpath('//*[@content-desc="确定"]')


# 设置管理员
adminset=d.xpath('//*[contains(@content-desc,"设置管理员")]')

# adminadd=d.xpath('//*[contains(@content-desc,"添加管理员")]/')
adminadd=d(description="添加管理员")

groupMute=d(description="设置群内禁言")
switch=d.xpath('//android.widget.Switch')

addFriend=d(description="禁止群内成员互加好友")

groupadditionMethod=d(description="加群方式")
everyone=d(description="允许任何人加群")
needVerify=d(description="需要发送验证消息")
forbid=d(description="不允许任何人加群")

groupBlacklist=d(description="群黑名单")
transferGroup=d(description="转让群")






















