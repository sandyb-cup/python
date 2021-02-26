import tensorflow as tf
from keras import backend as K 

x = tf.placeholder(dtype = tf.int32, name = "x")
num_exp = K.exp(x) # exp指数函数 

sess = tf.Session()
print(sess.run(num_exp), feed_dict = {x: 4})