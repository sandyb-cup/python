from PIL import Image, ImageDraw

def pict_draw(image_path,object,accutary):

    image_path = "woman_face.jpeg"

    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)
    # rectangle(xy, fill=None, outline = None, width = 1)
    # xy:定义边界的两个点,可以选则的顺序为[(x1, y1), (x2, y2)], 或者是[x1, y1, x2, y2]。绘制的矩阵不包括第二个点 
    # outline：边框得颜色
    # fill：如果要对矩阵内颜色进行填充，可以进行设置
    # width：边框的宽度，以像素为单位，
    draw.rectangle([38, 49, 419, 491], outline = (1, 255, 255),  width = 2)
    draw.text((38, 49), "woman_face:actuary:90%", fill = (1, 255, 255), )
    img.show()

