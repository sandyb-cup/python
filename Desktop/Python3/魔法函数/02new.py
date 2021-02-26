# -*- conding: utf-8 -*-
# author:Andy
# time:2020/7/29
class Son():

    def __new__(cls, *args, **kwargs):
        """
        魔法函数是特殊的函数
        __new__ 必须放回一个参数
        cls 类对象
        :param args:
        :param kwargs:
        """
        # 返回的对象从 object对象来
        instance = object.__new__(cls)

        return instance
    def __init__(self):
        # self 就是对象
        print("Son__init__")

son = Son()
print(son)

