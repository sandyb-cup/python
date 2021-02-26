import numpy as np
arr = np.arange(10).reshape(1, 10)
print(arr)
arr1 = np.copy(arr)
print(arr1)
lists = [[1,2,3,4,5,6],[1,2,3,4,5,6]]
num = lists[:]
print(num)