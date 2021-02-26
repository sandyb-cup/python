import numpy as np
np.random.seed(1)
shape1 = np.random.randn(2, 3)
print(shape1)

shape2 = shape1 == np.max(shape1) # shape2的维度跟shape1的维度一样 shape2中的只有最大值位置是True其他都是False

print(shape2)