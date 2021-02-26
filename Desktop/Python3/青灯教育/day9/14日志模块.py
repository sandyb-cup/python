# -*- conding: utf-8 -*-
# author:Andy
# time:2020/7/29
import logging

logging.basicConfig(level=logging.WARN,
                    format='%(name)s %(levelname)s %(message)s', # 日志的提示级别 日志的用户名字 日志里面写入的信息

                    datefmt = '%Y-%m-%d %H:%M:%S', # 写入日志的时间格式
                    filename = 'test_loagging.txt', # 日志的文件名字
                    filemode='a', # 日志文件写入的格式
                    )

logging.debug('debug信息') # 信息级别
logging.info('code运行信息')
logging.warning('警告信息')
logging.error('错误信息')
logging.critical('危机信息')
