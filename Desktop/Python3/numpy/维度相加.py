import numpy as np
arr1 = np.arange(20).reshape(10, 2)
print(arr1)
arr2 = np.arange(10).reshape(10, 1)


print(np.sum(arr1, axis=0, keepdims=True))
# np.sum(arr1, axis = 0, keepdims = True)
# axis ： 以行还是列作为轴 如果是0 就是以行作为轴对每一列进行相加 反之就是以行为轴对每行进行相加操作
# leepdims : 布尔值 用来指定输出的值是否保留他的维度



