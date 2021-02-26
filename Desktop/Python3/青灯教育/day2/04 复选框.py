# -*- conding: utf-8 -*-
# author:Andy
# time:2020/7/29
import tkinter as tk
root = tk.Tk()
root.geometry("500x300+100+100")
girls = ['西施', '王昭君', '貂蝉', '杨玉环']

# 创建可变变量容器
v = [tk.IntVar(), tk.IntVar(), tk.IntVar(), tk.IntVar()]

# # 提前选择内容
# v[3].set(1)

for index in range(4):
    # 创建一个复选框 text是复选框的显示内容 varable是复选框中的值
    c = tk.Checkbutton(root, text=girls[index], variable=v[index])
    c.pack(anchor='w')

def get_value():
    # 默认打印的是文字对象
    # print(v)
    print([i.get() for i in v])

button = tk.Button(text='获取参数', command=get_value)
button.pack()

root.mainloop()