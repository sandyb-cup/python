import  tkinter as tk


top = tk.Tk()

B1 = tk.Button(top, text ="FLAT", relief="flat" )
B2 = tk.Button(top, text ="RAISED", relief="raised" )
B3 = tk.Button(top, text ="SUNKEN", relief="solid")
B4 = tk.Button(top, text ="GROOVE", relief="ridge" )
B5 = tk.Button(top, text ="RIDGE", relief="groove")

B1.pack()
B2.pack()
B3.pack()
B4.pack()
B5.pack()
top.mainloop()