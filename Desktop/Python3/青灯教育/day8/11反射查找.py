# -*- conding: utf-8 -*-
# author:Andy
# time:2020/7/29
a, b, c, d, e, f, g = [1,2,3,4,5,6,7]

names = [a, b, c, d, e, f, g]

# 用同过 a 变量拿到'a'

# d = {
#     'a':a,
#     'b':b,
#     'c':c,
#     'd':d,
# }
vk = {}
# 通过a变量拿到a
print(globals().copy().items())
for k, v in globals().copy().items():
    # v id(v), k 重新构建一个字典
    #print(k,v)
    # print(k, v)

    # print(k)
    # print(v)

    vk[id(v)] = k
data_dict = {}
for name in names:
    print(name)

    # print(id(name))
    # print(vk[id(name)])

    data_dict.update({vk[id(name)]:name})
print(data_dict)

