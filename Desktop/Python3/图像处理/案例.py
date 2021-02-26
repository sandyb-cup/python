import cv2
import os

i = 1
cap=cv2.VideoCapture(0)

# 调用笔记本内置摄像头，所以参数为0 如果是其他摄像头可以调整参数为1，2
while 1:
    # 从摄像头读取找图片
    sucess, img = cap.read()
    cv2.imshow('img', img)
    # 保持画面维持
    flag = cv2.waitKey(1)
    if flag == 13: #按下回车键拍照
        cv2.imwrite("image2.jpg",img)
        # cv2.destroyAllWindows()
        # 退出拍照
        i += 1
    if flag == 27: #按下ESC键退出
        break
cap.release()