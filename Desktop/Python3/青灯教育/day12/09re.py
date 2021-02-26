# -*- conding: utf-8 -*-
# author:Andy
# time:2020/7/29
import re
# 首匹配
result1 = re.match('\d+','2913329720@qq.com')
print(result1.group())


# 与上面一样
result2 = re.findall('\d+',' 2913329720@qq.com')
print(result2)
# search 扫描整个字符串 匹配到第一个内容
result3 = re.search('\d+',' 2913329720@qq.com2323323232')
print(result3.group())

# findall 他会全部遍历一遍
result4 = re.findall('\d+',' 2913329720@qq.com2323323232')
print(result4)
