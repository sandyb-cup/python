import matplotlib.pyplot as plt
import numpy as np
import scipy 
from scipy import misc
from PIL import Image
fname = "/Users/sandy/Desktop/Python3/test_location.jpeg"
print(scipy.__version__)
image = np.array(plt.imread(fname)) # 
print(image)

image_tenspose_array = scipy.misc.imresize(image, size = (1,1, 3))
plt.imshow(image_tenspose_array)
plt.show()
