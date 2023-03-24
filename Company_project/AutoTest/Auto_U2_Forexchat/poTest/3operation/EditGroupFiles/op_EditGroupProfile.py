
from op_ManageGroup import manage_groups

# 取消编辑群名称
def editGroupName_cancel(NameInput):
    manage_groups()
    EditGroupProfile.click()
    Name.click()
    InputGroupName.send_keys(NameInput)
    Cancel.click()
    Sure.click()

# 编辑群名称成功
def editGroupName_set(NameInput):
    manage_groups()
    EditGroupProfile.click()
    Name.click()
    InputGroupName.send_keys(NameInput)
    complete.click()

# 清空输入框
def editGroupName_clear():
    manage_groups()
    EditGroupProfile.click()
    Name.click()
    InputGroupDescription.clear_text()
    complete.click()