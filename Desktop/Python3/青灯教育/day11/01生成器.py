# -*- conding: utf-8 -*-
# author:Andy
# time:2020/7/29
"""
     python 三大神器 迭代器 生成器 装饰器

     高级函数，range 返回的都是生成器
"""

# 满足重复运行
# while True:
#     print('hello world')

# 迭代
arr = [1,2,3,4,5,6]
# for i in arr:
#     print(i)

# 递归
def func(arr):
    if arr:
        print(arr) # pop是一个列表函数 移除列表中的某一个值
        func(arr)
func(arr)
