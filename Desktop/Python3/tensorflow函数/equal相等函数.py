import tensorflow as tf
import numpy as np

num = [1,2,3,5]
num2 = [1,2,3,5]

arr1 = np.array(num)
arr2 = np.array(num2)

equal = tf.equal(num, num2) # equal判断两个值是否相等

with tf.Session() as sess:
    resault = sess.run(equal)
    print(resault)
    
    


