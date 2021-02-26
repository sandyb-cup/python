import tensorflow as tf
from keras import backend as K
# 用argmax函数能获取最大概率值的索引 
list_num = [0.1,0.2,0.6,0.2]
list_conver_tensor = tf.convert_to_tensor(list_num, name='b',dtype='float32')# 将列表转换成tensor形式 参数解释一下 list_num是要转换的目标对象 
                                                                                                                # nume 对这一步操作命名 这里的名字为b
                                                                                                                # dtype 目标的格式这里是32浮点型 
# 初始化全局变量
init = tf.global_variables_initializer() # 函数初始化 相当于启动钥匙 必须要做的一步
session = tf.Session() # 实例化session对象
session.run(init) # 运行函数初始化
tensor_output = session.run(list_conver_tensor) # 运行转换函数
# print(tensor_output)
argmax_num = K.argmax(tensor_output) # argmex函数会选出最大值的索引
# print(session.run(argmax_num)) # 这里要打印其值需要调用session实例 要不然打印出来的是一个tensor的维度信息要 session.run()一下

