# -*- conding: utf-8 -*-
# Author:ononok
# Time:2020/12/9
class Father:
    def __init__(self, name, age, tall, height):
        self.name = name
        self.age = age
        self.tall = tall
        self.height = height

    @classmethod
    def Woke(cls):
        print('父亲要工作')
        return True

    def __repr__(self):
        return f'<{self.Woke()}>'

class Son(Father):
    def __init__(self, name, age, tall, height):
        super().__init__(name, age, tall, height)
        self.name = name
        self.age = age
        self.tall = tall
        self.height = height

    @ classmethod
    def Woke(cls): # 重写父类方法
        return False

    def __repr__(self):
        return f'{self.Woke()}'


result = Father.Woke() # 调用类属性时要使用()
print(result)

result = Son.Woke()
print(result)
