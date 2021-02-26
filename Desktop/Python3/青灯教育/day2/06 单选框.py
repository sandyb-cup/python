# -*- conding: utf-8 -*-
# author:Andy
# time:2020/7/29
import tkinter as tk
root = tk.Tk()
root.geometry('500x500+100+100')

v = tk.IntVar() # 设置一个整形的数字类型

# one = tk.StringVar()
# one.set('one')

# variable 是点击之后数据保存地址, valuew 是点击事件发生之后点击事件的代号
tk.Radiobutton(root,  text = 'one', variable=v, value=1).pack(anchor = tk.W)
tk.Radiobutton(root,  text='two',  variable=v, value=2).pack(anchor = tk.W)
tk.Radiobutton(root,  text = 'Three', variable=v, value=3).pack(anchor = tk.W)

def get_values():
    print(v.get())

button = tk.Button(text = '获取参数', command = get_values)
button.pack()
root.mainloop()
