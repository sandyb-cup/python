# -*- conding: utf-8 -*-
# Author:ononok
# Time:2021/1/5
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,11,1)
y = np.random.random(10)
'''
    plot控制条件
    color：曲线颜色，blue，green，red等等
label：图例，这个参数内容就自定义啦，注意如果写这个参数一定要加上plt.legend()，之后再plt.show()才有有用！
linestyle：曲线风格， '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'
linewidth：曲线宽度，自定义就可以
marker：标记点样式，’o’,’x’，也就是说这些符号会标示出曲线上具体的“点”，这样一来就易于观察曲线上那些地方是支撑点
markersize：标记点的大小，自定义就可以
'''
plt.plot(x, y, color='green',label='tum',linestyle = '-',linewidth='1',marker="o") #set_cmap里面有多种颜色可以设置
'''
BrBG      brown, white, blue-green
      PiYG      pink, white, yellow-green
      PRGn      purple, white, green
      PuOr      orange, white, purple
      RdBu      red, white, blue
      RdGy      red, white, gray
      RdYlBu    red, yellow, blue
      RdYlGn    red, yellow, green
      Spectral  red, orange, yellow, green, blue
'''
plt.legend()
plt.show()
