import tensorflow as tf
import numpy as np
# 建立容器
w = tf.Variable(np.arange(6).reshape(2,3),dtype=tf.float32, name = "w")
b = tf.Variable(np.arange(6).reshape(2,3),dtype=tf.float32, name = "b")
#不需要初始化
save = tf.train.Saver()

with tf.Session() as sess:
#提取数据
    resault = save.restore(sess,"my_net/save_net.ckpt")
    print(resault)
    
    print("weights",sess.run(b))
    print("biases",sess.run(w))
    print(resault)
    
# 只提取代码时他的提取顺序以定义容器的顺序有关 这个循序是由储存时候的顺序是有关联的

    new_saver = tf.compat.v1.train.import_meta_graph("my_net/save_net.ckpt.meta")
    print(new_saver)
    saver_data = new_saver.restore(sess, "my_net/save_net.ckpt")
    print(saver_data)

# print(new_saver.restore("my_net/save_net"))
# 实现精确提取在后面加上名字
