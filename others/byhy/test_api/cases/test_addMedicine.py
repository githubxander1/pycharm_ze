import pytest
import requests
from others.byhy.test_api.lib import APIMgr, host


class TestAddMedicine():
    # @classmethod
    def setup_class(cls):
        # 登录获取cookies
        cls.cookies = APIMgr().mgr_login('byhy',88888888)

    # 添加药品成功

    def test_add_medicine_success(self):
        response = requests.post(url=host + "/api/mgr/medicines", cookies=self.cookies,
                                json={
                                    "action":"add_medicine",
                                    "data":{
                                        "name": "青霉素",
                                        "desc": "青霉素 国字号",
                                        "sn": "099877883837"
                                    }
                                })
        print(response.json())
        assert 0 == response.json()['ret']
        assert response.json()['id'] in APIMgr().medicine_list_ids()

    # 添加失败，缺少必填参数
    def test_add_medicine_missing_parameter(self):
        response = requests.post(url=host + "/api/mgr/medicines", cookies=self.cookies,
                                 json={
                                     "action": "add_medicine",
                                     "data": {
                                         "name": "青霉素",
                                         "desc": "青霉素 国字号",
                                         # "sn": "099877883837"
                                     }
                                 })
        print(response.json())
        # assert response.status_code == 200
        assert 2 == response.json()['ret']
        # assert "no parameter: action" == response.json()['msg']

    # 添加失败，name为空
    def test_add_medicine_invalid_phonenumber(self):
        response = requests.post(url=host + "/api/mgr/medicines", cookies=self.cookies,
                                 json={
                                     "action": "add_medicine",
                                     "data": {
                                         "name": "",
                                         "desc": "青霉素 国字号",
                                         "sn": "099877883837"
                                     }
                                 })
        print(response.json())
        # assert response.status_code == 200
        assert 2 == response.json()['ret']
        # assert "no parameter: action" == response.json()['msg']

if __name__ == '__main__':
    pytest.main([__file__])
