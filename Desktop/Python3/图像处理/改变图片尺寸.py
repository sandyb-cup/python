from PIL import Image

inifle = '/Users/sandy/Desktop/CSS/css实战/images/exit2.jpeg'
# 输入的图片路径

outfile = '/Users/sandy/Desktop/CSS/css实战/images/exit2.jpeg'
# 输出图片路径

im = Image.open(inifle)
(x ,y) = im.size
# 读取原来图片的尺寸

x_s =20
y_s = 20
#修改图片的长和高的值

out = im.resize((x_s,y_s),Image.ANTIALIAS)

out.save(outfile)
print("original_size:",x,y)
print("adjust_size:",x_s,y_s)