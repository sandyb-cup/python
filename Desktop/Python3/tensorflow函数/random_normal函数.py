import tensorflow as tf
random_num1 = tf.random_normal([2,3], mean=1 ,seed=1, stddev=1) # tf.random_normal 从正太分布中随机输出随机值 参数解释；
                                                                                                            # shape： 一个一维张量或者是phthon的数组，代表输出张量的维度
                                                                                                            # mean：数据类型为dtype的张量或者是python值，是正态分布的均值
                                                                                                            # 也就是均值让数据在那个值之间浮动
                                                                                                            # stddev： 数据类型为dtype的张量或者是python的值，是正态分布的标准差
                                                                                                            # 标准差就是均方差 他可以反应出一组数据的平稳度
                                                                                                            # seed: 一个python整数。是随机种子
                                                                                                            # name: 操作名称(可以选填)
init = tf.global_variables_initializer() # 实例化函数值初始化函数 是session的开关 启动session之前都要执行的一步
sess = tf.Session() # 创建session会话
sess.run(init) # 运行函数初始化 函数

random_num = sess.run(random_num1) # 运行前面的正态分布函数

print(random_num) # 打印正态分布出来的随机值