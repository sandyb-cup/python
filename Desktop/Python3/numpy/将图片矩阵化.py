import numpy as np
import matplotlib.pyplot as plt
import time
import skimage.transform as tf
image_path = '/Users/sandy/Desktop/Python3/人物头像动漫化/婧琪.jpg' # 图片的路径
image_arr = np.array(plt.imread(image_path)) # 将图片进行矩阵化处理 读取图片
print(image_arr.shape)

image_shape = tf.resize(image_arr, (64,64),mode='reflect').reshape((1,64*64*3)) # 重新定义图片得尺寸大小
print(image_shape.shape)

plt.imshow(image_arr) # 在新的窗口显示图片

plt.show() # 显示图片


