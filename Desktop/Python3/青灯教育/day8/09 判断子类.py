# -*- conding: utf-8 -*-
# author:Andy
# time:2020/7/29


class Father:
    def __init__(self, name):
        self.name = name

    def att(self):
        print(self.name)

class Son(Father): # 继承父类
    def __init__(self, name, age):
        super().__init__(name) # 重写父类方法
        self.age = age # 父类中没有的属性重新定义
        self.att()
        self.Son_att()
    def Son_att(self):
        print(self.age)
        print(self.name)








father = Father(name = '爸爸')
#
son = Son(name = '儿子', age = 18)


print(issubclass(Son, Father))

# issibclass 里面放的两个参数是两个类参数 不是实例化对象
