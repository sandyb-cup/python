import tkinter as tk
from tkinter.constants import CENTER
import openpyxl
import time
from test import root_entry, admini_get, stud_info, stud_get,read_file, save_file, student_entry_information, get_student_name
user = []

class frame1():
    def __init__(self):
        frame_size = 500
        
        
        # 加载登入学生信息
        self.student_info = student_entry_information()

        self.student_name = get_student_name()
        
        self.frame = tk.Tk()
        self.frame.title("学生管理系统")

        self.creen_weith = self.frame.winfo_screenwidth()
        self.creen_hight = self.frame.winfo_screenheight()
        #frame_location 
        self.frame_location = "{}x{}+{}+{}".format(frame_size, frame_size, int((self.creen_weith - 500 )/2),int((self.creen_hight - 500)/2))
        self.frame.geometry(str(self.frame_location))

        

        self.entry_name_info = tk.StringVar()
        self.entry_password = tk.StringVar()

        self.frame2_use_name = tk.StringVar()
        self.frame2_use_name.set("")
        self.var_chineses = tk.StringVar()
        self.math_var = tk.StringVar()
        self.english_var = tk.StringVar()
        
        # self.log_password = self.entry_password.get() # 获取输入框输入密码
        
    def background_iamge(self,image_path):
        self.image = tk.PhotoImage(image_path)
        return self.image
    
    # 登入按钮   
    def entry_button(self):
        name = self.entry_name_info.get() # 获取输入框名字
        user.append(name)
        log_password = self.entry_password.get()# 获取输入框输入密码
        student_name = self.student_name
        _,root_name = root_entry() # 获取登入信息
        
        if name not in root_name and name not in self.student_name: 
            span_grid = tk.Label(self.frame, text = "该用户不存在", width=15, height=10).grid(row = 4, column=2)
        elif name in root_name:
            print("root_name",root_name)
            root_password = admini_get(name)
            if log_password == root_password:
                span_grid = tk.Label(self.frame, text = "你好～", width=15, height=10).grid(row = 4, column=2)
                self.frame.state("icon")
                frame2().create_toplevel_frame2()
            else:
                span_grid = tk.Label(self.frame, text = "密码错误", width=15, height=10).grid(row = 4, column=2)
        elif name in student_name:
            student_password = self.student_info['{}'.format(name)]
            if log_password == student_password:
                span_grid = tk.Label(self.frame, text = "你好～", width=15, height=10).grid(row = 4, column=2)
                self.frame.state("icon")
                frame2().create_toplevel_frame2_student()
            else:
                span_grid = tk.Label(self.frame, text = "密码错误", width=15, height=10).grid(row = 4, column=2)
    # 登入页面             
    def log_in(self):
        index = 5
        span_grid = tk.Label(self.frame, text = "", width=15, height=10).grid(row = 0, column=0)
        
        log_use_name = tk.Label(self.frame,text = "姓名:", font = ("正楷", 12)).grid(row=1, column=1, sticky=tk.W, padx = index, pady = index)
        log_use_entry = tk.Entry(self.frame, textvariable=self.entry_name_info).grid(row=1, column=2, sticky=tk.W,padx = index, pady = index)
        
        log_password = tk.Label(self.frame,text = "密码:", font = ("正楷", 12)).grid(row=2, column=1, sticky=tk.W,padx = index, pady = index)
        log_use_entry = tk.Entry(self.frame, textvariable=self.entry_password).grid(row=2, column=2, sticky=tk.W,padx = index, pady = index)
        
        log_entry = tk.Button(self.frame, text = "登入", font=("正楷", 12), width = 10, height = 1,command=self.entry_button).grid(row=3, column=2, sticky=tk.W,padx = index, pady = index)
        log_back  = tk.Button(self.frame, text = "登出", font=("正楷", 12), width = 10, height = 1,command=self.frame.quit).grid(row=3, column=2, sticky=tk.E,padx = index, pady = index)
        self.frame.mainloop()
        
