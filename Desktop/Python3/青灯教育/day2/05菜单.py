# -*- conding: utf-8 -*-
# author:Andy
# time:2020/7/29
from tkinter import *

root = Tk()
menubar = Menu(root)  # 创建菜单栏
file_menu = Menu(menubar, tearoff=False) # 创建空菜单
file_menu.add_command(label="a") # 向file_menu菜单中添加label
file_menu.add_command(label="b")
menubar.add_cascade(label="A", menu=file_menu) # 将file_menu菜单添加到菜单栏
root.config(menu=menubar) # display the menu
root.mainloop()
