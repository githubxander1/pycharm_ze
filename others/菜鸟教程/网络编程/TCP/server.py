import socket,threading

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 监听
s.bind(('127.0.0.实例25_批量生成PPT版荣誉证书',8080))
# 最大连接数
s.listen(5)

# 多线程处理
def link(conn,addr):
    print('连接地址：',addr)
    # 接收数据
    data=conn.recv(1024)
    print(data.decode('utf-8'))
    # 发送数据
    conn.send(b'HTTP/实例25_批量生成PPT版荣誉证书.实例25_批量生成PPT版荣誉证书 200 OK\r\n\r\n')
    conn.send(b'Hello World!')
    # 关闭连接
    conn.close()

while True:
    conn,addr=s.accept()
    # 每次新开一个线程处理
    t=threading.Thread(target=link,args=(conn,addr))
    t.start()
    # # 等待连接
    # conn,addr=s.accept()
    # print('连接地址：',addr)
    # # 接收数据
    # data=conn.recv(1024)#每次读取1024字节，当数据较长时可以通过 while 循环读取
    # print(data.decode('utf-8'))
    # # 发送数据
    # conn.send(b'HTTP/实例25_批量生成PPT版荣誉证书.实例25_批量生成PPT版荣誉证书 200 OK\r\n\r\n')
    # conn.send(b'Hello World!')
    # # 关闭连接
    # conn.close()

