import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 连接服务器
s.connect(('127.0.0.实例25_批量生成PPT版荣誉证书',8080))

# 发送数据
s.send('hello world'.encode('utf-8'))

# 接收数据
data=s.recv(1024)
print(data.decode('utf-8'))

# 关闭连接
s.close()