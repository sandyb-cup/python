# -*- conding: utf-8 -*-
# author:Andy
# time:2020/7/29
import time

location_time = time.gmtime()

print("结构化时间",location_time)

print("年",location_time.tm_year)
print("月",location_time.tm_mon)
print("日",location_time.tm_mday)
print('时',location_time.tm_hour)
print("分",location_time.tm_min)
print("秒",location_time.tm_sec)

