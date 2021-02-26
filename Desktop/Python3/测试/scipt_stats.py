# -*- conding: utf-8 -*-
# Author:ononok
# Time:2020/12/27
from scipy.stats import norm

print(norm(0,1).ppf(0.5))   # 知道 p = F(x) 反求 x
print(norm(0,1).pdf(0))     # 知道 x 求 f(x)
print(norm(0,1).cdf(0))     # 知道x 求p = F(x)
'''
输出
0.0
0.3989422804014327
0.5
'''