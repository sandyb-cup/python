import tensorflow as tf

a = tf.constant([[1, 2], [3, 4], [5, 6]], dtype= tf.int32)

a1 = tf.tile(a, [2]) # 含义将a的第一维数据跟第二维数据进行复制

sess = tf.Session()

print(sess.run(a1))

