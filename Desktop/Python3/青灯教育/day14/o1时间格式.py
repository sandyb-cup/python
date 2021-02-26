# -*- conding: utf-8 -*-
# Author:ononok
# Time:2020/12/16
# 将时间戳对象转换成人能读懂的格式
import time

# 获取当前时间戳
now_time = time.time()
print(now_time)

# 结构化时间
print(time.localtime())

# 将时间戳以结构化时间的形式进行输出
str_time = time.gmtime(int(time.time()))
# 这个功能与localtime函数的功能是一样的

print(str_time)

# 将结构化时间转换成字符串形式的格式输出
str_time = time.strftime('%Y-%m-%d', time.gmtime(int(time.time())))
print(str_time)
# 输出的时间会随着 时间输出的占位符的改变从而改变

str_time_hms = time.strftime('%H:%M:%S', time.gmtime())

# 打印时分秒时间
print(str_time_hms)

print(time.strftime('%Y-%m-%d %H:%M:%S %p', time.localtime()))
# 中间的符号是可以随意改变的


# 将字符串转换成结构化时间
time_float = time.strptime('2020-12-15 20:47:21 PM','%Y-%m-%d %H:%M:%S %p')
# 前面的参数要和后面参数一一相对应
print(time_float)