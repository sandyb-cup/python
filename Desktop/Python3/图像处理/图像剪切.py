from PIL import Image
import os
import matplotlib.pyplot as plt
import numpy as np
image = Image.open("woman_face.jpeg")
image_array = np.array(image)
plt.imshow(image_array)
plt.show()
box = (32, 67, 120, 167) # 剪切图片范围
ng = image.crop(box) # 剪切图片
plt.imshow(np.array(ng)) 
plt.show()

ng.save("ng.jpg")
