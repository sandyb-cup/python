# -*- conding: utf-8 -*-
# Author:ononok
# Time:2021/1/4
import serial
import matplotlib.pyplot as plt
from drawnow import *
import atexit
import time
values = []
plt.ion() #开启互交模式
serialArduino = serial.Serial('COM14', 9600) #监控端口 串口波率为9600

serialArduino.close()

print(serialArduino)



