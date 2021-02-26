import tensorflow as tf
import numpy as np
import os



list1 = [[0.1,0.3,0.5,0.1],[0.1,0.2,0.3,0.4]]
list2 = [[0.1,2,0.5,0.1],[0.2,1,1,0.3]]

num1 = np.array(list1)
num2 = np.array(list2)


sess = tf.Session()
os.system('clear')
print(num1.shape)

# print(num1)
print(num2)
# print(sess.run(tf.argmax(num1))) # 他这个是可以转换阶级来进行取最大值的索引 0表示一维数据进行索引 1表示对二维中的数据进行索引
print(sess.run(tf.argmax(num2)))




sess = tf.Session()

max1_index = tf.argmax(num1)
max2_index = tf.argmax(num2)

equal = tf.equal(max1_index,max2_index) # 相等的就为True它是一个bool值
equal_resault = sess.run(equal)
print(equal_resault)

cast = tf.reduce_mean(tf.cast(equal_resault, 'float')) # cost将数的形式进行转换 这里是将bool值转换成float类型
cast_resault = sess.run(cast)
print(cast_resault)


