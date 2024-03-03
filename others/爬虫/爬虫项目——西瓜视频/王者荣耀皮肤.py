import requests
from lxml import etree
from fake_useragent import UserAgent
headers={
    'user-agent':UserAgent().random
}
hero_list=requests.get('https://pvp.qq.com/web201605/js/herolist.json').json()
# print(hero_list)
for hero in hero_list:
    ename=hero['ename']
    cname=hero['cname']
    id_name=hero['id_name']
    # print(ename,cname,id_name)


# hero_id_name='yunying'
#     hero_url=requests.get(f'https://pvp.qq.com/web201605/herodetail/{id_name}.shtml')
    for number in range(1,7):
        skin_url=f'https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{ename}/{ename}-bigskin-{number}.jpg'
        print(skin_url)
        im=requests.get(skin_url,headers=headers)
        if im.status_code==200:
            # 保存图片
            with open(f'./王者荣耀皮肤/{id_name}_{number}.jpg','wb')as f:
                f.write(im.content)
                print(f'保存{id_name}_{number}.jpg成功')