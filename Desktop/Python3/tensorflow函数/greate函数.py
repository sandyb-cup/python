import tensorflow as tf
from keras import backend as K
# 介绍一下greate_equal函数它是一个 输入是目标函数跟一个阈值函数 输出是一个bool值函数 大于阈值的值会输出True 反之输出false
num_list = [0.4,0.5,0.8,0.9,0.1,0.3,0.6]
threshould = 0.5
conver = tf.convert_to_tensor(num_list, name = 'conver', dtype='float32') # 用tf.conver_to_tensor函数将列表转换成tensorf对象
sess = tf.Session() # 实例化Session对象
init = tf.global_variables_initializer() # 初始化函数这里是session的启动钥匙
sess.run(init) # 运行init函数让前面定义的有意义
conver_output = sess.run(conver) # 运行转换函数
bool_num = K.greater_equal(conver_output,threshould) # 实现greater_equal 函数输出是一个bool值
print(sess.run(bool_num))
