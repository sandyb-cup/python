# -*- conding: utf-8 -*-
# author:Andy
# time:2020/7/29
file = open('hello.text','r',encoding='utf-8')
print(file)
# next往后迭代一个元素
print(next(file))
print(next(file))
print(next(file))

# for i in file:
#     print(i)

# iter将一个对象变成一个可迭代对象(可以用next进行迭代)
arr = [1,2,3,4,5]
arr = iter(arr)
print(next(arr))

