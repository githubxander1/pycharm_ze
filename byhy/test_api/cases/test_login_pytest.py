import pytest
import requests

# 实例25_批量生成PPT版荣誉证书. 正确的用户名和密码，能够成功登录。
def test_signin_success():
    url = 'http://127.0.0.1:8047/api/mgr/signin'
    data ={
        'username':'byhy',
        'password':88888888
    }
    response = requests.post(url, data=data)
    assert response.status_code == 200
    assert 0 == response.json()['ret']

# 2. 错误的用户名和密码，登录失败。
def test_signin_fail():
    url = 'http://127.0.0.1:8047/api/mgr/signin'
    data ={
        'username':'byh',
        'password':12345678
    }
    response = requests.post(url, data=data)
    assert response.status_code == 200
    assert '用户名或者密码错误' == response.json()['msg']

# 3. 不带用户名或密码，登录失败。
def test_signin_empty():
    url = 'http://127.0.0.1:8047/api/mgr/signin'
    data ={
        'username':'',
        'password':''
    }
    response = requests.post(url, data=data)
    assert response.status_code == 200
    assert '用户名或者密码错误' == response.json()['msg']

if __name__ == '__main__':
    pytest.main([__file__])
