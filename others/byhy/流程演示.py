import time
from pprint import pprint

import requests
host = 'http://127.0.0.1:8047'

def login():
    global cookies
    response=requests.post(url=host+"/api/mgr/signin",
                                     data={
                                         'username': 'byhy',
                                         'password': 88888888
                                     }
                                     )
    cookies=response.cookies
#     # return response.cookies
login()

# customers_add = requests.post(url=host+"/api/mgr/customers",cookies=cookies,
#               json={
#                     "action":"add_customer",
#                     "data":{
#                         "name":'实例25_批量生成PPT版荣誉证书',
#                         "phonenumber":'123',
#                         "address":'1234'
#                     }
#                 })
# customersId=customers_add.json()['id']
# print(customersId)
# pprint(customers_add.json())

def customers_list():
    customers_list = requests.get(url=host+"/api/mgr/customers",cookies=cookies,
                  params={
                      'action' :'list_customer',
                      'pagesize' :100,
                      'pagenum' :1,
                      # 'keywords' : ,
                  })
    return customers_list.json()

# print(customers_list())
# 提取所有id
def customers_list_ids():
    global ids
    # 解析接口返回的json数据
    json_data = customers_list()
    # print(json_data)
    # # 遍历获取所有id
    ids = []
    for customer in json_data['retlist']:
        ids.append(customer['id'])
    return ids
print(customers_list_ids())

def customers_del(id):
    customers_del = requests.delete(host+"/api/mgr/customers",cookies=cookies,
                  json={
                        "action":"del_customer",
                        "id":id
                    })
    return customers_del.json()
print(customers_del(ids[0]))
# customers_del(70)
# assert customersId in ids
