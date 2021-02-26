import numpy as np
x = np.array([[1, 2], [3, 4]])
a = x.ravel()
a[1]=100
print(a)
print(x)