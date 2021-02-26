# -*- conding: utf-8 -*-
# author:Andy
# time:2020/7/29
# 进程包含线程 一个进程只能运行在一个核心里面
# python启动进程要指定 线程 但是java指定进程他自己回开辟线程
# 进程可以同时处理多个任务
# 并行 同时去做一个事情
# 并发 多进程 多线程都可以做

import time
import multiprocessing
def download():
 time.sleep(1)
 print("正在下载")


def upload():
  time.sleep(1)
  print("正在上传")

"""
   args:传递位置参数
   args:传递关键字参数
"""

download_process = multiprocessing.Process(target=download)
upload_process = multiprocessing.Process(target=upload)
if __name__ =="__main__":
 # 多进程里面必须使用main函数来启动

  download_process.start()
  upload_process.start()
  print("主进程运行完毕")
  time.sleep(0.5)








