# -*- conding: utf-8 -*-
# author:Andy
# time:2020/7/29
def add(x,y): return x + y

# 匿名函数
# Lambda 定义函数一般是一次性的
lambda_add = lambda x, y:x + y


def func(x):
    print("x",x)
    return x[1]

array = [(3, 4),(10, 11),(7, 1)]

# 更改排序规则
# sorted 可以指定排序规则
# key 最要接收一个函数对象，sorted排序会讲内容一个一个传递给key 指定的函数对象
# 函数对象需要放回排序规则
print(sorted(array, key = func))

print(sorted(array, key=lambda x: x[0] + x[1], reverse=True))
#
