# -*- conding: utf-8 -*-
# Author:ononok
# Time:2020/12/8
class Son(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # print(self)

    def __str__(self):
        """
            改变函数默认形式
                打印的
                强制转化
            """
        return f'<Son: {self.name} {self.age}>'

    def __repr__(self):
        """再调试的过程中使用的"""
        '''
         在类属性被使用时如果最后要打印出类属性的相关值时 repr会自动调用打印出实例属性值 否则返回的是一个内存地址
         # 当然也可以使用 __str__函数来查看其值 但是如果对象被列表包含 最后使用str打印出来的也是☝一个对象的内存地址
         # 但是使用__repr__函数不会出现这个情况 __repr__功能能覆盖__str__函数其功能
 
         
        '''
        return f'<Son: {self.name} {self.age}>'



son1 = Son('张三', 18)
son2 = Son('李四', 19)

print(son1)
print(str(son2))
print([son1, son2])
