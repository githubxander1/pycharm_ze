
# coding: utf-8
import time
import uiautomator2 as u2


from ele import adminadd,adminset,sure

from op_ManageGroup import  manage_groups


d=u2.connect('127.0.0.1:21513')
# 获取设备基本信息
# print(d.info)
d.implicitly_wait(10)
d.app_start('com.sy.fxchat')

# 取消更新
d(description="取消").click()


# 编辑群头像成功
def admin_set():
    manage_groups()
    adminset.click()
    time.sleep(3)
    adminadd.click()
    time.sleep(3)
    d.click(0.081, 0.267)
    # sure.click()



#
if __name__ == '__main__':
    admin_set()

