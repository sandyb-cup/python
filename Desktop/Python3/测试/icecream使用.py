# -*- conding: utf-8 -*-
# Author:ononok
# Time:2021/2/18
from icecream import ic
def Hello(para):
    if para:
        print("你好世界")
    return para+'wold'
ic(Hello('Hello'))
ic(Hello('hello'))
