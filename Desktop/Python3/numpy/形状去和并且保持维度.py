import numpy as np
arr = np.arange(1881).reshape(9, 209)
arr1 = np.arange(1881).reshape(9, 209)
arr_sum = np.sum(arr,axis=1,keepdims=True) # axis以列相加 形成每一行的总和 所以维度是(9, 1)
print(arr_sum)
print(arr_sum.shape)

arr_multiply = np.multiply(arr, arr1)
print(arr_multiply.shape)

