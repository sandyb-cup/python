import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np
imge_path = "woman_face.jpeg"
 
img = Image.open(imge_path)
draw = ImageDraw.Draw(img)
textsize = 20
tf = ImageFont.truetype("/Users/sandy/Desktop/Python3/font_luci.ttf", textsize)
# test((x, y), "text", font, fill)
# 第一个坐标值是以x y进行字体左上角的坐标位置 text 是文本信息， fill是填充颜色
draw.text((38, 49), "woman_face:actury:90%",font = tf, fill = (1, 255, 255))
img.show()