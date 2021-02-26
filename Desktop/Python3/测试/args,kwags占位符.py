import numpy as np
import requests
class Test:
    def __init__(self, name):
        self.name = name

    def args_print(self, *args, **kwargs):
        self.age = kwargs['age']
        # self.heith = b
        self.name = self.name
        print(f'{self.name}的年龄是{self.age}')
        height = kwargs.values()
        print(height)



        '''
            *args 返回的是一个元组类型的值
            **kwargs 返回的是一个字典参数的值 取里面的参数需要使用键值作为索引
        '''
t = Test('张三').args_print(12, age=13)







