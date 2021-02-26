import matplotlib.pyplot as plt
import scipy
import numpy as np
fname = "/Users/sandy/Desktop/Python3/人物头像动漫化/小姐姐.jpg"
image = np.array(plt.imread(fname))
image_tenspose_array = np.asarray(image) # 将image转换成array
image_tenspose_array.flags.writeable = True

print(image_tenspose_array)
plt.imshow(image_tenspose_array)
plt.show()

# IMage.fomarray(np.uint8(img)) array转换成image
