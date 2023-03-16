import logging

# 定义一个日志收集器
logger = logging.getLogger('ITester')

# 设置收集器的级别，不设定的话，默认收集warning及以上级别的日志
logger.setLevel('DEBUG')

# 设置日志格式
fmt =logging.Formatter('%(filename)s-%(lineno)d-%(asctime)s-%(levelname)s-%(message)s')

# 设置日志处理器-输出到文件
file_handler = logging.FileHandler('log.txt')

# 设置日志处理器级别
file_handler.setLevel("DEBUG")

# 处理器按指定格式输出日志
file_handler.setFormatter(fmt)

# 输出到控制台
ch = logging.StreamHandler()
# 设置日志处理器级别
ch.setLevel("DEBUG")
# 处理器按指定格式输出日志
ch.setFormatter(fmt)

# 收集器和处理器对接，指定输出渠道
# 日志输出到文件
logger.addHandler(file_handler)
# 日志输出到控制台
logger.addHandler(ch)

if __name__ == '__main__':
    logger.debug('自定义的debug日志')
    logger.info('自定义的info日志')
    logger.warning('自定义的warning日志')
    logger.error('自定义的error日志')
    logger.critical('自定义的critical日志')