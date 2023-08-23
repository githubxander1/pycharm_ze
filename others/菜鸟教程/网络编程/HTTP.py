import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(('127.0.0.1',8080))
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
    response=b'''HTTP/1.x 200 OK
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
