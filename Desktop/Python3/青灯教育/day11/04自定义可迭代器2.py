# -*- conding: utf-8 -*-
# author:Andy
# time:2020/7/29
import time
class Myrange:
    def __init__(self,start,stop,step):
        # 接收参数的时候可能是一个参数 可能是两个参数 也能可能是三个参数
        self.stmp = start - step
        self.stop = stop
        self.start = start
        self.step = step
    def __iter__(self):
        # 实现一个生成器，返回自己本身
        return self
    def __next__(self):
        # 如果运行结果还没到达结束值
        if self.stmp < self.stop:
            self.stmp += self.step
            time.sleep(1)
            return self.stmp
        else:
            pass

my_range = Myrange(1, 3, 3)
# 当进行 可迭代的时候他会触发 __next__ 函数
for i in my_range:
    print(i)
