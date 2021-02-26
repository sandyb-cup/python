import tkinter as tk
root = tk.Tk()

# 设置窗口属性
root.title("Tkinter window")
# 设置图标 一定是 ico结尾的文件放到同名文件夹下
root.iconbitmap("icon.ico")
# 设置背景颜色
root['background'] = "#00ffff"
# 设置窗口透明度
root.attributes("-alpha", 1)
# root.attributes("-toolwindow", True)

# True没有工具栏按钮 False显示工具栏 
root.overrideredirect(False)

# 设置窗口大小
window_size = "600x600+500+500"
root.geometry(window_size)

# 获取窗口大小属性
width = root.winfo_screenwidth()
hight = root.winfo_screenheight()
print("window width:", width)
print("hight:",hight)

# 进入窗口循环 显示窗口
root.mainloop()

