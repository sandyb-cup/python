# -*- conding: utf-8 -*-
# author:Andy
# time:2020/7/29
class Father:
    def __init__(self,name):
        self.name = name

    # 作用返回函数的类方法
    @classmethod
    def test(cls):
        '''
             类属性不能使用self 方法不能传参到classmethod里面
        '''

        a = 1
        b = 2
        c = a+b
        print('类方法调用')
        return f'a{a}+b{b}=c{c}'

    def test2(self):
        print('1233455')

    def test1(self):
        self.test()
        self.test2()
        print('普通函数')
# 调用方法一 实例化对象
# fa = Father(name = 'zhangxin')
# print(type(fa.test()))

# 调用方法直接调用类得属性 不需要传递参数 他就是类的属性
Father.test()


# 普通函数调用方法
Father(name='zangxin').test2()

# 报错
# Father.test1()
