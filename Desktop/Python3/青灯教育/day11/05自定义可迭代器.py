# -*- conding: utf-8 -*-
# author:Andy
# time:2020/7/29
"""
    自定义一个myrange 的类 实现range功能
    但是只接收两个元素 起始值跟步长 实现无限增长跟 for 无限循环
"""
import time
class Myrange:
    def __init__(self,iters, step):
        self.stmp = iters - step
        self.iters = iters
        self.step = step
    def __iter__(self):
        # 实现一个生成器，返回自己本身
        return self
    def __next__(self):
        self.stmp += self.step
        time.sleep(1)
        return self.stmp
my_range = Myrange(1, 3)
# 当进行 可迭代的时候他会触发 __next__ 函数
for i in my_range:
    print(i)
