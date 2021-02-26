# -*- conding: utf-8 -*-
# Author:ononok
# Time:2020/12/8
class Example:
    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        """把类对象可以当作想函数一样使用"""
        return "hello world !"


e = Example()
# 把实例对象当作函数使用
print(e())


def add(x, y):
    return x + y


class Add:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    '''
     回调函数返回的是一个对象 调用它时要使用调用类的方法
    '''
    def __call__(self, *args, **kwargs):
        return self.x + self.y


print(add(4, 5))
# 把类当作函数使用
# add_obj 是一个实例对象
add_obj = Add(4, 5)
print(add_obj())

# 面向对象

