import cv2
import os
output_dir = '/Users/sandy/Desktop/Python3/'
i = 1
cap = cv2.VideoCapture(1)
# 这个0是内置摄像头如果是外置或其他的摄像头可以用1，2等其他数字

# 写入一个死循环 不断调用摄像头
while 1:
    # 读取拍到的照片
    ret, frame = cap.read()
    print(ret)
    # 显示拍到的照片
    cv2.imshow('cap', frame)
    
    
    # 保持画面的持续 
    #如果这里为0的话，就是将现在的画面定格，为其他数字的时候比如说是1的时候，表示1秒结束程序。但由于是死循环，所以结束之后马上开启，就为连续图像
    flag = cv2.waitKey(1)
    # 按下回车进行拍照
    if flag == 13:
        # 图片保存路径
        output_path = os.path.join(output_dir, "computer_image%d.jpg")
        # 图片写入到上面路径中
        cv2.imwrite(output_path, frame)
        i+=1
    # 按下esc键退出摄像
    # flag==ord("s"):
    if flag == 27:
        break
# 关闭摄像头
cap.release()


