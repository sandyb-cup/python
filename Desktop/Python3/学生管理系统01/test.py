from tkinter.font import names


def root_entry():
    names = []
    # admini_info = {"sandy":"1234","mandy":"123456","kk":"321"}
    with open("teacher_infomation.text",'r',encoding='utf-8') as file:
        content = file.readline()
    admini_info = eval(content)
    for i in admini_info.keys():
        names.append(i)       
    
    return admini_info, names
def stud_info():
    names = []
    
    with open("student_information.text",'r',encoding='utf-8') as file:
        content = file.readline()
    stud_info = eval(content)
    
    for i in stud_info.keys():
        names.append(i)
        
    return stud_info, names

def stud_get(name):
    stud_info__,names = stud_info()
    scord = stud_info__[name]
    return scord

def admini_get(name):
    admini_info, names = root_entry()
    password = admini_info[name]
    return password

def read_file():
    with open("student_information.text",'r',encoding='utf-8') as file:
        content = file.readline()
    content_eval = eval(content)
    return content_eval

def save_file(content):
    with open("student_information.text",'w',encoding='utf-8') as file:
        file.write(str(content))
        
def student_entry_information():
    # student = {"zhangxin":"321","tt":"1234"}
    with open("student_ent_infomation.text",'r', encoding="utf-8") as file:
        studet = file.readline()
        # file.write(str(student))  
    student_json = eval(studet)
    student_name = []
    for i in student_json.keys():
        student_name.append(i)
    return student_json

def get_student_name():
    with open("student_ent_infomation.text",'r', encoding="utf-8") as file:
        studet = file.readline()   
    student_json = eval(studet)
    student_name = []
    for i in student_json.keys():
        student_name.append(i)
    return student_name

def main():
    # stud_get("张三")
    root_entry()
    # print(names)
    # content = get_file_modify()
    name = get_student_name()
    print(name)
    

    

if __name__ =="__main__":
    main()
    
