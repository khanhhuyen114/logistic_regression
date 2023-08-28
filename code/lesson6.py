import cv2
import numpy as np

img = cv2.imread('Sources/pic6.png', 1)
img_line = img.copy()
print(img.shape)

# Draw Line
pointA = (200,80)
pointB = (450,80)
cv2.line(img_line, pointA, pointB, (255,255,0), thickness = 3)
cv2.imwrite('Sources/ImageLine.png', img_line)
cv2.imshow('Image Line', img_line)
cv2.waitKey(0)

# Draw a circle
center = (500, 200)
img_cir = img.copy()
cv2.circle(img_cir, center, 100, (0,0,255), thickness = 3, lineType= cv2.LINE_AA )
cv2.imwrite('Sources/ImageCircle.png',img_cir)
cv2.imshow('Image Circle', img_cir)
cv2.waitKey(0)
cv2.destroyAllWindows()

