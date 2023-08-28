import cv2
import numpy as np

img = cv2.imread('Sources/pic6.png', 1)
print(img.shape)

# Draw Line
img_line = img.copy()
pointA = (200,80)
pointB = (450,80)
cv2.line(img_line, pointA, pointB, (255,255,0), thickness = 3)
cv2.imwrite('Sources/ImageLine.png', img_line)
cv2.imshow('Image Line', img_line)
cv2.waitKey(0)

# Draw a circle
img_line = img.copy()
center = (500, 200)
img_cir = img.copy()
cv2.circle(img_cir, center, 100, (0,0,255), thickness = -1, lineType= cv2.LINE_AA )  # thickness = -1: fulfill circle
cv2.imwrite('Sources/ImageCircle.png',img_cir)
cv2.imshow('Image Circle', img_cir)
cv2.waitKey(0)

# Draw a rectangle
img_rect = img.copy()
pointA = (300,115)
pointB = (450,225)
cv2.rectangle(img_rect, pointA, pointB, (255,255,0), thickness = 3)
cv2.imwrite('Sources/ImageLine.png', img_rect)
cv2.imshow('Image Rectangle', img_rect)
cv2.waitKey(0)

#Draw an Elipse
img_elip = img.copy()
center = (500,200)
axis1 = (150,50)
axis2 = (125,50)
cv2.ellipse(img_elip, center, axis1, 0,0,360, (250,0,0), thickness = 3, lineType= cv2.LINE_8)
cv2.ellipse(img_elip, center, axis2, 90,0,360, (0, 250,0), thickness = 3, lineType= cv2.LINE_8)
cv2.imwrite('Sources/ImageElip.png', img_elip)
cv2.imshow('Image Elip', img_elip)
cv2.waitKey(0)

#Draw a halfelipse
img_helip = img.copy()
center = (500,200)
axis1 = (150,50)
axis2 = (125,50)
cv2.ellipse(img_helip, center, axis1, 0,180,360, (250,0,0), thickness = 3, lineType= cv2.LINE_8)
cv2.ellipse(img_helip, center, axis1, 0,0,180, (0, 250,0), thickness = -2, lineType= cv2.LINE_8)
cv2.imwrite('Sources/ImagehaftElip.png', img_helip)
cv2.imshow('Image haft Elip', img_helip)
cv2.waitKey(0)

#Put a text
img_text = img.copy()
text = "This is a cute dog"
org = (50,350)
cv2.putText(img_text, text, org, fontFace = 2, fontScale = 1.5,color =  (0,0,250))
cv2.imwrite("Sources/Image Text.png", img_text)
cv2.imshow("Image with text", img_text)
cv2.waitKey(0)



cv2.destroyAllWindows()

