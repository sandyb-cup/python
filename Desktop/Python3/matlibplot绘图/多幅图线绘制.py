# -*- conding: utf-8 -*-
# Author:ononok
# Time:2021/1/5
import matplotlib.pyplot as plt
# plt.subplot(221)

# equivalent but more general == plt.sutplot(221)
ax1 = plt.subplot(2,2,1)

# add a subplot with no frame
ax2 = plt.subplot(222, frameon=False) # framemon控制处理x y轴的边缘其他边线是否显示

# add a polar subplot
plt.subplot(223, projection='polar')

# add a red subplot that shares the x-axis with ax1
plt.subplot(224, sharex=ax1, facecolor='red')

# delete ax2 from the figure
plt.delaxes(ax2) #在图像中删除222图像

# add ax2 to the figure again
plt.subplot(ax2) #在图像再次显示222图像
plt.show()
