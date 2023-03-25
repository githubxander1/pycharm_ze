from pprint import pprint

import requests

response = requests.post("http://127.0.0.1/api/mgr/signin",
                                 data={
                                     'username': 'byhy',
                                     'password': 88888888
                                 }
                                 )
cookies=response.cookies
print(cookies)
customers_list = requests.get("http://127.0.0.1/api/mgr/customers",cookies=cookies,
              params={
                  'action' :'list_customer',
                  'pagesize' :10,
                  'pagenum' :10,
                  'keywords' :1,
              })
print(customers_list.json())

customers_add = requests.post("http://127.0.0.1/api/mgr/customers",cookies=cookies,
              json={
                    "action":"add_customer",
                    "data":{
                        "name":'1',
                        "phonenumber":'123',
                        "address":'1234'
                    }
                })
customersId=customers_add.json()['id']
print(customersId)
pprint(customers_add.json())

customers_del = requests.delete("http://127.0.0.1/api/mgr/customers",cookies=cookies,
              json={
                    "action":"del_customer",
                    "id":31
                })
print(customers_del.json())

