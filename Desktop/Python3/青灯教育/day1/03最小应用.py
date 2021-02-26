# -*- conding: utf-8 -*-
# author:Andy
# time:2020/7/29
import tkinter as tk
# 创建的窗口对象 对象会有自己的属性
root = tk.Tk()
root.title('第一个窗口对象')
# root.title标题属性
# eidth x height 位置的x + 位置y
root.geometry('300x300+100+100')

root.title('第一个窗口对象')

# 图标属性
root.iconbitmap('/Users/sandy/Desktop/Python3/images/bomb.png')

# 相当于死循环一直显显示窗口对象
root.mainloop()

# 第一看原码 第二看官方文档 第三百度
