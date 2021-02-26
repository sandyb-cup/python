import tensorflow as tf
from keras import backend as K

conv_dim = K.arange(0, 361)
conv_dim = K.reshape(conv_dim, [1, 19, 19, 1, 1])
conv_dim = K.shape(conv_dim)[1:3]
conv_dim = K.reshape(conv_dim, [1, 1, 1, 1, 2])

sess = tf.Session()
print(sess.run(conv_dim))