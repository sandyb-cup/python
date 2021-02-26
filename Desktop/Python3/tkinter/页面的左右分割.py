import tkinter as tk
from tkinter.constants import BOTH, LEFT, RIGHT
from pykeyboard import PyKeyboard
k = PyKeyboard()
frame = tk.Tk()

frame.title("Segmention line")

frame_size = 500
creen_weith = frame.winfo_screenwidth()
creen_hight = frame.winfo_screenheight()

v =[tk.IntVar(), tk.IntVar(), tk.IntVar(), tk.IntVar(),tk.IntVar()]
#frame_location 
frame_location = "{}x{}+{}+{}".format(frame_size, frame_size, int((creen_weith - 500 )/2),int((creen_hight - 500)/2))
frame.geometry(str(frame_location))

left_frame = tk.Frame(frame) # 创建一个窗口

left_Labelframe = tk.LabelFrame(left_frame)
user_info = tk.Label(left_Labelframe, text="姓名:")
variable = tk.StringVar()
variable.set("男")
option_menu = tk.OptionMenu(left_Labelframe, variable, "男","女","保密")
left_frame.pack(anchor=tk.N, side=tk.LEFT)
left_Labelframe.pack()
user_info.pack()
option_menu.pack()

# left_frame2 = tk.LabelFrame(left_Labelframe)
user_age = tk.Label(left_Labelframe, text="年龄")
variable = tk.StringVar()
variable.set("20")
option_menu = tk.OptionMenu(left_Labelframe, variable, "20","25","自定义:")
user_info.pack()
user_age.pack()
option_menu.pack()

# # left_frame3 = tk.LabelFrame(left_Labelframe)
# user_age = tk.Label(left_Labelframe text="所在地")
# variable = tk.StringVar()
# variable.set("北京")
# option_menu = tk.OptionMenu(left_Labelframe, variable, "湖北","江西","自定义")

# user_age.pack()

# option_menu.pack()

# left_frame4 = tk.LabelFrame(left_Labelframe)
user_age = tk.Label(left_Labelframe, text="对薪资要求")
variable = tk.StringVar()
variable.set("2000")
option_menu = tk.OptionMenu(left_Labelframe, variable, "3000","4000","自定义")
user_age.pack()
option_menu.pack()

def end_activate(activate):
    activate.delete(0, "end")
var = tk.IntVar()
def button_info():
    num = var.get()
    variable.set("{}".format(num))
    return num

def printOption(Event):
    print(variable.get())
    print(type(variable.get()))
    if variable.get() == "自定义":
        frame_small = tk.LabelFrame(frame)
        frame_small.pack()
      
        input_entry = tk.Entry(frame_small, textvariable=var).pack()
        confim_button = tk.Button(frame_small, text = "确定", command=button_info).pack(side = tk.LEFT)
        cancel_button = tk.Button(frame_small, text = "取消",).pack(side=tk.RIGHT)
        # print(variable.get())
        # variable.set("{}".format(num))
        # frame.update()
        return input_entry, confim_button, cancel_button
    

    
    
option_menu.bind("<Button-1>", printOption) # 点击事件 触发函数

right_frame = tk.Frame(frame)
text_frame = tk.Text(right_frame)
right_frame.pack()
text_frame.pack()

frame.update()
frame.mainloop()
