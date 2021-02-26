# -*- conding: utf-8 -*-
# author:Andy
# time:2020/7/29
import os

print(__name__)
print(__file__)

"""
    路径操作
        # 获取当前项目运行的路径
"""

print(os.path.abspath('.')) # .代表当前的文件夹
print(os.path.abspath('..')) # .. 代表上一层路径

# 获取当前文件的绝对路径
print(os.path.basename(__file__))
print(os.path.dirname(__file__))

# 文件拓展
print(os.path.splitext(__file__))
print(os.path.split(__file__))

"""
判断文件路径
"""
print(os.path.isdir('root'))

print(os.path.isfile(''))

# 判断=目录是否存在

print(os.path.exists())





