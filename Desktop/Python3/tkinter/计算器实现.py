import tkinter as tk

frame =tk.Tk()
frame_size = 500

frame.title("Computer") 
creen_weith = frame.winfo_screenwidth()
creen_hight = frame.winfo_screenheight()

# 窗口长度 * 窗口高度 + 窗口位置x + 窗口位置y 将窗口设置为居中
frame_location = "{}x{}+{}+{}".format(frame_size, frame_size, int((creen_weith - 500 )/2),int((creen_hight - 500)/2))
frame.geometry(frame_location)

inv = tk.IntVar()
inv.set("0")
index = 4
index_height = 2
bg_colors = 'red'
num_screen = tk.Label(frame, textvariable=inv, font =("正楷",20),width=5, height=index_height,relief="flat", justify = tk.LEFT).grid(sticky=tk.SE)

num_screen = tk.Button(frame, text="C", font =("正楷",20),width=5,height=index_height,relief="flat").grid(row=1,column=0, padx=index, pady=index)
num_screen = tk.Button(frame, text="<--", font =("正楷",20),width=5,height=index_height,relief="flat").grid(row=1,column=1, padx=index, pady=index)
num_screen = tk.Button(frame, text="/", font =("正楷",20),width=5,height=index_height,relief="flat").grid(row=1,column=2, padx=index,pady=index)
num_screen = tk.Button(frame, text="x", font =("正楷",20),width=5,height=index_height,relief="flat").grid(row=1,column=3, padx=index, pady=index)
num_screen = tk.Button(frame, text="7", font =("正楷",20),width=5,height=index_height,relief="flat",bg = bg_colors).grid(row=2,column=0, padx=index, pady=index)
num_screen = tk.Button(frame, text="8", font =("正楷",20),width=5,height=index_height,relief="flat",bg = bg_colors).grid(row=2,column=1, padx=index, pady=index)
num_screen = tk.Button(frame, text="9", font =("正楷",20),width=5,height=index_height,relief="flat",bg = bg_colors).grid(row=2,column=2, padx=index, pady=index)
num_screen = tk.Button(frame, text="-", font =("正楷",20),width=5,height=index_height,relief="flat",bg = bg_colors).grid(row=2,column=3, padx=index, pady=index)
num_screen = tk.Button(frame, text="4", font =("正楷",20),width=5,height=index_height,relief="flat",bg = bg_colors).grid(row=3,column=0, padx=index, pady=index)
num_screen = tk.Button(frame, text="5", font =("正楷",20),width=5,height=index_height,relief="flat",bg = bg_colors).grid(row=3,column=1, padx=index, pady=index)
num_screen = tk.Button(frame, text="6", font =("正楷",20),width=5,height=index_height,relief="flat",bg = bg_colors).grid(row=3,column=2, padx=index, pady=index)
num_screen = tk.Button(frame, text="+", font =("正楷",20),width=5,height=index_height,relief="flat").grid(row=3,column=3, padx=index, pady=index) 
num_screen = tk.Button(frame, text="1", font =("正楷",20),width=5,height=index_height,relief="flat",bg = bg_colors).grid(row=4,column=0, padx=index, pady=index)
num_screen = tk.Button(frame, text="2", font =("正楷",20),width=5,height=index_height,relief="flat",bg = bg_colors).grid(row=4,column=1, padx=index, pady=index)
num_screen = tk.Button(frame, text="3", font =("正楷",20),width=5,height=index_height,relief="flat",bg = bg_colors).grid(row=4,column=2, padx=index, pady=index)
num_screen = tk.Button(frame, text="=", font =("正楷",20),width=5,height=5,relief="flat",).grid(row=4,column=3,rowspan=6,padx=index, pady=index)
num_screen = tk.Button(frame, text="0", font =("正楷",20),width=11,height=index_height,relief="flat",bg = bg_colors).grid(row=5,column=0,columnspan=2, padx=index, pady=index)
num_screen = tk.Button(frame, text=".", font =("正楷",20),width=5,height=index_height,relief="flat").grid(row=5,column=2, padx=index, pady=index)

frame.mainloop()

    