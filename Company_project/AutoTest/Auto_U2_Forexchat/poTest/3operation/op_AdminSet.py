
# coding: utf-8
import time
import uiautomator2 as u2


from op_ManageGroup import d,adminadd,adminset,sure,manage_groups

# from op_ManageGroup import  manage_groups


# d=u2.connect('127.0.0.1:21513')
d=u2.connect('127.0.0.1:21513')
# 获取设备基本信息
print(d.info)
d.implicitly_wait(10)
d.app_start('com.bv.forexchat')

# 取消更新
# d(description="取消").click()


# 编辑群头像成功
def admin_set():
    manage_groups()
    adminset.click()
    time.sleep(10)
    d.xpath('//*[contains(@content-desc="移除")]').click()
    # adminadd.click()
    # time.sleep(5)

    # d.xpath('//*[@content-desc="CC​钉​邮​"]/android.widget.ImageView[1]').click()
    # d.click(0.081, 0.267)
    # sure.click()



#
if __name__ == '__main__':
    admin_set()

