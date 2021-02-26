import tkinter as tk
import datetime
from tkinter import StringVar
import time
frame_size = 500
frame = tk.Tk()

frame.title("Time show") 
creen_weith = frame.winfo_screenwidth()
creen_hight = frame.winfo_screenheight()

# 窗口长度 * 窗口高度 + 窗口位置x + 窗口位置y 将窗口设置为居中
frame_location = "{}x{}+{}+{}".format(frame_size, frame_size, int((creen_weith - 500 )/2),int((creen_hight - 500)/2))
frame.geometry(str(frame_location))

alter_text = tk.StringVar() # 定义一个可变变量
text_info = str(datetime.datetime.now())[:-7] # 获取当前时间
alter_text.set(text_info) # 设置可变变量的值

label = tk.Label(frame, textvariable=alter_text, font = ('正楷', 24))
label.pack()

# get 函数实现
def click():
    shell_show = alter_text.get()
    print(shell_show)
    
button = tk.Button(frame, text = "点击", command=click, font = ("正楷", 24))
button.pack()
while True:
    text_info = str(datetime.datetime.now())[:-7] # 获取当前时间
    alter_text.set(text_info)
    frame.update()
    time.sleep(1)
frame.mainloop()
