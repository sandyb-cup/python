import os
 
def txt(name,text):              #定义函数名
    b = input("file name:")                             #判断当前路径是否存在，没有则创建new文件夹
    os.makedirs(b)
 
	xxoo = b + name + '.txt'
 
    file = open(xxoo,'w')
 
    file.write(text)        #写入内容信息
 
    file.close()
    print ('ok')
txt('test','hello,python')     