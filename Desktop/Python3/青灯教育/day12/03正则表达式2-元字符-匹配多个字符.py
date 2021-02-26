# -*- conding: utf-8 -*-
# author:Andy
# time:2020/7/29
import re
text = """
123453422@qq.com
122121323@qq.com
43435434@qq.com


"""
# + 与前面一个字符结合， 变成能够 匹配一个 或者多个
# . 匹配一个字符
result = re.findall('\d+', text)
print(result)

# . 匹配任意一个字符(\n除外） + 匹配一个或者是多个字符
# *可以匹配零个或者多个 \n
print(re.findall('\d*', text))

