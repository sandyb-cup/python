# -*- conding: utf-8 -*-
# Author:ononok
# Time:2020/12/12
import threading
import time
# 获取一把锁
lock = threading.Lock()
num = 0
def add_one():
    global num
    for i in range(10000000):
        # 获取一把锁
        lock.acquire()
        num+=1
        # 释放锁
        lock.release()

def add_two():
    global num
    for i in range(10000000):
        # 获取一把锁
        lock.acquire()
        num+=1
        lock.release()
        # 用一把锁，把六个操作变成一个整体

        """
        1. 锁定 number 的值
        2. 锁定 1 的值
        3. 执行加法操作
        4. 存储加完之后的结果
        5. 锁定加完之后的结果
        6. 返回保存修改
        """


if __name__ == '__main__':
    threading.Thread(target=add_one).start()
    threading.Thread(target=add_two).start()
    while len(threading.enumerate()) > 1:
        time.sleep(0.01)
    print(num)
