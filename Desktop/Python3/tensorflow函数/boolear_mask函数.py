import tensorflow as tf
from keras import backend as K
num_list = [0.1,0.3,0.6,0.7,0.8,0.3]
conver = tf.convert_to_tensor(num_list, name='conver', dtype='float32') # 用tf.convert_to_tensor 把list转换成tensor对象
sess = tf.Session() # 创建sess实例化对象
init = tf.global_variables_initializer() # 初始化全局对象函数治理可以理解成是sess执行操作的钥匙
sess.run(init) # 运行初始化对象
thershold = 0.5 # 设置阈值
conver_output = sess.run(conver) # 运行转换函数
bool_num = K.greater_equal(conver_output, thershold) # 将list转换成的tensor对象bool化
print(sess.run(bool_num))
last_out = tf.boolean_mask(num_list, bool_num) # 将原来的tensor对象进行bool值过滤
print(sess.run(last_out)) # 输出过滤后的函数

