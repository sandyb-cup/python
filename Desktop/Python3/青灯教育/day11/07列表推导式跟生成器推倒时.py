# -*- conding: utf-8 -*-
# author:Andy
# time:2020/7/29
# 列白推导式
arr = [f'http://www.baidu.com?{page}'for page in range(10)]

# 生成器推导式
tuple_ = (f'http://www.baidu.com?{page}'for page in range(10))

print(arr)
# 生成器对象可以用for 遍历ieyiel
print(tuple_)