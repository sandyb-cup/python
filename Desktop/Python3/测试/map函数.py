import numpy as np
# map函数会根据提供的函数对指定的序列做映射
# 第一个参数function以参数序列中的每个元素调用function，返回包括每次function函数放回值的新列表
# map(function, iterable..) iterable可迭代的
# function函数
# iterable-- 一个或多个序列
def square(x):
    return x**2
square_num = list(map(square ,[1,2,3,4]))
print('-------------------分 割 线------------------------')
square_num = list(map(lambda x: x**2, [1,2,3,4]))# 使用lambda匿名函数
# 这里的map函数如果没用添加前面的list函数打印出来的会是一个路径不会打印出他的值
for i in square_num:
    print(i)