# 创建查询页        
class frame2():
    def __init__(self):
        #frame_location 
        self.entry_name_info = tk.StringVar()
        self.entry_password = tk.StringVar()

        self.frame2_use_name = tk.StringVar()
        self.var_chineses = tk.StringVar()
        self.math_var = tk.StringVar()
        self.english_var = tk.StringVar()
        
    # 老师界面
    def create_toplevel_frame2(self):

        frame_size = 500
        self.info_frame2 = tk.Toplevel()
        self.creen_weith = self.info_frame2.winfo_screenwidth()
        self.creen_hight = self.info_frame2.winfo_screenheight()
        #frame_location 
        self.frame_location = "{}x{}+{}+{}".format(frame_size, frame_size, int((self.creen_weith - 500 )/2),int((self.creen_hight - 500)/2))
        self.info_frame2.geometry(str(self.frame_location))
        self.info_frame2.title("成绩查询_teacher")
        
        # frame.withdraw() 
        self.info_frame2.geometry(str(self.frame_location))
        
        index = 5
        span_grid = tk.Label(self.info_frame2, text = "", width=10, height=8).grid(row = 0, column=0, sticky=tk.W)
        
        log_use_name = tk.Label(self.info_frame2,text = "姓名:", font = ("正楷", 12)).grid(row=1, column=1, sticky=tk.W, padx = index, pady = index)
        log_use_entry = tk.Entry(self.info_frame2, textvariable=self.frame2_use_name).grid(row=1, column=2, sticky=tk.W,padx = index, pady = index)
        
        log_chineses_name = tk.Label(self.info_frame2,text = "语文:", font = ("正楷", 12)).grid(row=2, column=1, sticky=tk.W,padx = index, pady = index)
        log_chineses_entry = tk.Entry(self.info_frame2, textvariable=self.var_chineses).grid(row=2, column=2, sticky=tk.W,padx = index, pady = index)
        
        log_math_name = tk.Label(self.info_frame2,text = "数学:", font = ("正楷", 12)).grid(row=3, column=1, sticky=tk.W,padx = index, pady = index)
        log_math_entry = tk.Entry(self.info_frame2, textvariable=self.math_var).grid(row=3, column=2, sticky=tk.W,padx = index, pady = index)
        
        log_english_name = tk.Label(self.info_frame2,text = "英语:", font = ("正楷", 12)).grid(row=4, column=1, sticky=tk.W,padx = index, pady = index)
        log_english_entry = tk.Entry(self.info_frame2, textvariable=self.english_var).grid(row=4, column=2, sticky=tk.W,padx = index, pady = index)
        
        check_button = tk.Button(self.info_frame2, text = "查询", font=("正楷", 12), width = 5, height = 1,command=self.check_info_button).grid(row=5, column=2, sticky=tk.W,padx = index, pady = index)
        cancel_button = tk.Button(self.info_frame2, text = "退出", font=("正楷", 12), width = 5, height = 1,command=self.info_frame2.quit).grid(row=5, column=2, sticky=tk.E,padx = index, pady = index)
        modify_button = tk.Button(self.info_frame2, text = "修改", font=("正楷", 12), width = 5, height = 1,command=self.modify_button).grid(row=5, column=2, sticky=tk.N,padx = index, pady = index)
        add_button = tk.Button(self.info_frame2, text = "添加", font=("正楷", 12), width = 5, height = 1,command=self.add_button).grid(row=6, column=2, sticky=tk.E,padx = index, pady = index)
        del_button = tk.Button(self.info_frame2, text = "删除", font=("正楷", 12), width = 5, height = 1,command=self.del_button).grid(row=6, column=2, sticky=tk.W,padx = index, pady = index)
        clear_button =tk.Button(self.info_frame2, text = "清除", font=("正楷", 12), width = 5, height = 1,command=self.init_zero).grid(row=6, column=2, sticky=tk.N,padx = index, pady = index)
        clear_button =tk.Button(self.info_frame2, text = "生成excel表格", font=("正楷", 12), width = 10, height = 1,command=self.create_excel).grid(row=7, column=2, sticky=tk.N,padx = index, pady = index)
    # 学生界面   
    def create_toplevel_frame2_student(self):
        frame_size = 500
        self.info_frame2 = tk.Toplevel()
        self.creen_weith = self.info_frame2.winfo_screenwidth()
        self.creen_hight = self.info_frame2.winfo_screenheight()
        #frame_location 
        self.frame_location = "{}x{}+{}+{}".format(frame_size, frame_size, int((self.creen_weith - 500 )/2),int((self.creen_hight - 500)/2))
        self.info_frame2.geometry(str(self.frame_location))
        self.info_frame2.title("成绩查询")
        
        # frame.withdraw() 
        self.info_frame2.geometry(str(self.frame_location))
        
        index = 5
        span_grid = tk.Label(self.info_frame2, text = "", width=10, height=8).grid(row = 0, column=0, sticky=tk.W)
        
        log_use_name = tk.Label(self.info_frame2,text = "姓名:", font = ("正楷", 12)).grid(row=1, column=1, sticky=tk.W, padx = index, pady = index)
        log_use_entry = tk.Entry(self.info_frame2, textvariable=self.frame2_use_name).grid(row=1, column=2, sticky=tk.W,padx = index, pady = index)
        
        log_chineses_name = tk.Label(self.info_frame2,text = "语文:", font = ("正楷", 12)).grid(row=2, column=1, sticky=tk.W,padx = index, pady = index)
        log_chineses_entry = tk.Entry(self.info_frame2, textvariable=self.var_chineses).grid(row=2, column=2, sticky=tk.W,padx = index, pady = index)
        
        log_math_name = tk.Label(self.info_frame2,text = "数学:", font = ("正楷", 12)).grid(row=3, column=1, sticky=tk.W,padx = index, pady = index)
        log_math_entry = tk.Entry(self.info_frame2, textvariable=self.math_var).grid(row=3, column=2, sticky=tk.W,padx = index, pady = index)
        
        log_english_name = tk.Label(self.info_frame2,text = "英语:", font = ("正楷", 12)).grid(row=4, column=1, sticky=tk.W,padx = index, pady = index)
        log_english_entry = tk.Entry(self.info_frame2, textvariable=self.english_var).grid(row=4, column=2, sticky=tk.W,padx = index, pady = index)
        
        check_button = tk.Button(self.info_frame2, text = "查询", font=("正楷", 12), width = 5, height = 1,command=self.check_info_student).grid(row=5, column=2, sticky=tk.W,padx = index, pady = index)
        cancel_button = tk.Button(self.info_frame2, text = "退出", font=("正楷", 12), width = 5, height = 1,command=self.info_frame2.quit).grid(row=5, column=2, sticky=tk.E,padx = index, pady = index)
        
        clear_button =tk.Button(self.info_frame2, text = "清除", font=("正楷", 12), width = 5, height = 1,command=self.init_zero).grid(row=5, column=2, sticky=tk.N,padx = index, pady = index)
        
    # 将输入框初始化为0
    def init_zero(self):
        # self.entry_name_info.set("0")
        # self.entry_password.set("0")

        self.frame2_use_name.set("请输入学生姓名:")
        self.var_chineses.set("0")
        self.math_var.set("0")
        self.english_var.set("0")
        
    # 查看按钮
    def check_info_button(self):
        entry_name = self.frame2_use_name.get()
        
        # frame2 = self.create_toplevel()
        _,name = stud_info()
        if entry_name not in name:
            span_grid = tk.Label(self.info_frame2, text = "无该学员信息", width=12, height=4).grid(row = 10, column=2)
        else:
            scord = stud_get(entry_name)
            self.var_chineses.set(scord[0])
            self.math_var.set(scord[1])
            self.english_var.set(scord[2])
            span_grid = tk.Label(self.info_frame2, text = "查询成功", width=8, height=4).grid(row = 10, column=2) 
    # 学生查看按钮        
    def check_info_student(self):
        entry_name = self.frame2_use_name.get()
        print(entry_name)
        # frame2 = self.create_toplevel()
        print(user[-1])
        if entry_name != user[-1]:
            span_grid = tk.Label(self.info_frame2, text = "查询失败", width=12, height=4).grid(row = 10, column=2)
        else:
            scord = stud_get(entry_name)
            self.var_chineses.set(scord[0])
            self.math_var.set(scord[1])
            self.english_var.set(scord[2])
            span_grid = tk.Label(self.info_frame2, text = "查询成功", width=8, height=4).grid(row = 10, column=2) 
            
    # 修改按钮    
    def modify_button(self):
        entry_name = self.frame2_use_name.get()
        stud_info = read_file()
        scord=stud_info[entry_name]
        
        scord[0] = self.var_chineses.get()
        scord[1] = self.math_var.get()
        scord[2] = self.english_var.get()
        
        save_file(stud_info)

        self.var_chineses.set(scord[0])
        self.math_var.set(scord[1])
        self.english_var.set(scord[2])
        span_grid = tk.Label(self.info_frame2, text = "修改成功", width=8, height=4).grid(row = 10, column=2) 
    
    # 添加按钮
    def add_button(self):
        entry_name = self.frame2_use_name.get()
        stud_info = read_file()
        if entry_name in stud_info.keys():
            span_grid = tk.Label(self.info_frame2, text = "该学生已存在系统", width=12, height=4).grid(row = 10, column=2) 
        else:
            scord0 = self.var_chineses.get()
            scord1 = self.math_var.get()
            scord2 = self.english_var.get()
            stud_info[entry_name] = [scord0, scord1, scord2]
            
            save_file(stud_info)

            self.var_chineses.set(scord0)
            self.math_var.set(scord1)
            self.english_var.set(scord2)
            span_grid = tk.Label(self.info_frame2, text = "添加成功", width=8, height=4).grid(row = 10, column=2) 
            
    # 删除按钮
    def del_button(self):
        entry_name = self.frame2_use_name.get()
        print(entry_name)
        stud_info = read_file()
        if entry_name not in stud_info.keys():
            span_grid = tk.Label(self.info_frame2, text = "未找到该学生信息", width=12, height=4).grid(row = 10, column=2) 
        else:
            del stud_info[str(entry_name)]
            save_file(stud_info)
            span_grid = tk.Label(self.info_frame2, text = "删除成功", width=8, height=4).grid(row = 10, column=2)
            
    def create_excel(self):
        names = []
        wb = openpyxl.Workbook()
        sheet = wb.active
        
        sheet.title = "学生成绩"
        sheet["A1"] = "学生姓名"
        sheet["B1"] = "语文"
        sheet["C1"] = "数学"
        sheet["D1"] = "英语"
        with open("student_information.text",'r',encoding='utf-8') as file:
            content = file.readline()
        stud_info = eval(content)
        for i in stud_info.keys():
            names.append(i)
        for n in range(len(names)):
            sheet.append([names[n], stud_info[names[n]][0],stud_info[names[n]][1],stud_info[names[n]][2]])
        wb.save('/Users/sandy/Desktop/music.xlsx')
        span_grid = tk.Label(self.info_frame2, text = "表格已生成到桌面", width=16, height=4).grid(row = 10, column=2)
        
    
    def main(self):
        self.log_in()
        self.entry_button()
A = frame1().log_in()

# {'张三':[80,80,80, 240], '李四':[100, 100, 100]}