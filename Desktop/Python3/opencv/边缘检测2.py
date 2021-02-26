import cv2
import numpy as np
import matplotlib.pyplot as plt
import time
cv2.namedWindow("Image", 0)
image = cv2.imread("飞鸟.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # 转换成灰色图片

# 进行算子计算 进行3 * 3 convolution 计算x y方向上面的梯度                                                                  
gradX = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=-1)
gradY = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=-1)

# subtract the y-gradient from the x-gradient
# 将垂直边缘跟水平边缘进行相减 之后再进行scaleabs对高水平梯度跟低垂直梯度的图像区域进行缩小跟求平均值 
gradient = cv2.subtract(gradX, gradY) 
gradient = cv2.convertScaleAbs(gradient)

# 去除白噪声 用9*9内核平滑图像平滑图像中的高频噪声 将每个像素替换成周围像素的均值 
# 之后对图像进行模糊图像二值化,梯度图中不大于90的任何像素都设置为0黑色，否则像素点都设置为白色225
blurred = cv2.blur(gradient, (9, 9 ))
(_, thresh) = cv2.threshold(blurred, 90, 225, cv2.THRESH_BINARY)

# cv2.imshow("Image thresh",thresh)

# 填充蜜蜂身体上面的白色点 
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (25, 25))
closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

# 去除昆虫身边其他的白色噪点
closed = cv2.erode(closed,None,iterations = 4)
closed = cv2.erode(closed, None,iterations = 4)

# 边框 
# findContours第一个参数是要检所的图片 必须是二值图,即黑白图，不是灰度图，

# 第二个参数是图片的索检格式 
# cv2，RETR_EXTERNAL 表示只检测外轮廓
# cv2.RETR_LIST 检测的轮廓不建立等级关系
# cv2.RETR_CCOMP 建立一个等级树结构轮廓

# 第三个参数为轮廓的近似方法
# cv2.CHAIN_APPROX_NONE 储存所有的轮廓点，相邻的两个点的像素位置差不超过1，即max(abs(x1-x2),abs(y2-y1)) == 1
# cv2.CHAIN_APPROX_SIMPLE压缩水平方向， 对角线方向的元素，只保留该方向上面的终点坐标， 例如一个矩阵只需4个点来保存轮廓信息

# cv2.findContours()函数返回两个值，一个是轮廓的本身， 还有一个是轮廓对应的属性，
# cv2.findContours()函数返回的第一个值是list， list中每个元素都是图像中的一个轮廓numpy中的narray表示。每一个ndarray中保存的是轮廓上面的各个点坐标，把list排序， 点最多的轮廓就是昆虫的轮廓

'''
Opencv中通过cv2.drawContours来在图像上绘制轮廓
第一个参数指明在那幅图像上面绘制轮廓
第二个参数是轮廓本身，在python中它是一个列表
第三个参数指定绘制list中的哪条轮廓，如果是-1表示绘制list中的所有轮廓
第四个参数是轮廓的线条的颜色
第五个参数是轮廓的线条粗细
'''

# minAreaRect()函数：主要包含点集最小面积矩阵，这个矩阵是可以偏转角度的，可以与图像的边界不平行
(cnts, _) = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# (cnts, _) = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
c = sorted(cnts, key = cv2.contourArea, reverse = True)[0] # 取最短函数
rect = cv2.minAreaRect(c) # 取最小值
box = np.int0(cv2.boxPoints(rect))
cv2.drawContours(image, [box], -1, (0, 225, 0), 3)

cv2.imshow("Image draw",image)

# 修改框
# xs = [i[0] for i in box]
# ys = [i[1] for i in box]

# x1 = min(xs)
# x2 = max(xs)
# y1  = min(ys)
# y2  = max(ys)
# hight = y2 - y1
# width = x2 - x1

# cropImg = image[y1:y1+hight, x1:x1 + width]

# cv2.imshow("image",cropImg)
time.sleep(10)

cv2.waitKey(0)
cv2.destroyAllWindows()
