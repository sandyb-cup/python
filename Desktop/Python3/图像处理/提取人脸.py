from PIL import Image
import face_recognition
image_path = "woman_face.jpeg"
image = face_recognition.load_image_file(image_path)


face_locations = face_recognition.face_locations(image) # 提取人脸位置与人脸个数
print("I found {} face(s) in this photograph.".format(len(face_locations)))

for face_location in face_locations:
    top, right, bottom, left = face_location # 提取人脸位置
    print("A face is located at pixel location Top:{}, Letf:{},botton:{},Right:{}".format(top, left, bottom, right))
    face_image = image[top:bottom, left:right] # 限定图片的宽度与高度
    pil_image = Image.fromarray(face_image) # 将图片进行array化
    pil_image.show()
    