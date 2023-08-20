from urllib import parse,request
from fake_useragent import UserAgent

class TiebaSpider(object):
    def __init__(self):
        self.url='http://tieba.baidu.com/?{}'
        self.userAgent=UserAgent()

    def get_html(self,filename):
        self.headers = {f'User-Agent':'{self.userAgent}'}
        req=request.Request(self.url,headers=self.headers)
        res=request.urlopen(req)
        html=res.read().decode('utf-8')
        with open(filename,'w') as f:
            f.write(html)

if __name__ == '__main__':
    tieba=TiebaSpider()
    params='啊啊'
    url=tieba.url.format(params)
    tieba.get_html(tieba.html)