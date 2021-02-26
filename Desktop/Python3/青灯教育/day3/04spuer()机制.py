# -*- conding: utf-8 -*-
# author:Andy
# time:2020/7/29
class Father:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.P_attri()

    def P_attri(self):
        print(self.name)
        print(self.age)

class Son(Father): # 继承父类
    def __init__(self, name, age): # 子类的初始化函数 定义属性为name，age  到这一步参数回传递回父类 进行参数重新定义
        super().__init__(name, age) # 初始化 父类的方法重新定义属性 name, age
        '''
            这里的参数 与父类填写的参数是一样的 重新定义参数
        '''

        self.name = '儿子'
        self.age = '18'
        # self.P_attri()

    def P_attri(self):
        print(self.name)
        print(self.age)


Father(name='爸爸',age = '48')

Son(name ='儿子', age='17')


