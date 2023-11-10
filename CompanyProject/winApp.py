import time
import pywinauto

# 启动计算器应用程序
calc = pywinauto.Application().start("C:\\Windows\\System32\\calc.exe")

# 等待计算器窗口出现
time.sleep(2)

# 获取计算器窗口的句柄
calc_window = calc.window(title="Calculator")

# 输入数字和运算符
input_field = calc_window.child_window(auto_id="txtDigits")
input_field.set_focus()
input_field.type_keys("123+")
input_field.type_keys("{ENTER}")
input_field.type_keys("456-")
input_field.type_keys("{ENTER}")
input_field.type_keys("789*")
input_field.type_keys("{ENTER}")
input_field.type_keys("0=/")
input_field.type_keys("{ENTER}")

# 等待计算结果出现
time.sleep(1)

# 获取计算结果文本框的句柄
result_field = calc_window.child_window(auto_id="txtResult")
result = result_field.text()

# 验证计算结果是否正确
expected_result = "456"  # 假设这是我们期望的结果
if result == expected_result:
    print("测试通过！")
else:
    print("测试失败！实际结果为：", result)