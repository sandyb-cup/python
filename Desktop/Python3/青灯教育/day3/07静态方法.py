# -*- conding: utf-8 -*-
# author:Andy
# time:2020/7/29
class Father:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 使用静态修饰器时 不能传递参数进里面
    @staticmethod
    def static():
        a = 1
        b = 2
        print('静态方法调用')
        return f'a{a}+b{b}=c{a+b}'

# 调用方法一 实例化参数之后再调用
# fa = Father(name = 'zhangxin', age = '19')
#
# fa.static()

# 调用方法之2 不用实例化参数 不能传递参数
fa = Father.static()


