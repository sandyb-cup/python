# -*- conding: utf-8 -*-
# author:Andy
# time:2020/7/29
import time

location_time = time.localtime()
print(location_time)

# 时间的数字
# strftime f format 之后进行输入
print(time.strftime("%Y-%m-%d %H-%M-%S ", location_time))

'''
    注释里面是每一个方法的使用
    官方文档利用注释;自己写的一些说明构建
'''
