import numpy as np
rand = np.random.randint(1, 10000)
# randin函数他有两个参数分别是值的下限跟值的上限
rand_size = np.random.randint(3, size=2)
# 参数3是这个随机函数的取值范围 注意这里不包含0这个值
print(rand_size)
