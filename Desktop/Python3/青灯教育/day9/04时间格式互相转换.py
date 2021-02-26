# -*- conding: utf-8 -*-
# author:Andy
# time:2020/7/29
import time
location_time = time.localtime()
print(location_time)

# 时间的数字
# strftime f format 之后进行输入
print(time.strftime("%Y-%m-%d %H-%M-%S ", location_time))

# 时间戳转换成结构化时间
print("时间戳转换成结构化时间",time.localtime(1601987375-10000))

# 结构化时间转换成时间戳
print('结构化时间转时间戳',time.mktime(location_time))
