import json
import random
import time

import pytest

from CompanyProject.Fastbull.Api_fastbull.logic.comment import add_comment, delete_comment, get_comment_list
from CompanyProject.Fastbull.Api_fastbull.logic.conftest import common_data


class TestDeleteComment:
    def setUp(self):
        pass
    def tearDown(self):
        pass
        # if hasattr(self, 'comment_id'):  # 确保comment_id已定义才尝试删除
        #     delete_comment(self.comment_id)
        #     print('删除成功')
    def test_deleteComment(self):
        # ids=['65bb507835df7d0007cf6361', '65bb4e6b35df7d0007cf635f', '65bb4c0d35df7d0007cf635e',
        #      # '65bb4be835df7d0007cf635d', '65bb4bc935df7d0007cf6308', '65bb4b1d35df7d0007cf6304',
        #      # '65bb4acc35df7d0007cf6303', '65bb3b5d35df7d0007cf62ab', '65bb39f735df7d0007cf62a9',
        #      # '65bb37ef35df7d0007cf62a2', '65bb37d735df7d0007cf62a1', '65bb379e35df7d0007cf62a0',
        #      # '65bb373d35df7d0007cf629f', '65bb36ce35df7d0007cf629e', '65bb36b435df7d0007cf629d',
        #      # '65bb364e35df7d0007cf629c', '65bb35e035df7d0007cf629b', '65bb348235df7d0007cf629a',
        #      '65bb344335df7d0007cf6299', '65bb339535df7d0007cf6298']
        # for id in ids:
        #     self.response=delete_comment(id)
        #     time.sleep(random.randint(1,3))
        self.comment_id='65c04e29f5523e000783b4cb'
        self.response=delete_comment(self.comment_id)
        assert self.response['message']=='操作成功'
        print(self.response)
        # get_comment_list('3707814_1')
        # self.comment_id=self.response[-1]
        # print(self.comment_id)

if __name__ == '__main__':
    pytest.main(__file__,'-vs')
