import numpy as np
num_array = np.array(([[1,2,3],[4,5,6]])) # 两个不想等的维度如果进行ravel会出现两个list值 
array_ravel = np.ravel(num_array) # 进行ravel分解

print("num_array.shape",num_array.shape)

# 这里其实也可以用另外一种写法就是 
array_ravel = num_array.ravel()
print(array_ravel)
array_ravel[1]=100
print(num_array)
# revel解开函数是将一个二维或者是多维的矩阵进行降维的一个函数(可以这么理解)
# 比如所上面的num_array它是一个(2,3)矩阵的函数进行ravel解开之后他会变成一个(6,)的一维矩阵
print(array_ravel.shape)
array_flatten = num_array.flatten('F')
# 这里的F表示列序优先 无论是rarel还是flatten都是这样
print(num_array)
print(array_flatten)

x = 1
n = 2
list3 = []
for i in range(1):
    list1 = [x for i in range(10)]
    list2 = [n for i in range(10)]
list3.append(list1)
list3.append(list2)
print(list3)
print(np.array(list3))
print(np.ravel(np.array(list3)))