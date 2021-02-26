import numpy as np
np.random.seed(1)
permutation = np.random.permutation(3)
# permutation 排列 置换
list1 = [1,2,3,4,5,6,7,8]

arr1 = np.array(list1).reshape(2,4)

random_num = arr1.shape[1]

random_suffer = np.random.permutation(random_num) # 将样本数据进行随机打乱

shuffle_list1 = arr1[:, random_suffer]

# print(random_suffer)

# print(shuffle_list1)

arr_random = np.random.randn(2, 3)
print(arr_random)
random_num = arr_random.shape[1]

random_index = np.random.permutation(random_num)

random_arr = arr_random[:, random_index]
print(random_arr)


