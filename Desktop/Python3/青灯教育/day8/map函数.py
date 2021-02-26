# -*- conding: utf-8 -*-
# Author:ononok
# Time:2021/1/18
list1=[1,2,3,4,5]
def square(x):
    return x**2
c = list(map(square,list1))
b = list(map(str,list1))
print(c)
print(b)
