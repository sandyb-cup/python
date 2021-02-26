import tkinter as tk 
frame = tk.Tk()
frame_size = 500
weight_size = frame.winfo_screenwidth()
hight_size = frame.winfo_screenheight()

frame_frame = "{}x{}+{}+{}".format(frame_size, frame_size, int((weight_size - frame_size)/2),int((hight_size-frame_size)/2))
frame.geometry(frame_frame)

titile = frame.title("Config text")
use_name = tk.Label(frame, text = "姓名:", font = ("华文新魏", 18))
use_password = tk.Entry(frame)

button_next = tk.Button(frame, text="Next",font = ("华文新魏", 18), width= 12 )
button_cancel = tk.Button(frame, text = "Cancel", font = ("华文新魏", 18), width = 12)
# place()
use_name.place(relx = 0.3, rely = 0.4, anchor=tk.S)
use_password.place(relx = 0.55, rely = 0.4, anchor=tk.S)
button_next.place(relx = 0.55, rely = 0.5, anchor=tk.S)
button_cancel.place(relx = 0.55, rely = 0.60, anchor=tk.S)


# 设置一个点击函数
def fuc():
    print("走你~")
# config()
button_next.config(command = fuc)  
# 另外一种形式
# button_next["command"] = fuc
frame.mainloop()
