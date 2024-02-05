import json
import os
import time

import allure
import pytest

from CompanyProject.Fastbull.Api_fastbull.logic.comment import add_comment, delete_comment

class TestAddComment:
    def setUp(self):
        print("测试用例开始执行")
    def tearDown(self):
        delete_comment(self.comment_id)
        print("测试用例执行完毕")

    @allure.title("文字+表情+图片")
    def test_add_comment(self):
        self.body = {
            "comment": "国际油价重挫4%！沙特“服软”降价，原油将重启跌势？[憨笑]112",
            "imageInfoModel": [
                {
                    "high": 226,
                    "url": "https://img.fastbull.com/test/image/2024/02/3E6104A2BE7844E4923B6886D6F2D6A8",
                    "width": 448
                }
            ],
            "postId": "4279312_1",#对当今世界的资产泡沫要敬而远之
            "type": 1
        }
        try:
            response = add_comment(self.body)
            # 确保返回值中包含评论ID
            assert len(response) >= 2
            comment_id = response[-1]
            self.comment_id = comment_id
            # print(comment_id)
        except Exception as e:
            # 处理异常
            print(f"异常信息: {e}")
            return e
        # finally:
        #     # 清理评论
        #     # if hasattr(self, 'comment_id'):
        #     time.sleep(3)
        #     print(self.comment_id)
        #     de=delete_comment(self.comment_id)
        #     print(de['message'])
            # print('删除成功')

if __name__ == '__main__':
    pytest.main(['-s', '--alluredir=./allure-results', 'test_addComment.py'])
    os.system('allure generate ./allure-results -o open ./allure-results/report/html --clean ')
