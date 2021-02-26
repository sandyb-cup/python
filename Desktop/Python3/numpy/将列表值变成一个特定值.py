import numpy as np
list_2 = [0 for x in range(100)]

list_3 = [3 for x in range(12)]

list_5 = [list_2, list_3]

list_4 = np.array(list_5)

print(list_4.flatter())

list_2.extend(list_3) # 将两个列表合并在一起
# 还有一种方式是: list_2 + list_3

# 还有一种方式是: list4 = [list_2, list_3]
# list4.flatter()

one_hot = np.eye(4)[list_2]
# one_hot2 = np.eye(4)[list_3]


print(one_hot)




