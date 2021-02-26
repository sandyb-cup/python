import numpy as np
d1 = np.arange(4).reshape(4, 1)
d2 = np.arange(5, 7).reshape(2, 1)
print(d1)

for i in range(d2.shape[0]):
    d1[i, :] = d2[i, :]
    
print(d1)