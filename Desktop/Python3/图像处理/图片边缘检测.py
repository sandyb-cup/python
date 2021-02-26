import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import random 
random.seed(1)
image_path = "woman_face.jpeg"
img = Image.open(image_path) # 读取图片
img_convert = img.convert("L") # 讲图片转换成黑白形式

image_array1 = np.array(img) # 将image array化
print(image_array1.shape)
image_array2 = np.array(img_convert)

conv_filter = np.ones(81).reshape(9, 9)
random_list = [i for i in range(9)]
print(random_list)
random_num_x = np.random.randint(len(random_list), size = len(random_list))
random_num_y = np.random.randint(len(random_list), size = len(random_list))
for x in random_num_x:
    conv_filter[x,x] = -1
    
for L in range(conv_filter.shape[1]):
    for W in range(conv_filter.shape[1]):
