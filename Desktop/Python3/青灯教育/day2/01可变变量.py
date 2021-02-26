# -*- conding: utf-8 -*-
# author:Andy
# time:2020/7/29
import datetime
import tkinter as tk
import time
str_time = str(datetime.datetime.now())[:-7]
frame = tk.Tk()
frame.geometry('500x300+100+100')

# set往可变变量里面放置值
# get提取值
# textvariable指定可变变量
# 可变变量xixu
# tk.Label(root, textvariable=str_time, font = ('宋体', 24)). pack
str_time_var = tk.StringVar()
label = tk.Label(frame, textvariable=str_time_var, font=('宋体', 24))
label.pack()
while True:
    time.sleep(1)
    str_time = str(datetime.datetime.now())[:-7]
    str_time_var.set(str_time)
    frame.update()
    # result = str_time_var.get()
    # print(result)

root.mainloop()
