# -*- conding: utf-8 -*-
# author:Andy
# time:2020/7/29
# 实例对象的封包处理
class FilerAge:
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs): # 如果想要对函数进行回调处理在类中加上一个call回调函数
        result = self.func(*args, **kwargs)
        return result
def func(url):
    print(url)

# 实例对象默认情况下不能被直接调用
func = FilerAge(func)
func('http://www.baidu.com')
