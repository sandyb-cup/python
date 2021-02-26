import tkinter as tk

# 获取屏幕大小
root = tk.Tk()

root.title("window test")

window_size = "500x500+400+400"
root.geometry(window_size)

# 获取电脑屏幕大小信息
width = root.winfo_screenwidth()
hight = root.winfo_screenheight()
print("width:", width)
print("hight:", hight)

root.update()
# 获取窗口大小
print(root.winfo_width(),root.winfo_height())

root.mainloop()
