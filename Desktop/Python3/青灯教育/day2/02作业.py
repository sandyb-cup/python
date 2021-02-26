# -*- conding: utf-8 -*-
# author:Andy
# time:2020/7/29
import tkinter as tk

root = tk.Tk()
root.title('问卷调查')
root.geometry('500x500+100+100')

Left_frame = tk.Frame(root)
Left_frame.pack(side = tk.LEFT)

# 左边第一个Lable_frame
Label_frame1 = tk.LabelFrame(Left_frame, text = '个人信息', width = 20, height = 30)
Label_frame1.pack(anchor = tk.E)

radio_Int = tk.IntVar()
radio_button_1 = tk.Radiobutton(Label_frame1, text = '男', variable = radio_Int, value = 1)
radio_button_2 = tk.Radiobutton(Label_frame1, text = '女', variable = radio_Int, value = 2)
radio_button_3 = tk.Radiobutton(Label_frame1, text = '保密', variable = radio_Int, value = 3)

radio_button_1.pack(anchor = tk.W,padx = 5, pady = 20)
radio_button_2.pack(anchor = tk.W,padx = 5, pady = 20)
radio_button_3.pack(anchor = tk.W,padx = 5, pady = 20)

# 左边的第二个 Lable_frame
Label_frame2 = tk.LabelFrame(Left_frame, text = '爱好', width = 20, height = 30)
Label_frame2.pack(anchor = tk.E)

hobby_int = [tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar()]
hobbys = ['吃', '喝', '玩', '乐']

for i in range(4):
    check_button = tk.Checkbutton(Label_frame2, text=hobbys[i], variable=hobby_int[i])
    check_button.pack(anchor = tk.W, padx = 10, pady = 20)



# 右边视图的部分功能
def commit_log():
    print('已提交')

# 右边的视图
right_frame = tk.Frame(root)
right_frame.pack(side = tk.TOP)

right_frame_label = tk.Label(right_frame,text = '怎么敲代码才不会报错?')
right_frame_label.pack(anchor = tk.N)

loca_label = tk.Label(right_frame ,text = '所在省份:')
loca_label.pack(anchor = tk.N)

loca_label = tk.Label(right_frame ,text = ' ')
loca_label.pack(anchor = tk.N)

radio_loca = tk.IntVar()
radio_button_loca = tk.Radiobutton(loca_label, text = '北京', variable = radio_loca, value = 1).pack(anchor = tk.W, side = tk.RIGHT)
radio_button_loca = tk.Radiobutton(loca_label, text = '上海', variable = radio_loca, value = 2).pack(anchor = tk.W, side = tk.RIGHT)
radio_button_loca  = tk.Radiobutton(loca_label, text = '深圳', variable = radio_loca, value = 3).pack(anchor = tk.W, side = tk.RIGHT)


text_log = tk.Text(right_frame, width = 50, height = 20 )
text_log.pack(anchor = tk.N)

text_commit_button = tk.Button(right_frame, text = '提交', command = commit_log, padx=40, pady = 2)
text_commit_button.pack()

root.mainloop()

