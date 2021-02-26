import numpy as np
arr_num = [1,2,3,4]
arr_num2 = [5,6,7,8]
arr = np.array((arr_num,arr_num2))
# 将列表变成一个矩阵模型
print(arr)
print(arr.shape) # 打印出矩阵维度信息
print(arr[:,0].shape) # 打印出0维长度
