import tkinter as tk 
import datetime
frame_size = 500
frame = tk.Tk()

frame.title("Enter frame") 
creen_weith = frame.winfo_screenwidth()
creen_hight = frame.winfo_screenheight()

# 窗口长度 * 窗口高度 + 窗口位置x + 窗口位置y 将窗口设置为居中
frame_location = "{}x{}+{}+{}".format(frame_size, frame_size, int((creen_weith - 500 )/2),int((creen_hight - 500)/2))
frame.geometry(frame_location)

def top_frame_lever():
    frame.quit()
    top = tk.Toplevel()
    top.title("welcome")
    tk.Label(top,text = '你好').pack()
    top.geometry(frame_location)
    
numbar = tk.Menu(frame)

tk.Button(text = "顶级窗口", command = top_frame_lever).pack()

frame.config(menu = numbar)

frame.mainloop()