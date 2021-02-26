# -*- conding: utf-8 -*-
# Author:ononok
# Time:2020/12/10

class RectAngle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        return f'<RectAngle: area{self.area}>'

    def __gt__(self, other):
        print('大于符号被启用了')
        print(self.area)
        print(other.area)
        return self.area > other.area

    def test(self):
        print('子程序')

    def __del__(self):
        # 在清空内存之前可以做其他的事情 比如说是保存文件
        # 清除一个对象就调用一次调用几次实例对象就 __del__ 几次
        print('删除机制被调用')

c = RectAngle(1, 3)
# 在程序结束之前会调用__del__删除机制 清空内存
result = input('输入任何值继续')
c1 = RectAngle(3, 3)
c2 = RectAngle(3, 3).test()


