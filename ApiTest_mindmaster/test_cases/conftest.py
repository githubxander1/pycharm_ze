import pytest

from ApiTest_mindmaster.common.requests_handler import RequestsHandler


@pytest.fixture(autouse=True)
def set_init():
    # 请求类实例化
    req = RequestsHandler()
    yield
    req.close_session()