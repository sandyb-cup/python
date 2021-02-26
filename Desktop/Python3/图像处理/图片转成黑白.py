from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
img = Image.open("woman_face.jpeg")
img = img.convert("L")
print(np.array(img).shape)
print(np.array(img))

img.show()