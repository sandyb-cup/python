import numpy as np
import random
Ty = 1375
throght_list = []
sum_random=0
sum_output=0
for ran in range(Ty):
    num_list = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
    ran_num = random.choice(num_list)# 从上面的小数当中随机选取一个值
    if ran_num>=0.5: # 如果选取的值大于0.5
        sum_random+=1 # sum_random自加1
    throght_list.append(ran_num)# 将选取的值加入到throght_list字典当中
throght = 0.5
concecutive_timestep=0
activete_muisc = "叮叮" # 插入语句
print('sum_num==',sum_random) # 打印出有多少值是大于0.5的
for i in range(Ty): # 进行循环循环次数是1375
    concecutive_timestep +=1 # concecutive_timestep自加一
    if throght_list[i]>=0.5 and concecutive_timestep>=75: # 如果列表中的值大与0.5并且concecutive_step大于75时执行下面语句

        sum_output+=1# 作用看for循环下面有多少个值是满足条件的
        print('ok~ output%S',(activete_muisc))
        print("now i num:",i)# 查看for循环下面执行这一步的值是多少
        concecutive_timestep = 0# 初始化concecutive_timestep
print('sum_outou=',sum_output)# 输出有多少个小数是满足条件的 进行输出