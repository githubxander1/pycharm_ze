import json
import os

import allure
import pytest
from ApiTest_mindmaster.common.logger_handler import LoggerHandler
from CompanyProject.Fastbull.Api_fastbull.common.mongoDB_handler import MongoDBHandler
from CompanyProject.Fastbull.Api_fastbull.logic.ask import addAsk, deleteAsk, get_expert_ask_reply_page, get_ask_ids

from ApiTest_mindmaster.common.yaml_handler import YamlHandler

yamlhandler=YamlHandler('../data/ask.yaml')
filename=os.path.basename(__file__).split('.')[0]
logger=LoggerHandler(name='root',level='WARNING',file=f'../log/{filename}_log.log',format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class TestAddAsk:
    # def __init__(self):
    # added_ask_id = None
    def setup(self):
        self.client = MongoDBHandler(
            host='192.168.7.72',
            port=27017,
            username='fastbull',
            password='IOE*2EW#OIWddOPcDWE',
            db_name='fastbull_universal_test')
    def teardown(self):
        print(f'要删除的id: {self.added_ask_id}')
        filter_query = {"mId": self.added_ask_id}
        result = self.client.delete_document('mongo_quotes_ask_reply', filter_query)
        if result.deleted_count == 1:
            print("数据已删除")
            logger.warning(f"删除ask_id={self.added_ask_id}响应内容：{result}")
            # allure.attach(json.dumps(result), name='删除ask_id={self.added_ask_id}响应内容')
            self.client.close()
        else:
            print("数据不存在")
        # pass
        # if self.added_ask_id is not None:
        # delete_response = deleteAsk(self.added_ask_id)
        # print(delete_response)
        # logger.warning(f"删除ask_id={self.added_ask_id}响应内容：{delete_response}")
        # allure.attach(json.dumps(delete_response), name='删除ask_id={self.added_ask_id}响应内容')
        #
        # assert delete_response['message'] == '操作成功'

    @allure.feature('问答-接口测试')
    @allure.story('添加问答')
    @pytest.mark.parametrize('add_data',yamlhandler.read_yaml()['addAsk'],ids=lambda add_data: add_data['name'])
    def test_add_ask(self,add_data):
        # 获取请求参数
        body = add_data['data']
        try:
            # 发送请求
            response = addAsk(body)
            print(response)

            # 打印响应内容
            logger.warning(f"响应内容：{response}")

            # 添加Allure附件
            allure.attach(json.dumps(response), name='添加问答响应内容')

            # 断言响应结果
            assert response[0]['message'] == '操作成功'
            logger.warning('断言响应结果成功')

            self.added_ask_id = response[1]
            db_check=self.client.find_documents('mongo_quotes_ask_reply', query={"mId": self.added_ask_id})
            logger.warning(f"数据库查询结果：{db_check}")
            # allure.attach(json.dumps(db_check), name='数据库查询结果')
            assert db_check[0]['mId'] == self.added_ask_id
            logger.warning('断言数据库查询结果')

            assert self.added_ask_id in get_ask_ids()
            logger.warning('断言新增是否成功：在列表中')

            # 打印测试结束信息
            logger.info(f"测试结束")
        except Exception as e:
            logger.error(f"测试失败，错误信息：{e}")
            allure.attach(f"测试失败，错误信息：{e}", name='错误信息')
            pytest.fail()
            return e

if __name__ == '__main__':
    pytest.main([__file__,'-vs', '--alluredir', './result', '--clean-alluredir'])
    os.system('allure generate ./result/ -o ./report_allure/ --clean')
    os.system('allure serve result')
    os.system('allure open ./report_allure/index.html')
