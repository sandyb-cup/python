import time
import tkinter as tk

def twd():
    root.withdraw()
    # time.sleep(3)
    # root.wm_deiconify()

root = tk.Tk()
lb = tk.Label(root, text='test')
bt = tk.Button(root, text='withdraw root', command=twd)
lb.pack()
bt.pack()
root.mainloop()