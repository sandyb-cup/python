# -*- conding: utf-8 -*-
# author:Andy
# time:2020/7/29
import tkinter as tk

root = tk.Tk()

def create_button(root):
    say_hello = tk.Button(root, text="打招呼")
    # 方向控键 LEFT RIGHT TOP BUTTON
    say_hello.pack(side=tk.LEFT)
    return root
root = create_button(root)

root.geometry('300x300+100+100')

root.mainloop()
