import tkinter as tk
import datetime
frame = tk.Tk()

frame_size = 500
frame.title("Entry show")
creen_weith = frame.winfo_screenwidth()
creen_hight = frame.winfo_screenheight()

# 窗口长度 * 窗口高度 + 窗口位置x + 窗口位置y 将窗口设置为居中
frame_location = "{}x{}+{}+{}".format(frame_size, frame_size, int((creen_weith - 500 )/2),int((creen_hight - 500)/2))
frame.geometry(frame_location)
name = tk.Label(text = "user:", font = ('华文新魏', 18), )
name_entry = tk.Entry(text = "Place input your name")
button_update = tk.Button(text = "Update date", width=12)

# grid()
def label_tab(index):
    label_tab1 = tk.Label(frame, width ="12").grid(row = index, column = 0 ) # 向右移动5个像素点
    return label_tab1
label_tab(0)
name.place(relx = 0.3, rely = 0.2,  anchor=tk.N)
name_entry.place(relx = 0.55, rely = 0.2, anchor =tk.N)
label_tab(2)
button_update.place(relx = 0.5, rely = 0.5, anchor = tk.N)

# button
var = tk.StringVar()
laber = tk.Label(frame, textvariable=var).place(relx = 0.2, rely=0.9,  anchor= tk.N)
while True:
    data_show = datetime.datetime.now()
    date_now = str(data_show)[:-7]
    frame.update()
    var.set(date_now)

# 实例化一个变量参数
# 显示内容
frame.mainloop()