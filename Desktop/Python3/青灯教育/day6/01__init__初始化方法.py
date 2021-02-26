# -*- conding: utf-8 -*-
# Author:ononok
# Time:2020/12/9
class Son:
    def __init__(self):
        '''
            到了__init__函数时self对象就已经被创建
            self 是实例对象 可以绑定实例对象 可以调用实例方法
        '''
        print(self) # 它是一个实例对象

son = Son()
