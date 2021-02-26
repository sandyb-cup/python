# -*- conding: utf-8 -*-
# Author:ononok
# Time:2020/12/12
import threading
import time
num = 0
def add_one():
    global num
    for i in range(100000000):
        num+=1

def add_two():
    global num
    for i in range(100000000):
        num+=1
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
    print(num)
