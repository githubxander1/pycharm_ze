from urllib import request,parse
from fake_useragent import UserAgent

def get_url(words):
    params=parse.quote(words)
    url=f'http://www.baidu.com/s?wd={params}'
    return url

def request_url(url,filename):
    # 创建请求
    user_agent=UserAgent()
    headers={f'User-Agent':'{user_agent}'}
    query=request.Request(url,headers=headers)
    openurl=request.urlopen(query)
    html=openurl.read().decode('utf-8')
    # print(html)

    # 保存文件
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == '__main__':
    words='测试网页爬虫'
    filename=words+'.html'
    request_url(get_url(words),filename)
