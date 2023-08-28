import cv2
import numpy as np

img = cv2.imread('Sources/pic_filter.png', 1)
kernel1 = np.array([[0,0,0],
                   [0,1,0],
                   [0,0,0]])

img_iden = cv2.filter2D(img, -1, kernel1)
cv2.imwrite('Sources/Filter image.png',img_iden)
cv2.imshow('Original Image', img)
cv2.imshow('Filter Image', img_iden)

##
kernel2 = np.ones((5,5))/25
print(kernel2)
img_iden2 = cv2.filter2D(img, -1, kernel2)
cv2.imshow('Original Image', img)
cv2.imshow('Filter Image', img_iden2)

### 
img_iden3 = cv2.blur(img, ksize = (5,5))
cv2.imshow('Original Image', img)
cv2.imshow('Filter Image', img_iden3)

###
img_iden4 = cv2.GaussianBlur(img, ksize = (5,5), sigmaX = 0, sigmaY=0)
cv2.imshow('Original Image', img)
cv2.imshow('Filter Image', img_iden4)

###
img_iden5 = cv2.medianBlur(img,ksize = 5 )
cv2.imshow('Original Image', img)
cv2.imshow('Filter Image', img_iden3)

###
kernel3 = np.array([[0, -1, 0],
                    [-1, 5,-1],
                    [0, -1, 0]])
sharp_img = cv2.filter2D(src=img, ddepth=-1, kernel=kernel3)
cv2.imshow('Original', img)
cv2.imshow('Sharpened', sharp_img)
cv2.waitKey(0)
