import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def make_filter():
    filter = []
    for l in range(3):
        c = np.zeros(1).reshape(1, 1)
        filter.append(c)
    filter_array = np.array(filter)
    print(filter_array.shape)
    for L in range(filter_array.shape[1]):
        for W in range(filter_array.shape[1]):
            filter_array[1, L, W] = 3
    return filter_array

def conv_layer(f, step):
    filter_array = make_filter()
   
    image_path = "green.jpeg"
    image = Image.open(image_path)
    image_array = np.array(image) # (1200, 1200, 3)
   
    conv_L = int(image_array.shape[0] - filter_array.shape[1] + 1) # 1200
    conv_W = int(image_array.shape[1] - filter_array.shape[1] + 1) # 1200
   
    pix = conv_L * conv_W
    
    conv_last = np.zeros(pix * 3).reshape(conv_L, conv_W, 3)
    
    for L in range(conv_L - 1):
        for W in range(conv_W - 1):
            for c in range(3):
                
                l = L + f * step
                w = W + f * step
                conv_last[l, w, c] = np.multiply(image_array[L,W,c], filter_array[c,:,:])
    image_array[:,:, 1] = conv_last[:, :, 1]
    plt.imshow(image_array)
    plt.show()
   
def main():
    conv_layer(1, 1)     
if __name__ == "__main__":
    main()
    
