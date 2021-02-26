# -*- conding: utf-8 -*-
# author:Andy
# time:2020/7/29
import os

# 分隔符号
# os 提供了所有的系统接口
file_path = 'test'
file_name = "剑来.test"

file_path = os.path.join(file_path, file_name )

print(file_path)

print(os.sep)

