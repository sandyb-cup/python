import numpy as np
arr1 = np.array([[1, 2, 3]])
arr2 = np.array([[4, 5, 6]])
arr3 = np.concatenate((arr1, arr2), axis=0) # 还用一种拼接的方式是np.append()
print(arr3)