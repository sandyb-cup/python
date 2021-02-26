import tkinter as tk
frame = tk.Tk()

frame_size = 500
creen_weith = frame.winfo_screenwidth()
creen_hight = frame.winfo_screenheight()

v =[tk.IntVar(), tk.IntVar(), tk.IntVar(), tk.IntVar(),tk.IntVar()]
#frame_location 
frame_location = "{}x{}+{}+{}".format(frame_size, frame_size, int((creen_weith - 500 )/2),int((creen_hight - 500)/2))
frame.geometry(str(frame_location))

text = tk.StringVar()

def get_text( ):
    print(text.get())
entry = tk.Entry(frame, textvariable=text).grid(row =0, column=0)


button = tk.Button(frame,text="click me", command=get_text ).grid(row = 1, column=0)

frame.mainloop()
