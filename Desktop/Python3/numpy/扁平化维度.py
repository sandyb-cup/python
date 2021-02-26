import numpy as np
# 
arr = np.arange(12).reshape((2,2,3)) # 初始化·arr矩阵
print(arr)
print(arr[0])
print(arr.shape[0])
arr_reshape = arr.reshape(arr.shape[0],-1)
# 将arr的维度转换成arr第一维 后面两个维度进行扁平化 也就是缩合
print(arr_reshape)
print(arr_reshape)

