import requests
class RequestsHandler:
    def __init__(self):
        """session管理器"""
        self.session = requests.session()
    def visit(self, method, url, params = None, data= None, json= None, headers= None):
        result = self.session.request(method,url,params=params,data=data,json=json,headers=headers)
        try:
            # 返回json结果
            return result.json()
            # return result
        except Exception:
            return result
    def close_session(self):
        self.session.close()