import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(('127.0.0.1',8080))

# 循环 每次有新的连接触发
while  True:
    # 无连接
    # tcp 需要连接、获取一个可读写的 "流"
    # udp 无连接、直接接受数据包

    # 请求处理
    # data 当前数据包
    # addr 当前连接ip:port
    data,addr=s.recvfrom(1024)
    print(data)
    # 响应
    s.sendto(b'123456',addr)