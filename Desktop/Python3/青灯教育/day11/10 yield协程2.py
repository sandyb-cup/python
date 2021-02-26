# -*- conding: utf-8 -*-
# author:Andy
# time:2020/7/29
"""
    进程之间的切换
    线程之间的切换 (计算机最基本单位)
    协程之间的切换 (在一个线程之间进行切换)
    函数与函数之间的切换
"""
import time
from asyncio import sleep
import asyncio
def genrot_func1():
    num = 0
    while True:
        # yield 返回内容之后就会被挂起 等待下一次被激活(next(),send(None)
        # time.sleep(1)
        asyncio.sleep(1)
        argr = yield f"genrot_func1:{num}"
        print(f'genrot_func1{argr}')
        num += 1

def genrot_func2():
    num = 0
    while True:
        # yield 返回内容之后就会被挂起 等待下一次被激活(next(),send(None)
        # time.sleep(1)
        asyncio.sleep(1)
        argr = yield f"genrot_func2:{num}"
        print(f'genrot_func2:{argr}')
        num += 1

# 得到得是一个生成器
g1 = genrot_func1()
g2 = genrot_func2()
# print(g.send(None)) # 第一次激活要给None
# print(g.send('第二次激活'))

while True:
    print(g1.send(None))
    print(g2.send(None))
    """
        函数之间的切换，协程
        
        你操作的是一个生成器对象，操作生成器对象才能得到结果
    """
