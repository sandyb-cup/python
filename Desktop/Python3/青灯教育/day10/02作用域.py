# -*- conding: utf-8 -*-
# author:Andy
# time:2020/7/29
num = 20

def foo():
    # 局部作用域
    # 局部作用域优先与全局作用域，单数不能修改全局定义域的值

    num  = 10
    print('foo',num)
    def printer():
        # printer是一个嵌套函数
        # 它是一个局部定义域中的局部定义域
        print('printer', num)
    # 只有在foo环境里面才能使用 printer
    # 把函数里面函数当成一个对象返回出去
    # 虽然返回的是一个函数对象实际上把整个函数都返回出去了
    return printer
pri = foo()
print(pri())
"""
     闭包：是一个封闭的环境
     全局环境不能操作在b闭包环境里面
     
"""
