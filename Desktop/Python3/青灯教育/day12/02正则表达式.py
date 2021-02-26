# -*- conding: utf-8 -*-
# author:Andy
# time:2020/7/29
'''
    python, java, c, c++
    算法，数据结构， 设计模式，编译原理，网络编程，并发编程， 正则表达式
    正则 在不规范的数据中编写规则提取数据

    正则表达式(一种技术)
    re 是python中的正则库
'''
import re

text = """
#第一种
dic1 = {1:'alex',2:['a','b'],3:('c','d')}
dic2 = dic1.copy()
dic1[1] = 'taibai'
print(dic1)             输出结果：{1: 'taibai', 2: ['a', 'b'], 3: ('c', 'd')}
print(dic2)             输出结果：{1: 'alex', 2: ['a', 'b'], 3: ('c', 'd')}

#第二种
dic1 = {1:'alex',2:['a','b'],3:('c','d'),4:{'name':'zhu','age':18}}
dic2 = dic1.copy()
dic1[4]['name'] = 'taibai'
print(dic1)            输出结果：{1: 'alex', 2: ['a', 'b'], 3: ('c', 'd'), 4: {'name': 'taibai', 'age': 18}}
print(dic2)            输出结果：{1: 'alex', 2: ['a', 'b'], 3: ('c', 'd'), 4: {'name': 'taibai', 'age': 18}}
"""
# re.findall("正则表达式的匹配规则"，'需要进行匹配的目标')

"""
    元字符是特殊的字符
        \d 匹配数字
        \D 非数字
        \s 匹配空白 即空格 tab键
        \S 匹配非空白
"""
result = re.findall('\d', text)
print('匹配数字:',result)
result = re.findall('\D', text)
print('匹配非数字',result)
result = re.findall('\s', text)
print('匹配空白:',result)
result = re.findall('\S', text)
print('匹配非空白:',result)