import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import os
def convolution(filter_size, filter_type):
    image_path = "ng.jpg"
    img = Image.open(image_path)
    img = img.convert("L")
    # img.show()
    img_array = np.array(img)
    img_L = img_array.shape[0] # 514
    img_W = img_array.shape[1] # 500
    
    # 垂直过滤器 9 * 9
    filter_num = 2
    n = 0
    # 初始化过滤器
    vertical_filter = np.zeros(filter_size**2).reshape(filter_size, filter_size)
    
    # 给过滤器赋值
    for v in range(vertical_filter.shape[1]):
        if v % filter_size % 1 == 0:
            n+=1
            vertical_filter[v,:] = filter_num - n
    if filter_type == "h":
        vertical_filter = vertical_filter.T
    elif filter_type == "v":
        vertical_filter = vertical_filter
    print(vertical_filter)
    
    # 手工过滤器
    # array = np.zeros(9).reshape(3,3)
    # array[0, 0] = 3
    # array[2,0] = 3
    # array[1, 0] =10
    # array[:, 1] = 0
    # array[0, 2] = -3
    # array[1, 2] = -10
    # array[2, 2] = -3
    # vertical_filter = array
    # print(vertical_filter)
    
    # 初始化卷积之后的image
    conv_L = img_L - vertical_filter.shape[0] + 1 
    conv_W = img_W - vertical_filter.shape[1] + 1
    init_image = np.zeros(conv_L * conv_W).reshape(conv_L, conv_W) 
    
    # pixcel_location
    pixel_location = []
    
    # 进行convolution    
    for L in range(conv_L):
        for W in range(conv_W):
            l = L + filter_size
            w = W + filter_size
            init_image[L,W] = np.sum(np.multiply(vertical_filter, img_array[L:l,W:w]))
            if init_image[L, W] != 0:
                pixel = [L, W]
                pixel_location.append(pixel)
    pixel_location = np.array(pixel_location)
    return init_image, pixel_location

def get_pixcel():
    conv_image_array , pixel_location_v = convolution(3, "v") # conv_image.shape == (512, 498)
    conv_image_array , pixel_location_h = convolution(3, "h") 
    # print(pixel_location.shape) # pixel_location.shape(220453, 2)
    image = Image.open("ng.jpg")
    image_array = np.array(image) # image_array (514, 500, 3)
    
    sample_pix = []
    f = 0
    if pixel_location_h.shape[0] > pixel_location_v.shape[0]:
        for v in range(pixel_location_v.shape[0]):
            for h in range(pixel_location_v.shape[0]):
                if pixel_location_h[v,0] == pixel_location_v[h,0] and pixel_location_h[v, 1] == pixel_location_v[h, 1]:
                    pix_x_y = pixel_location_h[h,:]
                    sample_pix.append(pix_x_y)
                    f +=1
                    print('{}个像素点相同'.format(f))
                    os.system("clear")
    elif pixel_location_h.shape[0] < pixel_location_v.shape[0]:
        for h in range(pixel_location_h.shape[0]):
            for v in range(pixel_location_h.shape[0]):
                if pixel_location_h[v,0] == pixel_location_v[h,0] and pixel_location_h[v, 1] == pixel_location_v[h, 1]:
                    pix_x_y = pixel_location_h[h,:]
                    sample_pix.append(pix_x_y)
                    f +=1
                    print('{}个像素点相同'.format(f))
                    os.system("clear")
    else:
        print('pixel_location_h == pixel_location_h') 
    
    sample_pix = np.array(sample_pix) 
    for pix in range(sample_pix.shape[0]):
        image_array[sample_pix[pix, 0], sample_pix[pix, 1], :] = [300, 0, 0]
    plt.imshow(image_array)
    plt.show()
    
    return conv_image_array
    
def main():
    image = get_pixcel()
    image = np.array(image)
    plt.imshow(image)
    plt.show()
    
if __name__ == "__main__":
    main()
    
