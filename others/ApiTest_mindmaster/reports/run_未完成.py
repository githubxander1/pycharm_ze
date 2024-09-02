# from html_runner import HTMLTestRunner
import time,os,unittest

from HtmlTestRunner import HTMLTestRunner


class TestRunner(object):
    def __init__(self,cases='../',title=u'自动化测试报告',description=u'环境：windows 10'):
        self.cases = cases
        self.title = title
        self.des = description
    def run(self):
        # for filename in os.listdir(self.cases):
        #     if filename == 'report':
        #        break
        #     else:
        #         os.mkdir(self.cases+'/report')
        now = time.strftime('%Y%m%d%H%M%S')
        with  open("./"+".html", 'wb') as fp:
            suites = unittest.defaultTestLoader.discover('../test_cases', pattern='flashing_icon*.py') # 测试套件- 定义测试代码目录和测试用例前缀
            HTMLTestRunner(title='测试标题', description='描述本次测试的大概内容', stream=fp).run(suites)
            fp.close()

if __name__ == '__main__':
    test = TestRunner()
    test.run()