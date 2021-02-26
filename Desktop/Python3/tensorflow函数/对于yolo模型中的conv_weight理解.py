import tensorflow as tf
from keras import backend as K

hight_arage = K.arange(0, 19)
num_arange = K.arange(0,19)

conv_hight_index = K.tile(hight_arage, [19])

conv_weight_index = K.tile(K.expand_dims(num_arange, 0),[19, 1]) # 将tensor拓展一维 再进行第一维进行19次复制 第二维进行1次复制
# conv_weight_index = K.transpose(conv_weight_index)
conv_weight_index = K.flatten(K.transpose(conv_weight_index)) # 对conv_weight_index 进行倒置再进行flatten shape(19, 19)

# conv_index = K.stack([conv_hight_index, conv_weight_index]) # shape(2, 361)
conv_index = K.transpose(K.stack([conv_hight_index, conv_weight_index])) # 将数据进行合并再进行倒置(361, 2)

conv_index = K.reshape(conv_index, [1, 19, 19, 1, 2])
sess = tf.Session()
print(sess.run(conv_index[0, 2, 6, 0, :]))

