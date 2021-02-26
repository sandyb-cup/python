import tensorflow as tf
import numpy as np

w = tf.Variable([[11,12,13],[22,23,25]],dtype=tf.float32, name = "w")
b = tf.Variable([[7,8,9],[1,2,3]],dtype=tf.float32, name = "b")
init = tf.global_variables_initializer()

save = tf.train.Saver()

with tf.Session() as sess:
    sess.run(init)
    
    # print("保存路径：",save_path)
    print(sess.run(w))
    print(sess.run(b))
    save_path = save.save(sess,"my_net/save_net.ckpt")