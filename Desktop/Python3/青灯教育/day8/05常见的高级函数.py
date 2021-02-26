# -*- conding: utf-8 -*-
# author:Andy
# time:2020/7/29
array1 = ['a','b','c','d']

array2 = [1,2,3,4,5]
array = []
for i in range(len(array1)):
    array.append([array1[i], array2[i]])

print(array)
print(dict(array))

# zip 合并列表 如果又一个列表短了 按照列表短的列表来计算
print(list(zip(array1,array2)))
print(dict(zip(array1,array2)))
