import tkinter as tk 
frame = tk.Tk()
frame_size = 500
creen_weith = frame.winfo_screenwidth()
creen_hight = frame.winfo_screenheight()

v =[tk.IntVar(), tk.IntVar(), tk.IntVar(), tk.IntVar(),tk.IntVar()]
#frame_location 
frame_location = "{}x{}+{}+{}".format(frame_size, frame_size, int((creen_weith - 500 )/2),int((creen_hight - 500)/2))
frame.geometry(str(frame_location))


variabel = tk.StringVar()
variabel.set("one")

w = tk.OptionMenu(frame, variabel,'one',"two","three",'four')

w.pack()

frame.mainloop()