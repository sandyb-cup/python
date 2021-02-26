# -*- conding: utf-8 -*-
# Author:ononok
# Time:2020/12/10
class Add:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    '''
     回调函数返回的是一个对象 调用它时要使用调用类的方法
    '''
    def test(self, name, world):
        self.name = name
        self.world = world
        print(name, world)

    def __call__(self, name, world):
        self.test(name, world)
        return (self.x + self.y, name, world)

add = Add(1, 3)
print(add('张鑫', 'world'))
# 把类当作函数使用
# add_obj 是一个实例对象
add_obj = Add(4, 5)
print(add_obj) # 打印出来的是一个对象
print(add_obj('张鑫', 'world')) # 打印出来对象里面的内容
print(add_obj ('张鑫', 'world'))

