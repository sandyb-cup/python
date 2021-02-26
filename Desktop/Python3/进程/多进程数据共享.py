# -*- conding: utf-8 -*-
# author:Andy
# time:2020/7/29
"""
多进程数据共享
如果
"""
import multiprocessing
import time
def list_appene(array):
    # 队列get获取数据 put放入数据 qsize 获取队列中的个数
    array.put(1)
    array.put(2)
    array.put(3)
    # print(array.qsize())


if __name__=="__main__":
    array = multiprocessing.Queue()
    multiprocessing.Process(target=list_appene, args=(array,)).start()
    multiprocessing.Process(target=list_appene, args=(array,)).start()

    time.sleep(1)
    # 获取数据
    print([array.get()],[array.get()])