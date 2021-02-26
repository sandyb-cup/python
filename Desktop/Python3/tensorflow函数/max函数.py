import tensorflow as tf
from keras import backend as K
num_list = [0.1,0.6,0.6,0.7]
conver = tf.convert_to_tensor(num_list, name='conver', dtype='float32') # 将普通列表转换成tensor形式 解释一下参数含义:
                                                                                                    # 第一参数是要转换维度的对象 也就是操作目标
                                                                                                    # name: 这一步操作的名字是conver 
                                                                                                    # dtype: num_list 的类型是32位浮点型
sess = tf.Session() # 实例化session对象
init = tf.global_variables_initializer() # 初始化函数
sess.run(init) # 运行初始化函数
conver_output = sess.run(conver) # 运行转换对象
max_num = K.max(conver_output) # 输出tensor对象中的最大值

print(sess.run(max_num)) # 输出值 这里注意要sess.run()一下不然会打印出一个tensor的维度信息 而不是值