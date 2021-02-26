# -*- conding: utf-8 -*-
# Author:ononok
# Time:2021/1/18
import keyboard

print(0)
keyboard.wait('a')
#在按下a之前后面的语句都不会执行，下面同理
print(1)
keyboard.wait('b')
print(2)
keyboard.wait('c')
print(3)
keyboard.wait()

