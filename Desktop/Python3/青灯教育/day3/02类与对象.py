# -*- conding: utf-8 -*-
# author:Andy
# time:2020/7/29
"""
     类的概念 ： 指包含由各个事物或现象抽象出来的共同点的抽象概念
     面向对象  ：
        类 ： 是对一类事物抽象概念的总称
        对象 : 对单个事物的抽象概念

"""

class father:
     def bar(self, message):
        print(message)
class son(father): # 继承父类father
    def bar(self, message):
        father.bar(self,message)

son().bar('hello python')







