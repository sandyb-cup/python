# -*- conding: utf-8 -*-
# author:Andy
# time:2020/7/29
import tkinter as tk
root = tk.Tk()
menubar = tk.Menu(root) # 创建一个 菜单选项
file_menu = tk.Menu(menubar, tearoff = False) # 创建一个空菜单
file_menu.add_command(label = 'a')
file_menu.add_command(label = 'b')

menubar.add_cascade(label = 'A', menu = file_menu) # 将file_menu添加到菜单栏
root.config(menu = menubar) # 在root中添加 menu组件
root.mainloop()
