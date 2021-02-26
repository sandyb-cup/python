# -*- conding: utf-8 -*-
# author:Andy
# time:2020/7/29
def genrot_func():
    names = '张三, 李四, 王五, 赵六'

    for i in names.split(','):
        # return i
        # yield 不是返回一次而是多次
        yield i
    # 还可以放回不同的内容
    yield '张鑫'

# 得到得是一个生成器
name = genrot_func()
for i in name:
    print(i)

