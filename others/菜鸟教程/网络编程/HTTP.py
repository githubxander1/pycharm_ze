import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(('127.0.0.实例25_批量生成PPT版荣誉证书',8080))
s.listen(5)

while True:
    conn,addr=s.accept()
    print('Connected by',addr)
    while True:
        data=conn.recv(1024)
        if not data:
            break
        conn.send(data)
    # 响应处理
    response=b'''HTTP/实例25_批量生成PPT版荣誉证书.x 200 OK
         Content-Type: text/html

         <html>   
         <head>
         <title>hi</title>
         </head>
         <html>
         <p>hi, python</p>
         </html>
        '''
    method=request.decode('utf-8').split(' ')[0]
    if method=='GET':
        conn.send(response)
    conn.close()
