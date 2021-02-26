import numpy as np
activate = [1,2,3,4,5,6]
number_of_activate = np.random.randint(0,5) # 输出一个随机数 
# 这个random.randint函数随机输出一个值 后面的参数是一个随机取值的范围

print(number_of_activate)
random_indices = np.random.randint(len(activate),size = number_of_activate)
# random.randint函数中的size参数是输出值的大小也就是输出几个值 有这个函数来决定
random_activates = [activate[i] for i in random_indices] # 遍历随机出来的值进行输出 这里是对random_indices进行遍历
print(random_activates)

