import hashlib

md5= hashlib.md5()

md5.update('123456'.encode('utf-8'))

print(md5.hexdigest())

# 加密字符串
# 加密字符串，返回16进制字符串

# 加密文件
# 加密文件，返回16进制字符串

# 加密文件，返回二进制数据

# sha1= hashlib.sha1()
#
# sha1.update('123456'.encode('utf-8'))
#
# print(sha1.hexdigest())
