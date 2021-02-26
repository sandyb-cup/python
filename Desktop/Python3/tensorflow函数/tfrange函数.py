import tensorflow as tf
from keras import backend as K
num_arange = K.arange(0, 19)

num_arange_tile = K.tile(num_arange, [19])


sess = tf.Session()
print(sess.run(num_arange_tile))
