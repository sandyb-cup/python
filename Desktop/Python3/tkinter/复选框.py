import tkinter as tk
frame = tk.Tk()

frame_size = 500
creen_weith = frame.winfo_screenwidth()
creen_hight = frame.winfo_screenheight()

v =[tk.IntVar(), tk.IntVar(), tk.IntVar(), tk.IntVar(),tk.IntVar()]
#frame_location 
frame_location = "{}x{}+{}+{}".format(frame_size, frame_size, int((creen_weith - 500 )/2),int((creen_hight - 500)/2))
frame.geometry(str(frame_location))

honor_name = ["李白","苏轼","杜甫","王安石","李清照"]
def get_poet():
    for i in range(len(honor_name)):
        if v[i].get() == 1:
            print(honor_name[i])
# checkbutton 复选框
tk.Checkbutton(frame, text = honor_name[0], variable = v[0]).pack(anchor=tk.W) 
tk.Checkbutton(frame, text = honor_name[1],variable = v[1]).pack(anchor=tk.W) 
tk.Checkbutton(frame, text = honor_name[2],variable = v[2]).pack(anchor=tk.W) 
tk.Checkbutton(frame, text = honor_name[3],variable = v[3]).pack(anchor=tk.W) 
# tk.Checkbutton(frame, text = honor_name[4]).pack(anchor=tk.W) 

button = tk.Button(frame, text="选取角色:",command=get_poet).pack(anchor=tk.W)


frame.mainloop()