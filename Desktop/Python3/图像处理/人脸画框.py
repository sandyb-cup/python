from PIL import Image, ImageDraw
import face_recognition
image_path = "woman_face.jpeg"
img = Image.open(image_path)
image = face_recognition.load_image_file(image_path)
print(image)
face_locations = face_recognition.face_locations(image)
print("Found {} face(s)".format(len(face_locations)))

draw = ImageDraw.Draw(img)

for face_location in face_locations:
    top, left, bottom, right = face_location
    print("The face at photograph pixel location top:{}, Right:{}, bottom:{}, left:{} ".format(top, right, bottom, left))
    draw.rectangle([right, bottom, left, right], outline = (0, 255, 255), width = 2)
    img.show()
img.close()

    