import tkinter as tk
frame = tk.Tk()

frame_size = 500
creen_weith = frame.winfo_screenwidth()
creen_hight = frame.winfo_screenheight()

v =[tk.IntVar(), tk.IntVar(), tk.IntVar(), tk.IntVar(),tk.IntVar()]
#frame_location 
frame_location = "{}x{}+{}+{}".format(frame_size, frame_size, int((creen_weith - 500 )/2),int((creen_hight - 500)/2))
frame.geometry(str(frame_location))

group = tk.LabelFrame(frame, text="世界上最美的人是谁?")
group.pack()
group_dict = [("西施",0),
              ("貂蝉",1),
              ("杨玉环",2),
              ("王昭君",3)]
var = tk.IntVar()
check_var = [tk.IntVar for i in range(len(group_dict))]
print(check_var)
def get_poet():
    for i in range(len(group_dict)):
        if v[i].get() == 1:
            print(group_dict[i][0])
n = 0
for i in range(len(group_dict)):
    
    b = tk.Checkbutton(group, text=str(group_dict[i][0]), variable= v[n]).grid(row = n, column= 3)
    n += 1
button = tk.Button(group, text="答案",command=get_poet).grid()

frame.mainloop()
