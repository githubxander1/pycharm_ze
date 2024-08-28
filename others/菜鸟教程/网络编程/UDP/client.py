import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#无连接

#请求
s.sendto(b'Hello',('127.0.0.实例25_批量生成PPT版荣誉证书',8000))

#接收
data,addr=s.recvfrom(1024)
print(data.decode('utf-8'))

s.close()