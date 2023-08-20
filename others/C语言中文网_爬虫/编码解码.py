from urllib import parse

query_string = {
    'wd':'百度'
}
bianma=parse.urlencode(query_string)
url='http://www.baidu.com/?{}'.format(bianma)
print(url)

# quote编码：只能对字符串编码
query_string1='百度'
bianma1=parse.quote(query_string1)
jiema1=parse.unquote(query_string1)
# url1='http://www.baidu.com/?wd={}'.format(bianma1)
url1='http://www.baidu.com/?wd={}'.format(jiema1)
print(url1)