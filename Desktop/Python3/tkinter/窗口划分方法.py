import tkinter as tk 
import datetime
frame_size = 500
frame = tk.Tk()

frame.title("Enter frame") 
creen_weith = frame.winfo_screenwidth()
creen_hight = frame.winfo_screenheight()

# 窗口长度 * 窗口高度 + 窗口位置x + 窗口位置y 将窗口设置为居中
frame_location = "{}x{}+{}+{}".format(frame_size, frame_size, int((creen_weith - 500 )/2),int((creen_hight - 500)/2))
frame.geometry(frame_location)

alter_text = tk.StringVar() # 定义一个可变变量
text_info = "用户名:" # 获取当前时间
alter_text.set(text_info) # 设置可变变量的值

# label文本输入
label_use = tk.Label(frame, textvariable=alter_text, font = ('正楷', 12))
label_password = tk.Label(frame, text="密码:", font=('正楷', 12))

# 设置输入框:
enter_use = tk.Entry(frame)
enter_password = tk.Entry(frame)

# 设置按钮回馈
def enter_id():
    print("走你～")

# 设置按钮button
# 按钮属性
'''anchor:      　　　　  指定按钮上文本的位置；
    background(bg)    　  指定按钮的背景色；
    bitmap:       　　　　 指定按钮上显示的位图；
    borderwidth(bd)　　　　指定按钮边框的宽度；
    command:   　　　　　  指定按钮消息的回调函数；
    cursor:        　　　　指定鼠标移动到按钮上的指针样式；
    font:           　　  指定按钮上文本的字体；
    foreground(fg)　　　　 指定按钮的前景色；
    height:        　　　　指定按钮的高度；
    image:        　　　　 指定按钮上显示的图片；
    state:          　　　 指定按钮的状态（disabled）；
    text:           　　　 指定按钮上显示的文本；
    width:       　　　　  指定按钮的宽度
    padx          　　　　 设置文本与按钮边框x的距离，还有pady;
    activeforeground　　　 按下时前景色
    textvariable    　　  可变文本，与StringVar等配合着用'''
enter_button = tk.Button(frame, text="登入", font=('正楷', 18), fg ="#00CCFF", width=12,command=enter_id)

    
# 1.pack() 属性 

# side = tk.LEFT/BUTTON/TOP anchor = tk.E/N/W/S
# label_use.pack(side = tk.LEFT, anchor = tk.N) # 注意anchor锚点的位置是相对于side来讲的
# enter_use.pack(side = tk.LEFT, anchor = tk.N)
# label_password.pack(side = tk.LEFT, anchor = tk.N)
# enter_password.pack(side = tk.LEFT, anchor = tk.N)
# enter_button.pack(side = tk.LEFT, anchor =tk.N)


# 2.grid() 属性 

# row = 0, column = 1 stick 作用相当于anchor\
# def label_tab(index):
#     label_tab1 = tk.Label(frame, width ="12").grid(row = index, column = 0 ) # 向右移动5个像素点
#     return label_tab1
# tabel_tab = label_tab(0)
# label_use.grid(row = 1, column = 1) # 注意anchor锚点的位置是相对于side来讲的
# enter_use.grid(row = 1, column = 2)

# tabel_tab = label_tab(2)
# label_password.grid(row = 3, column = 1)
# enter_password.grid(row = 3, column = 2)

# tabel_tab  = label_tab(4)
# enter_button.grid(row = 5, column = 2, sticky=tk.W)


#3.place()属性 

# relx = float.num, rely = float.num
label_use.place(relx = 0.35, rely = 0.3, anchor=tk.N) # 注意anchor锚点的位置是相对于side来讲的
enter_use.place(relx = 0.4, rely = 0.3) 

label_password.place(relx = 0.35, rely = 0.4, anchor= tk.N)
enter_password.place(relx = 0.4, rely = 0.4)

enter_button.place(relx = 0.35, rely = 0.5, anchor = tk.N)

frame.update()
frame.mainloop()