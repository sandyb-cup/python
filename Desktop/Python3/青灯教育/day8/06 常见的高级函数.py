# -*- conding: utf-8 -*-
# author:Andy
# time:2020/7/29
array = [1, 2, 3, '1', '2', '3']

# 把字符串给过滤
arr = []

for i in array:
    if type(i) == str:
        pss

    else:
        arr.append(i)
print(arr)

# filter(过滤函数，可迭代对象）
# 如果过滤条件为True，就会返回内容
print(list(filter(lambda i: type(i) == str, array)))
# lambda后面跟随一个判断

