# -*- conding: utf-8 -*-
# author:Andy
# time:2020/7/29
import os

# 如果目录存在就不创建
dir_name = 'test'

if os.path.exists(dir_name):
    os.mkdicr('text')
else:
    print('该文件已经存在')


# 删除工作路径
# os.rmdir(dir_name)

# 切换工作目录
os.chdir('/Users/')
print(os.getcwd())

# 打印当前文件夹下面的所用文件名
print(os.listdir('.'))

