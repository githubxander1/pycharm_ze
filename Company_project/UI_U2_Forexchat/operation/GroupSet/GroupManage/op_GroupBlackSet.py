from Company_project.UI_U2_Forexchat.operation.GroupSet import ManageGroup
from Company_project.UI_U2_Forexchat import Base1, d

class GroupBlack(Base1):
    groupBlacklist = d(description="群黑名单")

    # 编辑群头像成功
    def friendAdd_set(self):
        ManageGroup().manage_groups()
        GroupBlack().groupBlacklist.click()



#
if __name__ == '__main__':
    GroupBlack().friendAdd_set()

