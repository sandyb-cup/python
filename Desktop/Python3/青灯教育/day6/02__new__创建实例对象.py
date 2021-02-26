# -*- conding: utf-8 -*-
# Author:ononok
# Time:2020/12/9
import pprint
class Son(object):
    name = '儿子'
    def __new__(cls, *args, **kwargs):
        '''
        创建一个实例对象然后返回给 __init__
        __new__是一个类方法
        :param args:
        :param kwargs:
        '''
        # print(dir(cls))
        # 可以在创建类对象之前 进行一些操作
        inst = object.__new__(cls)
        return inst


    def __init__(self):
        '''
            到了实例化方法的时候 实例对象就已经被创建
            实例对象可以绑定 实例对象 也可以调用实例方法

        '''
        print(self)

son = Son()
print(son)

