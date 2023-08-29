import cv2
import numpy as np

img = cv2.imread('Sources/pic11.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_blur = cv2.GaussianBlur(img_gray, (3,3), 0,0)

# Sobel Detection
sobelx = cv2.Sobel(img_blur, ddepth = cv2.CV_64F,dx = 1, dy = 0)
sobely = cv2.Sobel(img_blur, ddepth = cv2.CV_64F,dx = 0, dy = 1, ksize = 5)
sobelxy = cv2.Sobel(img_blur, ddepth = cv2.CV_64F,dx = 1, dy = 1, ksize= 5)

# Canny Detection
canny = cv2.Canny(img_blur, threshold1= 50, threshold2= 200)

cv2.imshow('Original image', img)
cv2.imshow('Sobelx Image', sobelx)
cv2.imshow('Sobely Image', sobely)
cv2.imshow('Sobelxy Image', sobelxy)
cv2.imshow('Canny Image', canny)
cv2.waitKey(0)
cv2.destroyAllWindows()