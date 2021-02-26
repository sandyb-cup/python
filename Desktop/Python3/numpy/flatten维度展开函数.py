import numpy as np
x = np.array([[1, 2], [3, 4]])
a = x.flatten() # 将维度展开 又点像降维
a[1] = 100
print(a)
print(x)
