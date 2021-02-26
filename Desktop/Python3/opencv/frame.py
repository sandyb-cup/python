import cv2
from PIL import Image
import time
import os
def video_image():
    cap = cv2.VideoCapture('/Users/sandy/Desktop/Python3/自动打码/cut.mp4')
    v_fps = cap.get(5) # 视频帧率
    v_width = cap.get(3) # 视频宽度
    v_height = cap.get(4) # 视频高度
    print(v_fps,v_width,v_height)
    guide_path = "/Users/sandy/Desktop/Python3/1/"
    image_num = -1
    while(cap.isOpened()):
        ret, frame = cap.read() # ret是否有内容 frame：每一帧图片
        if ret:
            image_num+=1 
            cv2.imwrite('/Users/sandy/Desktop/Python3/1/image'+str(image_num)+'.jpg',frame) # 进行每一帧图片的保存
        else: 
            break
    return guide_path
def image_video():
    path = video_image() 
    filelist = os.listdir(path) # 获取文件中文件名字 返回的是一个列表
    file_list = []
    for i in range(len(filelist)): # 遍历列表重新编排图片路径
        new_image_path = 'image'+str(i)+'.jpg' 
        file_list.append(new_image_path)       
    fps = 15 # 定义输出视频中每一秒输出出多少张图片
    # 获取图片尺寸大小
    temp_image = file_list[0]
    im = Image.open(path+temp_image)
    (x, y)=im.size # 获取图片大小
    
    size = (x,y) # 将图片大小实例化
    output_path = 'video_output.mp4'
    # 输出视频的名字
    fourcc = cv2.VideoWriter_fourcc('m','p','4','v') # 输出文件格式
    video = cv2.VideoWriter(output_path, fourcc, fps, size)
    # 输出视频的路径 格式 大小 目的：防止图片失真
    for items in file_list:
        if items.endswith('.jpg'): # 判断图片的后缀是否是jpg类型的
            item = path+'/'+items # 拼凑图片绝对路径 
            img = cv2.imread(item) # 使用opencv读取图像 返回numpy.darray类型值 对应RGB数值
            video.write(img) # 
    video.release() # 释放
def test_print():
    print("你好！！ python")
def main():
    image_video()
if __name__=="__main__":
    main()
    
    
