# -*- conding: utf-8 -*-
# author:Andy
# time:2020/7/29
score = [1,2,3,4,5]

# 把列表里面的数字变成字符串
score_copy = []
for i in score:
    score_copy.append(str(i))
print(score_copy)

# 一句话解决
# map返回的是一个生成器对象
# map(映射规则，可迭代对象) 映射
# 遍历可迭代对象 将内容一个一个传递给 映射规则

score_copy = map(str, score)
print(list(score_copy))


print(list(map(lambda x: str(x), score)))



