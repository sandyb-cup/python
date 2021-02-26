import tensorflow as tf
from keras import backend as K
num_arange = K.arange(0, 19)
num2_arange = K.arange(0, 19)

num_tile = K.tile(num_arange, [19]) # (1, 361)

num2_tile = K.tile(K.expand_dims(num2_arange, 0),[19, 1])
num2_tile = K.flatten(K.transpose(num2_tile)) 

num3 = K.transpose(K.stack([num_tile, num2_tile]))

conv_dim = K.reshape(num3, [1, 19, 19, 1, 2])
sess = tf.Session()
result = sess.run(conv_dim)
print(result[..., 0])
 