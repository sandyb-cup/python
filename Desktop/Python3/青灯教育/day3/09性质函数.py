# -*- conding: utf-8 -*-
# author:Andy
# time:2020/7/29
class Father:
    def __init__(self, name):

        self.name = name

    @property # 定义一个方法 他可以传递参数 只是于classmethod 于static一个区别
    def test1(self):
        print(self.name)
        print('proprty')

        # return f'c{c}'

    def test(self):
        c = self.test1
        print('普通函数')
        # print(c)

    @classmethod
    def test4(cls):
        print('类属性函数')
        c = 'class'
        return c

    @staticmethod
    def test3():
        c = 1
        b = 3
        g = c + b
        print('静态函数定义方法调用')
        return g


# 调用方法1
c = Father.test1
print(c)
# 他会返回一个对象
'''
    @property
    函数定义方法 他定义的是一个类属性 相当于是__init__(self): 下面的类属性 直接调用即可
'''
c = Father(name = '村花').test1

# 报错一行
# c = Father.test()

'''
    @classmethod 
    类属性调用方法 不用定义函数参数直接调用属性特征即可 (他定义的是一个类方法,不能在里面的传递参数)
'''
c = Father.test4()

'''
    普通函数
'''
# 没有加修饰器的函数 普通函数就是一个类方法 所以调用的时候需要加上一个类的()
c = Father(name = '村花').test()

'''
     加了静态方法的修饰器 他也是一个类属性但是他的属性值是一个静态的属性值 不允许传递任何参数调用时直接在类中"."上方法属性即可
     @staticmethod
'''
c = Father.test3()
# 静态函数也是一个对象

