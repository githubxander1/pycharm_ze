import requests
host = 'http://127.0.0.1:8047'

class APIMgr:

    def __init__(self):
        self.cookies = self.mgr_login('byhy',88888888)
        # print(self.cookies)

    def _printResponse(self,response):
        print('\n\n-------- HTTP response * begin -------')
        print(response.status_code)

        for k,v in response.headers.items():
            print(f'{k}: {v}')

        print(response.content.decode('utf8'))
        print('-------- HTTP response * end -------\n\n')

    def mgr_login(self,username,password):
        response=requests.post(url=host+"/api/mgr/signin",
                                 data={
                                     'username': username,
                                     'password': password
                                 }
                                 )

        # self._printResponse(response)
        self.cookies = response.cookies
        return self.cookies


# 客户操作
    def customer_list(self,pagesize=100,pagenum=1):
        print('列出客户')
        response = requests.get(url=host + "/api/mgr/customers",cookies=self.cookies,
                              params={
                                    'action': 'list_customer',
                                    'pagesize': pagesize,
                                    'pagenum': pagenum,
                                    'keywords': '',
        })

        # self._printResponse(response)
        return response.json()

    # 提取所有用户id
    def customers_list_ids(self):
        global ids
        # 解析接口返回的json数据
        json_data = APIMgr().customer_list()
        # print(json_data)
        # # 遍历获取所有id
        ids = []
        for customer in json_data['retlist']:
            ids.append(customer['id'])
        return ids

    def customer_add(self,name,phonenumber,address):
        print('添加客户')
        response = requests.post(url=host+"/api/mgr/customers",cookies=self.cookies,
              json={
                    "action":"add_customer",
                    "data":{
                        "name":name,
                        "phonenumber":phonenumber,
                        "address":address
                    }
                })

        self._printResponse(response)
        return response
#

    def customer_add2(self,data):
        print('添加客户')
        response = requests.post(url=host+"/api/mgr/customers",
              json={
                    "action":"add_customer",
                    "data":data
                })

        self._printResponse(response)
        return response

    def customer_del(self,cid):
        print('删除客户')
        response = requests.delete(url=host+"/api/mgr/customers",cookies=self.cookies,
              json={
                    "action":"del_customer",
                    "id": cid
                })

        self._printResponse(response)
        return response
#
#
    def customer_del_all(self):
        response = self.customer_list()

        theList = response["retlist"]
        for one in theList:
            self.customer_del(one["id"])

    # 药品操作

    def medicine_list(self):
        print('列出药品')
        response = requests.post(url=host+"/api/mgr/medicines",cookies=self.cookies,
              data={
                  'action' :'list_medicine',
                  'pagesize':100,
                  'pagenum' :1,
                  'keywords' :'',
              })

        self._printResponse(response)
        return response

        # 提取所有用户id
    def medicine_list_ids(self):
        # global ids
        # 解析接口返回的json数据
        json_data = APIMgr().medicine_list()
        # print(json_data)
        # # 遍历获取所有id
        medicine_ids = []
        for medicine in json_data['retlist']:
            medicine_ids.append(medicine['id'])
        return medicine_ids

    def medicine_del(self,mid):
        print('删除药品')
        response = requests.delete(url=host+"/api/mgr/medicines",cookies=self.cookies,
              json={
                    "action":"del_medicine",
                    "id": mid
                })

        self._printResponse(response)
        return response


    def medicine_del_all(self):
        response = self.medicine_list()

        theList = response["retlist"]
        for one in theList:
            self.medicine_del(one["id"])


    # 药品操作

    # 添加药品
    def medicine_add(self):
        response=requests.post(url=host+'/api/mgr/medicines',data=
                        {
                            "action":"add_medicine",
                            "data":{
                                "name": "青霉素",
                                "desc": "青霉素 国字号",
                                "sn": "099877883837"
                            }
                        })
        self._printResponse(response)
        return response

    def order_list(self,pagesize=10,pagenumber=1,keywords=''):
        print('列出订单')
        response = requests.get(url=host+"/api/mgr/orders",cookies=self.cookies,
              params={
                  'action' :'list_order',
                  'pagesize' :pagesize,
                  'pagenum' :pagenumber,
                  'keywords' :keywords,
              })

        self._printResponse(response)
        return response

    def order_del(self,oid):
        print('删除订单')
        response = requests.delete(url=host+"/api/mgr/orders",cookies=self.cookies,
              json={
                    "action":"delete_order",
                    "id": oid
                })

        self._printResponse(response)
        return response

    def order_del_all(self):
        response = self.order_list(100,1)

        theList = response["retlist"]
        for one in theList:
            self.order_del(one["id"])

#
# apimgr = APIMgr()
# # print(apimgr.customer_add('name','13256478908','地址'))
# # print(apimgr.mgr_login('byhy',88888888))
# # print(apimgr.customer_list())
# # print(apimgr.customer_del_all())
# # print(apimgr.order_list())
# # print(apimgr.order_del(15))
# print(apimgr.medicine_list())