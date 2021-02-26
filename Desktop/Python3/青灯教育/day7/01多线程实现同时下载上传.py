# -*- conding: utf-8 -*-
# Author:ononok
# Time:2020/12/12
import threading
import time

def download():
    print('下载开始')
    time.sleep(1)
    print('下载结束')

def upload():
    print('上传开始')
    time.sleep(1)
    print('上传结束')

start_time = time.time()
t1 = threading.Thread(target=download)
t1.start()

t2 = threading.Thread(target=upload)
t2.start()

# 设置一个判断防止线程还没有结束就打印出时间 threading.enumerate最后是一个等于1的数 1是一个主线程
'''
    threading.enumerate = 主线程+N个子线程
'''
while len(threading.enumerate()) > 1:
    pass
print('运行时间是:',time.time()-start_time)

