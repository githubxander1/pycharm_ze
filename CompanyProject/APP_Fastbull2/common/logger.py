
# https://blog.csdn.net/shuang_waiwai/article/details/132166813
# https://blog.csdn.net/shuang_waiwai/article/details/132007318
import logging


class Logger(object):
    def __init__(self,name):
        # 1创建日志记录器
        self.logger=logging.getLogger(name)
        # 2设置日志的记录等级:警告级别
        self.logger.setLevel(logging.DEBUG)# 设置日志的记录等级
        # 3设置日志输出渠道
        # 3.1创建一个handler，用于写入日志文件
        self.fh=logging.FileHandler('log.log',mode='a',encoding='utf-8')
        # 3.2设置日志的记录等级
        self.fh.setLevel(logging.DEBUG)
        # 3.3定义handler的输出格式
        formatter=logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levername)s %(message)s')
        self.fh.setFormatter(formatter)#设置写入日志文件的handler的日志格式
        # 4将logger添加到handler里面
        self.logger.addHandler(self.fh)

        # 创建一个handler，用于输出到控制台
        self.ch2=logging.StreamHandler()
        self.ch2.setLevel(logging.DEBUG)
        self.ch2.setFormatter(formatter)
        self.logger.addHandler(self.ch2)

        def log(self,msg):
            self.logger.log(msg)
        def critical(self,msg):
            self.logger.critical(msg)
        def error(self,msg):
            self.logger.error(msg)
        def warning(self,msg):
            self.logger.warning(msg)
        def info(self,msg):
            self.logger.info(msg)
        def debug(self,msg):
            self.logger.debug(msg)

logger=Logger('test')