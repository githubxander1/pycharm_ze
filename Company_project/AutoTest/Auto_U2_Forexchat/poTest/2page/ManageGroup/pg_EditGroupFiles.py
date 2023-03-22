import time
import uiautomator2 as u2

from Company_project.AutoTest.Auto_U2_Forexchat.operation.op_ManageGroup import manage_groups

d=u2.connect('127.0.0.1:21513')




# 点击群介绍
def Description_click(self):
    Description.click()

# 输入群介绍文案
def InputGroupDescription(self,editGropDescription_textInput):
    InputGroupDescription.send_keys(editGropDescription_textInput)

def Cancel_click(self):
    Cancel.click()

def Sure_click(self):
    Sure.click()

