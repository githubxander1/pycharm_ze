import requests
from lxml import etree
from fake_useragent import UserAgent

media='https://m701.music.126.net/20240303101119/5d233fa3b5940de3589d77e8e057a6c8/jdyyaac/obj/w5rDlsOJwrLDjj7CmsOj/29329992535/7d05/7b18/932a/4aab5591398c8ac68f501efe21243bca.m4a'
# 'https://music.163.com/#/song?id=2034187125'
hotsongs='https://music.163.com/#/discover/toplist?id=3778678'

m='https://m801.music.126.net/20240303102706/0a9dc843d8e3553f3672dbe869dca796/jdyyaac/obj/w5rDlsOJwrLDjj7CmsOj/29329992535/7d05/7b18/932a/4aab5591398c8ac68f501efe21243bca.m4a'
kaichu='https://m801.music.126.net/20240303102819/cb2508230d367ef2bef1f8ea4c60422a/jdyyaac/obj/w5rDlsOJwrLDjj7CmsOj/32103516877/3532/074b/bdea/4f512dfb86fec567b51062cc17695e22.m4a'
xuanni='https://m801.music.126.net/20240303103037/cca607b14fd0a349425716bbf2d6f9e5/jdyyaac/obj/w5rDlsOJwrLDjj7CmsOj/32048585194/3ae6/9029/4439/a1ee98567f8ef9469319a85700a24486.m4a'
# 20341871251709432105930

headers={
    'User-Agent':UserAgent().random
}
sourse=requests.get('https://music.163.com/discover/toplist?id=3778678',headers=headers).text
html=etree.HTML(sourse)

songsid_list=html.xpath('//a[contains(@href,"/song?id")]')
# print(songsid_list)
for id in songsid_list:
    href=id.xpath('./@href')[0]
    # print(href)
    music_id=href.split('=')[1]
    print(music_id)
    music_name=id.xpath('./text()')[0]
    print(music_name)
