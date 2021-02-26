import cv2
import numpy as np
import matplotlib.pyplot as plt

cv2.namedWindow("Image", 0)
image = cv2.imread("蜜蜂.jpg")
cv.imshow("Iamge",image)

# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Image",image)
# plt.imshow(image)
# plt.show()
# cv2.waitKey(0)
# cv2.destroyAllWindows()