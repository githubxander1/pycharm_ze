from Company_project.UI_U2_Forexchat.operation.GroupSet import ManageGroup
from Company_project.UI_U2_Forexchat import Base1, d

class GroupAdd(Base1):
    groupadditionMethod = d(description="加群方式")
    everyone = d(description="允许任何人加群")
    needVerify = d(description="需要发送验证消息")
    forbid = d(description="不允许任何人加群")
    # 加群方式
    def groupAdd_set(self):
        ManageGroup().manage_groups()
        ManageGroup().groupadditionMethod.click()
        GroupAdd().everyone.click()



#
if __name__ == '__main__':
    GroupAdd().groupAdd_set()

