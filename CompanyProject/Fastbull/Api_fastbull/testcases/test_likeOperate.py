import time

import requests
import json

from CompanyProject.Fastbull.Api_fastbull.logic.conftest import generate_sign_login, get_identity, generate_btoken, \
    generate_nonce, generate_token
from CompanyProject.Fastbull.Api_fastbull.logic.like import post_like_operate


class TestPostLikeOperate:
    """
    测试新闻点赞
    """
    def test_like(self):
        like=post_like_operate('65ba072cc1034b00073da295',0)
        assert like.status_code == 200  # 检查响应状态码是否为200（成功）
        # 根据实际需要添加更多断言，例如检查响应内容、头部信息等。
        # print(response.json())  # 打印响应内容（假设响应是JSON格式）