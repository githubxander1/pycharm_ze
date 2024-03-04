import json
import os

import allure
import pytest

from CompanyProject.Fastbull.Api_fastbull.common.mongoDB_handler import  MongoDBHandler
from CompanyProject.Fastbull.Api_fastbull.logic.comment import add_comment, delete_comment, logger


class TestAddComment:
    comment_id = None
    def setup(self):
        self.client = MongoDBHandler(
            host='192.168.7.72',
            port=27017,
            username='fastbull',
            password='IOE*2EW#OIWddOPcDWE',
            db_name='fastbull_news_test')
        print("测试用例开始执行")
        logger.warning("测试用例开始执行")
    def tearDown(self):
        # delete_comment(self.comment_id)
        print(f'要删除的id是：{self.comment_id}')
        result = self.client.delete_document('comment_info', filter_query={"_id": self.comment_id})

        if result.deleted_count == 1:
            print("成功删除了1条符合条件的数据")
        elif result.deleted_count > 1:
            print(f"成功删除了{result.deleted_count}条符合条件的数据")
        else:
            print("没有找到符合条件的数据进行删除")
        logger.warning("测试用例执行完毕")
        # print(f'要删除的id: {self.comment_id}')
        # filter_query = {"_id": self.comment_id}
        # result = self.client.delete_document('comment_info', filter_query)
        # if result.deleted_count == 1:
        #     print("数据已删除")
        #     logger.warning(f"删除ask_id={self.comment_id}响应内容：{result}")
        #     # allure.attach(json.dumps(result), name='删除ask_id={self.comment_id}响应内容')
        #     # self.client.close()
        # else:
        #     print("数据不存在")

    @allure.title("文字+表情+图片")
    def test_add_comment(self):
        body = {
            "comment": "1国际油价重挫4%！沙特“服软”降价，原油将重启跌势？[憨笑]112",
            "imageInfoModel": [
                {
                    "high": 226,
                    "url": "https://img.fastbull.com/test/image/2024/02/3E6104A2BE7844E4923B6886D6F2D6A8",
                    "width": 448
                }
            ],
            # "postId": "4279312_1",#对当今世界的资产泡沫要敬而远之
            "postId": "3707814_1",#对当今世界的资产泡沫要敬而远之
            "type": 1
        }
        try:
            response = add_comment(body)
            logger.warning(f"返回值: {response}")
            allure.attach(json.dumps(response, indent=4, ensure_ascii=False),name="返回值")
            # 确保返回值中包含评论ID
            assert len(response) >= 2
            self.comment_id = response[-1]
            print(f"评论ID: {self.comment_id}")
            # self.comment_id = comment_id
            db_check = self.client.find_documents('comment_info', {'_id': self.comment_id})
            # assert db_check.count_documents({}) == 1
            # assert db_check[0]['comment'] == body['comment']
            logger.warning(f"数据库中查询结果: {db_check}")
            # print(comment_id)
        except Exception as e:
            # 处理异常
            print(f"异常信息: {e}")
            return e
        finally:
        #     # 清理评论
            print(f'要删除的id是：{self.comment_id}')
            # 在执行删除前先检查评论是否存在
            found_comment = list(self.client.find_documents('comment_info', {"_id": self.comment_id}))

            if found_comment:
                # 确保只有一条记录匹配（通常_id是唯一的）
                assert len(found_comment) == 1, "预期只找到一条匹配的评论"

                # 删除这条存在的评论
                delete_result = self.client.delete_document('comment_info', {"_id": self.comment_id})

                if delete_result.deleted_count == 1:
                    print("成功删除了1条符合条件的数据")
                elif delete_result.deleted_count > 1:
                    print(f"意外情况：成功删除了{delete_result.deleted_count}条符合条件的数据")
                else:
                    print("删除操作未找到符合条件的数据，可能数据已被其他操作删除")
            else:
                print("在尝试删除之前，评论已不存在")

if __name__ == '__main__':
    pytest.main(['-vs', '--alluredir=./allure-results', 'test_addComment.py'])
    os.system('allure generate ./allure-results -o open ./allure-results/report/html --clean ')
