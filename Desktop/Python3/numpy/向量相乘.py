import numpy as np
w = np.arange(5).reshape(1,5) # 从0到4 输出4个值维度是1，5
x = np.arange(10).reshape(5,2) # 从0dao10输出10个值维度是5，2
print(w)
print(x)
z = np.dot(w,x) # 
print(z.shape)
print(z)
