import requests

url = 'https://userapi.edrawsoft.cn/api/user/login'
r = requests.post(url,
                  data={
                      'email': "2695418206@qq.com",
                      'from': "web",
                      'product': "master-online",
                      'pw': "f2d8ddfc169a0ee6f8b0ecd924b1d300"
                  })

# 获取保存token
token = r.json()['data']['token']
token ='Bearer'+' '+ token
print(token)
# token放到请求头中
headers={
    'Authorization':token
}
# token1=re.findall('"token":"(.+?)"')
# token1=token1[0]
# print(token1)
xinjian = requests.post(url='https://masterapi.edrawsoft.cn/api/oss/23928516/obj', headers=headers,
                    data={
                        # 'id': 23928516,
                        'prefix': 'test_'
                    })
print(xinjian.json())
