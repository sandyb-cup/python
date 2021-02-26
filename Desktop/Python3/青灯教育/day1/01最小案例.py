# -*- conding: utf-8 -*-
# author:Andy
# time:2020/7/29
import tkinter as tk
# 创建一个窗口
root = tk.Tk()

root.title('我的第一个组件')

# 添加一个lable组件
label = tk.Label(root, text = 'hello python')

root.mainloop()