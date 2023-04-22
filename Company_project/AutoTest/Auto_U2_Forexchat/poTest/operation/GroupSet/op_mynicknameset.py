# 编辑群头像成功
def nickname_set(name):
    manage_groups()
    mynickname.click()
    nameinput.send_keys(name)
    complete.click()




#
if __name__ == '__main__':
    nickname_set('我的群昵称')

