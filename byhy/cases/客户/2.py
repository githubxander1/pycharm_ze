import requests

# s=requests.session()
url = "http://127.0.0.1"
r=requests.post(url + '/api/mgr/signin',
                   data={
                       'username': 'byhy',
                       'password': 88888888
                   })
r1=r.post(url + '/api/mgr/customers',headers={'Content-Type':'application/json'},
                        json={
                            "action": "add_customer",
                            "data": {
                                "name": '26',
                                "phonenumber": '15318544154',
                                "address": '1111'
                            }
                        }
                        )
print(r.json())