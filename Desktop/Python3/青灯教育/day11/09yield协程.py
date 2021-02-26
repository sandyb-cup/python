# -*- conding: utf-8 -*-
# author:Andy
# time:2020/7/29
def genrot_func():
    num = 0
    while True:
       # yield 返回内容之后就会被挂起 等待下一次被激活(next(),send(None)
       yield f"genrot_func:{num}"
       num += 1
# 得到得是一个生成器
g = genrot_func()
print(g.send(None)) # 第一次激活要给None
print(g.send('第二次激活'))

