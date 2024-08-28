from wsgiref.simple_server import make_server

# application 由wsgi服务器调用、函数对http请求与响应的封装、使得Python专注与HTML
# environ http 请求 (dist)
# start_response 响应 (function)
def application(environ, start_response):
 # 请求
 if environ['REQUEST_METHOD'] == 'GET' and environ['PATH_INFO'] == '/':
  # 响应
  start_response('200 OK', [('Content-Type', 'text/html')])
  return [b'<h1>hi, py!</h1>']

# 启动服务器 | 这个服务器负责与 wsgi 接口的 application 函数对接数据
httpd = make_server('127.0.0.实例25_批量生成PPT版荣誉证书', 8000, application)

# 监听请求
httpd.serve_forever()