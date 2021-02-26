# -*- conding: utf-8 -*-
# author:Andy
# time:2020/7/29
"""
 自定义一个生成器对象
 从a-z循环3次结束
"""
class MyRang():
    """
        生成器里面用字符表示
    """
    def __init__(self, start, stop, step = 1, times=2):
        self.start = ord(start) - 1
        # 因为我们还需要对起始值进行重置
        # 进行ascll码的转换
        self.stop = ord(stop) # 进行ascll码的转换
        self.step = step
        self.times = times
        self.now_time = 0
        self.temp = self.start

    def __iter__(self):
        return self
    def __next__(self):
        # 当启始值小雨结束值的时候
        if self.now_time <= 3:
            if self.start < self.stop:
                self.start+=self.step
                return chr(self.start)
            else:
                print('ord_self.start', self.start)
                self.start = self.temp
                self.now_time += 1
                self.temp += self.step
                # 在里面重置之前判断是否已经结束
                if self.now_time >= self.times:
                    return StopIteration
                return chr(self.temp)
        else:
            raise StopIteration

g = MyRang('a', 'z', 1)
for i in g:
    print(i)

'''
    re, csv, os, 
    opempyxl, pdflit, word, 
'''