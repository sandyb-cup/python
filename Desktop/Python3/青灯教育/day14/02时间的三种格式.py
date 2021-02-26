# -*- conding: utf-8 -*-
# Author:ononok
# Time:2020/12/16
import time
time_float = time.time()
print(time_float)

time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())
print(time_str)

# 返回时间对象
print(time.gmtime())