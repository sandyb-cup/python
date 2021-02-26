import numpy as np
np.random.seed(1)
random_num = np.random.randn(1,3,3,1)
print(random_num)

pad = 2
pad_num = np.pad(random_num,((0,0), (pad, pad), (pad, pad), (0, 0)), "constant", constant_values = 0)

print(pad_num)
print('pad_num.shape',pad_num.shape) # shape(1, 7, 7, 1)
print('pad_num[0, 3]',pad_num[0,1,1]) 

