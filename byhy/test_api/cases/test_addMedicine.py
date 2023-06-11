import pytest
import requests
from byhy.test_api.lib.libapi import APIMgr, host


class TestAddMedicine():
    # @classmethod
    def setup_class(cls):
        # 登录获取cookies
        cls.cookies = APIMgr().mgr_login('byhy',88888888)
        url='/api/mgr/medicines'

    # 添加药品成功

    def test_add_medicine_success(self):
        response = requests.post(url=host + "/api/mgr/medicines", cookies=self.cookies,
                                data={
                                    'action': 'list_medicine',
                                    'pagesize': 100,
                                    'pagenum': 1,
                                    'keywords': '',
                                })
        print(response.json())
        assert 0 == response.json()['ret']
        assert response.json()['id'] in APIMgr().customers_list_ids()

    # 添加客户失败，缺少必填参数
    def test_add_medicine_missing_parameter(self):
        url = 'http://127.0.0.1:8047/api/mgr/customers'
        data ={
            "action":"add_customer",
            "data":{
                "name":"test_customer2",
                "phonenumber":"13245698745",

            }
        }
        response = requests.post(url, cookies=self.cookies, json=data)
        print(response.json())
        # assert response.status_code == 200
        assert 2 == response.json()['ret']
        # assert "no parameter: action" == response.json()['msg']

    # 添加客户失败，手机号格式不正确
    def test_add_medicine_invalid_phonenumber(self):
        url = 'http://127.0.0.1:8047/api/mgr/customers'
        data ={
            "action":"add_customer",
            "data":{
                "name":"test_customer",
                "phonenumber":"",
                "address":"test_address"
            }
        }
        response = requests.post(url, cookies=self.cookies, json=data)
        print(response.json())
        # assert response.status_code == 200
        assert 2 == response.json()['ret']
        # assert "no parameter: action" == response.json()['msg']

if __name__ == '__main__':
    pytest.main([__file__])
