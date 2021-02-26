# -*- conding: utf-8 -*-
# author:Andy
# time:2020/7/29
import time

# 默认的时间是十三位
# 16开头10或者是13位长度的 就是时间戳
print(time.time())
print("时间戳(10)",int(time.time()))
print("十六进制时间:",hex(int(time.time())))


# 结构化时间 UTC 格林威治时间
print(time.gmtime())

print('字符串时间','2020-10-06 20:14:50')


