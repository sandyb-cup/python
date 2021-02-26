from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
image = Image.open("woman_face.jpeg")
image_array = np.array(image)
for p in range(100):
    image_array[p,p,:] = [200, 0, 0]
    image_array[p+1, p+2] = [200, 0, 0]
    
plt.imshow(image_array)
plt.show()

 