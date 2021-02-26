import numpy as np
gradient = np.array([-3,-3,1,2,3])
gradients = np.array([1,2,3])

clip_num = np.clip(gradient, -2, 8, out = gradient  )
# 这个裁剪函数会讲上面的gradient进行裁剪 -2，8 是裁剪的范围 如果小于这个范围他会取最小的那个值 反之取最大的为输出
# out参数会把裁剪后的数据储存在里面 注意原函数有多少个值他输出就是多少个值
print(gradient)