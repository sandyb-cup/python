# -*- conding: utf-8 -*-
# author:Andy
# time:2020/7/29
"""
在一个包子铺中
顾客吃包子
厨师做包子

不可能将包子做出来 再给顾客
"""
import multiprocessing
import time
# 存放30个内容
pipeline = multiprocessing.Queue()

def produce(pipe):
    # 生产者在 pipd里面一直生产
    index = 1
    while True:
        bz = f'第{index}个包子'
        pipeline.put(bz)
        # 队列的内容如果满了 队列就是一个阻塞 等队列有空闲的时候才会进行操作
        print(f"厨师已经做了{index}个包子")
        index += 1
        time.sleep(3)
def consumer(pipe):
    while True:
        bz = pipe.get()
        print(f"消费者买了{bz}个包子")
        time.sleep(1)

if __name__ =="__main__":
    pipeline = multiprocessing.Queue(30)
    multiprocessing.Process(target=produce, args=(pipeline, )).start()
    multiprocessing.Process(target=consumer, args=(pipeline, )).start()

    # 核心数*2+1 进程数量 每一个进程里面再加2个线程
