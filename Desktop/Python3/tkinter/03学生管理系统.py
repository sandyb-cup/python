import tkinter as tk
from tkinter.constants import CENTER 


frame_size = 500
frame = tk.Tk()
frame.title("学生管理系统")

creen_weith = frame.winfo_screenwidth()
creen_hight = frame.winfo_screenheight()

v =[tk.IntVar(), tk.IntVar(), tk.IntVar(), tk.IntVar(),tk.IntVar()]
#frame_location 
frame_location = "{}x{}+{}+{}".format(frame_size, frame_size, int((creen_weith - 500 )/2),int((creen_hight - 500)/2))
frame.geometry(str(frame_location))


def background_iamge(image_path):
    image = tk.PhotoImage(image_path)
    return image

# 成功登入后的页面创建
def entry_button():
    info_frame = tk.Toplevel()
    info_frame.title("查询学生信息表")
    # frame.withdraw() 
    frame.state("icon")
    info_frame.geometry(str(frame_location))
    
    info_frame__(info_frame)

def log_in():
    entry_name_info = tk.StringVar()
    index = 5
    span_grid = tk.Label(frame, text = "", width=15, height=10).grid(row = 0, column=0)
    
    
    log_use_name = tk.Label(frame,text = "姓名:", font = ("正楷", 12)).grid(row=1, column=1, sticky=tk.W, padx = index, pady = index)
    log_use_entry = tk.Entry(frame, textvariable=entry_name_info).grid(row=1, column=2, sticky=tk.W,padx = index, pady = index)
    
    entry_password = tk.StringVar()
    log_use_name = tk.Label(frame,text = "密码:", font = ("正楷", 12)).grid(row=2, column=1, sticky=tk.W,padx = index, pady = index)
    log_use_entry = tk.Entry(frame, textvariable=entry_name_info).grid(row=2, column=2, sticky=tk.W,padx = index, pady = index)
    
    log_entry_button = tk.Button(frame, text = "登入", font=("正楷", 12), width = 10, height = 1,command=entry_button).grid(row=3, column=2, sticky=tk.W,padx = index, pady = index)
    log_back_button  = tk.Button(frame, text = "登出", font=("正楷", 12), width = 10, height = 1,command=frame.quit).grid(row=3, column=2, sticky=tk.E,padx = index, pady = index)

def info_frame__(info_frame):
    index = 5
    span_grid = tk.Label(info_frame, text = "", width=10, height=8).grid(row = 0, column=0, sticky=tk.W)
    
    entry_name_info = tk.StringVar()
    log_use_name = tk.Label(info_frame,text = "姓名:", font = ("正楷", 12)).grid(row=1, column=1, sticky=tk.W, padx = index, pady = index)
    log_use_entry = tk.Entry(info_frame, textvariable=entry_name_info).grid(row=1, column=2, sticky=tk.W,padx = index, pady = index)
    
    var_chineses = tk.StringVar()
    log_chineses_name = tk.Label(info_frame,text = "语文:", font = ("正楷", 12)).grid(row=2, column=1, sticky=tk.W,padx = index, pady = index)
    log_chineses_entry = tk.Entry(info_frame, textvariable=var_chineses).grid(row=2, column=2, sticky=tk.W,padx = index, pady = index)
    
    math_var = tk.StringVar()
    log_math_name = tk.Label(info_frame,text = "数学:", font = ("正楷", 12)).grid(row=3, column=1, sticky=tk.W,padx = index, pady = index)
    log_math_entry = tk.Entry(info_frame, textvariable=math_var).grid(row=3, column=2, sticky=tk.W,padx = index, pady = index)
    
    english_var = tk.StringVar()
    log_english_name = tk.Label(info_frame,text = "英语:", font = ("正楷", 12)).grid(row=4, column=1, sticky=tk.W,padx = index, pady = index)
    log_english_entry = tk.Entry(info_frame, textvariable=english_var).grid(row=4, column=2, sticky=tk.W,padx = index, pady = index)
    
    check_button = tk.Button(info_frame, text = "查询", font=("正楷", 12), width = 5, height = 1,command="").grid(row=5, column=2, sticky=tk.W,padx = index, pady = index)
    cancel_button = tk.Button(info_frame, text = "取消", font=("正楷", 12), width = 5, height = 1,command=frame.quit).grid(row=5, column=2, sticky=tk.E,padx = index, pady = index)
    modify_button = tk.Button(info_frame, text = "修改", font=("正楷", 12), width = 5, height = 1,command="").grid(row=5, column=2, sticky=tk.N,padx = index, pady = index)
def main():
    log_in()
    
if __name__ == "__main__":
    main()
    frame.mainloop()
