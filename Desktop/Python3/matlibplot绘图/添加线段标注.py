# -*- conding: utf-8 -*-
# Author:ononok
# Time:2021/1/5
import matplotlib.pyplot as plt
import numpy as np


y = np.random.random(10)
x = np.arange(1, 11,1)
plt.title('test') # 添加标题
plt.xlabel('month') #添加x轴标签
plt.ylabel('water') #添加y轴标签
#x轴标签旋转plt.gca().set_xticklabels(df['manufacturer'], rotation=60, horizontalalignment= 'right')
plt.plot(x, y, color=plt.set_cmap('BrBG'),label='train_accruracy')
y1 = np.random.random(10)
plt.plot(x, y1,color='red',label = 'test_accruracy')
# 添加线段标注
plt.legend()
plt.show()