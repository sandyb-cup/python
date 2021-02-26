def root_entry():
    admini_info = {"sandy":"1234","mandy":"123456"}
    name = []
    for i in admini_info.keys():
        name.append(i)
    return admini_info,name

def stud_info():
    stud_info = {"张三":[90, 100, 120]}
    return stud_info

def stud_get(name):
    stud_info__ = stud_info()
    scord = stud_info__[name]
    return scord

def admini_get(name):
    admini_info, names = root_entry()
    password = admini_info[name]
    return password

def main():
    stud_get("张三")
if __name__ =="__main__":
    main()
    
