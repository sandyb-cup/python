# -*- conding: utf-8 -*-
# Author:ononok
# Time:2020/12/9
class Father:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def P_P(self):
        print(f'{self.name} age:{self.age}')

class Son(Father):
    def __new__(cls, *args, **kwargs):
        modify = Father.__new__(cls)
        modify.name = '儿子'
        modify.age = '18'

        return modify

    def __init__(self):
        print(self.name)
        print(self.age)

father = Father(name = '爸爸', age = '58')

Son()



