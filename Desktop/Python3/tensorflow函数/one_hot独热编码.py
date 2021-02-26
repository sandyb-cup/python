import tensorflow as tf
import numpy as np
type_num = tf.constant(6, name = "type_num")
y_lables = np.array([1, 2, 3, 4, 1])
one_hot = tf.one_hot(y_lables, type_num, axis = 0) # lables在行中表示 列表示的是one_hot的类型
sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)
print(sess.run(one_hot))



