# -*- conding: utf-8 -*-
# author:Andy
# time:2020/7/29
import tkinter as tk
root = tk.Tk()
root.geometry('500x500+100+100')
label_frame1 = tk.LabelFrame(root, text='世界上最好用的脚本语言是?', padx = 5, pady = 10)

label_frame1.pack(side = tk.LEFT, padx = 10, pady = 20)

langs = [
    ('python', 1),
    ('perl', 2),
    ('ruby', 3),
    ('lua', 4),
]

v = tk.IntVar()
v.set(1)

for lang, on in langs:
    b = tk.Radiobutton(label_frame1, text = lang, variable = v, value = on)
    b.pack(anchor=tk.W)

info_frame = tk.LabelFrame(root).pack(side = tk.RIGHT)

tk.Label(info_frame, text = "世界上最好的脚本语言是？", ).pack()
text_area = tk.Text(info_frame, height = 20, width = 100)

text_area.pack(side = tk.LEFT)


root.mainloop()
