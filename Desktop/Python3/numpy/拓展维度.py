import numpy as np
a = np.array([[[1,2,3],[4,5,6]]])
print(a.shape)
#np.expand_dims(a, axis=0)# 表示在0的位置添加数据，转换结果如下
b = np.expand_dims(a, axis=0)
print(b)
print(b.shape)
# 表示在1的位置添加一个维度
c = np.expand_dims(a, axis=1)
print(c)
print(c.shape)
# 在二的位置添加一个维度
d = np.expand_dims(a, axis=2)
print(d)
print(d.shape)

