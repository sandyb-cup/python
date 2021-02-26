# -*- conding: utf-8 -*-
# Author:ononok
# Time:2021/1/5
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(2011,2015,1)

y = np.random.random(4)
# plt.plot(x, y)  #折线图
# plt.show()
#
# plt.scatter(x, y)
# plt.show()

value = np.arange(1, 9, 1)
values = np.random.random(8)
print(values)
#直方图绘制函数，bins为直方图间隔份数
plt.hist(value,values, bins=12)
plt.show()




