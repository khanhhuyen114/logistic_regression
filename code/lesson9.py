import cv2
import numpy as np

img = cv2.imread('Sources/pic9.png', cv2.IMREAD_GRAYSCALE)
#th, dst = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY)
# cv2.imwrite('Sources/thres_output.png', dst)
# cv2.imshow('Original Image', img)
# cv2.imshow('Thes Image', dst)

#
#th, dst = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
#th, dst = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
th, dst = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
th, dst = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)
cv2.imwrite('Sources/thres_output.png', dst)
cv2.imshow('Original Image', img)
cv2.imshow('Thes Image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()