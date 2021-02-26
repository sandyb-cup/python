# -*- conding: utf-8 -*-
# author:Andy
# time:2020/7/29
'''
案例.
    1，将'1997-10-10' 格式化成struct_time 时间
    2，将struct_time 时间变成字符串时间
    3，将struct_time 时间变成时间戳
    4，将时间戳 变成struct_time 时间
'''
import time

now_time = '1997-10-10'

print(time.strptime(now_time, '%Y-%m-%d'))
print(time.strftime('%Y-%m-%d %I %p', time.strptime(now_time, '%Y-%m-%d')))
print(time.mktime(time.strptime(now_time,'%Y-%m-%d')))
print(time.gmtime(time.time()))

