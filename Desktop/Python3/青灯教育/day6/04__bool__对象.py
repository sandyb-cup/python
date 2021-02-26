# -*- conding: utf-8 -*-
# Author:ononok
# Time:2020/12/9
class Son:
    def __init__(self, name , age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'<{self.name},{self.age}>'

    # def __bool__(self):
    #     return False

son = Son('张三', ' 15')

if bool(son):
    print('它是一个对象')
else:
    print('他不是一个对象')

'''
    这里只要对象不是一个空的''or None False bool放回的bool值都是True
    '''