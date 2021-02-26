import tkinter as tk 
import datetime
from tkinter import Label
frame_size = 500
frame = tk.Tk()

frame.title("Menu frame") 
creen_weith = frame.winfo_screenwidth()
creen_hight = frame.winfo_screenheight()

# 窗口长度 * 窗口高度 + 窗口位置x + 窗口位置y 将窗口设置为居中
frame_location = "{}x{}+{}+{}".format(frame_size, frame_size, int((creen_weith - 500 )/2),int((creen_hight - 500)/2))
frame.geometry(frame_location)

# 定义菜单组件

menubar = tk.Menu(frame)
menubar.add_command(label = "新建", command = "")
menubar.add_command(label = "退出", command = frame.quit)


label = tk.Label(frame,text = "菜单组件").pack()

# 将menu配置到frame中(显示)
frame.config(menu=menubar)
frame.update()
# 二级菜单
file_menu = tk.Menu(menubar)
file_menu.add_command(label = "打开")
file_menu.add_command(label = "关闭")

# 把二级菜单挂到一级菜单上面
menubar.add_cascade(label = "文件", menu = file_menu)


frame.mainloop()