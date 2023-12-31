import time
# 时间
import unittest
# 加载测试模块
import os
# 处理路径
import HTMLTestRunner
# 生成测试报告必须要用的库
def getSuite():
    # start_dir=加载所有的测试模块来执行,pattern=通过正则的模式加载所有的模块
    '''获取所有执行的测试模块'''
    suite = unittest.TestLoader().discover(
        start_dir=os.path.dirname(os.path.dirname(__file__)),

        pattern='test_*.py'

    )
    return suite


# 获取当前时间
def getNowtime():
    return time.strftime("%y-%m-%d %H_%M_%S",time.localtime(time.time()))

# 执行获取的测试模块,并获取测试报告
def main():
    filename=os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))),os.path.dirname(__file__),'report',getNowtime()+"_report.html")
    # print(filename)
    # 把测试报告写入文件中,b是以二进制的方式写入
    fp=open(filename,"wb")
    # HTMLTestRunner实例化的过程，stream是流式写入，title是测试报告的标题，description是对测试报告的描述
    runner=HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title="ForexChat自动化测试报告",
        description="基于python语言的自动化测试实战"
    )
    runner.run(getSuite())

if __name__=="__main__":
    main()