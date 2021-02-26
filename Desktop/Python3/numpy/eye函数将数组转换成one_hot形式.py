import numpy as np

list1 = np.array([[0],[1],[1],[3]])
print(list1.shape)
one_hot = np.eye(4)[list1] # eye使用格式前面一个参数是one_hot的种类总和 后面是要转换的具体数字
print(one_hot)
print(one_hot.shape)
