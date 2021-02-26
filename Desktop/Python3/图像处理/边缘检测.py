import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
vertical_filter = np.zeros(9).reshape(3, 3)

v_reduce_num = 2
for v in range(vertical_filter.shape[0]):
    vertical_filter[:][v] = v_reduce_num - v_reduce_num/2 * (v + 1)
real_vertical_filter = vertical_filter
print("filter",real_vertical_filter)

conv_layer = np.zeros(36).reshape(6, 6)
for c in range(int(conv_layer.shape[1]/2)):
    conv_layer[:][c] = 10
real_conv_layer = conv_layer
print("conv_layer",real_conv_layer)

# 遍历conv_layer的长和宽
s = 1
p = 1

# 初始化卷积之后的filter array
conv_late_array = np.zeros(16).reshape(4, 4)

# 用垂直边缘检测
for L in range(real_conv_layer.shape[0] - vertical_filter.shape[1] + 1):
    for W in range(real_conv_layer.shape[1] - vertical_filter.shape[1] + 1):
        l = L + 3
        w = W + 3
        conv_late_array[W,L]= np.sum(np.multiply(real_vertical_filter, real_conv_layer[W:w,L:l]))
        if conv_late_array[W,L] != 0 :
            print("pixcel_location,X {},Y {}".format(W, L))
        
        
print(conv_late_array)

# plt.imshow(conv_late_array[:,:])
# plt.show()


        

