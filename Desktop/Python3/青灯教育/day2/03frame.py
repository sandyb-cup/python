# -*- conding: utf-8 -*-
# author:Andy
# time:2020/7/29
import tkinter as tk
root = tk.Tk()
root.geometry('500x500+100+100')
left_frame = tk.Frame(root, width = 250)
left_frame.pack(side = tk.LEFT)

tk.Button(left_frame, text = '按我', width = 10, height = 2).pack()
tk.Button(left_frame, text = '按我', width = 10, height = 2).pack()
tk.Button(left_frame, text = '按我', width = 10, height = 2).pack()

right_frame = tk.Frame(root, width = 250)
tk.Button(right_frame, text = '不要按我', width = 20, height = 3).pack()
tk.Button(right_frame, text = '不要按我', width = 20, height = 3).pack()
tk.Button(right_frame, text = '不要按我', width = 20, height = 3).pack()
right_frame.pack(side = tk.RIGHT)
root.mainloop()
