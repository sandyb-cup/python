# -*- conding: utf-8 -*-
# Author:ononok
# Time:2021/1/5
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1,11,1)
y = np.random.random(10)
y_tick = [0.2, 0.4, 0.6, 0.8, 1]
#给y轴的尺寸打上标注
plt.yticks([0.2, 0.4, 0.6, 0.8, 1],[f'LOW {y_tick[0]}',f'MIDLOW{y_tick[1]}',f'MID{y_tick[2]}',f'MIDHIGHT{y_tick[3]}',f'HIGHT{y_tick[4]}'])
plt.plot(x,y)
plt.show()
