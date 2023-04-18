
# coding: utf-8
import time
import uiautomator2 as u2


from op_ManageGroup import d,adminadd,adminset,sure,manage_groups

# from op_ManageGroup import  manage_groups


d=u2.connect('127.0.0.1:21513')
# d=u2.connect('5ENDU18C21003487')
# 获取设备基本信息
print(d.info)
d.implicitly_wait(10)
d.app_start('com.bv.forexchat')

# 添加管理员
def admin_add():
    manage_groups()
    adminset.click()
    time.sleep(3)
    # adminadd.click()
    d.xpath('//*[contains(@content-desc="添加管理员")]').click()
    # d.click(0.857, 0.379)
    time.sleep(1)
    # d(description="确认").click()

# 移除管理员
def admin_remove():
    manage_groups()
    adminset.click()
    time.sleep(3)
    d.click(0.857, 0.379)
    time.sleep(1)
    d(description="确认").click()
    # time.sleep(5)
    # 获取toast,当没有找到toast消息时，返回default内容
    # assert '管理员身份已移除' in d.toast.get_message(timout=15, default='no toast')
    # # 清空toast缓存
    # d.toast.reset()




#
if __name__ == '__main__':
    admin_add()

