import json
import unittest
# from common.requests_handler import RequestsHandler
from pprint import pprint

import ddt

from ApiTest_mindmaster.common.excel_handle import ExcelHandler
from ApiTest_mindmaster.common.requests_handler import RequestsHandler



res = req.visit(method=items['method'],
                             url=items['url'],
                             json=items['payload'])
        print(res)