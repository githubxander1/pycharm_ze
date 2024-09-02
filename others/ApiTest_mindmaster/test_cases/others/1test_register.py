import json
import unittest
from common.db_handler import DBHandler
from common.helper import generate_mobile
from common.logger_handler import logger
from common.requests_handler import RequestHandler
from common.excel_handler import ExcelHandler
from config.setting import config
from libs import ddt
from middleware.yaml_handler import yaml_data

# 大致思路如下：
# ①从excel中读取用例数据；
# ②判断用例数据中是否包含#new_phone#；
# ③如包含#new_phone#，则随机生成手机号；
# ④如随机生成的手机号在数据库中存在，则重新生成；
# ⑤如随机生成的手机号在数据库中不存在，则用此手机号替换#new_phone#，进行注册。


@ddt.ddt
class TestRegister(unittest.TestCase):
    # 读取register sheet数据
    excel = ExcelHandler(config.data_path)
    data = excel.read_excel('register')

    def setUp(self):
        self.req = RequestHandler()
        self.db = DBHandler(host=yaml_data['mysql']['host'], port=yaml_data['mysql']['port'],
                            user=yaml_data['mysql']['user'], password=yaml_data['mysql']['password'],
                            database=yaml_data['mysql']['db'], charset=yaml_data['mysql']['charset'])

    def tearDown(self):
        self.req.close_session()
        self.db.close()

    @ddt.data(*data)
    def test_register(self, items):

        # 判断#new_phone#是否在用例数据中
        if "#new_phone#" in items['payload']:
            while True:
                # 使用自动生成手机号的函数
                mobile = generate_mobile()
                # 从数据库中查询此手机号是否存在
                query_mobile = self.db.query("select * from member where mobile_phone=%s;", args=[mobile])
                # 如果不存在，就跳出循环
                if not query_mobile:
                    break
            # 将#new_phone#替换为生成的手机号
            items['payload'] = items['payload'].replace('#new_phone#', mobile)
        logger.info('*' * 30)
        logger.info('测试第{}条测试用例:{}'.format(items['case_id'], items['case_title']))
        logger.info('测试数据是:{}'.format(items))
        # 访问注册接口，获取实际结果
        res = self.req.visit(items['method'], config.host + items['url'],
                             json=json.loads(items['payload']))
        # 断言：预期结果与实际结果对比
        try:
            self.assertEqual(res['code'], items['expected_result'])
            logger.info(res)
            result = 'PASS'
        except AssertionError as e:
            logger.error("测试用例执行失败{}".format(e))
            result = 'fail'
            raise e
        finally:
            TestRegister.excel.write_excel(config.data_path, 'register', items['case_id'] + 1, 8, res['code'])
            TestRegister.excel.write_excel(config.data_path, 'register', items['case_id'] + 1, 9, result)


if __name__ == '__main__':
    unittest.main()