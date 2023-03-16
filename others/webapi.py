import requests
from pprint import  pprint


class APIMgr:

    def _printResponse(self,response):
        print('\n\n-------- HTTP response * begin -------')
        print(response.status_code)

        for k,v in response.headers.items():
            print(f'{k}: {v}')

        print('')

        print(response.content.decode('utf8'))
        print('-------- HTTP response * end -------\n\n')

    def mgr_login(self,username,password):
        self.s = requests.Session()
        response = self.s.post("http://127.0.0.1/api/mgr/signin",
                                 data={
                                     'username': username,
                                     'password': password
                                 }
                                 )

        self._printResponse(response)
        return response


    def customer_list(self,pagesize,pagenumber,keywords):
        response = self.s.get("http://127.0.0.1/api/mgr/customers",
              params={
                  'action' :'list_customer',
                  'pagesize' :pagesize,
                  'pagenum' :pagenumber,
                  'keywords' :keywords,
              })

        self._printResponse(response)
        return response
    def customer_add(self,pagesize,pagenumber,keywords):
        response = self.s.get("http://127.0.0.1/api/mgr/customers",
              params={
                  'action' :'list_customer',
                  'pagesize' :pagesize,
                  'pagenum' :pagenumber,
                  'keywords' :keywords,
              })

        self._printResponse(response)
        return response