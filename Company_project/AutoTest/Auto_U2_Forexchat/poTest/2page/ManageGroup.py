import time
import uiautomator2 as u2

from Company_project.AutoTest.Auto_U2_Forexchat.page.ManageGroup.pg_EditGroupFiles import session1, groupSet

d=u2.connect('127.0.0.1:21513')

EditGroupProfile = d(description="编辑群资料")
AddAdmins = d.xpath('//*[contains(@content-desc,"管理员"]')
RestrictSendingMessage = d.xpath('//*[contains(@content-desc,"设置群内禁言"]')
RestrictSendingFriendsRequest = d(description="禁止群内成员互加好友")
AddGroupMethod = d(description="加群方式")
GroupBlacklist = d(description="群黑名单")
TransferOwenership = d(description="转让群")



