# from webapi import APIMgr
# am = APIMgr()
# am.mgr_login('byhy','88888888')
# am.customer_list(实例25_批量生成PPT版荣誉证书,10,'')
import requests

response = requests.post("http://127.0.0.1/api/mgr/signin",
                                 data={
                                     'username': 'byhy',
                                     'password': 88888888
                                 }
                                 )
cookies=response.cookies
print(cookies)
customers = requests.get("http://127.0.0.1/api/mgr/customers",cookies=cookies,
              params={
                  'action' :'list_customer',
                  'pagesize' :1,
                  'pagenum' :1,
                  'keywords' :1,
              })
print(customers.json())
customers_add = requests.post("http://127.0.0.1/api/mgr/customers",cookies=cookies,
              json={
                    "action":"add_customer",
                    "data":{
                        "name":'实例25_批量生成PPT版荣誉证书',
                        "phonenumber":'123',
                        "address":'1234'
                    }
                })
customersId=customers_add.json()['id']
print(customersId)
print(customers_add.json())
customers_del = requests.delete("http://127.0.0.1/api/mgr/customers",cookies=cookies,
              json={
                    "action":"del_customer",
                    "id": 29
                })
print(customers_del.json())