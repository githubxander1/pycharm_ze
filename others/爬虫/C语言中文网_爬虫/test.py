import re
# 题目1： 给定一个字符串，判断该字符串是否为有效的手机号码。 例如： 输入: "13812345678" 输出: True
txt="13812345678"
r1=re.match("^1[345789]\d{9}$",txt)
print(r1)
# 题目2： 给定一个字符串，判断该字符串是否为有效的邮箱地址。 例如： 输入: "example@example.com" 输出: True
t='example@example.com'
r2=re.match("^[0-9a-zA-Z_]+@[0-9a-zA-Z_]+([0-9a-zA-Z_]+)+",t)
print(r2)
# 题目3： 给定一个字符串，判断该字符串是否为有效的URL地址。 例如： 输入: "https://www.example.com" 输出: True
url='https://www.example.com'
r3=re.match('(http|https)://([0-9a-zA-Z.-]+)(:[0-9]+)?(/.*)?',url)#(http∣https)表示匹配http或https，://表示必须包含://，([a−zA−Z0−9.−]+)表示匹配一个或多个字母、数字、点号或短横线，(:[0−9]+)?表示端口号部分可选，可以是一个冒号加一个或多个数字，(/.∗)?表示路径部分可选，可以是一个斜杠加任意字符，表示匹配字符串的结束
print(r3)
# 题目4： 给定一个字符串，判断该字符串是否为有效的身份证号码。 例如： 输入: "110101199001011234X" 输出: True
idcard='110101199001011234'
r4=re.match('^[0-9]{17}[0-9xX]$',idcard)
# r4=re.match('^\d{17}{\d|X}',idcard)
print(r4)
# 题目5： 给定一个字符串，提取出所有的数字。 例如： 输入: "abc123def456ghi789" 输出: ['123', '456', '789']
input1='abc123def456ghi789'
r5=re.findall('\d+',input1)

print(r5)