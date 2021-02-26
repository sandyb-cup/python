# -*- conding: utf-8 -*-
# author:Andy
# time:2020/7/29
import multiprocessing
import time
def list_appene(array):
    array.append(1)
    array.append(2)
    array.append(3)
    print(array)

if __name__=="__main__":
    array = []

    multiprocessing.Process(target=list_appene(array), args=(array)).start()
    multiprocessing.Process(target=list_appene(array), args=(array)).start()
    list_appene(array)
    list_appene(array)
    # 多进程会把当前代码全部复制一份，然后重新创建新的对象
