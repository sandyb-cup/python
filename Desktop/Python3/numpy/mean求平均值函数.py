import numpy as np
arr = np.arange(10).reshape((5,2))
# np.mean(arr, dtype, keepdim, out, axis)
# 各参数解释 arr输入要求平均值的矩阵 dtype 数据格式， axis 默认不填不填就是对所有的值进行平均求值 如果axis为0的话对行压缩 对列求平均值 反之对行求平均值
arr_mean = np.mean(arr)
predic = 100 - (np.mean(np.abs(arr-5))*100)
print(predic)