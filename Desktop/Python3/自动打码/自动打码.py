import os 
import cv2
import face_recognition
import subprocess
from PIL import Image

# ffmpag 音品转码工具
# 将视频文件转换成声音文件
def video2mp3(file_name):
    '''
    : param filename : 传入视频文件的路径
    : return: 处理过后的文件路径
    '''
    outfile_name = file_name.split('.')[0]+'.mp3' # mp3格式处理过后的输出文件名字 
    cmd = 'ffmpeg -i '+file_name+' -f mp3 '+outfile_name # 终端运行指令
    # ffmoeg -i XXX.mp3 -f mp3 outfile_name
    subprocess.call(cmd, shell=True) # 这里要在终端运行如果shell为False的话这里会报错
    # shell为True 进程会调用操作系统的shell来执行操作
    # https://www.runoob.com/w3cnote/python3-subprocess.html
    return None
    
def mask_video(input_video, output_video, mask_path='mask.jpg'): # 打码函数
    # 读取图片
    mask = cv2.imread(mask_path)
    # 读取打码图片 赋值给mask变量

    # 读取要打码的视频
    cap = cv2.VideoCapture(input_video)

    # 读取打码视频参数
    v_fps = cap.get(5) # 视频帧率
    v_width = cap.get(3) # 视频宽度
    v_height = cap.get(4) # 视频高度

    # 写入视频
    # 设置写视频参数 格式mp4 保证输出视频大小不变
    size = (int(v_width),int(v_height))
 
    fourcc = cv2.VideoWriter_fourcc('m','p','4','v') # 定义视频输出格式 赋值给fourcc参数

    # 定义输出视频 参数赋值给out变量 里面参数有输出视频的名字 输出视频的格式 输出视频的帧率 输出视频的大小
    out = cv2.VideoWriter(output_video, fourcc, v_fps, size)
    
    # 用face_recognition.load_image_file参数识别出已知人脸 将其数值赋值给已知人脸变脸know_face
    know_face = face_recognition.load_image_file('tmr.jpg') # 读取出来的数据是一个三维矩阵 是图片的像素通道值 也就是颜色值

   # 将已知人脸的参数进行编码 并将编码的参数传递给 biden_encoding变量 
    biden_encoding = face_recognition.face_encodings(know_face)[0] 
    # 它是一个列表里面有编码人脸的关键点位置 坐标
    
    # 读取视频这里是一帧一帧的视频
    cap = cv2.VideoCapture(input_video)

    # cap.isOpened 如果视频是打开的
    while (cap.isOpened()):
        ret, frame = cap.read()
        # ret为True或者是False表示头没有读取到图片
        # frame表示截取到的每一帧图片
        # 如果视频中有东西
        if ret:
            # 识别视频注意这里是每一帧中的人脸区域 人脸轮廓
            face_locations = face_recognition.face_locations(frame)

            for (top_right_y, top_right_x, left_bottom_y, left_bottom_x ) in face_locations: # 对人脸区域坐标进行遍历

                unknown_image = frame[top_right_y-50:left_bottom_y+50,left_bottom_x-50:top_right_x+50] # 让图框变小为的是mask更贴合人脸

                if face_recognition.face_encodings(unknown_image) != []:# 进行解码
                    # 进行人脸数据的解码
                    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
                    # 对比人脸 原来的mask编码与后面每一帧的图像中人脸进行比较
                    results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
                    # 贴图
                    if results ==[True]:
                        # 变的是mask打码图片大小 实时更新
                        mask = cv2.resize(mask,(top_right_x - left_bottom_x, left_bottom_y - top_right_y))

                        # 把打码图片的位置给节选出来
                        frame[top_right_y:left_bottom_y,left_bottom_x:top_right_x] = mask
                        # 这一步是将mask放到 frame位置上面
            out.write(frame)
        else:
            break
def video_add_mp3(file_name, mp3_file):
    '''
    视频文件加上声音文件
    return :合成的视频声音文件
    '''
    outfile_name = "mp3_add.mp4"
    # print('ffmpeg -i ' + file_name + ' -i '+ mp3_file + ' -strict -2 -f mp4 ' + outfile_name)
    subprocess.call('ffmpeg -i ' + file_name + ' -i '+ mp3_file + ' -strict -2 -f mp4 ' + outfile_name, shell=True)
def main():
    video2mp3('cut.mp4')    
    mask_video(input_video='cut.mp4', output_video='output.mp4')
    video_add_mp3(file_name='output.mp4',mp3_file='cut.mp3')
if __name__=="__main__":
    main()
