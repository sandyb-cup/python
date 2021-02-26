import tensorflow as tf
import os
tf.add_to_collection('losses', tf.constant(2.2)) # 创建一个列表 
tf.add_to_collection('losses', tf.constant(3.))
with tf.Session() as sess:
    os.system('clear')
    print(sess.run(tf.get_collection('losses'))) # 获取列表
    print(sess.run(tf.add_n(tf.get_collection('losses')))) # 将列表的值进行相加
                   