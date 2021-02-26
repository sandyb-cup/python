# -*- conding: utf-8 -*-
# Author:ononok
# Time:2020/12/9
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

    def __ge__(self, other):
        print('大于等于函数被启用了')
        print(self.area)
        print(other.area)
        return self.area >= other.area

    @property
    def area(self):
        ar = self.width * self.height
        return ar

class Compare:
    def __init__(self, c1):
        self.c1 = c1
        # self.c2 = c2

    def __gt__(self, other):
        print(self.c1)
        print(other)

        return self.c1 > other



rect1 = RectAngle(3, 4)
rect2 = RectAngle(5, 6)

print(Compare(rect1.area).__gt__(other=rect2.area))

# other参数可以从外面传进


