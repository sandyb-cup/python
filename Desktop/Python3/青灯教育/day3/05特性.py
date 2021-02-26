# -*- conding: utf-8 -*-
# author:Andy
# time:2020/7/29
class Father:
    name = '爸爸'
    @staticmethod
    def test():
        """

        这个封装函数相当于定义一个类属性
        可以不用self. 而可以直接调用

        :return:
        """
        print('hello python staticmethod')

    @property
    def test2(self):
        """
        这个函数确保了后面数据的保密性
        这个方法不接受任何参数
        他就像是定义了一个新的属性
        相当于在类的__init__函数当中定义的self.XXXXX
        这个类 可以定一个函数直接返回 里面可以是一个运算函数
        后面直接返回 后期调用时不能对其进行修改
        :return:

        """
        a = 1
        b = 2
        c = a + b
        return f"{a}+{b} = {c}"

    @classmethod
    def test3(cls):
        """
        声明一个类属性
        后面想要调用这个类属性 函数名字的后面得加上一个()
        相当于调用一个类
        这样的好处在于在类当中还可以去分裂出一个子类
        方便理解
        :return:
        """
        return cls.name



baba = Father()
result2 = baba.test()
print(result2)

result = baba.test2
print(result)

print(baba.test3())

